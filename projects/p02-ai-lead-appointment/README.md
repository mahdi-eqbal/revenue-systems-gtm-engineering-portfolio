# P02 — AI Lead Qualification & Appointment Handoff (HighLevel)

**Status:** Verified synthetic integration demo · **Tested:** 17–18 November 2026 · **Environment:** HighLevel test subaccount and GitHub Pages test surface.

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
  -> Public Estimate Call form booking (verified same contact, 18 Nov)
  -> OR API-confirmed appointment (using original contact ID)
  -> Workflow: "Estimate Call - Move to Booked"
  -> SAME Estimates opportunity / Booked stage
```

Qualification requires (a) new **residential interior painting** estimate, (b) property in **Dublin, Ireland**, and (c) clear intent to proceed or book an estimate call. The agent excludes commercial/exterior work, locations outside Dublin, existing bookings, and general enquiries from automated qualification.

**[Open synthetic chat test surface](https://mahdi-eqbal.github.io/revenue-systems-gtm-engineering-portfolio/demos/dublin-painting-ai-chat/)** — The agent is intentionally limited to pre-tagged test visitors. An ordinary public visitor should not expect an AI reply. This page is not a customer booking channel.

## Verified tests and evidence (17–18 November 2026)

Evidence below was checked via HighLevel's conversation, contact, opportunity, appointment, calendar and pipeline records. Identifiers are for **synthetic test records**; the repository does not contain API credentials or private customer data.

| Test | Observed evidence | Result |
| --- | --- | --- |
| Positive qualification | New chat visitor `Guest Visitor tuotg` submitted an eligible residential interior-painting estimate request in Dublin; conversation activity recorded `Qualify Residential Painting Lead`, contact gained `demo-estimate-qualified`, and an opportunity appeared in `Estimates / Qualified` | **PASS** |
| Duplicate enquiry (same visitor) | Follow-up in the same conversation received a booking-link response; opportunity search still returned **one** record with the original opportunity ID | **PASS for tested path** |
| Negative qualification | New visitor `Guest Visitor dogyq` requested **commercial exterior painting in Cork**. Agent said it was outside the estimate-call criteria and suggested team review. Contact retained only `p02-ai-test`; opportunity search returned zero; no booking link sent | **PASS** |
| Appointment-driven handoff | A **confirmed appointment was created through the HighLevel API using the original contactId**, for a verified available 30-minute slot. The original opportunity moved from `Qualified` to `Booked`; its ID and open status remained unchanged; opportunity count remained one | **PASS — API-driven stage transition** |
| Public booking form → existing chat identity (18 Nov) | A tester booked via the real public Estimate Call page in a normal browser, with the exact synthetic email belonging to the qualified chat contact and a reserved synthetic phone. HighLevel returned a **confirmed** appointment linked to the **original contact ID**; contact email lookup returned one matching contact, and opportunity search returned exactly the **original opportunity**. The booking form updated that contact's phone. | **PASS — tested identity reconciliation, one existing opportunity** |
| Rebooking from Reschedule Needed (18 Nov) | A new `Reschedule Needed` stage was added without removing any existing stage. The original synthetic opportunity was moved there manually and a fresh **confirmed** appointment was booked into an available 23 Nov slot. The opportunity **stayed in Reschedule Needed** during two post-booking reads, despite one existing opportunity and a confirmed appointment. Current booking automation is not verified for rebooking from this stage. The QA appointment was subsequently cancelled with notifications suppressed. | **FAIL — workflow extension required** |
| Rebooking after user-reported Find Opportunity edit (18 Nov) | After the operator reported removing the Qualified-stage filter, the workflow API still reported published `version 7` unchanged. A new confirmed API appointment `0cQWGeKY2czkM1ZkSJsW` was created for the original contact; two CRM reads still showed the original opportunity at `Reschedule Needed`, count one. The test appointment was cancelled after verification. | **FAIL — edit persistence/publication or execution needs inspection** |
| Rebooking after confirmed published v8 save (18 Nov) | HighLevel workflow list confirmed `Estimate Call - Move to Booked` is `published`, `version 8`, updated 18 Nov 16:08:44 UTC. A fresh confirmed test appointment `TcV8e8m0eiQ3UgJt9FgM` for the original contact on a verified free 23 Nov 11:00 UTC slot did **not** move the existing single opportunity out of `Reschedule Needed` on repeated CRM reads. Test appointment was then cancelled (`toNotify:false`). Workflow execution logs could not be read via API due `WORKFLOW_API_NOT_ENABLED_FOR_LOCATION`. | **FAIL — published v8 did not transition; inspect UI execution logs** |
| Rebooking after pipeline-order correction (18 Nov) | UI logs identified `HTTP 400: Moving an opportunity backward in the pipeline is not allowed`. The original stages were reordered, preserving IDs, to `New → Qualified → Reschedule Needed → Booked → Needs Review`. Confirmed synthetic appointment `yMQ4hgmOxiVj6XuoLBML` then moved the **same original opportunity** automatically from `Reschedule Needed` to `Booked`, with one opportunity total. That test appointment was later cancelled. | **PASS — verified rebooking** |
| Public booking form → stage change | At the time of the public form test, the original opportunity was **already Booked** from the earlier API booking. This public form test verifies contact identity and no new opportunity, **not an independent Qualified → Booked transition**. | **NOT RETESTED IN THIS PATH** |

### Traceable synthetic record identifiers

| Resource | ID |
| --- | --- |
| Qualified chat contact | `KAKvjUgMGaydw6MwTxNL` |
| Qualified chat conversation | `m2d3UP0rnu2BoKD6OV56` |
| Original opportunity, preserved after booking | `0Lj65DjKimZK2fx2jDcM` |
| Negative-test contact | `uRliDwktRq8OrS4sU21a` |
| Original API synthetic appointment (later cancelled) | `KCp5ZqZuQrNjh7aznFJW` |
| Public booking form synthetic appointment (later cancelled) | `r0sxu0JIRKG7LzpzglFV` |
| Rebooking API QA appointment (cancelled) | `ft6qbmjlVbR2f52BNKqq` |
| Post-edit rebooking QA appointment (cancelled) | `0cQWGeKY2czkM1ZkSJsW` |
| Published v8 rebooking QA appointment (cancelled) | `TcV8e8m0eiQ3UgJt9FgM` |
| Successful rebooking appointment, cancelled after QA | `yMQ4hgmOxiVj6XuoLBML` |
| Reschedule Needed stage (new) | `8c19363b-dd68-4d3f-9b59-4f8a28ddd3b6` |
| Booking workflow (published; not modified) | `bb12e102-44b1-4753-8355-d62145e36d0a` |
| Estimate Call calendar | `s1XzFCVuxsZzUIKBqeej` |
| Qualification action target workflow | `e0c2bfa7-346c-4682-b8b0-ec6c452c4be2` |
| Tag-to-opportunity workflow | `ce2c9588-6fac-4e33-a3fa-51dd6442a61f` |

The API-created test appointment was scheduled for **19 November 2026, 10:00–10:30 Europe/Dublin** and cancelled on 18 November. A subsequent confirmed **public-form appointment** was successfully submitted for **20 November 2026, 11:00–11:30 Europe/Dublin**, on the existing contact, and subsequently **cancelled on 18 November 2026** after evidence capture (`toNotify:false` for the connector cancellation). The original opportunity remained in **Booked** after cancellation. No real customer appointment, production deployment or live client meeting is claimed. The cancellation-state handling policy is now specified below, but **has not been automated**. The opportunity was moved manually to `Reschedule Needed` for the rebooking test and remains there after the QA appointment was cancelled. No new opportunity was created.

## Controls / architecture decisions

- **Restricted agent access:** `p02-ai-test` tag filter prevents general anonymous visitors from joining the agent's active test audience. The test operator attaches this tag to a newly created guest contact before qualification. The exact public-form QA test used a preexisting synthetic contact with a known email.
- **Action-driven qualification:** The agent must trigger a separate workflow and apply the CRM qualification tag rather than treating a conversational booking link as proof of successful handoff.
- **Opportunity identity:** In the observed duplicate test and confirmed appointment test, one original opportunity persisted; the booking workflow changed the existing opportunity stage.
- **Explicit negative path:** An out-of-scope request is answered without applying the qualification tag, creating an opportunity, or providing the booking link.
- **Privacy/testing:** Synthetic contact data; publicly hosted test page has a no-index directive and no API keys. The embedded chat is hosted/processed by HighLevel.

## What is **not** yet verified

1. **Generalized identity reconciliation:** The public form correctly matched the **specific tested visitor** whose email was already attached to the chat contact before booking; this does not establish identity matching for anonymous visitors who have not supplied a stable email/phone identifier, or cross-browser sessions without matching details.
2. **Broad duplicate-proof guarantees:** The repeat-enquiry test covered only one contact and one conversation. Cross-browser identity, concurrent triggers, tag re-application, multiple opportunities, and error retries need dedicated tests.
3. **Human handoff execution:** The negative-test agent *suggested* human review, but there is no confirmed review task, owner assignment, ticket, or escalation workflow.
4. **Production readiness:** Security, consent/privacy, abuse handling, monitoring, operational SLAs, and customer deployment have not been validated.
5. **Appointment cancellation reconciliation and rebooking:** A `Reschedule Needed` stage exists, but automatic cancellation routing and rebooking back to `Booked` are **not implemented**. Three actual rebooking tests (including the confirmed published v8 retest) observed no automatic stage transition from `Reschedule Needed` to `Booked`; the workflow list initially reported published version 7 after the reported UI edit, then confirmed version 8 after an explicit Save; even v8 failed the transition. No assertion of a passing end-to-end cancellation/rebooking workflow is supported.
6. **Publicly reproducible CRM logs:** HighLevel live records were verified through an authorized connection; this markdown reports observations rather than exposing customer data or publishing an authenticated execution-log export.

## Follow-up checklist

- [x] Verify chat-to-public-booking identity stitching for **one known-email synthetic contact**: public booking submitted and confirmed 18 Nov 2026; original contact reused; no duplicate opportunity. Earlier issues with default mandatory Phone, an already-used phone, the failed Form Builder and hosted-browser Turnstile were resolved for this test by a normal Chrome booking and a reserved synthetic phone. Generalized anonymous identity matching remains untested.
- [ ] Expand negative-case matrix: residential exterior in Dublin, residential interior outside Dublin, existing appointment question, ambiguous intent.
- [ ] Add human-review action and confirm ownership/notifications, if that is part of the desired scope.
- [ ] Verify repeat workflow triggers and concurrent duplicate suppression explicitly.
- [x] Cancel **all six** synthetic QA appointments after evidence capture (original API, public-form, first 23 Nov rebooking test, post-edit retest, and published v8 retest). Appointment states returned `cancelled` on 18 November 2026. After manually moving the opportunity to `Reschedule Needed`, it remained there; this is not proof of automatic cancellation routing.
- [x] Define cancellation and rebooking stage policy; create the `Reschedule Needed` pipeline stage without altering existing stage IDs.
- [ ] Implement and test the *automatic* cancellation workflow and extend the booking workflow to handle rebooking from `Reschedule Needed`. An authorized HighLevel UI editor is required because Workflow Definition API calls are denied with `WORKFLOW_API_NOT_ENABLED_FOR_LOCATION`.
- [x] Inspect UI execution logs: Find Opportunity found the original opportunity; Update Opportunity was skipped due to HTTP 400 backward-stage restriction. Reorder existing stages so `Reschedule Needed` precedes `Booked`.
- [x] Re-test confirmed rebooking after stage reorder: same original opportunity automatically moved from `Reschedule Needed` to `Booked`, count 1. Test appointment cancelled with notifications suppressed; opportunity was then **manually** reset to `Reschedule Needed` because automatic cancellation routing is not implemented.
- [ ] Capture redacted screenshots or exported trace artifacts for a customer-facing technical walkthrough.


## Cancellation and rebooking design (18 November 2026 — rebooking verified, cancellation pending)

**Live pipeline change:** `Estimates` now contains `New`, `Qualified`, `Reschedule Needed`, `Booked`, and `Needs Review` in that order. All four original stage IDs were preserved. The P02 synthetic opportunity was manually put in `Reschedule Needed` because all six QA appointments have been cancelled; automatic cancellation routing is **not** claimed.

**Workflow A — cancellation (new, not yet created).** Use an appointment-status-changed trigger filtered to calendar `Estimate Call` and status `Cancelled`. Restrict safely to tagged P02 test contacts during verification, and only to the existing `Estimates` pipeline. Before changing an opportunity, check for *any other future confirmed or active Estimate Call appointment* for the same contact. If one exists, preserve `Booked`; otherwise locate the existing **Open** `Estimates` opportunity in `Booked` and move that **same opportunity** to `Reschedule Needed`. If no matching opportunity or multiple ambiguous opportunities exist, take the safe no-write/review path. Repeated Cancelled events must be idempotent. Never create a new opportunity in this workflow.

**Workflow B — confirmed/rebooked appointment (extend existing [Estimate Call - Move to Booked](https://app.gohighlevel.com/v2/location/Bhxlfbj7Gq9U12A2Hhg2/automation/workflow/bb12e102-44b1-4753-8355-d62145e36d0a)).** Trigger on confirmed appointments for the same calendar. Find the existing Open `Estimates` opportunity in either `Qualified` **or** `Reschedule Needed`; update *that opportunity* to `Booked` only if an unambiguous match exists. The currently published flow handled a prior `Qualified → Booked` case, but in the rebooking test from `Reschedule Needed` it did **not** change the stage. Avoid changing the existing published workflow until the conditions have been examined in the builder; editing the workflow via API is blocked by the location's feature gate.

**Acceptance matrix before marking complete:**

| Scenario | Expected state | Current evidence |
| --- | --- | --- |
| Cancel sole confirmed appointment | Same Open opportunity → `Reschedule Needed` | **Not automated**; manually staged for QA |
| Cancel one appointment while another future confirmed appointment exists | Same opportunity stays `Booked` | Not tested |
| Rebook from `Reschedule Needed` | Same opportunity → `Booked`, count 1 | **PASS** after stage reorder; opportunity remained unique |
| Duplicate cancel / confirmation event | No new opportunity or unwanted stage change | Not tested |
| Out-of-scope contact/calendar, ambiguous opportunities | No automatic write / review path | Not tested |

The observed failure is important technical evidence; do not modify the case-study or customer-facing narrative to say rebooking automation passed until a **fresh confirmed appointment** and resulting CRM stage transition have both been verified.


## Cancellation review task — verified 18 November 2026

A **separate cancellation-review workflow**, `Estimate Call - Move to Reschedule Needed` (HighLevel workflow `32c187f6-81ce-42d2-83e2-909117d126f6`), was published at **version 3**. Its appointment status trigger was configured with `Event type = Normal`, `Appointment status = cancelled`, `In calendar = Estimate Call`, and contact `Has tag = p02-ai-test`. It uses Find Opportunity on the existing Open/Booked Estimates opportunity; the `Opportunity Found` branch adds a review task, while `Not Found` is empty. **There is no automated cancellation-stage move.**

A fresh confirmed synthetic QA appointment `HN20yfzgF1pCfbgLMGSw` was created for contact `KAKvjUgMGaydw6MwTxNL`. The published booking workflow moved the same original opportunity to `Booked`. The appointment was then cancelled with `toNotify:true` to let the cancellation workflow run. HighLevel `get-all-tasks` returned exactly one newly created task on that contact: `52hH0g8hzI7l6EeZJMmD`, titled `P02 - Review Cancelled Estimate Call`, assigned to the subaccount user `88mBWm40OltG96Gi5Xcm`, incomplete. The opportunity remained `Booked` and opportunity search returned exactly **one** record with the original ID. **PASS — cancellation-triggered human review task and safe no-write behavior for the tested case.**

The task instructs the reviewer to check the contact's other future confirmed appointments and manually move the same opportunity to `Reschedule Needed` only if no future confirmed booking remains. This step requires a reviewer and is **not** an automated reconciliation. Additional scenarios involving multiple active appointments, duplicate cancellation triggers and unrelated contacts/calendars are not yet verified.


### Completed cancellation-review task — 18 November 2026

After the published cancellation workflow automatically created task `52hH0g8hzI7l6EeZJMmD`, an authorized reviewer checked the contact's live HighLevel appointment records. All **seven** test appointments on the `Estimate Call` calendar were `cancelled`; no remaining confirmed/active booking appeared in the returned records. Opportunity search showed exactly **one** existing Open `Estimates` opportunity, `0Lj65DjKimZK2fx2jDcM`, still at `Booked`.

The reviewer **manually** moved that same opportunity to `Reschedule Needed` through the authorized opportunity update API, then marked the existing task **completed**. Follow-up read calls confirmed one opportunity at `Reschedule Needed`, seven cancelled appointments, and task `completed=true`. This **passes the review-assisted cancellation path for the tested synthetic contact**, but does **not** mean the cancellation workflow automatically updated the opportunity stage or that multi-appointment edge cases were tested.

## Source and implementation boundaries

The public repository hosts the static [demo page](../../demos/dublin-painting-ai-chat/index.html) and this case study. The chatbot agent, workflows, pipeline, calendar, and CRM data are configured inside HighLevel; they are **not** represented as source-code implementations within this repository. No invented backend, custom API integration, or production event processor is claimed.


**Post-test state, 18 November 2026:** All six synthetic appointments are cancelled; the single synthetic opportunity is Open at `Reschedule Needed` after a **manual reset**. Automatic cancellation-state handling still needs its own workflow; do not represent this manual reset as an automated outcome.
