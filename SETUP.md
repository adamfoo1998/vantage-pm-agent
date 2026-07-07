# Vantage PM Agent — Setup & Operating Manual

A Claude Code starter kit for a Vantage Senior PM. Built on the **"less is more / progressive
disclosure"** model: a lean `AGENTS.md` plus a small set of Skills whose full instructions load
only when needed.

## What's in here
```
vantage-pm-agent/
├── AGENTS.md                         # loads every turn — keep it lean (9/10 line budget used)
├── SETUP.md                          # this file
├── STATUS.md                         # live snapshot — active projects, action items, blockers
├── vault/                            # second brain (Obsidian-compatible) — see below
├── inbox/                            # drop zone routed by /standup — see below
├── scripts/transcribe/               # local Whisper transcription (Phase 5)
└── .claude/
    ├── commands/
    │   ├── standup.md                # morning routine
    │   └── eod.md                    # end-of-day wrap
    ├── agents/
    │   ├── librarian.md              # haiku — files deliverables, maintains vault/INDEX.md + STATUS.md
    │   ├── pm-researcher.md          # general web research delegate
    │   ├── competitor-analyst.md     # one named competitor, primary-source-first
    │   ├── citation-verifier.md      # opus — verify one claim vs its primary source
    │   ├── deliverable-critic.md     # opus — scores a draft against pm-quality-gate
    │   └── doc-drafter.md            # haiku — format/write from material already in hand
    └── skills/
        ├── competitive-intel-brief/SKILL.md
        ├── prd-authoring/SKILL.md
        ├── meeting-synthesis/SKILL.md
        ├── hop-brief/SKILL.md
        ├── sop-builder/SKILL.md
        ├── weekly-report/SKILL.md
        ├── pm-quality-gate/SKILL.md
        ├── storm-research/SKILL.md
        ├── market-briefing/SKILL.md          # Phase 3
        ├── report-from-images/SKILL.md       # Phase 4
        ├── ops-check-runbook/SKILL.md        # Phase 6
        └── launch-conductor/SKILL.md         # Phase 7
```

### `vault/` — second brain
Obsidian-compatible notes with enforced YAML frontmatter (`type`, `project`, `status`,
`confidence`, `owner`, dates, `tags`). `vault/INDEX.md` is the always-cheap map — one line per
note, read that first. Subfolders: `projects/` (MOCs), `decisions/`, `sops/` (incl.
`sops/runbooks/`), `people/`, `competitive/`, `daily/` (briefings), `meetings/`. `librarian`
(haiku, no web) files everything here and keeps `INDEX.md` + root `STATUS.md` current — never
erases confidence tiers or `VERIFY` flags.

### `inbox/` — routing drop zone
`transcripts/`, `reports/`, `notes/`, each with an `_about.md` naming which skill consumes it.
`/standup` lists anything sitting here unprocessed and proposes routing.

### `scripts/transcribe/` — local transcription
`transcribe.py` (faster-whisper) + `transcribe.ps1` (drag-and-drop wrapper) turn a recording into
`inbox/transcripts/YYYY-MM-DD-<meeting-name>.md`. Fully local — see `scripts/transcribe/setup.md`
for install + the privacy rules (audio/transcripts git-ignored, source audio deleted once the
transcript is confirmed good).

## Daily flow
Record or drop today's inputs (a meeting recording onto `transcribe.ps1`, a report screenshot
into `inbox/reports/`, raw notes into `inbox/notes/`) → run **`/standup`** to triage the inbox,
get the morning market briefing, and see what STATUS.md is surfacing → do the day's work through
whichever skill applies → run **`/eod`** to file the day's deliverables via `librarian`, refresh
STATUS.md, and see what rolled over to tomorrow.

## Install
1. Copy `AGENTS.md` and the `.claude/` folder into the root of the repo/folder where you run
   Claude Code. (Project-level skills live in `.claude/skills/<name>/SKILL.md`. Confirm the path
   matches your Claude Code version; the convention is stable but verify with `/skills` or your
   docs.)
2. Start Claude Code in that folder. Run `/skills` (or your version's equivalent) to confirm the
   skills are detected.
3. Ask the agent a question that should trigger a skill (e.g. "benchmark Bybit perps vs Binance
   for XAUUSD-style exposure") and confirm it reaches for `competitive-intel-brief`.

## How the context model works (why AGENTS.md stays thin)
Every turn, the agent's context holds: system prompt + AGENTS.md + each skill's **name +
description** + tools + your conversation. Skill **bodies** are NOT loaded until the agent decides
a skill applies. So: put rules the agent must always follow in `AGENTS.md` (cheap, short); put
procedures in skill bodies (free until triggered). If `AGENTS.md` grows past ~one screen, move the
overflow into a skill.

---

## The Agent Workflow Optimization Loop (operating SOP)
Do **not** trust the scaffolds in this kit as finished. They are v0.1 hypotheses. Earn each
finished skill through this loop:

1. **Identify the objective** — pick one specific, repeated task (e.g. "fact-check a Binance
   claim", "gap-analyse a PRD").
2. **Manual pilot run** — walk the agent through the task step by step. Correct it in real time.
   Don't let it guess; guide it to the known-good output.
3. **Validate success** — confirm the output meets the quality bar (would it pass Karlos?). If
   not, fix and re-run until it does.
4. **Codify** — once a run is genuinely good, tell the agent: *"Update
   `.claude/skills/<name>/SKILL.md` to capture exactly what worked here."* Let it rewrite the
   body from the successful run, not from imagination.

### Recursive Refinement (when a skill fails on an edge case)
1. **Capture** — isolate the exact error: what went wrong, on what input.
2. **Fix** — feed the failure + the correct result back to the agent.
3. **Update** — explicitly instruct: *"Add a rule to this skill's body so this specific failure
   can't recur."* The skill gets smarter; the mistake is retired.

Treat failures as training data. Over a few weeks the skill bodies become *your* high-quality
workflow, not a generic template.

---

## Scale deliberately (don't over-architect)
The kit has grown past the original four skills (see the file tree above) through the v2 phased
build — vault, inbox, command centre, market briefing, generalized reporting, transcription,
ops-check runbooks, and launch conductor. Every new skill was piloted or is awaiting its first
real pilot before being trusted (see the pilot-status table below) — don't add more surface area
than you're actually running.

## Backlog — skills to grow next, experientially (not pre-written on purpose)
- `roadmap-prioritisation` — RICE/WSJF scoring for roadmap items (CFD/perp, equities).
- `risk-policy-draft` — structured first-draft risk policy (e.g. pre-IPO perp), every line
  `VERIFY`-flagged for compliance review.
- `product-knowledge-library` — maintain the unified product knowledge base / user manuals.

Build each only after you've run the task manually with the agent a few times.
