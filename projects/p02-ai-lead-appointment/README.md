# P02 — AI Lead Qualification & Appointment Handoff (HighLevel)

**Status:** Verified synthetic integration demo · **Tested:** 17 November 2026 · **Environment:** HighLevel test subaccount and GitHub Pages test surface.

> This is an independent engineering demonstration for a fictional Dublin residential interior-painting business. It is **not** a customer deployment, commercial painting service, production-ready agent, or evidence of earned revenue. Use synthetic visitor data only.

## Business problem

A website chat can answer visitor questions yet fail to create actionable CRM records. P02 tests the full handoff from a qualified AI conversation through a tagged workflow, CRM opportunity creation, repeat-request control, and appointment-driven stage transition.

## Demonstrated flow

```text
Public GitHub Pages test surface
  -> HighLevel Live Chat widget
  -> Auto-Pilot conversation agent (restricted to contacts tagged p02-ai-test)
  -> Qualification action: "Qualify Residential Painting Lead"
  -> Workflow: "AI Qualification - Apply Qualified Tag"
  -> Contact tag: demo-estimate-qualified
  -> Workflow: "Website Chat - Create Qualified Estimate"
  -> Estimates pipeline / Qualified opportunity
  -> Confirmed Estimate Call appointment (API, existing contact ID)
  -> Workflow: "Estimate Call - Move to Booked"
  -> SAME Estimates opportunity / Booked stage
```

Qualification requires (a) new **residential interior painting** estimate, (b) property in **Dublin, Ireland**, and (c) clear intent to proceed or book an estimate call. The agent excludes commercial/exterior work, locations outside Dublin, existing bookings, and general enquiries from automated qualification.

**[Open synthetic chat test surface](https://mahdi-eqbal.github.io/revenue-systems-gtm-engineering-portfolio/demos/dublin-painting-ai-chat/)** — The agent is intentionally limited to pre-tagged test visitors. An ordinary public visitor should not expect an AI reply. This page is not a customer booking channel.

## Verified tests and evidence (17 November 2026)

Evidence below was checked via HighLevel's conversation, contact, opportunity, appointment, calendar and pipeline records. Identifiers are for **synthetic test records**; the repository does not contain API credentials or private customer data.

| Test | Observed evidence | Result |
| --- | --- | --- |
| Positive qualification | New chat visitor `Guest Visitor tuotg` submitted an eligible residential interior-painting estimate request in Dublin; conversation activity recorded `Qualify Residential Painting Lead`, contact gained `demo-estimate-qualified`, and an opportunity appeared in `Estimates / Qualified` | **PASS** |
| Duplicate enquiry (same visitor) | Follow-up in the same conversation received a booking-link response; opportunity search still returned **one** record with the original opportunity ID | **PASS for tested path** |
| Negative qualification | New visitor `Guest Visitor dogyq` requested **commercial exterior painting in Cork**. Agent said it was outside the estimate-call criteria and suggested team review. Contact retained only `p02-ai-test`; opportunity search returned zero; no booking link sent | **PASS** |
| Appointment-driven handoff | A **confirmed appointment was created through the HighLevel API using the original contactId**, for a verified available 30-minute slot. The original opportunity moved from `Qualified` to `Booked`; its ID and open status remained unchanged; opportunity count remained one | **PASS — API-driven booking path** |

### Traceable synthetic record identifiers

| Resource | ID |
| --- | --- |
| Qualified chat contact | `KAKvjUgMGaydw6MwTxNL` |
| Qualified chat conversation | `m2d3UP0rnu2BoKD6OV56` |
| Original opportunity, preserved after booking | `0Lj65DjKimZK2fx2jDcM` |
| Negative-test contact | `uRliDwktRq8OrS4sU21a` |
| Confirmed synthetic appointment | `KCp5ZqZuQrNjh7aznFJW` |
| Estimate Call calendar | `s1XzFCVuxsZzUIKBqeej` |
| Qualification action target workflow | `e0c2bfa7-346c-4682-b8b0-ec6c452c4be2` |
| Tag-to-opportunity workflow | `ce2c9588-6fac-4e33-a3fa-51dd6442a61f` |

At the time of verification, the confirmed test appointment was scheduled for **19 November 2026, 10:00–10:30 Europe/Dublin**. Its creation was explicitly marked synthetic; it may occupy calendar capacity until cancelled. No client meeting was claimed.

## Controls / architecture decisions

- **Restricted agent access:** `p02-ai-test` tag filter prevents general anonymous visitors from joining the agent's active test audience. The test operator attaches this tag to a newly created guest contact before qualification.
- **Action-driven qualification:** The agent must trigger a separate workflow and apply the CRM qualification tag rather than treating a conversational booking link as proof of successful handoff.
- **Opportunity identity:** In the observed duplicate test and confirmed appointment test, one original opportunity persisted; the booking workflow changed the existing opportunity stage.
- **Explicit negative path:** An out-of-scope request is answered without applying the qualification tag, creating an opportunity, or providing the booking link.
- **Privacy/testing:** Synthetic contact data; publicly hosted test page has a no-index directive and no API keys. The embedded chat is hosted/processed by HighLevel.

## What is **not** yet verified

1. **Public booking form identity reconciliation:** The final appointment was created by API using a known `contactId`. It does **not** prove that a visitor using the public booking form would be associated with the original anonymous chat contact; without email/phone capture this may create a separate contact.
2. **Broad duplicate-proof guarantees:** The repeat-enquiry test covered only one contact and one conversation. Cross-browser identity, concurrent triggers, tag re-application, multiple opportunities, and error retries need dedicated tests.
3. **Human handoff execution:** The negative-test agent *suggested* human review, but there is no confirmed review task, owner assignment, ticket, or escalation workflow.
4. **Production readiness:** Security, consent/privacy, abuse handling, monitoring, operational SLAs, and customer deployment have not been validated.
5. **Publicly reproducible CRM logs:** HighLevel live records were verified through an authorized connection; this markdown reports observations rather than exposing customer data or publishing an authenticated execution-log export.

## Follow-up checklist

- [ ] Verify anonymous chat-to-public-booking identity stitching with controlled synthetic email/phone and inspect matched contact IDs.
- [ ] Expand negative-case matrix: residential exterior in Dublin, residential interior outside Dublin, existing appointment question, ambiguous intent.
- [ ] Add human-review action and confirm ownership/notifications, if that is part of the desired scope.
- [ ] Verify repeat workflow triggers and concurrent duplicate suppression explicitly.
- [ ] Clean up/cancel the synthetic appointment after evidence capture and verify downstream impact before modifying the opportunity.
- [ ] Capture redacted screenshots or exported trace artifacts for a customer-facing technical walkthrough.

## Source and implementation boundaries

The public repository hosts the static [demo page](../../demos/dublin-painting-ai-chat/index.html) and this case study. The chatbot agent, workflows, pipeline, calendar, and CRM data are configured inside HighLevel; they are **not** represented as source-code implementations within this repository. No invented backend, custom API integration, or production event processor is claimed.
