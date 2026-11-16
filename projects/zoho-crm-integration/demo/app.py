"""Local lead intake demo. The CRM records in this demo live in SQLite."""
import csv
import hashlib
import hmac
import io
import json
import os
import re
import sqlite3
import uuid
from contextlib import closing
from datetime import datetime, timezone
from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from urllib.parse import parse_qs

DATABASE = Path(os.environ.get("DEMO_DB_PATH") or Path(__file__).with_name("demo.sqlite3"))
FIELDS = ("last_name", "company", "email", "phone")
HTML = Path(__file__).with_name("index.html")


def connect(path):
    db = sqlite3.connect(path)
    db.row_factory = sqlite3.Row
    db.executescript("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY, last_name TEXT, company TEXT,
            email TEXT UNIQUE, phone TEXT, owner TEXT DEFAULT 'Demo Sales',
            status TEXT DEFAULT 'New'
        );
        CREATE TABLE IF NOT EXISTS events (
            source TEXT, source_id TEXT, correlation_id TEXT, received_at TEXT,
            campaign TEXT, utm TEXT, result TEXT, lead_id INTEGER,
            PRIMARY KEY (source, source_id)
        );
    """)
    return db


def normalize(data):
    lead = {name: str(data.get(name) or "").strip() for name in FIELDS}
    lead["email"] = lead["email"].lower()
    lead["phone"] = re.sub(r"[^0-9+]", "", lead["phone"])
    if not lead["last_name"] or not lead["company"]:
        raise ValueError("Last name and company are required.")
    if lead["email"] and not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", lead["email"]):
        raise ValueError("Email is invalid.")
    if lead["phone"] and not re.fullmatch(r"\+?[0-9]{7,15}", lead["phone"]):
        raise ValueError("Phone is invalid.")
    if not (lead["email"] or lead["phone"]):
        raise ValueError("Email or phone is required.")
    if any(len(value) > 250 for value in lead.values()):
        raise ValueError("A lead field is too long.")
    return lead


def process(db, source, source_id, data):
    with db:
        db.execute("BEGIN IMMEDIATE")
        previous = db.execute(
            "SELECT result, lead_id, correlation_id FROM events WHERE source=? AND source_id=?",
            (source, source_id),
        ).fetchone()
        if previous:
            return {**dict(previous), "replayed": True}
        lead_id = None
        try:
            lead = normalize(data)
        except ValueError as error:
            result = f"Invalid: {error}"
        else:
            email = lead["email"]
            phone = lead["phone"]
            match = db.execute("SELECT * FROM leads WHERE email=?", (email,)).fetchone() if email else None
            phones = db.execute("SELECT id FROM leads WHERE phone=?", (phone,)).fetchall() if phone else []
            if any(row["id"] != (match["id"] if match else None) for row in phones):
                result = "Review: phone matches another or unconfirmed lead"
            elif match:
                lead_id = match["id"]
                if phone and not match["phone"]:
                    db.execute("UPDATE leads SET phone=? WHERE id=?", (phone, lead_id))
                    result = "Updated empty phone"
                else:
                    result = "Recorded interaction"
            else:
                lead_id = db.execute(
                    "INSERT INTO leads(last_name,company,email,phone) VALUES (?,?,?,?)",
                    (lead["last_name"], lead["company"], email or None, phone),
                ).lastrowid
                result = "Created"
        correlation = uuid.uuid4().hex
        db.execute("INSERT INTO events VALUES (?,?,?,?,?,?,?,?)", (
            source, source_id, correlation, datetime.now(timezone.utc).isoformat(),
            str(data.get("campaign_id") or "")[:250],
            json.dumps({key: data[key] for key in ("utm_source", "utm_medium", "utm_campaign") if data.get(key)}),
            result, lead_id,
        ))
        return {"result": result, "lead_id": lead_id, "correlation_id": correlation}


def csv_preview(content):
    reader = csv.DictReader(io.StringIO(content.lstrip("\ufeff"), newline=""), strict=True)
    if not reader.fieldnames or not {"last_name", "company"} <= set(reader.fieldnames):
        raise ValueError("CSV requires last_name and company headers.")
    digest = hashlib.sha256(content.encode()).hexdigest()
    seen = set()
    rows = []
    for index, row in enumerate(reader, 1):
        if index > 500:
            raise ValueError("Maximum 500 CSV rows per import.")
        item = {"number": index, "id": f"{digest}:{index}", "data": row}
        try:
            if None in row:
                raise ValueError("Unexpected extra CSV columns.")
            lead = normalize(row)
            identity = lead["email"] or lead["phone"]
            if identity in seen:
                raise ValueError("Duplicate identity in file.")
            seen.add(identity)
        except ValueError as error:
            item["error"] = str(error)
        rows.append(item)
    return rows


def google_lead(payload, key):
    supplied_key = payload.get("google_key", payload.get("Google_key"))
    if not key or not isinstance(supplied_key, str) or not hmac.compare_digest(key, supplied_key):
        raise PermissionError("Invalid webhook key.")
    if payload.get("is_test") is not True:
        raise ValueError("Only Google Ads test events are accepted in this demo.")
    if not payload.get("lead_id"):
        raise ValueError("Missing Google Ads lead_id.")
    columns = {entry["column_id"]: entry.get("string_value", "") for entry in payload["user_column_data"]}
    full_name = (columns.get("FULL_NAME") or "").split()
    return str(payload["lead_id"]), {
        "last_name": columns.get("LAST_NAME") or (full_name[-1] if full_name else ""),
        "company": (columns.get("COMPANY_NAME") or "").strip() or "Not provided",
        "email": columns.get("EMAIL", ""), "phone": columns.get("PHONE_NUMBER", ""),
        "campaign_id": payload.get("campaign_id"),
    }


class Handler(BaseHTTPRequestHandler):
    def reply(self, content, status=200, kind="text/plain"):
        self.send_response(status)
        self.send_header("Content-Type", f"{kind}; charset=utf-8")
        self.end_headers()
        self.wfile.write(content.encode())

    def page(self, content="", submission_id=None, status=200):
        with closing(connect(DATABASE)) as db:
            events = db.execute(
                "SELECT source, result, lead_id, correlation_id, campaign, utm FROM events ORDER BY rowid DESC LIMIT 30"
            ).fetchall()
        history = "".join(
            "<tr>" + "".join(f"<td>{escape(str(value if value is not None else ''))}</td>" for value in row) + "</tr>"
            for row in events
        )
        self.reply(HTML.read_text(encoding="utf-8-sig").replace(
            "{{submission_id}}", submission_id or uuid.uuid4().hex
        ).replace("{{history}}", history).replace("{{result}}", content), status, "text/html")

    def do_GET(self):
        if self.path == "/":
            self.page()
        else:
            self.reply("Not found", 404)

    def do_POST(self):
        try:
            host = f"127.0.0.1:{self.server.server_port}"
            if self.headers.get("Host") != host:
                raise PermissionError("Use the local demo address.")
            origin = self.headers.get("Origin")
            if origin and origin != f"http://{host}":
                raise PermissionError("Unexpected origin.")
            size = int(self.headers.get("Content-Length", "0"))
            if not 0 < size <= 256_000:
                raise ValueError("Invalid request length.")
            body = self.rfile.read(size).decode()
            with closing(connect(DATABASE)) as db:
                if self.path == "/google-ads":
                    source_id, lead = google_lead(json.loads(body), os.environ.get("DEMO_GOOGLE_KEY"))
                    result = process(db, "Google Ads test", source_id, lead)
                    self.reply(json.dumps(result), kind="application/json")
                    return
                form = parse_qs(body, keep_blank_values=True)
                data = {name: values[0] for name, values in form.items()}
                if self.path == "/lead":
                    source_id = data.get("submission_id", "")
                    if not re.fullmatch(r"[a-f0-9]{32}", source_id):
                        raise ValueError("Invalid submission ID.")
                    result = process(db, "Website", source_id, data)
                    self.page(f"<p>{escape(result['result'])}" + (" (replay)" if result.get("replayed") else "") + "</p>")
                elif self.path in ("/csv/preview", "/csv/import"):
                    rows = csv_preview(data.get("csv", ""))
                    if self.path == "/csv/import":
                        selected = set(form.get("selected", []))
                        results = [
                            process(db, "CSV", row["id"], row["data"]) for row in rows
                            if "error" not in row and row["id"] in selected
                        ]
                        self.page("<ul>" + "".join(
                            f"<li>{escape(result['result'])}" + (" (replay)" if result.get("replayed") else "") + "</li>"
                            for result in results
                        ) + "</ul>")
                    else:
                        summary = []
                        for row in rows:
                            label = escape(row.get("error") or row["data"]["last_name"])
                            choice = "" if "error" in row else (
                                f'<input type="checkbox" name="selected" value="{row["id"]}" checked>'
                            )
                            summary.append(f"<li>{choice} Row {row['number']}: {label}</li>")
                        self.page('<form action="/csv/import" method="post"><ul>' + "".join(summary)
                            + f'</ul><textarea name="csv" hidden>{escape(data["csv"])}</textarea>'
                            + '<button>Import selected rows</button></form>')
                else:
                    self.reply("Not found", 404)
        except PermissionError as error:
            self.reply(str(error), 403)
        except (ValueError, csv.Error, KeyError, TypeError, AttributeError) as error:
            self.reply(str(error), 400)


if __name__ == "__main__":
    print("Local CRM demo: http://127.0.0.1:8765", flush=True)
    HTTPServer(("127.0.0.1", 8765), Handler).serve_forever()

