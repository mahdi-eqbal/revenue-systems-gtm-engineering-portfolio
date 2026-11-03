# HandoffTrace — Public validation evidence and limits

**Updated:** 2026-11-03. **Project:** HandoffTrace, originally developed under the Revenue Leak Monitor name. **Evidence levels are deliberately separate:** public synthetic replay, local engine/browser checks, selected authorized HubSpot Sandbox observations, and unverified production/customer claims.

**Public preview:** https://handofftrace.htlabs.workers.dev/

## Evidence summary as of 2026-11-03

| Claim | Observed evidence | Boundary / what it does not prove |
|---|---|---|
| Public product preview is viewable | Owner supplied desktop screenshots of the hosted `workers.dev` site and a successful Chrome Incognito opening without Cloudflare account sign-in | This demonstrates browser access on that occasion, not independent uptime, geographic availability or a secured customer service |
| Public sample data comes from the implemented audit engine | Private build runs deterministic reconciliation on pinned fictional fixture data before emitting one HTML file; release-preflight checks content boundaries | Visitors interact with **precomputed output**, not with the live Python engine or a customer dataset |
| Five fictional event outcomes are inspectable | Five distinct source events from six source rows and three CRM rows; two handoff-evidence findings, two review exceptions, one intentional exclusion, with a repeated event deduplicated | No customer leads, lost revenue, completed prospect contact or operational completeness implied |
| Fixed preview navigation/filtering works | Owner reviewed desktop at approximately 1366px and a mobile 390px full-page capture; local preview displayed interactive evidence cases | Visual review is not exhaustive accessibility or cross-browser acceptance |
| Static release checks passed locally | On 2026-11-03 owner ran `pytest tests/test_showcase.py tests/test_showcase_release_preflight.py -q`: **10 passed**, followed by build and `verify_showcase_release.py`: **PASS** | Only this subset and generated artifact were observed; not a full production or customer-data regression |
| Request Pilot action opens an email handler | Screenshot of Windows choosing an email application when the CTA was clicked | Does not prove delivery of an inquiry or functioning email on every device |
| Configurable rules affect the engine's outcome | Earlier private/local checks of versioned rule profiles and a 4-hour versus 24-hour Task-SLA assessment on otherwise unchanged synthetic data | Public preview has **no** customer rule editor or live audit configuration |
| Internal Django operator features exist | Earlier local Windows and private-test observations of authenticated audits, workspace-scoped reports, saved run history, read-only review and exports | Not a publicly deployed multi-tenant SaaS, authorization certification or customer-safe data-processing environment |

## Selected real HubSpot Sandbox evidence — narrow and explicit

Controlled, owner-authorized experiments progressed beyond the original mocked Contact adapter:

- **2026-10-30:** Three synthetic Form submissions were sent to a separately controlled test account. A selected **operator-exported native HubSpot Form CSV** contained the three independent probe tokens and distinct Conversion IDs (**3/3** in that selected file). Two submissions referred to the **same Contact**, and one to another Contact (**two distinct Contacts**). This demonstrates the event-versus-Contact identity distinction in one bounded export, **not complete source coverage**.
- **2026-10-31 to 2026-11-01:** Restricted sandbox OAuth and bounded, read-only Contact/Task diagnostics were exercised in a controlled environment. Three selected Task IDs were read for candidate metadata. Contact–Task association is **not** equivalent to proven event-attributed sales follow-up.
- **Form history/API pagination:** Repeated offsets and missing trustworthy termination/completeness evidence prevented an end-to-end API coverage claim. Under such conditions the safe conclusion is **unknown / review required**, not “lead missing.”
- OAuth credential-vault, guarded refresh, restore containment and fencing designs have isolated synthetic/private regression evidence. These are **not** certifications of a hosted credential-management service or approval to connect customer production portals.

**Not established:** independent historical submission completeness; an unambiguous event → form → CRM record → eligible owner → event-specific Task → actual human follow-up chain; production scopes, recovery, or universal HubSpot tenant support.

## Experimental Salesforce status

The private code includes bounded GET-only inventory for Lead, Contact and Task metadata and conservative normalization. It is **not** linked to a public customer OAuth flow or validated end-to-end against an authorized live Salesforce organization. A Task related to a person is not proof it was created for the source event.

## Historical development acceptance record

These dated observations remain useful, but should not be interpreted as the **current** hosting or integration state.

| Period | Recorded private/local development observation | Important qualification |
|---|---|---|
| v0.1, October 2026 | Deterministic Python CSV reconciliation with 43 reported local unit checks | Not end-to-end customer cases |
| v0.2, October 2026 | Local Django audit page, sign-in, uploads, saved history and exports | Local development only |
| v0.3, October 2026 | Explainable findings and versioned policy profiles; 4h versus 24h synthetic SLA outcome changed as expected | Policy-dependent synthetic evidence, not real customer validation |
| v0.4, October 2026 | Mocked connector and pending-versus-overdue distinction with local tests | Mock results not proof of provider behavior |
| 2026-10-29 | Private GitHub baseline, CI on multiple Python versions, v0.5 workspace and upgrade regression | Private workflow details are not publicly reproducible from this case study |
| 2026-10-29 | Owner-observed isolated Windows preview, preserved historical reports/profile and cross-workspace 404 | Not multi-tenant penetration testing or hosted service |
| 2026-10-31 | Internal private operator review board, read-only repair-readiness preview and synthetic secure-credential controls | None authorizes CRM writes, customer processing or autonomous repairs |
| 2026-11-03 | v0.5 static synthetic product page built, preflight PASS, public browser screenshot and Incognito check | The public page remains a demonstration rather than a live audit system |

## What the system deliberately does not infer

- A workflow success code means that the right salesperson received or contacted the lead.
- A Task associated with a Contact is automatically proof for every submission by that Contact.
- A missing CRM record in a **selected snapshot** necessarily means the lead was lost.
- An operator-declared complete source/CRM export is independently verified complete.
- A synthetic rule passing means revenue was recovered or real money was lost.
- A local encrypted-vault test and CI pass mean all security, restore, KMS and customer-onboarding gates are satisfied.
- The published static page can accept production data, connect to HubSpot/Salesforce, remediate CRM records or send alerts.

## Read-only managed-pilot release gates

Before any use of real customer records, the project must accept the specifically relevant requirements for the proposed scope: owner authorization, source coverage, exact event-specific correlation, tenant/role isolation, secure file/secret handling, approved nondevelopment hosting, backup/recovery, data retention, and end-to-end regression. Customer data must **not** be uploaded to the public preview or emailed to request a pilot.

## How technical reviewers can assess the work

1. Explore the [public fictional demonstration](https://handofftrace.htlabs.workers.dev/) and its reason codes.
2. Read [the architecture choices](ARCHITECTURE.md) and [dated development milestones](BUILD_LOG.md).
3. Request a controlled technical walkthrough to discuss requirements, the selected-data limitations and possible read-only pilot evidence.

**Source/test limitation:** Proprietary code and most private tests are not public, so this GitHub case study cannot independently establish every internal implementation claim. The descriptions above distinguish owner-observed results from source-level/private verification.

[Return to HandoffTrace overview](README.md).
