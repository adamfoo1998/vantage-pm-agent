---
name: meeting-synthesis
description: Use when turning meeting notes, transcripts, or raw discussion into a structured summary — FCA product-launch cross-functional syncs, vendor calls (Wintermute, StarPrime), or internal product reviews. Triggers on "summarise these notes", "extract action items", "what did we decide in this call", or any pasted transcript/meeting dump.
---

# Meeting Synthesis

Goal: convert messy input into a decision-ready record that anyone who missed the meeting can act
on. Copy-paste ready, plain language.

## Output structure (always this order)
1. **TL;DR** — 2–3 sentences: what was decided and what happens next.
2. **Decisions** — each decision + who made it. If a decision was deferred, say so and why.
3. **Action items** — table:
   | # | Action | Owner | Due | Status |
   |---|---|---|---|---|
   Owner must be a named person, not a team, where the input allows. If owner/due is unstated,
   write `UNASSIGNED` / `TBC` — never guess silently.
4. **Risks & blockers** — anything that threatens timeline, scope, compliance, or budget.
5. **Open questions** — unresolved items needing a decision, with who can resolve each.
6. **Follow-ups** — meetings to schedule, docs to produce, people to loop in.

## Known stakeholders (map names when context is ambiguous)
- **Karlos** — Head of Product (decision-maker / approver).
- **Jennifer Jiang** — analytics / data (DPI).
- **Pandy** — upstream integration (Path A / Binance API).
- **Lucas Xue, Caleb Chen, Kelly Sun** — FCA launch cross-functional.
If a name in the notes isn't recognised, keep it verbatim and flag it.

## Rules
- Distinguish a **decision** (settled) from a **discussion** (raised, unresolved → goes to Open
  Questions, not Decisions).
- Do not invent action items the meeting didn't produce. Under-reporting beats fabricating.
- Mark any compliance/regulatory action `VERIFY`.
- Keep it scannable; no walls of prose.
