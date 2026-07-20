---
name: weekly-report
description: Use to draft the Unlimited Leverage weekly performance report for the "APAC_Product溝通群" and "New Product Committee" groups, OR any recurring weekly product-performance report. Produces a short, 繁體中文-only report matching the actual sent-report precedent, from the week's data, then self-iterates against a Product-Manager-grade standard until it meets the bar. Triggers on "draft the weekly report", "UL weekly report", "this week's leverage numbers", or the scheduled Sunday run.
---

# Weekly Report (self-improving, PM-grade)

Goal: produce a weekly performance report that reads like a **top-tier product manager** wrote it —
not a data dump — while staying exactly as short and plain as the reports Adam actually sends. It states
the numbers and the *why* in the same breath, and every external claim traces to a verifiable source. The
report is not finished when the sections are filled; it is finished when it **passes the standard below**.
If it does not pass, iterate. Substance and brevity are both requirements — a report that's insightful but
twice as long as precedent has *not* passed.

## Audiences (produce both, in this order)
1. **"APAC_Product溝通群"** — the detailed report. Full base data, WoW, regional breakdown, Top5/Bottom5 clients.
2. **"New Product Committee"** — the summary report. Headline WoW + the one narrative that matters.

**Format precedent (follow this, not the bilingual template): both reports are 繁體中文 only — no English
mirror.** Adam's actual working format is short and plain: numbered points under each header, one sentence
per point (number + one-line reason, no separate "→ Next" line, no bolding/markdown escaping), WoW bullets
with 🔴/🟢, and a one-line parenthetical for the "so what" — nothing more. Match the length and tone of
`.claude/reporting/unlimited-leverage-report/6th-12th-july-2026/Report_APAC_Product_6July-12July-2026.txt`
and `Report_New_Product_Committee_6July-12July-2026.txt` exactly — that is the real bar, not the older
`templates/Unlimited Leverage Report Template.md` (which is bilingual/verbose and superseded by precedent).
Do not add an English mirror or a separate "What to watch / decide / escalate" close section unless Adam
asks for one explicitly for that run.

**Audience-appropriate jargon:** the "New Product Committee" summary audience does not know internal team
names like "DPI" — never introduce them there (no "需與DPI核對..."); state the open question in plain terms
instead (e.g. "需持續留意資金流出狀況" not "需與DPI核對提現明細"). The "APAC_Product溝通群" detailed report
CAN reference DPI — the precedent report already does ("需與DPI核對明細") — because that audience works with
the data team directly. When a causal explanation needs simplifying for the committee report, cite the
specific date of the market move if you can source one (e.g. "7/17黃金因美伊局勢升溫下跌逾3%") rather than
the technical revenue-line breakdown (RR/RFR) that belongs in the detailed report only.

## Input contract (where the data comes from)
- The week's data lives in `.claude/reporting/unlimited-leverage-report/{date-range}/` (e.g. `22th-28th-june-2026/`):
  the analytics tables (Weekly Report *.png from DPI / Jennifer Jiang) and any prior narrative `.txt`.
- You need **this week's numbers and last week's numbers** to compute WoW. If last week's are missing,
  pull them from the previous folder or the report template's history.
- **If the week's data is not present, STOP and notify — do not invent numbers.** Say exactly which
  input is missing and who owns it (DPI / Jennifer Jiang).

## Report structure (mirror the template)
**一、基礎數據分享 / Base data**
- Cumulative-since-launch line (3/9 to week-end): Net Company PnL, Volume (Mil), Net Deposit, Net internal transfer.
- Last week's PnL with the *reason* it moved (e.g. "6/26 gold drop hurt client long positions → company PnL up").
- Net PnL country split and Volume country split (name the top 2-3 with %).
- Full-open-market growth callouts (e.g. Thailand +407%).
- Product mix: XAUUSD share of volume and PnL (the anchor product), then next-ranked products.
- Problem-client status: Top5 / Bottom5, each with country + single-week P&L + Risk-team verdict.

**二、整體表現總攬 WoW / Overall WoW** — Volume, Deposit, Net Deposit, Net Company PnL, each with 🔴/🟢 and %.

**三、區域表現 / Regional** — top-5 regions: Volume growth % and Net PnL growth %, each 🔴/🟢. Flag `數據確認中 / data pending` where a figure isn't in yet (do not guess — mirror the Hong Kong rows in past reports).

## THE STANDARD (the loop's stop condition)
This is the shared PM-grade quality bar from the **`pm-quality-gate`** skill, adapted to this report's
real format precedent. All 6 dimensions below are critical — the report **passes only when all 6 pass**.
A number-correct report that reads flat FAILS. So does a correct, insightful report that's bloated past
precedent length or reintroduces the English mirror / decision-close block — that is the whole point of
this skill.

| # | Dimension | Critical? | Passes when… |
|---|---|---|---|
| 1 | **Numbers correct** | ✅ | Every figure traces to the input data. No invented or mis-copied numbers. Deltas recompute correctly. |
| 2 | **"So what" on every move** | ✅ | Each material metric movement has a stated *why*, folded into the same sentence/line as the number (hypothesis ok if labelled) — never a bare delta, but also never its own paragraph. |
| 3 | **Verifiable sourcing** | ✅ | Every *external* claim (market events like a gold selloff, competitor moves, regulatory items) has a primary source or is flagged `VERIFY`, stated in one clause — not a cited-source paragraph. Internal numbers cite the data table. |
| 4 | **Risk surfaced** | ✅ | Client concentration / whale exposure / anomalous P&L explicitly called out with Risk-team status, inline in the Top5/Bottom5 point — not a separate section. |
| 5 | **Format matches precedent** | ✅ | 繁體中文 only (no English mirror), one sentence per numbered point, no "→ Next" lines, no separate decision-close block. Matches the length/tone of the `6th-12th-july-2026` reports. |
| 6 | **Concise** | ✅ | Detailed report ≈ same length as the `6th-12th-july-2026` precedent (roughly 35-45 lines incl. headers/placeholders); committee report ≈ same length as its precedent (~25 lines). If a draft is longer than precedent, cut prose, don't add sections. |

**The "so what" is the signature of this skill, but it stays terse.** A top-tier PM does not report "India
volume -63%." They report, in one sentence: "India Net PnL -63% WoW while volume held — margin per lot
compressed, not activity, likely tighter spreads or a shift out of XAUUSD (needs product-mix check)." The
insight is real; the delivery is still one line, matching the density of the actual sent reports.

## Iterative refinement loop (do not skip — this is a self-improving loop)
Follow the goal-based / builder-validator pattern. Draft, then have a FRESH critic judge it, then revise.

1. **Draft v1** against the structure above.
2. **Adversarial critic pass.** Spawn the **`deliverable-critic`** agent (fresh context = honest judgment).
   Give it the draft, this skill's standard table (all 6 dimensions, all critical), and explicitly point it
   at the `6th-12th-july-2026` reports as the format/length precedent — otherwise a fresh critic will default
   to the generic bilingual/verbose pm-quality-gate expectations and flag brevity as a defect, which is wrong
   for this report. It scores each dimension PASS/FAIL with the specific gap, independently verifies every
   external/market claim against a PRIMARY source, and returns the single weakest thing + a corrected fact
   for anything that failed sourcing. (If several market claims need checking, also fan out `citation-verifier`.)
   Sanity-check any numeric correction yourself against the raw source table before applying it — critics
   have mis-read table columns before (e.g. off-by-one on a wide WoW% table); don't accept a "correction"
   that doesn't survive your own recount.
3. **Revise → v2** addressing every FAILED critical dimension and every sourcing correction. Do not argue with
   the critic; fix the gap.
4. **Repeat** (critic → revise) until all critical dimensions PASS, **max 4 iterations**.
5. **If still failing at v4:** deliver the best version and state plainly, at the top, exactly which dimension
   still falls short and why. NEVER fake a pass. NEVER silently ship a substandard report.
6. **Deliver:** final report (both audiences) + a one-line iteration log (`v1→v3, fixed: sourced the 7/13 gold
   move, trimmed back to precedent length`) + the verification tally (`N external claims checked, X corrected`).

## Scheduled run (Sunday 22:00 GMT+8, Kuala Lumpur)
When run on schedule: check the input contract first. If the week's data is present, run the full loop and
leave the finished draft **for Adam's review — never auto-send.** If data is missing, notify Adam with the
specific missing input. Pilot manually on real data before trusting the schedule (watch token cost — the loop
spawns a critic each iteration).

## Known failure modes (do not repeat)
- Shipping bare deltas with no "so what" (fails dimension 2) — the most common way this report reads junior.
- Inventing a number when data is missing instead of flagging `數據確認中 / data pending`.
- Asserting a market cause ("gold dropped") with no source (fails dimension 3).
- Defaulting back to the bilingual template, a separate "→ Next" line per finding, or a "What to watch /
  decide / escalate" close block — that was the pre-precedent format and Adam explicitly corrected it back
  to short/繁中-only/inline. Always check length and language against the `6th-12th-july-2026` reports before
  delivering (fails dimension 5/6).
- Declaring a pass without actually running the critic (defeats the whole loop).
- Trusting a critic's numeric "correction" without recounting the source table column yourself.
