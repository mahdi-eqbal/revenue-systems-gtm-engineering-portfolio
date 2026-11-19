# P02 — AI Lead Qualification & Appointment Handoff

**[View the visual case study — business problem, 49-second demo, verified tests, technical walkthrough, and collaboration link](https://mahdi-eqbal.github.io/revenue-systems-gtm-engineering-portfolio/projects/p02-ai-lead-appointment/)**

**Stack:** HighLevel Conversation AI · Live Chat · Workflows · Opportunities · Estimate Call Calendar · GitHub Pages  
**Evidence reviewed:** 17–18 November 2026  
**Type:** Independent, controlled engineering demonstration for a fictional residential interior-painting business in Dublin, Ireland. Not a paid client deployment or production-readiness claim.

## Business objective

Connect a qualified website enquiry to the **same** CRM contact, opportunity, appointment and follow-up process. A chat response or booking link alone does not prove that the CRM was updated correctly.

[Open interactive chat test surface](https://mahdi-eqbal.github.io/revenue-systems-gtm-engineering-portfolio/demos/dublin-painting-ai-chat/) · [Portfolio](https://mahdi-eqbal.github.io/revenue-systems-gtm-engineering-portfolio/)

## Implemented flow

```text
GitHub Pages chat surface
  → HighLevel live chat (agent restricted using p02-ai-test tag)
  → Qualification policy: residential + interior + Dublin + intent to proceed
  → Agent action: Qualify Residential Painting Lead
  → AI Qualification - Apply Qualified Tag
  → demo-estimate-qualified contact tag
  → Website Chat - Create Qualified Estimate
  → Existing Contact + Open Estimates / Qualified Opportunity
  → Public Estimate Call booking matches that known-email contact
  → Estimate Call - Move to Booked
  → SAME opportunity / Booked

Confirmed booking cancellation
  → Estimate Call - Move to Reschedule Needed workflow
  → Find existing Open/Booked opportunity
  → Add assigned cancellation review task (Found branch only)
  → Reviewer checks other future confirmed appointments
  → If none remain, reviewer moves SAME opportunity to Reschedule Needed
  → Review task marked completed
  → Subsequent confirmed booking can move same opportunity back to Booked
```

## Verified test matrix

| Scenario | HighLevel evidence | Result |
| --- | --- | --- |
| Eligible enquiry | Agent action invoked; contact gained `demo-estimate-qualified`; Open opportunity created in Estimates/Qualified | **Pass** |
| Repeat enquiry, same chat | One opportunity remained; original ID preserved | **Pass for tested contact** |
| Commercial exterior request, Cork | No qualification tag, no new opportunity and no automated booking link | **Pass** |
| API booking for existing contact | Confirmed appointment moved original opportunity Qualified → Booked | **Pass** |
| Public calendar booking | Normal Chrome form submission confirmed; email matched prior chat contact and no second opportunity was created | **Pass for known-email contact** |
| Rebooking from Reschedule Needed | Confirmed API appointment moved the **same** original opportunity to Booked after pipeline-stage order correction | **Pass** |
| Cancellation event | Published, calendar- and test-tag-filtered workflow created the assigned review task; no blind opportunity change | **Pass** |
| Review decision | All seven test appointments were Cancelled; same Open opportunity manually moved Booked → Reschedule Needed and task marked Completed | **Pass — human-reviewed path** |

**Observed debugging evidence:** A real HighLevel execution log originally returned `HTTP 400: Moving an opportunity backward in the pipeline is not allowed`. At that point `Reschedule Needed` came after `Booked`. Changing the stage order (while preserving the existing IDs) to **New → Qualified → Reschedule Needed → Booked → Needs Review** enabled the subsequent confirmed rebooking to move forward to Booked. The failing and passing tests are both preserved as engineering evidence.

## Workflow and record traceability

| Resource | Identifier / state |
| --- | --- |
| Qualified test contact | `KAKvjUgMGaydw6MwTxNL` |
| Original opportunity (the same record throughout tests) | `0Lj65DjKimZK2fx2jDcM` |
| Estimates pipeline | `4UUkAbMdTOHupQgWSFnD` |
| Public Estimate Call calendar | `s1XzFCVuxsZzUIKBqeej` |
| Qualification workflow | `e0c2bfa7-346c-4682-b8b0-ec6c452c4be2` |
| Chat-to-opportunity workflow | `ce2c9588-6fac-4e33-a3fa-51dd6442a61f` |
| [Confirmed-booking workflow](https://app.gohighlevel.com/v2/location/Bhxlfbj7Gq9U12A2Hhg2/automation/workflow/bb12e102-44b1-4753-8355-d62145e36d0a) | `bb12e102-44b1-4753-8355-d62145e36d0a` (published v8 in tested run) |
| [Cancellation-review workflow](https://app.gohighlevel.com/v2/location/Bhxlfbj7Gq9U12A2Hhg2/automation/workflow/32c187f6-81ce-42d2-83e2-909117d126f6) | `32c187f6-81ce-42d2-83e2-909117d126f6` (published v3) |
| Created cancellation-review task | `52hH0g8hzI7l6EeZJMmD` — completed |
| Successful rebooking test appointment | `yMQ4hgmOxiVj6XuoLBML` — cancelled after QA |
| Final cancellation-workflow test appointment | `HN20yfzgF1pCfbgLMGSw` — cancelled after QA |

**Final observed test state (18 November 2026):** The seven recorded Estimate Call QA appointments are all `cancelled`; opportunity search returns **one** Open opportunity in **Reschedule Needed**; cancellation-review task returns `completed=true`. All state claims come from authorized HighLevel readbacks.

## Controls and engineering decisions

- **Isolation:** Agent and cancellation-trigger audience are limited with the `p02-ai-test` contact tag during verification.
- **Identity preservation:** The tested public form reused a contact that already had its email associated with the earlier chat record; this does not establish generalized anonymous or cross-device matching.
- **Opportunity integrity:** Confirmed booking and rebooking update the **existing** Open opportunity. The negative and same-chat duplicate tests preserve the documented scope of their findings.
- **Cancellation safety:** The published cancellation workflow creates a task for an authorized reviewer. It does **not** automatically move the opportunity when the appointment is cancelled. The reviewer determines whether another confirmed future appointment exists before editing the stage.
- **Failure visibility:** Execution logs captured the stage-order restriction and the subsequent targeted fix.
- **Data handling:** The test page includes a `noindex` directive and contains no private API credentials. HighLevel remains the system of record.

## Presentation assets

Two 1080p demonstration cuts have been prepared separately for client and technical audiences, using the original HighLevel screenshots supplied during implementation:

- **Client / agency demo:** business problem, qualification, pipeline integrity, public booking, cancellation review
- **Technical walkthrough:** trigger chain, action routing, Find Opportunity execution, HTTP 400 root cause, rebooking repair, cancellation workflow and verified state

Screenshots are authentic captures of the HighLevel interface. Any diagrams and visual callouts are editorial reconstructions, not claims of additional execution. **[Watch / download client demo (49 s, 1080p)](https://youtu.be/wDQ9OIw7vF8)** · **[Watch / download engineering walkthrough (2 min 2 s, 1080p)](https://youtu.be/YzEYjj9Y1rY)**. Both linked YouTube videos include freshly generated English narration tailored to their intended audiences. The natural-voice render uses Joanna (client) and Lewis (technical). The footage is an editorial montage of genuine interface screenshots and diagram cards, with the video timeline fitted to the newly recorded voice duration. The montage is not a continuous live screen recording.

## Scope and limitations

This case study validates the listed scenarios, not arbitrary traffic, concurrency, cross-browser identity reconciliation, complete production security controls or every possible appointment lifecycle. Fully unattended cancellation reconciliation is intentionally **not** claimed; the verified implementation uses an automatically generated human-review task. The project does not claim a customer deployment, earned revenue or a finished SaaS product.
