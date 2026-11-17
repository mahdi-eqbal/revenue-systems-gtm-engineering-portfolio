"""Offline regression checks for Zoho EU OAuth and Sandbox write safety."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch
from urllib.parse import parse_qs

import sandbox_smoke
import verify_zoho_sandbox as oauth


class SandboxAuthRegression(unittest.TestCase):
    def test_token_request_uses_urlencoded_form_body(self):
        fields = {
            "grant_type": "authorization_code",
            "client_id": "client",
            "client_secret": "secret with + &",
            "code": "grant+code",
        }
        request = oauth.token_request(fields)
        self.assertEqual(
            request.get_header("Content-type"),
            "application/x-www-form-urlencoded",
        )
        self.assertEqual(parse_qs(request.data.decode("utf-8")), {key: [value] for key, value in fields.items()})
        self.assertEqual(request.full_url, "https://accounts.zoho.eu/oauth/v2/token")

    @patch.object(oauth.sys, "argv", ["test_sandbox_auth.py"])
    def test_verified_sandbox_org_read_uses_returned_api_domain(self):
        responses = [
            {"access_token": "fake-test-token", "api_domain": "https://www.zohoapis.eu"},
            {"org": [{"id": oauth.EXPECTED_ORG_ID, "type": "sandbox",
                       "domain_name": oauth.EXPECTED_DOMAIN_NAME}]},
        ]
        with patch.object(oauth, "read_json", side_effect=responses) as mock_read:
            oauth.verify_token("client", "secret", "grant", self_client=True)
        org_request = mock_read.call_args_list[1].args[0]
        self.assertEqual(org_request.full_url, "https://www.zohoapis.eu/crm/v8/org")

    @patch.object(oauth.sys, "argv", ["test_sandbox_auth.py"])
    def test_production_org_fails_closed(self):
        responses = [
            {"access_token": "fake-test-token", "api_domain": "https://www.zohoapis.eu"},
            {"org": [{"id": oauth.EXPECTED_ORG_ID, "type": "production",
                       "domain_name": oauth.EXPECTED_DOMAIN_NAME}]},
        ]
        with patch.object(oauth, "read_json", side_effect=responses):
            with self.assertRaisesRegex(RuntimeError, "No CRM write was attempted"):
                oauth.verify_token("client", "secret", "grant", self_client=True)

    def test_smoke_helper_rejects_wrong_org_without_write(self):
        sender = Mock()
        wrong_org = {"id": "other-org", "type": "sandbox",
                     "domain_name": sandbox_smoke.EXPECTED_DOMAIN_NAME}
        with self.assertRaisesRegex(RuntimeError, "No Lead was sent"):
            sandbox_smoke.check_lead(
                wrong_org, "fake-test-token", sender,
                api_domain="https://www.zohoapis.eu",
            )
        sender.assert_not_called()

    def test_smoke_helper_verifies_one_write_and_replay(self):
        org = {"id": sandbox_smoke.EXPECTED_ORG_ID, "type": "sandbox",
               "domain_name": sandbox_smoke.EXPECTED_DOMAIN_NAME}
        lead_id = "1023543000000729999"
        calls = []

        def send(request):
            calls.append(request)
            if request.data:
                return {"data": [{"code": "SUCCESS", "details": {"id": lead_id}}]}
            return {"data": [{"id": lead_id, "Email": sandbox_smoke.EMAIL}]}

        with tempfile.TemporaryDirectory() as directory:
            journal = Path(directory) / "journal.sqlite3"
            first = sandbox_smoke.check_lead(
                org, "fake-test-token", send, journal,
                api_domain="https://www.zohoapis.eu",
            )
            replay = sandbox_smoke.check_lead(
                org, "fake-test-token", send, journal,
                api_domain="https://www.zohoapis.eu",
            )
        self.assertIn("Created and verified", first)
        self.assertIn("Replay verified without another write", replay)
        self.assertEqual(sum(request.data is not None for request in calls), 1)
        self.assertTrue(all(
            request.full_url.startswith("https://www.zohoapis.eu/crm/v8/Leads")
            for request in calls
        ))


if __name__ == "__main__":
    unittest.main()
