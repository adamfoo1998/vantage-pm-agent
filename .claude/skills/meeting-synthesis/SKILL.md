---
name: meeting-synthesis
description: Use when turning meeting notes, transcripts, or raw discussion into a structured summary — FCA product-launch cross-functional syncs, vendor calls (Wintermute, StarPrime), Head of Product reviews, or internal product meetings. Triggers on "summarise these notes", "extract action items", "what did we decide in this call", or any pasted transcript/meeting dump.
---

# Meeting Synthesis

Goal: convert messy input into a decision-ready record that anyone who missed the meeting can
act on immediately. Plain language, copy-paste ready.

## Output structure (always this order)

1. **TL;DR** — 2–3 sentences: what was decided and what happens next.
2. **Decisions** — each decision + who made it. If deferred, state it and why.
3. **Action items table:**

| # | Action | Owner | Due | Status |
|---|---|---|---|---|

   Owner must be a named person where the input allows. If unstated → `UNASSIGNED`. Due unstated → `TBC`. Never guess silently.

4. **Risks & blockers** — anything threatening timeline, scope, compliance, or budget.
5. **Open questions** — unresolved items needing a decision, with who can resolve each.
6. **Follow-ups** — meetings to schedule, docs to produce, people to loop in.

---

## Vantage stakeholder map (use to assign names when context is ambiguous)

**Product / Leadership**
| Name | Role |
|---|---|
| Karlos | Head of Product — decision-maker, final approver |
| Adam | PM (you) — action owner for product items |
| Caleb | Outgoing PM — handover, leaving imminently |

**Cross-functional team (from PRD POC table)**
| Name | Department | Responsibility |
|---|---|---|
| Vincent Zhang | BIT (main) | All system/module content, overall BIT project owner |
| Eason Zhang | BIT (vice) | BIT support |
| Betty | Operation (main) | IB/sales impact, customer comms during launches |
| Jin | Operation (vice) | OP business support |
| Amin | Risk | Risk control review and sign-off |
| Andy Chang | Admin (main) | System test, MT5 group config, launch docking |
| Elio Chang | Admin (vice) | Admin support |
| Vladimir | Plugin | Underlying system developer — not in front-end meetings |
| Jennifer Jiang | Analytics / Data (DPI) | Data analysis, reporting |
| Pandy | Upstream / Integration | Path A (Binance API integration) |

**FCA launch cross-functional**
| Name | Role |
|---|---|
| Lucas Xue | FCA sync participant |
| Caleb Chen | FCA sync participant |
| Kelly Sun | FCA sync participant |

If a name in the notes is not on this list, keep it verbatim and flag it as `[UNKNOWN — verify role]`.

---

## Rules
- Distinguish **decision** (settled, agreed) from **discussion** (raised, unresolved → goes to
  Open Questions, never to Decisions).
- Do not fabricate action items the meeting didn't produce. Under-reporting beats inventing.
- Any compliance/regulatory action → mark `VERIFY` with the relevant regulator/document.
- Keep it scannable. No walls of prose.
- If a follow-up meeting was agreed but not scheduled, list it in Follow-ups with a suggested
  owner to drive it.

## Known failure modes (do not repeat)
- Writing `[team]` as the action owner when a named person was in the room.
- Listing a discussion point as a decision.
- Omitting a risk that was raised but not formally documented.
