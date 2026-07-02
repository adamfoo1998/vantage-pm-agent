---
name: pm-quality-gate
description: The reusable Vantage PM-grade quality standard and self-improving-loop protocol. Use when any deliverable must "reach top-tier PM standard" — reports, competitive briefs, PRDs, news scans — or when running a draft→critique→revise loop. Referenced by weekly-report and by the deliverable-critic agent. Triggers on "hold this to the PM standard", "iterate until it's good enough", "is this decision-ready", or any self-improving loop.
---

# PM Quality Gate

The canonical standard Adam's deliverables must reach, plus the loop that gets them there. A deliverable
is not done when its sections are filled — it is done when it **passes this bar**. If it doesn't, iterate.

## The standard (dimensions 1–6 are CRITICAL — all must pass)

| # | Dimension | Critical | Passes when… |
|---|---|---|---|
| 1 | **Accurate** | ✅ | Every figure/fact traces to a real source or the input data. Nothing invented or mis-copied. |
| 2 | **"So what"** | ✅ | Every material point states why it matters — never a bare fact or delta. |
| 3 | **Chain-of-thought** | ✅ | Each interesting finding surfaces the NEXT question it raises. A point that dead-ends fails. |
| 4 | **Verifiable sourcing** | ✅ | Every external claim has a primary source or is flagged `VERIFY`. Internal numbers cite their data. |
| 5 | **Risk surfaced** | ✅ | The relevant risks (concentration, regulatory, delivery, market) are named, not buried. |
| 6 | **Decision-ready close** | ✅ | Ends with what to watch · what to decide · what to escalate. Not just a summary. |
| 7 | Plain & clean | | Jargon decoded, acronyms expanded once, tables over prose, copy-paste clean. |
| 8 | Concise | | Length matched to purpose. Analysis, not padding. |

**Chain-of-thought (dim 3) is the signature.** A top-tier PM doesn't stop at "metric X moved 20%" — they
say what it implies, what it rules in or out, and the next thing to check. When you find an interesting
number, a problem, or a piece of news, it should open the NEXT question, which opens the next. Every
interesting finding opens a door.

## The self-improving loop
1. **Draft v1.**
2. **Critique.** Spawn the `deliverable-critic` agent (fresh context = honest judgment). It scores v1
   against the standard and spot-checks sourcing. (Fan out `citation-verifier` too if the deliverable
   leans on several external claims.)
3. **Revise → v2**, fixing every FAILED critical dimension and every sourcing correction. Don't argue with
   the critic — fix the gap.
4. **Repeat** (critique → revise), **max 4 iterations**.
5. **If still failing at v4:** deliver the best version and state plainly at the top which dimension still
   falls short and why. NEVER fake a pass; NEVER silently ship substandard.
6. **Deliver:** final + a one-line iteration log (`v1→v3, fixed: …`) + a verification tally
   (`N external claims checked, X corrected`).

## Tuning
This is the shared bar. A skill may ADD dimensions for its own artifact (e.g. `weekly-report` adds
bilingual output) but must not drop a critical one. When Adam corrects an output, add the lesson here or
in the specific skill so the bar ratchets up over time — that is the Recursive Refinement loop from SETUP.md.
