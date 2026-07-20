---
name: weekly-report
description: Use to draft the Unlimited Leverage weekly performance report for the "APAC_Product溝通群" and "New Product Committee" groups, OR any recurring weekly product-performance report. Produces a bilingual (English + 繁體中文) report from the week's data, then self-iterates against a Product-Manager-grade standard until it meets the bar. Triggers on "draft the weekly report", "UL weekly report", "this week's leverage numbers", or the scheduled Sunday run.
---

# Weekly Report (self-improving, PM-grade)

Goal: produce a weekly performance report that reads like a **top-tier product manager** wrote it —
not a data dump. It states the numbers, explains the *why*, surfaces the *next* question each finding
raises, and every external claim traces to a verifiable source. The report is not finished when the
sections are filled; it is finished when it **passes the standard below**. If it does not pass, iterate.

## Audiences (produce both, in this order)
1. **"APAC_Product溝通群"** — the detailed report. Full base data, WoW, regional breakdown, Top5/Bottom5 clients.
2. **"New Product Committee"** — the summary report. Headline WoW + the one narrative that matters.

Both are bilingual: lead in 繁體中文 (the group's working language) with an English mirror, matching the
tone and structure of `.Codex/reporting/unlimited-leverage-report/templates/Unlimited Leverage Report Template.md`.

## Input contract (where the data comes from)
- The week's data lives in `.Codex/reporting/unlimited-leverage-report/{date-range}/` (e.g. `22th-28th-june-2026/`):
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
This is the shared PM-grade quality bar from the **`pm-quality-gate`** skill, plus report-specific
dimensions (bilingual, template). The report **passes only when every CRITICAL dimension passes**.
A number-correct report that reads flat FAILS — that is the whole point of this skill.

| # | Dimension | Critical? | Passes when… |
|---|---|---|---|
| 1 | **Numbers correct** | ✅ | Every figure traces to the input data. No invented or mis-copied numbers. Deltas recompute correctly. |
| 2 | **"So what" on every move** | ✅ | Each material metric movement has a stated *why* (hypothesis ok if labelled) — never a bare delta. |
| 3 | **Chain-of-thought / next question** | ✅ | Each interesting finding surfaces the *next* question it raises. (e.g. "Vietnam PnL +151% — same whale 20884988 recovering, or broad-based? → check client concentration.") A finding that dead-ends fails this. |
| 4 | **Verifiable sourcing** | ✅ | Every *external* claim (market events like a gold selloff, competitor moves, regulatory items) has a primary source or is flagged `VERIFY`. Internal numbers cite the data table. |
| 5 | **Risk surfaced** | ✅ | Client concentration / whale exposure / anomalous P&L explicitly called out with Risk-team status. |
| 6 | **Decision-ready close** | ✅ | Ends with: What to watch · What to decide · What to escalate. Not just "end of report". |
| 7 | **Bilingual & clean** | | 繁中 + English mirror, copy-paste clean, matches template tone, acronyms expanded once. |
| 8 | **Concise** | | Detailed report ≤ ~1.5 screens; committee report ≤ ~0.5 screen. Analysis, not padding. |

**Chain-of-thought is the signature of this skill.** A top-tier PM does not report "India volume -63%." They
report: "India Net PnL -63% WoW while volume held → margin per lot compressed, not activity. Hypothesis:
tighter spreads or a shift out of XAUUSD. → Next: pull India product mix vs last week; if XAUUSD share dropped,
that's a pricing signal, not a demand signal." Every interesting number should open the next door.

## Iterative refinement loop (do not skip — this is a self-improving loop)
Follow the goal-based / builder-validator pattern. Draft, then have a FRESH critic judge it, then revise.

1. **Draft v1** against the structure above.
2. **Adversarial critic pass.** Spawn the **`deliverable-critic`** agent (fresh context = honest judgment).
   Give it the draft and this skill's standard table (the 8 dimensions, 1–6 CRITICAL, plus the bilingual/
   template rows). It scores each dimension PASS/FAIL with the specific gap, independently verifies every
   external/market claim against a PRIMARY source, and returns the single weakest thing + a corrected fact
   for anything that failed sourcing. (If several market claims need checking, also fan out `citation-verifier`.)
3. **Revise → v2** addressing every FAILED critical dimension and every sourcing correction. Do not argue with
   the critic; fix the gap.
4. **Repeat** (critic → revise) until all critical dimensions PASS, **max 4 iterations**.
5. **If still failing at v4:** deliver the best version and state plainly, at the top, exactly which dimension
   still falls short and why. NEVER fake a pass. NEVER silently ship a substandard report.
6. **Deliver:** final report (both audiences) + a one-line iteration log (`v1→v3, fixed: chain-of-thought on
   regional rows, sourced the 6/26 gold move`) + the verification tally (`N external claims checked, X corrected`).

## Scheduled run (Sunday 22:00 GMT+8, Kuala Lumpur)
When run on schedule: check the input contract first. If the week's data is present, run the full loop and
leave the finished draft **for Adam's review — never auto-send.** If data is missing, notify Adam with the
specific missing input. Pilot manually on real data before trusting the schedule (watch token cost — the loop
spawns a critic each iteration).

## Known failure modes (do not repeat)
- Shipping bare deltas with no "so what" (fails dimension 2) — the most common way this report reads junior.
- A finding that dead-ends instead of opening the next question (fails dimension 3).
- Inventing a number when data is missing instead of flagging `數據確認中 / data pending`.
- Asserting a market cause ("gold dropped") with no source (fails dimension 4).
- Declaring a pass without actually running the critic (defeats the whole loop).
