---
name: prd-authoring
description: Use when drafting a new PRD/FSD, upgrading an existing one, or running a gap analysis on a PRD for a Vantage product (FCA Classic STP / Unlimited Perpetual, CFD/perp launch, equities, pricing-engine changes). Triggers on "write a PRD", "review/upgrade this PRD", "what's missing in this requirements doc", or "turn these requirements into a spec".
---

# PRD Authoring & Gap Analysis

Context: Vantage has a history of delivery failures caused by PRD gaps — missing acceptance
criteria, no RACI, absent compliance sections, undefined "done". This skill enforces the
IDEAL PRD structure so those gaps cannot recur.

## Two modes
- **Author mode** — build a PRD from inputs (notes, transcripts, prior PRDs).
- **Gap-analysis mode** — score an existing PRD against the required structure and list every
  missing/weak section with a concrete fix. Default to this when handed an existing document.

## Required PRD structure (IDEAL PRD baseline)
1. **Header / version control** — doc owner, version, date, change log.
2. **Cross-sectoral POC (RACI)** — department · member · responsibility (Product, BIT, Risk,
   Operation, Admin, Plugin). This is the team-consensus anchor; never omit.
3. **Background & problem statement**
4. **Objectives & success metrics** — measurable (volume, retention, revenue, NPS, risk).
5. **Scope** — 5.1 In scope · 5.2 Out of scope (explicit out-of-scope prevents "out of scope"
   disputes mid-build).
6. **User segments & roles**
7. **Functional requirements** — each with a unique ID and **acceptance criteria** (below).
8. **Non-functional requirements** — performance/latency, security, availability (numbers, even
   if flagged as assumptions to be finalised).
9. **Dependencies**
10. **Risk management requirements** — market, credit, operational, regulatory.
11. **Compliance / regulatory requirements** — FCA/FSRA/etc. Mark each item `VERIFY` + source.
12. **Reporting requirements**
13. **Open questions**
14. **Definition of Done (DoD)** — code done + tested + meets acceptance criteria.
15. **Change control** — how new asks are logged (CR), assessed (timeline/cost/resource),
    decided (include now / defer).

## Acceptance-criteria format (mandatory per functional requirement)
Use Given/When/Then. Every requirement must be testable:
> **Given** [precondition] **When** [action/event] **Then** [observable, verifiable result].
No requirement ships without at least one acceptance criterion. Flag any that can't be made
testable as an open question.

## Gap-analysis output
| Section | Present? | Quality | Gap / risk it creates | Fix |
|---|---|---|---|---|
Score each of the 15 sections; end with a prioritised remediation list and the top 3 delivery
risks the gaps create.

## House rules
- Single source of truth: version-controlled, one approved doc.
- Never assert regulatory/compliance detail from memory — mark `VERIFY` and name the source.
- If a requirement touches another team's logic (e.g. pricing engine, credit/margin, swap
  rollover), name the owning team in the RACI and flag the cross-team dependency.
- Decode jargon for the Taiwan-based reviewers; expand acronyms on first use.
