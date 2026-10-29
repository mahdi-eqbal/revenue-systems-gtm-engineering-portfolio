# Revenue Leak Monitor — Public architecture decisions

This document summarizes design reasoning. It intentionally omits proprietary source, internal rule tables, private access details, credentials and customer-specific configurations.

## Decision 1 — Independent assurance layer, not another CRM

The product compares evidence from a source of lead events with separately obtained evidence from a CRM/sales process. It is a *reader and verifier* in the current milestone, not a replacement for Salesforce, HubSpot, Make or n8n.

**Why:** A workflow's successful execution and a CRM contact's existence are necessary data points in some workflows, not sufficient proof of the expected operational result.

## Decision 2 — Deterministic reconciliation before ML/AI matching

The prototype requires an explicit shared source event identifier and declared expected record cardinality. Ambiguous or missing evidence is reported as uncertainty or an exception rather than silently guessed.

**Why:** Operational audits require reproducible and explainable findings. A visually appealing score is less useful than a traceable decision that an operator can inspect.

**Known trade-off:** Not all customer systems preserve a common event key. Identity strategies for more complex paths will require separate adapters and explicit validation, not optimistic assumptions.

## Decision 3 — Time is part of the evidence

Different timestamps describe when a source event happened, when a CRM snapshot was taken, when follow-up evidence appeared and when an audit was evaluated. A missing task *before* its deadline is different from a missing task *after* a complete and timely snapshot.

**Why:** Without this separation, an audit can create false overdue or missing-lead alerts.

## Decision 4 — Version rules without rewriting history

Per-run policy snapshots identify the rule version and relevant evidence boundary used for a decision. Reusable client profiles provide defaults; a later rule change should not silently mutate the findings stored for an older audit.

**Why:** Customers need to explain why the system classified the same event differently under different operational policies.

## Decision 5 — Modular monolith and controlled extension points

A framework-independent Python reconciliation engine is kept separate from a Django web adapter and future source/CRM connectors. PostgreSQL and hosted multi-workspace isolation are planned production architecture, **not** features claimed as completed in the local v0.4 milestone.

**Why:** A small commercial beta benefits from traceability and low operational complexity. Additional connectors and rule modules should extend a tested contract rather than require a rewrite of the decision engine.

## Decision 6 — Commercial source stays private

The source repository uses private visibility, source-control reviews, automated CI checks and an All-rights-reserved notice. This public site documents technical capability without releasing implementation secrets.

**Limits:** Private repository visibility is not a substitute for security testing, contractual terms, access auditing or a production deployment review.

[Return to the case study](README.md).
