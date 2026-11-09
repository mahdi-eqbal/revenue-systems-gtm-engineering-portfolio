# Revenue Systems & GTM Engineering Portfolio

Selected end-to-end implementations across CRM architecture, GTM automation, operational data, qualification and routing, AI-assisted intelligence, reliability, and governance.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Focus](https://img.shields.io/badge/focus-Revenue_Systems-1f2937)
![Discipline](https://img.shields.io/badge/discipline-GTM_Engineering-0f766e)
![CRM](https://img.shields.io/badge/CRM-HubSpot_%7C_Salesforce-2563eb)
![Automation](https://img.shields.io/badge/automation-n8n_%7C_Make-ea4b71)
![Data](https://img.shields.io/badge/data-PostgreSQL_%7C_Supabase-3ecf8e)

> I design revenue infrastructure that turns fragmented product, lead, company, and GTM signals into controlled business decisions—with explicit ownership, persistent state, failure handling, and operational evidence.

**[Explore the live portfolio](https://mahdi-eqbal.github.io/revenue-systems-gtm-engineering-portfolio/)** · **[Try the HandoffTrace synthetic preview](https://handofftrace.htlabs.workers.dev/)**

## Portfolio at a Glance

| System | Revenue problem | Core stack | Primary capability |
|---|---|---|---|
| [P1 — Product-Led Revenue Qualification & Sales Handoff](https://github.com/mahdi-eqbal/p1-product-led-revenue-system) | Product signals do not become reliable sales action | HubSpot, n8n, PostgreSQL/Supabase, APIs, JavaScript | Identity resolution, qualification, deal guards, and sales handoff |
| [P2 — Lead-to-Opportunity Revenue Operations](https://github.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system) | Inbound leads enter the CRM with inconsistent quality, routing, and follow-up | Salesforce, Salesforce Flow, n8n, PostgreSQL/Supabase, APIs | Validation, routing, SLA, CRM identity, and failure handling |
| [P3 — AI-Assisted GTM Intelligence & Account Prioritization](https://github.com/mahdi-eqbal/p3-ai-gtm-intelligence-system) | Target-account lists lack evidence, timing, prioritization, and uncertainty controls | Clay, Claygent, GTM Signals, structured AI, deterministic scoring | Enrichment, evidence-aware research, scoring, and human review |
| [Campaign Learning Engine — controlled experiment learning](https://github.com/mahdi-eqbal/revenue-systems-gtm-engineering-portfolio/tree/main/projects/campaign-learning-engine) | Campaign signals can drive premature conclusions or outreach | n8n, JavaScript, Data Tables | Synthetic-only, review-first outcome analysis |
| [HandoffTrace — standalone assurance product](projects/revenue-leak-monitor/README.md) ([interactive preview](https://handofftrace.htlabs.workers.dev/)) | Automation success does not prove the event-specific lead handoff | Python, Django, CSV, JavaScript | Engine-generated synthetic replay, deterministic event reconciliation, explainable findings and configurable rules; product in development |

These are current selected implementations. The portfolio is not limited to these projects and will expand as additional Revenue Systems capabilities are implemented and validated.

---

## P1 — Product-Led Revenue Qualification & Sales Handoff

[![View Repository](https://img.shields.io/badge/View-Repository-24292f?style=for-the-badge&logo=github)](https://github.com/mahdi-eqbal/p1-product-led-revenue-system)

A product-led B2B SaaS may collect signup and usage signals without a controlled way to convert them into sales action. P1 introduces an operational decision layer that authenticates and validates product events, resolves contact and company identity, calculates product intent, applies deterministic qualification rules, checks existing handoffs and active deals, routes eligible records, and creates an auditable HubSpot sales handoff.

### System Flow

```text
Product Signal
→ Validation & Persistence
→ Identity Resolution
→ Intent + ICP + Data Readiness
→ Qualification
→ Handoff & Active-Deal Guards
→ Routing
→ HubSpot Sales Handoff
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

![P1 complete workflow](https://raw.githubusercontent.com/mahdi-eqbal/p1-product-led-revenue-system/main/evidence/n8n/final-workflow-overview.png)

**Review:** [Architecture](https://github.com/mahdi-eqbal/p1-product-led-revenue-system/tree/main/architecture) · [Workflow](https://github.com/mahdi-eqbal/p1-product-led-revenue-system/tree/main/workflows) · [Evidence](https://github.com/mahdi-eqbal/p1-product-led-revenue-system/tree/main/evidence)

---

## P2 — Lead-to-Opportunity Revenue Operations

[![View Repository](https://img.shields.io/badge/View-Repository-24292f?style=for-the-badge&logo=github)](https://github.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system)

Inbound leads frequently arrive with incomplete data, duplicate submissions, inconsistent qualification, unclear ownership, and no reliable follow-up SLA. P2 controls the lead lifecycle before and during Salesforce handoff, preserving processing state separately from CRM availability.

### System Flow

```text
Inbound Lead
→ Validation & Idempotency
→ Data Readiness
→ Qualification
→ Routing & SLA
→ Salesforce Identity Resolution
→ Lead Reuse or Creation
→ Salesforce Flow Task
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

![P2 complete workflow](https://raw.githubusercontent.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system/main/evidence/n8n/00-final-workflow-architecture.png)

**Review:** [Architecture](https://github.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system/tree/main/architecture) · [Test Matrix](https://github.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system/blob/main/TEST-MATRIX.md) · [Evidence](https://github.com/mahdi-eqbal/p2-lead-to-opportunity-revenue-system/tree/main/evidence/n8n)

---

## P3 — AI-Assisted GTM Intelligence & Account Prioritization

[![View Repository](https://img.shields.io/badge/View-Repository-24292f?style=for-the-badge&logo=github)](https://github.com/mahdi-eqbal/p3-ai-gtm-intelligence-system)

A target-account list does not explain which accounts fit, what recent GTM signals exist, why timing matters, or when AI research is too uncertain for action. P3 combines company enrichment, job-posting signals, Claygent research, structured output, deterministic scoring, and human-review governance.

### System Flow

```text
Target Accounts
→ Company Enrichment
→ GTM Signal Monitoring
→ Signal-to-Account Resolution
→ Evidence-Aware AI Research
→ Deterministic Scoring
→ Human Review Gate
→ Actionable Accounts or Review Queue
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

![P3 actionable accounts](https://raw.githubusercontent.com/mahdi-eqbal/p3-ai-gtm-intelligence-system/main/evidence/clay/09-actionable-accounts-view.png)

**Review:** [Implementation Summary](https://github.com/mahdi-eqbal/p3-ai-gtm-intelligence-system/blob/main/docs/implementation-summary.md) · [Prioritization Model](https://github.com/mahdi-eqbal/p3-ai-gtm-intelligence-system/blob/main/docs/prioritization-model.md) · [Evidence Manifest](https://github.com/mahdi-eqbal/p3-ai-gtm-intelligence-system/blob/main/evidence/EVIDENCE-MANIFEST.md)

---

## HandoffTrace — Standalone Lead Handoff Assurance Product

**Public [interactive synthetic preview v0.5](https://handofftrace.htlabs.workers.dev/) published on 2026-11-03; commercial product remains under active development.** HandoffTrace is a standalone, evidence-first audit product built under the earlier code name Revenue Leak Monitor. It is **not** another CRM workflow or a hosted customer-connected SaaS.

The private Python engine compares source events with CRM evidence, evaluates event identity, ownership, Task and timing expectations under configurable rules, and returns reason codes and next checks. A private local Django application supports saved audits and operator review. The **public site** is a safe, static replay of engine-generated results on five fictional events; it does not accept user records or connect to a CRM.

- **[Try the HandoffTrace interactive preview](https://handofftrace.htlabs.workers.dev/)**
- [Public technical case study](projects/revenue-leak-monitor/README.md)
- [Verification evidence and limitations](projects/revenue-leak-monitor/EVIDENCE.md)
- [Architecture decisions](projects/revenue-leak-monitor/ARCHITECTURE.md)
- [Dated build log](projects/revenue-leak-monitor/BUILD_LOG.md)

Authorized HubSpot Sandbox form/Contact/Task diagnostics have been carried out on bounded synthetic examples, but event-specific source-to-sales follow-up, production integration, continuous monitoring, and customer self-service remain **unverified or unreleased**. A scoped, read-only pilot may be discussed only after feasibility, permission and security reviews. No customer deployment or recovered revenue is claimed.

---

## Capability Matrix — Core Systems and HandoffTrace

The Campaign Learning Engine is a smaller, review-first n8n prototype rather than a full CRM implementation, so it is not included in this comparison. HandoffTrace is a **private product prototype** with a public static demonstration; its evidence-review features should not be confused with production CRM execution.

| Capability | P1 | P2 | P3 | HandoffTrace |
|---|---|---|---|---|
| Main role | Product-led sales handoff | Lead-to-opportunity operations | AI-assisted GTM research | Independent handoff assurance |
| CRM focus | HubSpot | Salesforce | Account signals | Source-event and CRM evidence |
| Event or signal processing | Product events | Inbound leads | GTM signals | Source/CRM snapshot reconciliation |
| Identity controls | Contact and company | Lead and CRM record | Account and signal | Event IDs, repeats, shared-record exceptions |
| Deterministic decisions | Qualification and routing | Qualification and SLA | Scoring and review gates | Evidence findings and reason codes |
| State and auditability | PostgreSQL/Supabase | PostgreSQL/Supabase | Structured Clay tables | Private audit history and rules |
| Integration scope | Implemented HubSpot flows | Implemented Salesforce flows | Clay platform integrations | Selected HubSpot Sandbox reads; no live customer connection |
| SLA/sales follow-up | Creates handoff | Creates CRM Task | Prioritizes accounts | Reviews owner/Task/SLA evidence; does not execute follow-up |
| AI research | — | — | Claygent | Not a released feature |
| Review and limitations | Identity exceptions | Readiness and API failures | Confidence and uncertainty | Explicit evidence bounds and manual checks |
| Public verification | Repository and test evidence | Repository and test evidence | Repository and evidence manifest | Case study, limitations and synthetic public preview |

## Engineering Principles

- The CRM is the revenue lifecycle and execution layer—not the raw event store.
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

They do not represent client deployments, employer projects, paid engagements, production SaaS implementations, or claimed commercial revenue results. The HandoffTrace (formerly Revenue Leak Monitor) commercial source is private and not licensed under this public portfolio's MIT license.

The portfolio is intended to demonstrate practical Revenue Systems and GTM Engineering capability through implemented, tested, documented, and evidence-backed systems.

## Contact

- **GitHub:** [github.com/mahdi-eqbal](https://github.com/mahdi-eqbal)
- **LinkedIn:** [linkedin.com/in/mahdi-eqbal-b50329296](https://www.linkedin.com/in/mahdi-eqbal)
- **Email:** [m.mahdi.eqbal@gmail.com](mailto:m.mahdi.eqbal@gmail.com)

---

Built and maintained by [Mahdi Eqbal](https://github.com/mahdi-eqbal).

