# HandoffTrace — Public development log (HandoffTrace legacy name)

This log is a **truthful, retrospective milestone record** followed by ongoing public documentation. It does not claim that each local milestone was a separate GitHub commit.
| Period | Milestone | What was actually verified | Remaining limitation |
|---|---|---|---|
| October 2026, prior to GitHub import | v0.1 Python reconciliation engine | Synthetic CSV matching, classification and baseline unit tests | No web app or live CRM |
| October 2026, prior to GitHub import | v0.2 local Django web app | Local sign-in, upload, audit, saved history, CSV/JSON exports | Not a hosted deployment |
| October 2026, prior to GitHub import | v0.3 explainable findings and Rule Profiles | Local rule-profile creation, change from four- to 24-hour SLA, observed different classifications | Complete-source coverage manually declared |
| October 2026, prior to GitHub import | v0.4 reliability and connector foundation | Pending/breach distinction; mocked HubSpot contact-read adapter; independent Python tests | No customer CRM access or multi-tenant service |
| 2026-10-29 | First **private GitHub** baseline of v0.4 | One recorded import commit; GitHub Actions execution on three Python versions | Earlier v0.1–v0.3 work **was not** separate GitHub history |
| 2026-10-29 | Private security hardening merged after review | Browser-cache protection on authenticated reports/configuration; regression test added; private PR passed CI on Python 3.11–3.13 and was merged to the commercial codebase | Response headers are a limited safeguard; no production security certification or multi-tenant deployment |
| 2026-10-29 | First **public GitHub** case-study publication | This public evidence pack, architecture note and portfolio entry | Public documentation only, no proprietary source or live demo hosting |
| 2026-10-29 | v0.5 development candidate — workspace isolation foundation | Private code PR reviewed and merged; one operator can separate multiple clients' audit histories and rule profiles. GitHub CI passed on Python 3.11/3.12/3.13, including 21 Django integration/migration tests and preservation of legacy policy/report snapshots | Development code only; Windows installation still v0.4. Not a production-ready multi-user tenant or a live CRM integration |
| 2026-10-29 | v0.5 Windows backup-and-migration rehearsal tool | Private-code PR reviewed and merged after synthetic SQLite backup and disposable-copy migration tests passed: 71 Python and 21 Django tests across Python 3.11–3.13 | The owner’s real Windows installation has NOT been upgraded or rehearsed yet; BAT launcher not yet tested on-device. A separate live-upgrade and rollback gate remains open |
| 2026-10-29 | Windows-specific migration rehearsal defect fixed | The first on-device backup-only rehearsal exposed a Windows temporary-file lock; private source was patched to close SQLite handles, and synthetic rehearsal subsequently passed on a Windows GitHub Actions runner plus the three existing Linux Python jobs | Actual Windows installation has **not** yet been re-tested with the patched tool. Original database was not upgraded |
| 2026-10-29 | Local Windows rehearsal accepted; separate v0.5 preview prepared | Actual Windows backup and disposable migration returned PASS, the original database remained unchanged; a subsequent private-code change added an isolated v0.5 preview based on the verified backup, with Windows and Linux synthetic CI success | Preview UI has not yet been checked on the owner's Windows PC; v0.4 remains installed and no live overwrite occurred |
| 2026-10-29 | v0.5 on-device workspace acceptance | The owner's isolated Windows preview opened preserved saved reports and a versioned rule profile; a second synthetic client workspace showed empty audit/profile lists; requesting an original-workspace report URL while in the second workspace returned HTTP 404 | Verified only on local synthetic-data preview and private regression tests, not production multi-tenant hosting; debug diagnostics remain enabled locally |
| 2026-10-29 | Local/deployment configuration security controls | Private code change passed CI on Linux Python 3.11-3.13 and Windows; the local preview now rejects remote clients and production-shaped settings reject insecure defaults | Preventative configuration safeguards only, not approval for hosting, real client data or production multi-tenant use |
| 2026-10-29 | HubSpot read-only connector safety tests | Private CI passed including 22 Windows synthetic tests; malformed API pagination, duplicate event-to-contact correlations and concurrent CSV export collisions are rejected. A date-versioned read path is optionally supported | No live HubSpot sandbox/tenant access or complete task-evidence collection; not a working customer integration |
| 2026-10-29 | HubSpot Task candidate evidence reader | Private GET-only connector code passed three Linux Python CI environments and 36 Windows synthetic tests; collects bounded associated Task IDs, creation times and status candidates without silently treating them as event-specific follow-up | Not connected to live HubSpot, web UI or certified task-completeness evidence. Contact association alone cannot prove a particular lead was followed up |

| 2026-10-29 | Revenue Assurance UI v1 — responsive design foundation | Private code PR merged after passing three Linux Python CI jobs and the Windows regression suite; redesigned home, audit KPIs, evidence table, navigation, saved history, rule profiles and workspaces, with accessible focus and mobile layout rules | Automated HTML/CSS tests are not visual QA; desktop/mobile browser acceptance still pending. Source, data and engine rules remain private |

## Newer checkpoints — evidence and public-preview release

The earlier entries above are **dated historical checkpoints**; phrases such as “not yet hosted,” “not tested on-device,” or “no sandbox call” describe what was known **at that particular milestone**, not the current status.

| Date | Milestone | Observed evidence | Still not proven |
|---|---|---|---|
| 2026-10-30 | HubSpot selected native Form export acceptance | Three independent synthetic form submissions observed 3/3 in an owner-selected export; two referenced one Contact, the third a different Contact | Historical source completeness, production OAuth and exact event-to-Task follow-up |
| 2026-10-31 | Review continuity and private operator triage | Source-controlled local/private tests for immutable audit comparison, workspace-scoped Review Board and non-writing repair-readiness output | Hosted customer-safe workflows, actual corrective CRM writes |
| 2026-10-31–2026-11-01 | Controlled HubSpot read-only acceptance | Restricted Sandbox OAuth and bounded Contact/Task candidate diagnostics; source API coverage concerns remained fail-closed | Comprehensive form-history pagination, verified source-event → Task/owner lineage, production credential lifecycle |
| 2026-11-01 | Commercial V1 release gates defined | Explicit checklist covering authorized source identity, complete evidence, secure production operation and regression | These gates are not all passed; no production customer onboarding |
| 2026-11-03 | HandoffTrace branded public static preview v0.5 | Engine-based synthetic one-file build; 10 targeted local pytest checks passed; release-preflight PASS; owner screenshots of desktop and 390px mobile; Incognito opened public `workers.dev` address | Browser-only synthetic replay, not live CRM ingestion, monitoring, payments or customer audits |
| 2026-11-03 | Public documentation synchronization | Case study, architecture, evidence and public portfolio entry updated to reflect published HandoffTrace name and preview | Public docs do not disclose the proprietary code or certify customer readiness |

**Public preview:** https://handofftrace.htlabs.workers.dev/  
**Public technical record:** [Overview](README.md) · [Architecture](ARCHITECTURE.md) · [Evidence](EVIDENCE.md)

The **public** product name is HandoffTrace; the `revenue-leak-monitor` URL path remains as a historical compatibility link. Any alternative prototype branch, draft pull request, or future roadmap item should not be described as an already deployed customer capability.

## Future update standard

For every **subsequent** change that deserves a public claim:

1. Make the change in the **private source repository**, on a feature branch with a reviewed Pull Request.
2. Run automated tests and capture a dated, non-sensitive acceptance outcome.
3. Record what was **implemented**, what was **verified**, and what is **not yet verified**.
4. Update this public log with a concise milestone and link to **public** evidence where available; do not expose private branches, code or client data.
5. If a customer-facing demo is released, distinguish the public fictional demo from private customer processing.

This creates an honest, growing GitHub record of the project without rewriting history or exposing the commercial codebase.

**Responsible engineering direction:** Mahdi Eqbal; implementation includes AI-assisted development and human validation of local test outcomes.
