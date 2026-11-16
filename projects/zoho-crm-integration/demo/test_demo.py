"""Run the three intake channels against an isolated database."""
import http.client
import json
import os
import re
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.parse import urlencode

import app

ROOT = Path(__file__).resolve().parent


class DemoAcceptance(unittest.TestCase):
    def test_google_sample_without_company(self):
        payload = {
            "lead_id": "sample-lead-id",
            "campaign_id": 42,
            "Google_key": "local-demo-key",
            "is_test": True,
            "user_column_data": [
                {"column_id": "FULL_NAME", "string_value": "Alex Rivera "},
                {"column_id": "PHONE_NUMBER", "string_value": "+12025550123"},
            ],
        }
        source_id, lead = app.google_lead(payload, "local-demo-key")
        self.assertEqual(source_id, "sample-lead-id")
        self.assertEqual(lead["last_name"], "Rivera")
        self.assertEqual(lead["company"], "Not provided")
        self.assertEqual(lead["campaign_id"], 42)
        with app.closing(app.connect(":memory:")) as db:
            first = app.process(db, "Google Ads test", source_id, lead)
            self.assertEqual(first["result"], "Created")
            replay = app.process(db, "Google Ads test", source_id, lead)
            self.assertTrue(replay["replayed"])
            self.assertEqual(replay["correlation_id"], first["correlation_id"])
        with self.assertRaises(PermissionError):
            app.google_lead({**payload, "google_key": "wrong"}, "local-demo-key")

    def test_three_sources_and_replay(self):
        with tempfile.TemporaryDirectory() as folder:
            database = Path(folder) / "acceptance.sqlite3"
            with patch.object(app, "DATABASE", database), patch.dict(
                os.environ, {"DEMO_GOOGLE_KEY": "local-demo-key"}
            ), app.HTTPServer(("127.0.0.1", 0), app.Handler) as server:
                thread = threading.Thread(target=server.serve_forever, daemon=True)
                thread.start()

                def request(path, body=None):
                    conn = http.client.HTTPConnection(*server.server_address, timeout=5)
                    try:
                        conn.request("GET" if body is None else "POST", path, body)
                        response = conn.getresponse()
                        return response.status, response.read().decode()
                    finally:
                        conn.close()

                try:
                    status, page = request("/")
                    self.assertEqual(status, 200)
                    submission = re.search(r'name="submission_id" value="([a-f0-9]+)"', page)[1]
                    lead = dict(submission_id=submission, last_name="Rivera",
                                company="Example Studio", email="alex@example.com")
                    self.assertIn("Created", request("/lead", urlencode(lead))[1])
                    self.assertIn("replay", request("/lead", urlencode(lead))[1])

                    payload = json.loads((ROOT / "google-ads-test.json").read_bytes())
                    status, response = request("/google-ads", json.dumps(payload))
                    self.assertEqual(status, 200)
                    first = json.loads(response)
                    self.assertEqual(first["result"], "Recorded interaction")
                    self.assertEqual(first["lead_id"], 1)
                    again = json.loads(request("/google-ads", json.dumps(payload))[1])
                    self.assertTrue(again["replayed"])
                    self.assertEqual(first["correlation_id"], again["correlation_id"])
                    self.assertEqual(request("/google-ads", json.dumps({**payload, "google_key": "bad"}))[0], 403)

                    content = (ROOT / "sample-leads.csv").read_text(encoding="utf-8-sig")
                    status, preview = request("/csv/preview", urlencode({"csv": content}))
                    self.assertEqual(status, 200)
                    self.assertIn("Duplicate identity", preview)
                    self.assertIn("Last name and company are required", preview)
                    selected = re.findall(r'name="selected" value="([^"]+)"', preview)
                    self.assertEqual(len(selected), 2)
                    body = urlencode({"csv": content, "selected": selected}, doseq=True)
                    self.assertIn("Updated empty phone", request("/csv/import", body)[1])
                    self.assertIn("replay", request("/csv/import", body)[1])

                    lead.update(submission_id="a" * 32, email="other@example.net", phone="+12025550111")
                    self.assertIn("Review:", request("/lead", urlencode(lead))[1])
                    with app.closing(app.connect(database)) as db:
                        self.assertEqual(db.execute("SELECT count(*) FROM leads").fetchone()[0], 2)
                        self.assertEqual(db.execute("SELECT count(*) FROM events").fetchone()[0], 5)
                        self.assertEqual(tuple(db.execute(
                            "SELECT owner, status FROM leads WHERE id=1"
                        ).fetchone()), ("Demo Sales", "New"))
                finally:
                    server.shutdown()
                    thread.join()


if __name__ == "__main__":
    unittest.main()
