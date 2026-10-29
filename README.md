# Revenue Systems & GTM Engineering Portfolio

Selected end-to-end implementations across CRM architecture, GTM automation, operational data, qualification and routing, AI-assisted intelligence, reliability, and governance.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Focus](https://img.shields.io/badge/focus-Revenue_Systems-1f2937)
![Discipline](https://img.shields.io/badge/discipline-GTM_Engineering-0f766e)
![CRM](https://img.shields.io/badge/CRM-HubSpot_%7C_Salesforce-2563eb)
![Automation](https://img.shields.io/badge/automation-n8n_%7C_Make-ea4b71)
![Data](https://img.shields.io/badge/data-PostgreSQL_%7C_Supabase-3ecf8e)

> I design revenue infrastructure that turns fragmented product, lead, company, and GTM signals into controlled business decisionsâ€”with explicit ownership, persistent state, failure handling, and operational evidence.

## Portfolio at a Glance

| System | Revenue problem | Core stack | Primary capability |
|---|---|---|---|
| [P1 â€” Product-Led Revenue Qualification & Sales Handoff](https://github.com/mahdi-eqbal/p1-product-led-revenue-system) | Product signals do not become reliable sales action | HubSpot, n8n, PostgreSQL/Supabase, APIs, JavaScript | Identity resolution, qualification, deal guards, and sales handoff |
| [P2 â€” Lead-to-Opportunity Revenue Operations](https://github.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system) | Inbound leads enter the CRM with inconsistent quality, routing, and follow-up | Salesforce, Salesforce Flow, n8n, PostgreSQL/Supabase, APIs | Validation, routing, SLA, CRM identity, and failure handling |
| [P3 â€” AI-Assisted GTM Intelligence & Account Prioritization](https://github.com/mahdi-eqbal/p3-ai-gtm-intelligence-system) | Target-account lists lack evidence, timing, prioritization, and uncertainty controls | Clay, Claygent, GTM Signals, structured AI, deterministic scoring | Enrichment, evidence-aware research, scoring, and human review |

| [Campaign Learning Engine — controlled experiment learning](https://github.com/mahdi-eqbal/revenue-systems-gtm-engineering-portfolio/tree/main/projects/campaign-learning-engine) | Campaign signals can drive premature conclusions or outreach | n8n, JavaScript, Data Tables | Synthetic-only, review-first outcome analysis |
| [Revenue Leak Monitor — product in development](https://github.com/mahdi-eqbal/revenue-systems-gtm-engineering-portfolio/tree/main/projects/revenue-leak-monitor) | Successful automation can still leave an unverified or overdue lead handoff | Python, Django, CSV, GitHub Actions | Read-only reconciliation, explainable evidence, versioned SLA profiles |

These are current selected implementations. The portfolio is not limited to these projects and will expand as additional Revenue Systems capabilities are implemented and validated.

---

## P1 â€” Product-Led Revenue Qualification & Sales Handoff

[![View Repository](https://img.shields.io/badge/View-Repository-24292f?style=for-the-badge&logo=github)](https://github.com/mahdi-eqbal/p1-product-led-revenue-system)

A product-led B2B SaaS may collect signup and usage signals without a controlled way to convert them into sales action. P1 introduces an operational decision layer that authenticates and validates product events, resolves contact and company identity, calculates product intent, applies deterministic qualification rules, checks existing handoffs and active deals, routes eligible records, and creates an auditable HubSpot sales handoff.

### System Flow

```text
Product Signal
â†’ Validation & Persistence
â†’ Identity Resolution
â†’ Intent + ICP + Data Readiness
â†’ Qualification
â†’ Handoff & Active-Deal Guards
â†’ Routing
â†’ HubSpot Sales Handoff
```

### Key Controls

- authenticated webhook ingress;
- durable event persistence;
- event-level idempotency;
- email and product-user identity resolution;
- rolling product-intent state;
- deterministic qualification;
- duplicate-handoff protection;
- active-deal suppression;
- retry-safe completion and audit history.

![P1 complete workflow](https://raw.githubusercontent.com/mahdi-eqbal/p1-product-led-revenue-system/master/evidence/n8n/final-workflow-overview.png)

**Review:** [Architecture](https://github.com/mahdi-eqbal/p1-product-led-revenue-system/tree/master/architecture) Â· [Workflow](https://github.com/mahdi-eqbal/p1-product-led-revenue-system/tree/master/workflows) Â· [Evidence](https://github.com/mahdi-eqbal/p1-product-led-revenue-system/tree/master/evidence)

---

## P2 â€” Lead-to-Opportunity Revenue Operations

[![View Repository](https://img.shields.io/badge/View-Repository-24292f?style=for-the-badge&logo=github)](https://github.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system)

Inbound leads frequently arrive with incomplete data, duplicate submissions, inconsistent qualification, unclear ownership, and no reliable follow-up SLA. P2 controls the lead lifecycle before and during Salesforce handoff, preserving processing state separately from CRM availability.

### System Flow

```text
Inbound Lead
â†’ Validation & Idempotency
â†’ Data Readiness
â†’ Qualification
â†’ Routing & SLA
â†’ Salesforce Identity Resolution
â†’ Lead Reuse or Creation
â†’ Salesforce Flow Task
```

### Key Controls

- invalid-lead rejection;
- incomplete-data review routing;
- deterministic ICP and buying-intent qualification;
- event identity separated from lead identity;
- Salesforce Lead lookup before creation;
- SLA state persisted before CRM handoff;
- CRM-native follow-up task;
- explicit API retry and failure states.

![P2 complete workflow](https://raw.githubusercontent.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system/master/evidence/n8n/00-final-workflow-architecture.png)

**Review:** [Architecture](https://github.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system/tree/master/architecture) Â· [Test Matrix](https://github.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system/blob/master/TEST-MATRIX.md) Â· [Evidence](https://github.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system/tree/master/evidence/n8n)

---

## P3 â€” AI-Assisted GTM Intelligence & Account Prioritization

[![View Repository](https://img.shields.io/badge/View-Repository-24292f?style=for-the-badge&logo=github)](https://github.com/mahdi-eqbal/p3-ai-gtm-intelligence-system)

A target-account list does not explain which accounts fit, what recent GTM signals exist, why timing matters, or when AI research is too uncertain for action. P3 combines company enrichment, job-posting signals, Claygent research, structured output, deterministic scoring, and human-review governance.

### System Flow

```text
Target Accounts
â†’ Company Enrichment
â†’ GTM Signal Monitoring
â†’ Signal-to-Account Resolution
â†’ Evidence-Aware AI Research
â†’ Deterministic Scoring
â†’ Human Review Gate
â†’ Actionable Accounts or Review Queue
```

### Key Controls

- real and synthetic record separation;
- multi-row signal-to-account lookup;
- evidence and inference separation;
- structured AI output preservation;
- deterministic post-AI scoring;
- signal-recency logic;
- confidence and uncertainty handling;
- manual review before uncertain action.

![P3 actionable accounts](https://raw.githubusercontent.com/mahdi-eqbal/p3-ai-gtm-intelligence-system/master/evidence/clay/09-actionable-accounts-view.png)

**Review:** [Implementation Summary](https://github.com/mahdi-eqbal/p3-ai-gtm-intelligence-system/blob/master/docs/implementation-summary.md) Â· [Prioritization Model](https://github.com/mahdi-eqbal/p3-ai-gtm-intelligence-system/blob/master/docs/prioritization-model.md) Â· [Evidence Manifest](https://github.com/mahdi-eqbal/p3-ai-gtm-intelligence-system/blob/master/evidence/EVIDENCE-MANIFEST.md)

---

## Revenue Leak Monitor — Private Commercial Product, Public Engineering Record

**In development (local v0.4 milestone; not customer production-ready).** The proprietary Revenue Leak Monitor source remains in a **private repository**. A separate public case study shares the engineering rationale, synthetic-data validation, the limits of current tests, and an honest chronology of the build without revealing commercial source code.

- [Public technical case study](projects/revenue-leak-monitor/README.md)
- [Verification evidence and limitations](projects/revenue-leak-monitor/EVIDENCE.md)
- [Dated build log](projects/revenue-leak-monitor/BUILD_LOG.md)
- [Architecture decisions](projects/revenue-leak-monitor/ARCHITECTURE.md)

The prototype reconciles source and CRM exports, explains exceptions and provides versioned operational rules through a local Django application. An experimental HubSpot contact-read adapter has **only** been tested with mock API responses. No customer CRM deployment or revenue recovery is claimed.

---

## Capability Matrix

| Capability | P1 | P2 | P3 |
|---|:---:|:---:|:---:|
| CRM architecture | HubSpot | Salesforce | â€” |
| Event or signal processing | Product events | Inbound lead events | GTM signals |
| Identity resolution | Contact and company | Lead and CRM record | Account and signal |
| Deterministic qualification/scoring | Yes | Yes | Yes |
| Operational database state | PostgreSQL/Supabase | PostgreSQL/Supabase | Structured Clay tables |
| API/webhook integration | Yes | Yes | Platform integrations |
| Idempotency/duplicate controls | Yes | Yes | Record and signal controls |
| SLA/sales execution | Sales handoff | Salesforce task and SLA | Actionable-account delivery |
| AI-assisted research | â€” | â€” | Claygent |
| Human review | Identity exceptions | Data readiness | Confidence and uncertainty |
| Test/evidence package | Yes | Yes | Yes |

## Engineering Principles

- The CRM is the revenue lifecycle and execution layerâ€”not the raw event store.
- Operational state must survive transient workflow execution and integration failure.
- Deterministic rules should control repeatable business decisions.
- AI-generated research should expose evidence, inference, confidence, and uncertainty.
- Duplicate events, missing data, partial failures, and retry behavior are architecture requirements.
- Evidence is part of implementation, not an afterthought added during packaging.

## Technology Coverage

| Area | Tools and methods |
|---|---|
| CRM & RevOps | HubSpot, Salesforce, HubSpot Workflows, Salesforce Flow |
| Automation | n8n, Make, event-driven and scheduled workflows |
| Data | PostgreSQL, Supabase, SQL, operational state, audit trails |
| Integration | REST APIs, webhooks, JSON, authentication, pagination, JavaScript |
| GTM Intelligence | Clay, Claygent, enrichment, GTM signals, ICP rules, deterministic scoring |
| Reliability | Idempotency, validation, retries, failure paths, testing, observability |
| Governance | Source-of-truth design, architecture decisions, human review, evidence capture |

## Project Positioning

These projects and the in-development product are documented engineering implementations using synthetic or public-safe evidence. Some were built with AI-assisted implementation, guided by explicit engineering requirements and local validation.

They do not represent client deployments, employer projects, paid engagements, production SaaS implementations, or claimed commercial revenue results. The Revenue Leak Monitor source is private and not licensed under this public portfolio's MIT license.

The portfolio is intended to demonstrate practical Revenue Systems and GTM Engineering capability through implemented, tested, documented, and evidence-backed systems.

## Contact

- **GitHub:** [github.com/mahdi-eqbal](https://github.com/mahdi-eqbal)
- **LinkedIn:** [linkedin.com/in/mahdi-eqbal-b50329296](https://www.linkedin.com/in/mahdi-eqbal-b50329296)
- **Email:** [m.mahdi.eqbal@gmail.com](mailto:m.mahdi.eqbal@gmail.com)

---

Built and maintained by [Mahdi Eqbal](https://github.com/mahdi-eqbal).

