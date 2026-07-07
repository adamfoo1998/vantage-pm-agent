---
name: market-briefing
description: Use for Adam's daily open-sharing input — a morning scan of US/overnight news that could move volatility, tuned to a CFD/multi-asset brokerage audience. Triggers on "morning briefing", "market brief", "what moved overnight", or the /standup command.
---

# Market Briefing

Goal: the thing Adam actually says out loud in the morning open-sharing meeting — tight, material,
sourced. Not a general news digest.

## Step 1 — Delegate the scan to `pm-researcher`
Do not create a new research agent or do the scanning inline. Send `pm-researcher` the coverage
checklist below in one call, dated for today, and ask it to report back only items that are
*material* to a CFD/multi-asset brokerage — skip anything that wouldn't move volatility or product
positioning. Better to under-report than pad with noise.

## Step 2 — Coverage checklist
For each category, search and include only if material (with a primary source):
- **Macro** — Fed/FOMC, CPI/NFP/PCE prints, Treasury yields, DXY moves.
- **Regulators** — SEC, CFTC, FCA, ADGM/FSRA announcements touching brokers, CFDs, leverage,
  crypto, tokenized/pre-IPO equities.
- **Exchanges/venues** — CME (especially 24/7 gold & crude expansion), major outages or rule
  changes.
- **Big tech & earnings** that move index CFDs; crypto regulatory/market-structure news.
- **Competitors, in passing only** (Binance, Bybit, Robinhood, etc.) — do not run a deep dive here;
  if something warrants one, flag it and route to `competitor-analyst` separately.

## Step 3 — Tier every item
Same tiers as the rest of the kit: `Confirmed` / `Inferred` / `Speculative`. Regulatory items
follow the hard rule from `AGENTS.md` — mark `VERIFY` and name the source; never assert regulatory
detail from memory.

## Step 4 — Output structure
1. **BLUF** — 3 bullets max: the things Adam should actually say in the meeting.
2. **Per-item reasoning chain** — one block per material item, in this order, not a flat table:
   - **News** — what happened, dated, with the primary source linked.
   - **Why** — the causal/contextual chain: what drove it (e.g. which print, which policy shift,
     which structural rule change) — not just restating the headline.
   - **Watch for** — the concrete implication for Vantage (volatility/product impact, anchored to
     XAUUSD/SPCX where relevant) *and* what to keep an eye on next (a follow-on event, a decision
     Vantage needs to make, a date something resolves).
   - Confidence tier tag on the News line; regulatory items get the `VERIFY` flag per Step 3.
   Order items by what Adam would actually lead with, most material first — not by category.
3. **Watch today** — one line: data prints / events scheduled today, times in MYT.
4. Close with: Assumptions · Risks · Open Questions · Next Steps (per the standing house rule).

## Step 5 — File it
Write the result to `vault/daily/YYYY-MM-DD-briefing.md` via `librarian` (type: `briefing`). Have
librarian update `STATUS.md`'s "Last briefing date" line.

## Known failure modes (do not repeat)
- **Flat table reads as a news digest, not a briefing.** A bare `Item | What happened | Impact`
  table lists facts without reasoning. Adam needs the chain: what happened → why it happened →
  what to watch for. Always write the per-item reasoning chain (Step 4.2), never collapse it back
  into a flat comparison table.
