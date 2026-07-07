---
name: ops-check-runbook
description: Use to execute a named ops-check runbook (dividend adjustments, weekend swaps, or any ad hoc checklist verification) from `vault/sops/runbooks/` against inputs Adam provides — screenshots, exported tables, MT5 admin values. Triggers on "run the [X] check", "check dividends/swaps", or naming a runbook file.
---

# Ops-Check Runbook

Goal: execute a checklist runbook item by item against real evidence, and never claim something
passed that wasn't actually checked.

## Step 1 — Load the runbook
Read the named runbook from `vault/sops/runbooks/<runbook-name>.md`. If it doesn't exist, say so
and stop — don't improvise a checklist from memory. If the runbook's check items are still
placeholders (not yet filled from a live `sop-builder` session), say so and stop; ask Adam to run
`sop-builder` with the team first.

## Step 2 — Match inputs to check items
Adam provides the evidence for this run: screenshots, exported tables, MT5 admin values, etc.
Go through the runbook's check items one by one and match each to the evidence provided.

## Step 3 — Verdict per item
For every check item:
- **PASS** — evidence directly supports it. Cite the evidence (which screenshot/table/value).
- **FAIL** — evidence directly contradicts it. Cite the evidence and state the discrepancy.
- **UNCHECKED** — no evidence was provided for this item. **Never infer or assume PASS from
  absence of evidence.** An unchecked item stays unchecked, full stop.

Tag each verdict with a confidence tier (`Confirmed` from direct evidence / `Inferred` if it
required a computed step from the evidence, e.g. summing an exported table).

## Step 4 — Output
1. **PASS/FAIL/UNCHECKED table** — one row per check item: Item | Verdict | Evidence cited | Confidence.
2. **Exceptions section** — every FAIL and UNCHECKED item, routed to the owner named in the
   runbook's escalation section (pull from the Vantage stakeholder map in `meeting-synthesis` if
   the runbook doesn't name one directly — typically Ops: Betty/Jin · Risk: Amin · Admin:
   Andy/Elio).
3. Close with: Assumptions · Risks · Open Questions · Next Steps.

## Known failure modes (do not repeat)
- Marking an item PASS because it "sounds like it should be fine" with no evidence — always
  UNCHECKED instead.
- Running a runbook whose check items are still placeholder skeletons instead of stopping and
  asking for a live `sop-builder` session to fill them first.
