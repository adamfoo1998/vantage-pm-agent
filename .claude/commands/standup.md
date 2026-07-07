---
description: Morning routine — inbox triage, today's market briefing, STATUS.md surfacing, top-3 for the day.
---

Run Adam's morning standup. Total output must fit on one screen — be terse, no preamble.

1. **Inbox triage.** List every file under `inbox/transcripts/`, `inbox/reports/`, `inbox/notes/`
   (ignore `_about.md`). For each, propose routing:
   - `inbox/transcripts/*` → `meeting-synthesis`
   - `inbox/reports/*` → `weekly-report` (if it's the UL folder) or `report-from-images`
   - `inbox/notes/*` → `sop-builder` or `prd-authoring`
   If a file's routing is ambiguous, ASK Adam rather than guessing. If inbox is empty, say so in
   one line and move on.

2. **Today's market briefing.** Check `vault/daily/` for a file named `YYYY-MM-DD-briefing.md`
   for today's date. If it doesn't exist and the `market-briefing` skill is available, run it now.
   If the skill doesn't exist yet (not yet built), skip this step and note it's pending Phase 3.

3. **STATUS.md scan.** Read `STATUS.md` at repo root and surface only what's actionable:
   - Overdue action items (due date has passed)
   - Blocked/waiting-on items
   - Decisions awaiting sign-off
   Skip sections that are empty — don't print "none" noise for every heading.

4. **Top 3 for the day.** Based on 1–3 above, propose the three highest-leverage things for Adam
   to do today, one line each.

Keep the whole response scannable in under a screen. Do not pad with restating this prompt.
