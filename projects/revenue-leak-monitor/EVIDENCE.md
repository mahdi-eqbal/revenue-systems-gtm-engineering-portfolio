# Revenue Leak Monitor — Public verification record

**Evidence scope:** Fictional input data, observed local application behavior and CI metadata. No live customer data, commercial deployment or revenue-recovery claims.

## Recorded local acceptance tests
| Check | Observed outcome | Evidence level |
|---|---|---|
| CSV reconciliation, five unique events from six source rows and three CRM rows | Two verified handoffs; one missing CRM record; one owner-related exception; one intentional exclusion; duplicated E105 evaluated once | Local Windows web UI and CSV/JSON export reviewed |
| Source/CRM upload, authentication and report rendering | Local Django app rendered an authenticated saved run | User-verified browser session |
| CSV and JSON exports | Five findings; matching event IDs, reason codes and statuses | Exports were compared against the synthetic test fixture |
| Saved audit history | Prior report appeared in My runs and reopened | User-verified browser session |
| Versioned client rule profile | Demo Agency A created with four-hour task SLA; profile changed to v2 with 24-hour SLA | User-verified browser session |
| Three-record SLA boundary test: four-hour rule | 2 records needed review, 1 handoff verified | Local UI screenshot reviewed |
| Same inputs: 24-hour rule | 1 needed review, 2 handoffs verified; one task remained absent but was not overdue | Local UI screenshot reviewed |
| Private source repository import | One baseline commit covering v0.4 source and tests | GitHub private-repository metadata verified |
| GitHub Actions | Baseline CI and PR CI green; PR jobs were verified as successful for Python 3.11, 3.12 and 3.13 | GitHub workflow status in private repository; **not publicly inspectable** |
| v0.5 client workspace controls | Same-operator client A/B report, download, deletion and rule-profile access was tested with forged workspace identifiers and cross-client URLs. Unauthorized access was rejected | Private GitHub-hosted Django integration suite; synthetic records |
| v0.5 migration backfill | Legacy v0.4 user-specific reports and rule profiles were migrated to separate Personal workspaces in an isolated test database; existing policy/report JSON remained unchanged | MigrationExecutor regression test, not yet performed on owner's working Windows database |
| v0.5 Windows backup and copy-only migration rehearsal | Synthetic v0.4 SQLite records backed up and verified; migration ran on a disposable copy, historical account/report/profile fingerprints matched, and unsafe path/already-migrated inputs were rejected | Private CI: 71 Python tests and 21 Django tests on 3 Python versions; no on-device Windows acceptance yet |
| v0.5 local Windows workspace acceptance | Preserved historical saved reports and v2 profile remained accessible in the original workspace; a separate synthetic workspace had empty audit/profile lists; direct URL to an original-workspace report returned HTTP 404 while the second workspace was active | Owner-provided localhost screenshots and existing private CI; not a penetration test or production authorization assessment |
| v0.5 local/deployment configuration gate | Automated checks reject non-loopback local requests, unsafe local Host settings and insecure production-mode environment configuration | Private CI passed on Python 3.11-3.13 and Windows regression; not a production deployment security assessment |
| HubSpot connector resilience (synthetic only) | Rejects invalid pagination data, duplicate source event keys across contacts, and concurrent overwrite of CRM CSV snapshots; GET-only optional API path tested with mocks | Private Linux Python CI and Windows regression suite passed; no live API integration verified |
| Contact–Task candidate evidence (synthetic only) | A bounded GET-only reader retrieves associated Task IDs plus creation timestamps, status and owner metadata, while refusing to claim lead-specific follow-up or task completeness; HTTP failures and malformed IDs/pages abort | Private 3× Linux CI plus 36 Windows synthetic regression tests passed; no live HubSpot calls or completed follow-up evidence |

| UI v1 template and responsive stylesheet regression | Synthetic demo, evidence drill-down, empty workspace/profile states, semantic navigation and mobile CSS breakpoints verified through automated private CI | Browser pixel/contrast/mobile usability testing not yet performed; private PR merged without altering data or engine logic |

**Interpretation:** The SLA test demonstrates that changing a rule changes the engine's decision on the *same* synthetic data. It is **not** a production-service reliability benchmark.

## Baseline development and test history

- v0.1: deterministic CLI reconciliation and unit tests (43/43 reported successful during local development).
- v0.2: Django app and audit-service testing (53/53 independent tests reported successful); local browser execution subsequently verified.
- v0.3: versioned rule profiles and explanatory output (56/56 independent tests reported successful); four-versus-24-hour boundary behavior verified in the app.
- v0.4: clearer pending/overdue/unverifiable semantics and isolated mocked HubSpot contact reader (68/68 independent tests reported successful); private GitHub CI subsequently passed.

**Important:** These are development milestones and test observations. Versions v0.1–v0.4 were not individually published as GitHub commits when first developed. They were imported as a single private baseline at v0.4 on 2026-10-29. See [the build log](BUILD_LOG.md). The unit-test counts are not claims of 68 end-to-end customer scenarios.

## Representative coverage

The regression design includes exact matching, conflicting duplicate event IDs, incomplete or stale snapshots, missing CRM records, ambiguous matches, unknown owners, pending sync windows, absent or late task evidence, evidence timestamps beyond the snapshot, CSV export safety, access-control failures and rule-profile versioning.

### Claims we explicitly do not make

- That a green workflow or a task record proves an actual salesperson contacted a lead.
- That a record mismatch equals a lost lead, a lost deal or a quantified amount of lost revenue.
- That every HubSpot account can be reconciled without a shared identifier.
- That an operator's declaration of a complete snapshot has been independently proven.
- That the mocked HubSpot reader is a fully working live OAuth/task connector.
- That per-user Django ownership is equivalent to tested multi-company SaaS isolation.
- That synthetic-data performance proves hosted production scalability.

## How technical reviewers can evaluate the work

The public materials describe **problem framing, test boundaries, engineering decisions and observed outputs**. Detailed implementation, test runs and code review history remain private for commercial-IP protection. A controlled, synthetic-only demonstration or guided technical walkthrough can be arranged; a public case study alone cannot independently prove every internal implementation detail.

No proprietary source, private workflow log, token, customer record, machine path, API endpoint credential, or sensitive screenshot is published in this evidence record.
