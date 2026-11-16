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

CRM records currently live in SQLite. The Google Ads payload is synthetic. Live Sandbox writes and readback were verified through Make. The Sandbox exists, but both OAuth flows returned HTTP 400 with an HTML response at the token exchange.

## Sandbox write verification

The optional `--smoke-lead` mode checks the Sandbox identity, creates a single synthetic Lead, and reads back its ID and email. The local journal blocks a second creation on replay and blocks an automatic retry if the first write's outcome is uncertain. The mode is separate from the web demo.

The read-only check requires `ZohoCRM.org.READ`. The write check also requires `ZohoCRM.modules.leads.CREATE` and `ZohoCRM.modules.leads.READ`. Authorization must target the EU Sandbox. The expected alias is based on the Sandbox URL and still needs confirmation against the organization API response. Keep credentials and codes local.

Mocked verification passed for creation and readback, replay, Production rejection, and a lost write response. This direct OAuth smoke test used mocked writes. Both browser and Self Client authorization reached the token exchange, where real requests returned HTTP 400 with an HTML body. This does not identify the source of the rejection.
See DEMO.md for the customer walkthrough and run python -m unittest -v test_demo for reproducible acceptance checks.

## Latest integration evidence

- The local Google Ads test receiver supports the key spelling shown in Google's test samples and accepts a test form without a company field, recording the missing company as `Not provided`.
- HighLevel form -> Make -> Zoho CRM EU Sandbox passed using synthetic data. Make handles the Zoho duplicate-email error separately from invalid input.
- The direct Python OAuth flow remains unverified against Zoho. The corrected script submits token parameters in the POST body.

## Portfolio webhook validation

For the portfolio, a direct webhook test served as the alternative to the Google Ads console test. A synthetic Google Ads-format JSON lead was posted to Make (scenario 8616887). The webhook returned HTTP 200, and Zoho EU Sandbox record 1023543000000726002 was read back with Lead Source = Advertisement and Company = Not provided. Delivery initiated by Google Ads remains a deployment acceptance check.

Google Sheets → Make → Zoho EU Sandbox was verified in scenario 8617442. Row 2 created Lead 1023543000000729002, row 3 took the duplicate-email Skip route, and row 4 failed validation for missing Last_Name.
