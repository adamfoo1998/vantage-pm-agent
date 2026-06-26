---
name: competitive-intel-brief
description: Use when producing, fact-checking, or correcting competitive intelligence on brokers or exchanges (Binance, Bybit, Bitget, Robinhood/Bitstamp, Moomoo) or benchmarking any trading product (FX, commodities, equities, crypto, perpetuals, tokenized RWA) for the Vantage roadmap. Triggers on requests like "benchmark X against Y", "is this Binance claim accurate", "build a competitive brief", or "what does competitor Z offer for [instrument]".
---

# Competitive Intelligence Brief

Goal: produce a brief that survives review by the Head of Product, where prior feedback was that
quality/accuracy fell short. Accuracy and source discipline outrank completeness.

## Step 1 — Frame the comparison question
Before researching, write the precise question in one line. Use the question-building pattern:
`[subject] vs [benchmark] on [specific dimension] for [instrument], as of [date]`.
Vague question → vague brief. If the requester's ask is broad, narrow it and state the narrowing.

## Step 2 — Primary-source-first verification (hard rule)
- A claim about an entity must come from **that entity's own** primary source: official domain
  (e.g. binance.com, academy.binance.com), regulatory filing (ADGM/FSRA, FCA, SEC), or the
  entity's published T&C / product pages.
- **Never** substitute a third party for the subject. A Bitget article is not evidence about
  Binance. Aggregators, blogs, and forums are leads to verify, not sources to cite.
- If a claim cannot be traced to a primary source, label it and explain why — do not drop it
  silently and do not upgrade an inference to a fact.

## Step 3 — Anchor with the two reference instruments
Where the dimension allows, illustrate with the standing instruments so briefs stay comparable:
- **XAUUSD** (gold) for commodities/liquidity/spread/swap questions.
- **SPCX / SpaceX** for equities / pre-IPO / tokenized-equity questions.

## Step 4 — Tier every claim
Tag each material claim:
| Tier | Meaning | Requirement |
|---|---|---|
| `Confirmed` | Primary source verified | Link the exact source |
| `Inferred` | Reasoned from confirmed facts | State the inference chain |
| `Speculative` | Plausible, unverified | Say what would confirm it |

## Step 5 — Output structure
1. **BLUF** — 2–3 sentences: the answer and why it matters to Vantage.
2. **Comparison table** — subject vs benchmark(s), one row per dimension, tier tag per cell.
3. **Gaps & implications for Vantage** — tie to roadmap (e.g. Path A Binance-API vs Path B
   StarPrime; CFD/perp launch; oracle/market-maker sourcing). Mark regulatory items `VERIFY`.
4. **Confidence summary** — what is solid vs thin.
5. **Open questions & suggested next steps** — including which sources still need pulling.

## Pre-send validation checklist
- [ ] Every `Confirmed` claim links a PRIMARY source for the correct entity.
- [ ] No third-party source stands in for the subject.
- [ ] Tiers applied; no inference dressed as fact.
- [ ] Regulatory claims marked `VERIFY` with the document to check.
- [ ] BLUF answers the Step 1 question directly.

## Known failure modes (do not repeat)
- Substituting a competitor's source for the subject entity.
- Presenting an inference at `Confirmed` confidence.
- Brief reads as a general summary instead of a decision-ready intelligence product.
