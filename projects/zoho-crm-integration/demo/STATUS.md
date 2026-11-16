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

The Python and SQLite demo covers website forms, CSV preview and import, a synthetic Google Ads payload, and replay. The Sandbox smoke-test helper is covered with mocked responses. Run python -m unittest -v test_demo.

## Remaining verification

- The direct Python OAuth token exchange returned HTTP 400 with text/html. The support inquiry applies to this optional path. The verified Make path can proceed independently.
- Native Excel ingestion and a general-purpose REST API remain supplemental. CSV is verified locally.
