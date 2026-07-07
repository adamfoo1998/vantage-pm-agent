---
name: report-from-images
description: Use for any recurring stakeholder report built from PowerBI (or other dashboard) screenshots plus a template — the generalized version of the weekly-report pattern for reports that aren't the Unlimited Leverage weekly. Triggers on "build the [X] report from these screenshots", "run the [report-name] pipeline", or dropping images into `.claude/reporting/<report-name>/<period>/`.
---

# Report From Images (generalized recurring-report pipeline)

Goal: turn a folder of dashboard screenshots into a stakeholder-ready report, for ANY recurring
report — not just Unlimited Leverage (that stays on `weekly-report`, unchanged). Same discipline:
read only what's actually in the images, never invent a figure, hold the output to PM-grade
standard before it ships.

## Input contract
- **Screenshots**: `.claude/reporting/<report-name>/<period>/` — the current period's PowerBI (or
  other dashboard) images.
- **Template**: `.claude/reporting/<report-name>/templates/` — Adam supplies this per report; it
  defines sections, audience groups, and tone. Mirror it exactly, the way `weekly-report` mirrors
  the UL template.
- **Prior period**: the previous `<period>/` folder under the same `<report-name>/`, for WoW/MoM
  deltas. If there's no prior period (first run for this report), state that explicitly and skip
  deltas rather than fabricating a baseline.
- **If the current period's screenshots or the template are missing, STOP and say exactly what's
  missing and who owns supplying it** (Adam, or whoever he names) — never proceed on partial input.

## Step 1 — Extract
Read every figure that's actually visible in the images.
- A transcribed figure is tagged `Confirmed (from image)`.
- Anything you compute (a delta, a ratio, a %) is shown with its formula, not just the number.
- **If a number is unreadable (cropped, blurry, obscured) or a figure the template needs isn't in
  any image, STOP — list precisely which figure is missing/unreadable and from which image/section
  it should have come from, and who owns getting a clean version.** Never interpolate, estimate,
  or carry forward a stale number to fill the gap.

## Step 2 — Draft
Build the report against the template's structure and audience groups (a report may need more
than one version, same pattern as weekly-report's detailed vs. committee split — check the
template for how many audiences it defines). Apply the same chain-of-thought discipline as every
other Vantage deliverable: state the number, state why it moved, state what it implies next.

## Step 3 — Quality loop (the `pm-quality-gate` standard)
Same loop as `weekly-report`, unchanged:
1. Draft v1.
2. Spawn `deliverable-critic` with the draft + the `pm-quality-gate` standard (add report-specific
   dimensions from the template if it defines any, e.g. bilingual — never drop a critical one).
3. Revise → v2, fixing every FAILED critical dimension.
4. Repeat, max 4 iterations. If still failing at v4, deliver the best version and state plainly at
   the top which dimension falls short and why — never fake a pass.

## Step 4 — Output
- The finished report file(s), one per audience group defined in the template.
- A ready-to-send message draft (email or Lark, matching how the template's audience normally
  receives it) per audience group.
- File both via `librarian` into the vault, then close with: Assumptions · Risks · Open Questions ·
  Next Steps.

## Onboarding a new recurring report
Adam onboards a new report by creating `.claude/reporting/<report-name>/templates/` with the
template and dropping the first period's screenshots into `.claude/reporting/<report-name>/<first-period>/`.
Run one manual pilot end-to-end before the report is trusted to run unattended — same rule as
every other new skill in this kit: nothing is "done" until piloted.

## Known failure modes (do not repeat)
- Filling a missing/unreadable figure with a guess instead of stopping — the single most important
  rule this skill exists to enforce.
- Skipping the critic loop because "it's just a data report" — number-correct but flat still fails
  dimension 2/3 of `pm-quality-gate`.
- Treating this skill as a rewrite of `weekly-report` — it isn't; UL keeps using `weekly-report`
  as-is. This skill is for every OTHER recurring image-based report.
