"""Create one synthetic Lead and verify replays locally before any second write."""
import json
import sqlite3
from contextlib import closing
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request

SANDBOX = "https://sandbox.zohoapis.eu"
EXPECTED_ALIAS = "zohocrmintegration"
EMAIL = "portfolio-smoke-test@example.com"
JOURNAL = Path(__file__).with_name("sandbox-smoke.sqlite3")


def check_lead(org, token, send, journal=JOURNAL):
    if org.get("type") != "sandbox" or org.get("alias") != EXPECTED_ALIAS or not org.get("id"):
        raise RuntimeError("The expected Sandbox identity could not be confirmed. No Lead was sent.")
    endpoint = f"{SANDBOX}/crm/v8/Leads"
    headers = {"Authorization": f"Zoho-oauthtoken {token}", "Content-Type": "application/json"}
    with closing(sqlite3.connect(journal)) as db:
        with db:
            db.execute("CREATE TABLE IF NOT EXISTS smoke (org_id TEXT PRIMARY KEY, lead_id TEXT)")
            claim = db.execute("INSERT OR IGNORE INTO smoke VALUES (?, NULL)", (org["id"],))
            first_attempt = claim.rowcount == 1
        if first_attempt:
            body = {"data": [{"Last_Name": "Portfolio Smoke Test", "Company": "Example Studio",
                              "Email": EMAIL}], "trigger": []}
            outcome = send(Request(endpoint, data=json.dumps(body).encode(), headers=headers))
            records = outcome.get("data", [])
            record = records[0] if len(records) == 1 else {}
            lead_id = record.get("details", {}).get("id")
            if record.get("code") != "SUCCESS" or not isinstance(lead_id, str) or not lead_id.isdigit():
                raise RuntimeError("Zoho creation could not be confirmed. Review Sandbox before any retry.")
            with db:
                db.execute("UPDATE smoke SET lead_id=? WHERE org_id=?", (lead_id, org["id"]))
        else:
            lead_id, = db.execute("SELECT lead_id FROM smoke WHERE org_id=?", (org["id"],)).fetchone()
            if not lead_id:
                raise RuntimeError("An earlier write has an uncertain outcome. Inspect Sandbox before retrying.")

        response = send(Request(f"{endpoint}/{quote(lead_id, safe='')}?fields=Email", headers=headers))
        records = response.get("data", [])
        if len(records) != 1 or records[0].get("id") != lead_id or records[0].get("Email") != EMAIL:
            raise RuntimeError("The saved Lead could not be verified in Sandbox.")
        action = "Created and verified" if first_attempt else "Replay verified without another write"
        return f"{action}: Sandbox Lead {lead_id}"
