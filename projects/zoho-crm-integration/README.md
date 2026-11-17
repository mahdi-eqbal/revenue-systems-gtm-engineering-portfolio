# P01 — Zoho CRM Lead Intake

A portfolio implementation for estimate inquiries from web forms and spreadsheets. Make maps incoming fields to Zoho CRM EU Sandbox, skips duplicate-email errors and surfaces required-field errors in execution history.

## What was verified

| Input | Test | Observed result |
| --- | --- | --- |
| HighLevel form | Submit a new lead | Zoho Sandbox saved the lead with source `Web Form`. |
| Google Sheets | Read three rows through Make | A new lead was created, a repeated email took the Skip route, and a blank last name surfaced a validation error. |
| Google Ads payload | POST a synthetic JSON lead directly to the Make webhook | The webhook returned HTTP 200 and the saved Zoho Sandbox lead showed source `Advertisement`. |

The direct webhook test exercised the downstream Google Ads flow for the portfolio. Delivery initiated from the Google Ads console remains a deployment acceptance check.

## Technical review

- **Field mapping:** The Sheets workflow reads `Leads!A2:E4` and maps email, surname and company. The lead description records the source row.
- **Duplicate handling:** Zoho enforces email uniqueness. Make takes its Skip route only for `DUPLICATE_DATA` on the email field.
- **Validation:** A missing `Last_Name` caused `BundleValidationError` before the CRM write. This deliberate negative case marked the overall execution as Error while preserving the successful first write.
- **Sandbox scope:** The integration runs used synthetic fixtures and Zoho EU Sandbox.
- **OAuth verification:** The EU Self Client token exchange and Sandbox organization read succeeded in PowerShell on 2026-11-17. The optional Python helper has been corrected but has not been live-retested. Production access or direct Python write execution is not claimed.

## Run the local demo

The runnable [demo](demo/) uses Python 3 and SQLite. The hosted Make and Zoho tests above were exercised separately.

```bash
cd projects/zoho-crm-integration/demo
python -m unittest discover -v -p "test_*.py"
python app.py
```

Open <http://127.0.0.1:8765>. See the [demo walkthrough](demo/DEMO.md), [setup and payload examples](demo/README.md), and [verification status](demo/STATUS.md).

[Project page](https://mahdi-eqbal.github.io/revenue-systems-gtm-engineering-portfolio/projects/zoho-crm-integration/)
