# Campaign Learning Engine (CLE) — n8n prototype

A review-first workflow prototype for capturing campaign outcomes, comparing variants, and checking whether example B2B accounts have enough evidence to enter human review.

## What is demonstrated

- Event intake validates a small, explicit set of outcome types and normalizes event data.
- The variant report uses unique delivered prospects as its rate denominator and labels small samples as directional only.
- A synthetic acquisition walkthrough creates fictional account records, applies transparent illustrative fit checks, and holds records for human review when evidence is incomplete.
- Outbound sending is disabled throughout the demo.

## Run the synthetic walkthrough

1. Import `workflows/n8n/03_synthetic_acquisition_walkthrough.json` into n8n.
2. Open the workflow and choose **Execute workflow**.
3. Inspect the output of **Score, draft, and hold for review**.

The verified demo run created 3 fictional records, put 2 into the human-review queue, held 1 for missing evidence, and sent 0 messages. This is a functional n8n demo, not a live prospecting or production deployment. Names, signals, scores, and example.com URLs are fabricated placeholders.

## Workflows

| File | Purpose | Requirements |
|---|---|---|
| [`03_synthetic_acquisition_walkthrough.json`](workflows/n8n/03_synthetic_acquisition_walkthrough.json) | Self-contained fictional account triage, draft-only message illustration, and review/hold routing | Manual trigger and Code nodes; no credentials |
| [`01_campaign_event_intake.json`](workflows/n8n/01_campaign_event_intake.json) | Validate and accept a campaign outcome event into an n8n Data Table | Create a Data Table named `cle_campaign_events`; configure a webhook test or production URL before use |
| [`02_variant_outcome_report.json`](workflows/n8n/02_variant_outcome_report.json) | Summarize A/B outcomes from the Data Table | Requires `cle_campaign_events`; set the campaign ID in the Code node |

The screenshot in [`evidence/n8n-execution-success.png`](evidence/n8n-execution-success.png) documents the successful synthetic walkthrough execution. The independent intake and reporting workflows are packaged for inspection; this screenshot does not claim they were run in a live system.

## Boundaries

- Fictional records only; no real people or companies are researched.
- No CRM, email, calendar, or outbound-provider connection is configured.
- No message is sent, and the demo does not authorize outreach.
- A human must independently verify evidence, fit, recipient, and consent before any real campaign activity.
- Rates from small samples are not presented as reliable performance conclusions.

## License

MIT. See [`LICENSE`](LICENSE).
