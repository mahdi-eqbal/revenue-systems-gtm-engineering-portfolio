# CRM Lead Integration

Local portfolio demo using Python and SQLite. Use synthetic data.

Run `python app.py` and open http://127.0.0.1:8765.

1. Submit Rivera / Example Studio / alex@example.com in the website form.
2. Preview sample-leads.csv and import the eligible rows. Rivera's missing phone is filled, Chen is created, and the duplicate and invalid rows are excluded.
3. To test the webhook, start the app with DEMO_GOOGLE_KEY set to local-demo-key, then run:
   ```powershell
   curl.exe -H "Content-Type: application/json" --data-binary "@google-ads-test.json" http://127.0.0.1:8765/google-ads
   ```
   Refresh the page to see the interaction. Repeating the request returns the original tracking ID.

Verified on Windows with a temporary database via HTTP. The test covered new leads, website and webhook replay, cross-source matching, invalid webhook key, CSV preview and reimport, and phone conflicts. It ended with two leads and five unique events.

The local demo stores synthetic data in SQLite. The Google Ads payload is synthetic. Separately, live CRM writes and readback were verified through Make against Zoho EU Sandbox. The earlier direct OAuth HTTP 400 issue was later resolved in a PowerShell Self Client verification on 2026-11-17; see the updated status below.

## Sandbox write verification

The optional `--smoke-lead` mode checks the Sandbox identity, creates a single synthetic Lead, and reads back its ID and email. The local journal blocks a second creation on replay and blocks an automatic retry if the first write's outcome is uncertain. The mode is separate from the web demo.

The read-only check requires `ZohoCRM.org.READ`. The optional write check also requires `ZohoCRM.modules.leads.CREATE` and `ZohoCRM.modules.leads.READ`. Authorization must target the correct EU Sandbox organization. The confirmed organization identity is `type=sandbox`, ID `1023543000000023712`, and `domain_name=zohocrmintegration` (the `alias` field was empty in the observed response). The helper now checks these values before a write. Keep grant codes, access/refresh tokens and client credentials local; never commit them.

Previously, mocked verification passed for creation/readback, replay, Production rejection and lost-write-response handling. The direct Python smoke test has **not** performed a real write. The earlier OAuth error is historical: an EU Self Client exchange succeeded via PowerShell on 2026-11-17 using `application/x-www-form-urlencoded`, followed by a successful authenticated `/crm/v8/org` read. The token response returned `api_domain=https://www.zohoapis.eu`; the organization response confirmed the Sandbox. The Python helper was corrected to use the same encoding and validate the returned EU API domain and exact organization identity, but the corrected Python helper has not been rerun live.
See DEMO.md for the customer walkthrough. Run `python -m unittest discover -v -p "test_*.py"` from this folder for offline demo and OAuth/Sandbox-safety regression checks (mocked, no live network or CRM writes). The new regression checks have not yet been executed in a fresh runtime after publication.

## Latest integration evidence

- The local Google Ads test receiver supports the key spelling shown in Google's test samples and accepts a test form without a company field, recording the missing company as `Not provided`.
- HighLevel form -> Make -> Zoho CRM EU Sandbox passed using synthetic data. Make handles the Zoho duplicate-email error separately from invalid input.
- A direct EU Self Client OAuth token exchange and Sandbox organization read were verified in PowerShell on 2026-11-17. The Python helper now sends token parameters as `application/x-www-form-urlencoded` in the POST body; its updated path has not been separately live-tested.

## Portfolio webhook validation

For the portfolio, a direct webhook test served as the alternative to the Google Ads console test. A synthetic Google Ads-format JSON lead was posted to Make (scenario 8616887). The webhook returned HTTP 200, and Zoho EU Sandbox record 1023543000000726002 was read back with Lead Source = Advertisement and Company = Not provided. Delivery initiated by Google Ads remains a deployment acceptance check.

Google Sheets → Make → Zoho EU Sandbox was verified in scenario 8617442. Row 2 created Lead 1023543000000729002, row 3 took the duplicate-email Skip route, and row 4 failed validation for missing Last_Name.
