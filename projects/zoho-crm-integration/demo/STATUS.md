# P01 — Zoho CRM Integration status

## Verified in Zoho CRM EU Sandbox

- HighLevel test form submissions reached Make and created Leads in the Sandbox.
- The duplicate email test kept the original Lead. Make ran the duplicate-specific Skip handler.
- Zoho record 1023543000000724001 was opened in the Sandbox and showed Lead Source = Web Form.
- A missing Last Name produced a visible validation error without running the duplicate handler.
- The HighLevel workflow was returned to Draft and the Make scenario to Inactive after testing.

- Google Sheets → Make → Zoho EU Sandbox was verified in scenario 8617442. Row 2 created Lead 1023543000000729002, row 3 took the duplicate-email Skip route, and row 4 failed validation for missing Last_Name.
- For the portfolio, a direct webhook test served as the alternative to the Google Ads console test. A synthetic Google Ads-format JSON lead was posted to Make (scenario 8616887). The webhook returned HTTP 200, and Zoho EU Sandbox record 1023543000000726002 was read back with Lead Source = Advertisement and Company = Not provided. Delivery initiated by Google Ads remains a deployment acceptance check.

## Verified locally

The Python and SQLite demo covers website forms, CSV preview and import, a synthetic Google Ads payload, and replay. The Sandbox smoke-test helper is covered with mocked responses. Run `python -m unittest discover -v -p "test_*.py"` for the local demo plus newly added offline OAuth and Sandbox safety tests. The new tests are published but not yet rerun in a fresh runtime.

## OAuth status updated 2026-11-17

- The earlier Self Client token exchange had returned HTTP 400 with an HTML response. A fresh EU Self Client authorization code subsequently exchanged successfully using `application/x-www-form-urlencoded` in PowerShell; both an access token and refresh token were returned.
- A subsequent authenticated GET to `/crm/v8/org` succeeded. The organization response identified `type=sandbox`, `id=1023543000000023712`, and `domain_name=zohocrmintegration`; the token response returned `api_domain=https://www.zohoapis.eu`.
- The optional Python helper was updated to submit URL-encoded token fields, use the returned EU API domain, and check Sandbox type, organization ID and domain name before any optional write. A separate live run of that updated Python helper has **not** been performed.
- The live CRM writes/readback for this project were verified through Make; the direct Python write smoke test has only mocked evidence.

## Remaining verification

- Google Ads console-originated delivery; the downstream synthetic-format webhook test is verified.
- Native Excel ingestion and a general-purpose REST API remain supplemental. CSV is verified locally.
