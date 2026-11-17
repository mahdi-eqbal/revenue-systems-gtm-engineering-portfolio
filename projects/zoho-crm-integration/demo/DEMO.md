# CRM Lead Integration demo

## Customer walkthrough

A sales team receives leads from its website, advertising, and partner files. An operator needs to see which requests created a lead, which belong to an existing lead, and which need review. The application uses a common validation and processing path. The history shows source, outcome, lead ID, and a tracking ID for each accepted event.

1. Submit Rivera, Example Studio, and alex@example.com in the website form. Point out the new Lead ID in Processing history.
2. Preview sample-leads.csv. The duplicate Rivera row and the row without a last name are excluded. Import both selected rows. Rivera's existing record gains a phone and Chen gets a new Lead ID.
3. Send the synthetic Google Ads event using the command in README.md. Refresh the page and show that the ad interaction uses Rivera's Lead ID. Send it again and compare the tracking IDs. The replay does not add a history row.
4. Submit a website lead with any last name and company, other@example.net, and +12025550111. Show that it goes to review because the phone is already associated with Rivera.

For a clean run set DEMO_DB_PATH to a new local SQLite filename before launching the application. Existing demo data stays in its original file.

## Acceptance evidence

Run python -m unittest -v test_demo from the project folder. The test exercises the website, CSV preview and import, synthetic webhook, replay, an invalid webhook key, and a conflicting phone. It uses an isolated temporary database and checks for exactly two leads and five unique events. It also checks that the existing owner and lead status stay intact.

## Deployment status

This demo uses synthetic data stored in local SQLite. Separate HighLevel and Make workflows were verified with saved Leads and readback in Zoho CRM EU Sandbox. An earlier direct Python OAuth exchange returned HTTP 400; on 2026-11-17 an EU Self Client token exchange succeeded independently in PowerShell using URL-encoded form fields, and an authenticated organization read confirmed the Sandbox identity. The Python helper was corrected accordingly but has not been live-rerun, and no direct Python write is claimed.

For the portfolio, a direct webhook test served as the alternative to the Google Ads console test. A synthetic Google Ads-format JSON lead was posted to Make (scenario 8616887). The webhook returned HTTP 200, and Zoho EU Sandbox record 1023543000000726002 was read back with Lead Source = Advertisement and Company = Not provided. Delivery initiated by Google Ads remains a deployment acceptance check.

Google Sheets → Make → Zoho EU Sandbox was verified in scenario 8617442. Row 2 created Lead 1023543000000729002, row 3 took the duplicate-email Skip route, and row 4 failed validation for missing Last_Name.
