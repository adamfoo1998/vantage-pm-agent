---
name: prd-authoring
description: Use when building a PRD from scratch given context (notes, handover info, meeting transcripts, requirements), OR when gap-analysing an existing PRD. DEFAULT is author mode — user provides context and agent builds the full IDEAL PRD. Gap-analysis mode triggers only when user explicitly says "review this PRD" or "gap-check this". Triggers on: "write a PRD", "build requirements for", "turn these notes into a PRD", "create a spec for", or any request to document a Vantage product (FCA Classic STP / Unlimited Perpetual, CFD/perp launch, pricing engine changes, equities).
---

# PRD Authoring & Gap Analysis

Context: Vantage has a history of delivery failures caused by PRD gaps — missing acceptance
criteria, no RACI, absent compliance sections, undefined "done". This skill produces the IDEAL
PRD structure so those gaps cannot recur.

## Default mode: AUTHOR (build from context)
The user gives you raw inputs: meeting notes, handover docs, transcripts, bullet points,
scattered requirements, or even just a verbal description. Your job is to build a complete,
structured IDEAL PRD from that material.

### Step 1 — Extract and clarify before writing
Before writing the PRD, read all inputs and list:
- What is confirmed (explicitly stated)
- What can be reasonably inferred (state the inference)
- What is missing and must be flagged as an Open Question (do not invent it)

If a critical input is missing (e.g. no launch date, no success metric, no RACI names), flag it
as an open question inside the PRD — do NOT invent a plausible-sounding value.

### Step 2 — Build the full 15-section IDEAL PRD

**Required PRD structure:**

1. **Header / version control** — doc owner (Adam), version, date, change log. Flag missing fields.
2. **Cross-sectoral POC (RACI)** — department · member · responsibility. Use known Vantage
   stakeholders (see reference list below). Flag any department with no named person.
3. **Background & problem statement** — what exists today, what problem this solves, why now.
4. **Objectives & success metrics** — measurable targets (trading volume, AUM, retention, NPS,
   complaint reduction, risk metrics). If the user provides none, prompt for them before proceeding.
5. **Scope** — 5.1 In scope / 5.2 Out of scope. Out-of-scope must be explicit — this is what
   prevents mid-build scope disputes.
6. **User segments & roles** — who uses this product and how (client-facing, admin, data/analytics).
7. **Functional requirements** — each with: unique ID · description · acceptance criteria (below).
8. **Non-functional requirements** — performance/latency numbers (flag as assumptions if
   unconfirmed), security, availability.
9. **Dependencies** — systems, teams, data sources, third-party vendors.
10. **Risk management requirements** — market, credit, operational, regulatory.
11. **Compliance / regulatory requirements** — FCA/FSRA/SEC/etc. Mark EVERY item `VERIFY`
    with the source document to check. Never assert regulatory detail as confirmed from memory.
12. **Reporting requirements**
13. **Open questions** — every gap, assumption, or unresolved item goes here with a named owner.
14. **Definition of Done (DoD)** — code done + tested + meets acceptance criteria.
15. **Change control process** — how new asks are logged (CR), assessed, decided.

### Acceptance-criteria format (mandatory for every functional requirement)
Given/When/Then — every requirement must be testable:
> **Given** [precondition] **When** [action/event] **Then** [observable, verifiable result]

No functional requirement is complete without at least one acceptance criterion. If a requirement
cannot be made testable, it goes to Open Questions, not to Functional Requirements.

---

## Secondary mode: GAP ANALYSIS (triggered only when user says "review/gap-check this PRD")
Score each of the 15 sections:

| Section | Present? | Quality (Strong/Weak/Missing) | Gap / delivery risk | Fix |
|---|---|---|---|---|

End with: top 3 delivery risks the gaps create + prioritised remediation list.

---

## Vantage stakeholder reference (for RACI population)
| Department | Known Members | Note |
|---|---|---|
| Product | Adam (you — owner), Karlos (HoP, approver), Caleb (handover, leaving) | |
| BIT | Vincent Zhang (main), Eason Zhang (vice) | Controls all system/module content |
| Operation | Betty (main), Jin (vice) | IB/sales impact, customer comms |
| Risk | Amin | Risk control review owner |
| Admin | Andy Chang (main), Elio Chang | System test, MT5 config |
| Plugin | Vladimir | Underlying system dev, not in front-end meetings |
| Analytics / Data | Jennifer Jiang (DPI) | |
| Upstream integration | Pandy | Path A (Binance API) |

If a department has no named person for the specific project, write `TBC — [department]` and flag
as an open question. Never leave RACI blank silently.

## House rules
- Single source of truth: version-controlled, one approved doc.
- Regulatory/compliance items: always `VERIFY` flagged, never asserted from memory.
- Cross-team logic (pricing engine, credit/margin, swap rollover): name the owning team in RACI
  and add a dependency entry.
- Decode jargon for Taiwan-based reviewers (Karlos). Expand acronyms on first use.
- If input is messy or scattered, organise it — that IS the work.
