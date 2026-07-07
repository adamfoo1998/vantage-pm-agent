---
name: launch-conductor
description: Use to turn an approved PRD into a launch package — stakeholder/comms matrix, launch comms calendar, customer notification drafts, and a go/no-go checklist. Triggers on "build the launch package for [PRD]", "launch plan for X", or "get [feature] ready to launch".
---

# Launch Conductor

Goal: take an approved PRD (the IDEAL structure from `prd-authoring`) and produce everything
needed to actually run the launch — who's told what and when, the comms timeline, draft customer
notifications, and the go/no-go gate. This skill does not re-derive requirements; it operationalizes
a PRD that's already been written.

## Step 0 — PRD linter (refuse if the PRD isn't launch-ready)
Before producing anything, check the input PRD has:
- **Section 2 — Cross-sectoral POC (RACI)**, populated (not all `TBC`).
- **Section 7 — Functional requirements with acceptance criteria** (Given/When/Then present).
- **Section 11 — Compliance/regulatory requirements**, including a sign-off section/owner.
- **Section 14 — Definition of Done.**

**If any of these is missing or is a placeholder, STOP.** Do not improvise a launch package from
an incomplete PRD. Instead, route to `prd-authoring` in gap-analysis mode and report back exactly
which section(s) are missing.

## Step 1 — Stakeholder/comms matrix
Derive from the PRD's RACI (section 2): for each stakeholder/department, state what they need to
be informed of, when (relative to launch date), and via which channel (email, Lark group, meeting).
Format:

| Stakeholder | Informed of | When | Channel |
|---|---|---|---|

Use the Vantage stakeholder map (same reference list as `prd-authoring`/`meeting-synthesis`) to
resolve names; if the PRD's RACI names someone not on that list, keep it verbatim and flag
`[UNKNOWN — verify role]`.

## Step 2 — Launch comms calendar
Work backward from the PRD's launch date. Standard checkpoints (adjust to what the PRD actually
specifies — don't invent a date the PRD doesn't give):
- Internal announcement (cross-functional team, per RACI)
- Training / enablement (Ops, Admin — per RACI)
- Marketing brief handoff
- Customer notification (see Step 3)
- Go-live
- Post-launch check-in

If the PRD doesn't state a launch date, flag it as a blocking open question — the calendar cannot
be built without one.

## Step 3 — Customer notification draft(s)
Draft the customer-facing notification(s) using Vantage's standard notification conventions from
the Unlimited Leverage PRD in `.claude/knowledge-dump/unlimited-leverage/` — including the
standard reservation clause pattern ("...events during special time periods may vary depending on
risk management requirements" or equivalent wording) that covers Vantage's ability to adjust
terms around high-volatility/event windows. **This clause pattern is `Inferred` from the master
build spec, not independently re-verified against the source PDF in this pass (PDF page-rendering
isn't available in this environment) — VERIFY exact wording against the primary UL PRD document
before anything ships externally.**

Every notification draft:
- Is marked **`DRAFT — Legal/Compliance sign-off required`** at the top, in bold, not buried.
- Goes through Amin (Risk) and Legal/Compliance before anything is customer-facing.

## Step 4 — Go/no-go checklist
Build directly from the PRD's Definition of Done (section 14) — one checklist row per DoD item,
plus a blocking row for **Legal/Compliance sign-off on customer notifications** (this gate is
always present regardless of what the PRD's DoD says, since it's a hard rule of this skill, not
optional). Format: Item | Status (Done/Not done/Blocked) | Evidence | Owner.

## Step 5 — File it
File the full package (comms matrix, calendar, notification drafts, go/no-go checklist) via
`librarian` under the project's vault MOC (`vault/projects/<project>.md`). Close with:
Assumptions · Risks · Open Questions · Next Steps.

## Known failure modes (do not repeat)
- Producing a launch package from a PRD with a blank/TBC RACI or missing acceptance criteria —
  always route to `prd-authoring` gap mode instead.
- Shipping a customer notification without the `DRAFT — Legal/Compliance sign-off required` marker,
  or treating that sign-off as optional because the PRD's own DoD didn't happen to list it.
- Inventing a launch date or comms checkpoint the PRD doesn't actually specify.
