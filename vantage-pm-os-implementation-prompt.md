# MASTER IMPLEMENTATION PROMPT — Vantage PM Operating System v2
# Paste everything below this line into Claude Code, run from the vantage-pm-agent repo root.
# Execute ONE PHASE AT A TIME. Stop at each checkpoint and wait for my confirmation.

---

You are extending my existing Claude Code PM agent kit in this repo. Before writing anything:

## PHASE 0 — ORIENT (read-only, then report back)

1. Read `AGENTS.md`, `SETUP.md`, every `.claude/skills/*/SKILL.md`, every `.claude/agents/*.md`,
   and list the contents of `.claude/reporting/` and `.claude/knowledge-dump/`.
2. Confirm back to me in a table: existing skills, existing agents (with model tier), and the
   conventions you must preserve (progressive disclosure, confidence tiering
   Confirmed/Inferred/Speculative, primary-source-first, Recursive Refinement protocol,
   the pm-quality-gate standard, bilingual output conventions in weekly-report).
3. Do NOT modify any existing file in this phase.
4. HARD RULES for the entire build:
   - AGENTS.md may grow by a maximum of 10 lines total across all phases. Everything else
     goes in skill bodies or agent files.
   - Never duplicate a capability an existing skill/agent already has — extend or route to it.
   - Everything runs 100% locally on my Windows PC. No cloud services, no external APIs
     except web search/fetch that agents already use.
   - Every new skill ends its outputs with: Assumptions · Risks · Open Questions · Next Steps.

**CHECKPOINT: report findings, then STOP and wait for my "proceed".**

---

## PHASE 1 — SECOND BRAIN (Obsidian vault + librarian agent)

Goal: a local Obsidian-compatible vault that becomes shared memory for all agents, so new
sessions load a ~500-token index instead of re-reading past conversations.

1. Create `vault/` at repo root with this structure (each folder gets a `_about.md` explaining
   its purpose in 3 lines):
   - `vault/INDEX.md`          ← the master map (see step 3)
   - `vault/projects/`         ← one MOC (map-of-content) note per initiative. Seed three:
                                  `fca-launch.md`, `h2-2026-perps.md`, `2027-physical-equities.md`
   - `vault/decisions/`        ← decision log, one file per decision (see template, step 2)
   - `vault/sops/`             ← final SOPs (sop-builder outputs land here)
   - `vault/people/`           ← stakeholder notes (seed from the stakeholder map inside
                                  the meeting-synthesis skill: Karlos, Vincent/Eason, Betty/Jin,
                                  Amin, Andy/Elio, Vladimir, Jennifer, Pandy)
   - `vault/competitive/`      ← competitive-intel-brief outputs land here
   - `vault/daily/`            ← morning briefings (Phase 3) land here
   - `vault/meetings/`         ← meeting-synthesis outputs land here

2. Frontmatter schema (YAML, enforced on every note):
   ```yaml
   ---
   title:
   type: project | decision | sop | person | competitive | briefing | meeting
   project:            # links to a projects/ MOC, e.g. fca-launch
   status: active | done | blocked | superseded
   confidence: confirmed | inferred | speculative   # for factual notes
   owner:
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   tags: []
   ---
   ```
   Decision-note body template: **Decision / Date / Context / Options considered /
   Rationale / Who signed off / Revisit trigger.**

3. `vault/INDEX.md`: one line per note — `[[wikilink]] | type | one-line summary | updated`.
   Grouped by folder. Target ≤ 500 tokens; when it exceeds that, archive `done`/`superseded`
   entries to `vault/INDEX-archive.md`.

4. New agent `.claude/agents/librarian.md`:
   - model: haiku · tools: Read, Write, Edit, Grep, Glob (NO web)
   - Duties: (a) file any deliverable I hand it into the right vault folder with valid
     frontmatter; (b) update INDEX.md after every filing; (c) on request, answer
     "what do we know about X" by reading INDEX.md first, then only the 1–3 relevant notes —
     never bulk-read the vault; (d) refuse to erase confidence tiers or VERIFY flags.
   - Description must trigger on: "file this", "update the vault", "what do we know about",
     "load context on [project]".

5. Add to AGENTS.md (≤5 lines): the vault is the single source of truth for past work;
   at session start on a known project, ask librarian for INDEX.md + the project MOC
   instead of asking me to re-explain; all finished deliverables get filed via librarian.

6. PILOT (do this with me now): take the most recent competitive brief or weekly report in
   this repo, have librarian file it, and show me the resulting note + updated INDEX.md.

**CHECKPOINT: show vault tree, one seeded project MOC, the librarian file, the pilot result. STOP.**

---

## PHASE 2 — COMMAND CENTRE (inbox + STATUS.md + /standup)

Goal: a folder-watch-style routing layer and one command that runs my morning.

1. Create `inbox/` at repo root: `inbox/transcripts/`, `inbox/reports/`, `inbox/notes/`,
   each with a `_about.md` describing what to drop there and which skill consumes it.
2. Create `STATUS.md` at repo root — maintained by librarian: Active projects (from vault MOCs),
   Open action items (owner + due), Blocked/waiting-on, Last briefing date, Inbox items
   not yet processed.
3. Create `.claude/commands/standup.md` — a slash command that:
   a. Lists unprocessed files in `inbox/` and proposes routing (transcript → meeting-synthesis;
      report images → the reporting skill; notes → sop-builder or prd-authoring — ASK if ambiguous).
   b. Runs the market-briefing skill (Phase 3) if today's briefing doesn't exist in `vault/daily/`.
   c. Reads STATUS.md and surfaces: overdue action items, blocked items, decisions awaiting sign-off.
   d. Ends with a suggested top-3 for my day. Total output ≤ 1 screen.
4. Create `.claude/commands/eod.md` — end-of-day: file today's deliverables via librarian,
   update STATUS.md, list what rolled over to tomorrow.

**CHECKPOINT: show both commands; dry-run /standup with me. STOP.**

---

## PHASE 3 — MARKET BRIEFING SKILL (morning US news sharing)

Goal: my daily open-sharing input — US news that could move volatility, tuned to a
CFD/multi-asset brokerage audience.

1. New skill `.claude/skills/market-briefing/SKILL.md`. Triggers: "morning briefing",
   "market brief", "what moved overnight", or the /standup command.
2. Research step: delegate scanning to `pm-researcher` (do not create a new research agent).
   Coverage checklist — for each, search and report only if material:
   - Macro: Fed/FOMC, CPI/NFP/PCE prints, Treasury yields, DXY moves
   - Regulators: SEC, CFTC, FCA, ADGM/FSRA announcements touching brokers, CFDs,
     leverage, crypto, tokenized/pre-IPO equities
   - Exchanges/venues: CME (esp. 24/7 gold & crude expansion), major outage/rule changes
   - Big tech & earnings that move index CFDs; crypto regulatory/market structure news
   - Competitors in passing (Binance, Bybit, Robinhood) — route deep dives to
     competitor-analyst, don't do them here
3. Output format (file to `vault/daily/YYYY-MM-DD-briefing.md` via librarian):
   - BLUF: 3 bullets max — the things I should say in the meeting
   - Table: Item | What happened | Source (primary link) | Volatility/product impact for
     Vantage ("so what" column, XAUUSD/SPCX anchored where relevant) | Confidence tier
   - One "watch today" line (data prints / events scheduled today, with times in MYT)
   - Regulatory items follow the existing rule: mark VERIFY + name the source, never assert
     from memory.
4. PILOT: run it now for today; I will grade it against what I'd actually share, then you
   codify fixes into the skill body per the Recursive Refinement protocol.

**CHECKPOINT: today's briefing draft. STOP.**

---

## PHASE 4 — GENERALIZED DATA-REPORT PIPELINE (PowerBI screenshots → stakeholder report)

Goal: extend the existing weekly-report pattern (PNG screenshots + template + self-improving
loop) into a reusable pipeline for ANY recurring report, since I cannot get PowerBI API access.

1. Do NOT rewrite `weekly-report` — it stays as-is for the UL report. Instead create
   `.claude/skills/report-from-images/SKILL.md` that generalizes its input contract:
   - Input: (a) a folder of PowerBI screenshot images under
     `.claude/reporting/<report-name>/<period>/`, (b) a template under
     `.claude/reporting/<report-name>/templates/` (I will supply templates per report),
     (c) the prior period's folder for WoW/MoM deltas.
   - Extraction rule: read every figure from the images; if a number is unreadable or a
     needed figure is absent, STOP and list exactly what's missing and who owns it —
     never interpolate. Transcribed figures are `Confirmed (from image)`; anything computed
     is shown with its formula.
   - Loop: draft → `deliverable-critic` (pm-quality-gate standard) → revise, same stop
     condition as weekly-report (every CRITICAL dimension passes).
   - Output: report file + a ready-to-send message draft (email/Lark) per audience group,
     filed via librarian.
2. Migration note inside the skill: new recurring reports get onboarded by me dropping a
   template + first period of images, then one manual pilot run before the skill is trusted.
3. PILOT: I will drop a template + one set of screenshots into a new report folder; run the
   pipeline end-to-end with me and codify what breaks.

**CHECKPOINT after skill is written, BEFORE pilot. STOP.**

---

## PHASE 5 — LOCAL TRANSCRIPTION PIPELINE (recording policy approved)

Goal: local Whisper transcription feeding meeting-synthesis / prd-authoring / sop-builder.
All processing stays on my PC.

1. Create `scripts/transcribe/` with:
   - `setup.md` — Windows setup steps for **faster-whisper** (recommended over whisper.cpp on
     Windows: `pip install faster-whisper`, plus ffmpeg via winget). Include the whisper.cpp
     alternative path for CPU-only or if I prefer no Python. Recommend model `large-v3` for
     Mandarin/English code-switching accuracy; `medium` as the fast fallback. Note first-run
     model download size and rough runtime expectations per hour of audio on CPU vs GPU.
   - `transcribe.py` — takes an audio file (m4a/mp3/wav/mp4), outputs
     `inbox/transcripts/YYYY-MM-DD-<meeting-name>.md` with: frontmatter (date, meeting name,
     attendees=UNKNOWN placeholder), timestamped transcript body, and a footer flagging
     low-confidence segments. Language auto-detect ON (meetings mix EN/中文).
   - `transcribe.ps1` — PowerShell wrapper so I can drag-and-drop a recording onto it.
2. New routing rule appended to the `meeting-synthesis` skill (extend, don't fork): when
   invoked on a file from `inbox/transcripts/`, additionally ask me which downstream doc the
   meeting feeds — (a) notes only, (b) PRD section via prd-authoring, (c) SOP capture via
   sop-builder, (d) HoP brief — then chain the chosen skill. Attendee names get matched
   against `vault/people/`; unmatched speakers stay as `Speaker N` — never guess identities.
3. Privacy rules written into setup.md: recordings and transcripts are git-ignored
   (add `inbox/` and `*.wav,*.m4a,*.mp3,*.mp4` to `.gitignore`); transcripts containing client
   data never leave the machine; delete source audio after the transcript is confirmed good.
4. PILOT: I will record a short test clip; we run the full chain
   (audio → transcript → meeting-synthesis → filed in vault) once, then codify.

**CHECKPOINT after scripts + setup.md exist, BEFORE pilot. STOP.**

---

## PHASE 6 — OPS-CHECK RUNBOOKS (dividends, weekend swaps, ad hoc checks)

1. New skill `.claude/skills/ops-check-runbook/SKILL.md`: executes a named checklist runbook
   from `vault/sops/runbooks/`, item by item, against inputs I provide (screenshots, exported
   tables, MT5 admin values). Output: PASS/FAIL table per checklist item with evidence cited,
   confidence tier, and an exceptions section routed to the right owner (Ops: Betty/Jin,
   Risk: Amin, Admin: Andy/Elio — pull from the stakeholder map).
   Rule: an item with no evidence is `UNCHECKED`, never assumed PASS.
2. Seed two runbook SKELETONS in `vault/sops/runbooks/`: `dividend-adjustment-check.md` and
   `weekend-swap-check.md` — structure only (purpose, trigger, inputs needed, check items
   placeholder, owners, escalation). I will fill the actual check items from a live
   sop-builder session with the team, per the "capture live, not retrospectively" rule.

**CHECKPOINT. STOP.**

---

## PHASE 7 — LAUNCH CONDUCTOR (feature launch comms & stakeholder management)

1. New skill `.claude/skills/launch-conductor/SKILL.md`. Input: an approved PRD (IDEAL
   template). Output package, filed under the project's vault MOC:
   - Stakeholder/comms matrix derived from the PRD's RACI (who is informed of what, when,
     via which channel)
   - Launch comms calendar working backward from the launch date (internal announcements,
     training, marketing brief handoff, customer notification timeline)
   - Customer notification draft(s) using the notification conventions in the knowledge-dump
     UL PRD (including the "special time period events may vary per risk management" clause
     pattern) — every notification draft is marked DRAFT — Legal/Compliance sign-off required,
     with the sign-off gate as a blocking checklist item
   - Go/no-go checklist referencing the PRD's Definition of Done
2. Rule: the skill refuses to produce a launch package from a PRD missing acceptance criteria,
   RACI, or the compliance sign-off section — it routes to prd-authoring gap mode instead.
   (This is the PRD linter, enforced at the moment it matters.)

**CHECKPOINT. STOP.**

---

## FINAL PHASE — DOCUMENTATION & HYGIENE

1. Update `SETUP.md` with the new architecture map (vault, inbox, commands, new skills/agents,
   transcription scripts) and a one-paragraph "daily flow": record/drop inputs → /standup →
   work → /eod.
2. Verify `.gitignore` covers: `vault/` (contains internal knowledge — confirm with me whether
   I want it in git at all), `inbox/`, `.claude/knowledge-dump/`, `.claude/reporting/`,
   audio/video extensions, `scripts/transcribe/models/`.
3. Print a final table: every new file created, its purpose, and its trigger — plus the pilot
   status of each new skill (piloted ✅ / awaiting pilot ⏳). Nothing is "done" until piloted.
