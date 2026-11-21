# Kajabi Workflow Lab Academy — controlled QA evidence

**Review dates:** 20–21 November 2026  
**Environment:** Independent Kajabi trial/test implementation, fictional learning business, controlled test contacts  
**Evidence classification:** Account configuration + observed contact/automation states + separately confirmed recipient-inbox message.

## Verified observations

| Test | Observed evidence | Status |
| --- | --- | --- |
| Published landing and resource pages | Both pages returned HTTP 200 without an authenticated administrator session in the 20 Nov Work review | Observed |
| Form + Double Opt-in | Confirmation email received; confirmed/subscribed test contact appeared in Kajabi | Verified in controlled test |
| Consent-positive enrollment | Published conditional workflow applied the project tag and the contact appeared Active in the three-email sequence | Verified in controlled test |
| Consent-negative enrollment | The tested no-consent resubmission did not increase sequence enrollment | Verified for the specified case |
| Resource access | Confirmation link opened the published Starter Kit page in the browser | Verified in controlled test |
| **Day 0 marketing email inbox delivery** | **`Your AI Productivity Starter Kit`** appeared in the Gmail recipient inbox on **21 Nov 2026** after the test opt-in and confirmation; the received body included the welcome, three example AI prompts, checklist and email-preferences link | **Verified** |
| Day 2 sequence email | Configured/scheduled for Day 2; delivery was not due at the 21 Nov review | Pending scheduled observation |
| Day 4 sequence email | Configured/scheduled for Day 4; delivery was not due at the 21 Nov review | Pending scheduled observation |
| Unsubscribe / opt-out after enrollment | No completed, separately documented unsubscribe-delivery test | Not independently verified |

### Recipient-side Day 0 evidence

The Gmail message was opened and read directly through authorized account access rather than inferred from Kajabi's `Sent` metric.

- **Subject:** Your AI Productivity Starter Kit
- **Recipient:** controlled Gmail test alias (redacted in public documentation)
- **Gmail timestamp:** 21 Nov 2026, 08:20 UTC
- **Mailbox location:** Inbox / Updates
- **Observed content:** Welcome to Workflow Lab Academy; three AI productivity prompts; a checklist; preferences-management link
- **Privacy:** The raw private Gmail message, recipient address, and Kajabi account details are not copied into the public repository.

This verifies successful receipt of **one Day 0 message by one test inbox**. It is not a general deliverability-rate measurement or proof that Day 2/Day 4 emails have been received.

### Delivery investigation

Earlier testing on 20 Nov found sequence `Sent` entries without confirmed inbox delivery. Kajabi Support subsequently identified an **incomplete Marketing Contact Address** under **Settings > Marketing Settings** as an outbound marketing-email blocker. Following the account investigation and the fresh Nov 21 test, Day 0 was observed in Gmail.

The confirmed receipt establishes the current Day 0 test outcome; it does **not** retrospectively prove that previously unreceived sends were delivered.

### Open checks

1. Verify Day 2 email receipt after its scheduled date (**23 Nov 2026** according to the Work test plan).
2. Verify Day 4 email receipt after its scheduled date (**25 Nov 2026** according to the Work test plan).
3. If this project is used as a customer deployment reference, test opt-out behavior, mobile public-form submission and recipient-domain variation in the appropriate client environment.

**Scope statement:** This is an independent demo; no paid client deployment, production-conversion improvement or broad email-delivery performance is claimed.
