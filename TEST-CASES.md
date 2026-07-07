# Test Cases & Usage Guide

A practical map of every skill, agent, and command in this kit — what it's for, an example
prompt to actually try, what you should get back, and whether it's been proven on a real task yet
or is still waiting for its first real run. Use this to navigate: "I need to do X" → find X below
→ copy the example prompt.

**Pilot status key:** ✅ piloted on real work · ⏳ built, awaiting first real use · 🚧 blocked (needs input from you first)

---

## Skills
Skills trigger automatically when your request matches their description — you don't need to
name them, just describe what you want. Named here for reference.

| Skill | What it's for | Try this | Expect | Status |
|---|---|---|---|---|
| **competitive-intel-brief** | Competitive intel on a broker/exchange, or benchmarking any trading product against Vantage | *"Benchmark Bybit's perpetual leverage against our Unlimited Leverage product"* | A structured brief: BLUF, comparison table, every claim tiered Confirmed/Inferred/Speculative with a primary source, `VERIFY` flags on anything regulatory | ✅ |
| **prd-authoring** (author mode) | Build a full PRD from raw notes/context | *"Write a PRD for [feature] — here's what I know: [notes]"* | The 15-section IDEAL PRD (RACI, acceptance criteria in Given/When/Then, DoD, open questions for every gap) | ✅ |
| **prd-authoring** (gap mode) | Audit an existing PRD for missing sections | *"Review this PRD"* / *"gap-check this"* (with the PRD attached/pasted) | Section-by-section PASS/WEAK/MISSING table + top 3 delivery risks | ⏳ |
| **meeting-synthesis** | Turn a transcript or notes dump into decisions/action items | Paste a meeting transcript and say *"summarise this"* | TL;DR, decisions vs. open discussion, action-item table with named owners, risks, follow-ups | ✅ (used repeatedly pre-v2) |
| **hop-brief** | Convert a technical output into a plain-language brief for Karlos/Taiwan | *"Make this ready for Karlos"* (after a competitive brief or PRD) | Same content, jargon-decoded, acronyms expanded once, copy-paste ready | ⏳ |
| **sop-builder** | Turn messy/raw knowledge into a structured SOP | *"Document how MT5 group config works — here's what Caleb told me: [notes]"* | Header block (owner, confidence, status) + numbered step-by-step procedure + common errors section | ⏳ |
| **weekly-report** | The bilingual Unlimited Leverage weekly report | *"Draft the weekly report"* (with this week's PowerBI screenshots in `.claude/reporting/unlimited-leverage-report/<week>/`) | Two bilingual reports (detailed + committee summary), self-iterated against `pm-quality-gate` via `deliverable-critic` until it passes | ✅ (production skill) |
| **pm-quality-gate** | The shared quality bar + draft→critique→revise loop | *"Hold this to the PM standard"* on any draft | Per-dimension PASS/FAIL, iterated up to 4 rounds, final verification tally | ✅ (used inside weekly-report/market-briefing) |
| **storm-research** | Deep multi-perspective, citation-verified research briefing | *"Storm research: tokenized equities regulatory landscape 2026"* | HTML report: 5 expert lenses → contradiction map → synthesis → adversarial peer review | ✅ |
| **market-briefing** | Daily morning news scan for the open-sharing meeting | *"Morning briefing"* or just run `/standup` | BLUF (3 bullets) + per-item News→Why→Watch-for reasoning chain, filed to `vault/daily/` | ✅ piloted twice (Jul 5, Jul 7), format locked in |
| **report-from-images** | Generalized PowerBI-screenshot → stakeholder report (any report besides UL) | Drop a template into `.claude/reporting/<name>/templates/` + screenshots into `.claude/reporting/<name>/<period>/`, then *"build the [name] report"* | Report file(s) per audience group + a ready-to-send message draft, filed via `librarian` | 🚧 needs you to drop a template + first period of screenshots |
| **ops-check-runbook** | Execute a named checklist runbook against evidence you provide | *"Run the dividend adjustment check"* (with screenshots/exports) | PASS/FAIL/UNCHECKED table with evidence cited + exceptions routed to the right owner | 🚧 blocked — both seeded runbooks (`dividend-adjustment-check`, `weekend-swap-check`) are empty skeletons; need a live `sop-builder` session with Ops/Risk/Admin to fill real check items first |
| **launch-conductor** | Turn an approved PRD into a launch package | *"Build the launch package for [PRD]"* | Stakeholder/comms matrix, launch comms calendar, DRAFT customer notifications (Legal/Compliance-gated), go/no-go checklist — refuses and routes to `prd-authoring` gap mode if the PRD's RACI/acceptance-criteria/compliance sections are missing | 🚧 needs an approved PRD to run against |

---

## Agents
These are usually invoked automatically by the skills above (e.g. `market-briefing` calls
`pm-researcher`; `weekly-report` calls `deliverable-critic`). You can also call them directly by
name if you want just that one piece.

| Agent | Model | What it does | Direct-invoke example |
|---|---|---|---|
| **librarian** | Haiku | Files deliverables into `vault/` with proper frontmatter, keeps `vault/INDEX.md` + `STATUS.md` current, answers "what do we know about X" | *"File this to the vault"* / *"What do we know about the FCA launch?"* |
| **pm-researcher** | — | General web research delegate (not a single named competitor) | *"Research the current state of tokenized RWA regulation"* |
| **competitor-analyst** | — | Primary-source-first deep dive on ONE named competitor | *"What does Bitget offer for XAUUSD-equivalent commodity CFDs?"* |
| **citation-verifier** | Opus | Verifies one already-written claim against its primary source | *"Verify this claim: [claim + source]"* |
| **deliverable-critic** | Opus | Fresh-eyes adversarial scorer against `pm-quality-gate` | *"Critique this draft against the PM standard"* |
| **doc-drafter** | Haiku | Formats/writes from material already in hand — no web access | *"Format these raw notes into a clean comparison table"* |

---

## Commands

| Command | What it does | Status |
|---|---|---|
| **`/standup`** | Inbox triage + proposed routing → today's market briefing (runs it if missing) → STATUS.md scan (overdue/blocked/decisions-pending) → top-3 for the day | ✅ piloted 2026-07-07 — scaffolding proven; inbox-triage *logic* still untested since inbox has been empty both runs |
| **`/eod`** | Files today's deliverables via `librarian` → refreshes STATUS.md → lists rollover to tomorrow | ✅ piloted 2026-07-08 |

---

## Local transcription pipeline (`scripts/transcribe/`)

| Tool | What it does | Try this | Status |
|---|---|---|---|
| **`transcribe.py`** / **`transcribe.ps1`** | Transcribes an existing audio file (m4a/mp3/wav/mp4) | Drag a recording onto `transcribe.ps1` | 🚧 needs one real test file to pilot |
| **`watch_and_record.py`** / **`start_watcher.ps1`** | Auto-detects Zoom/Teams/Lark running, records mic+system audio, auto-transcribes when the call ends | Run `start_watcher.ps1`, join a real (low-stakes) Lark call | 🚧 unverified — confirm Lark's real process name first (see `setup.md`), then pilot on one call |

---

## Vault lookups (no skill needed — just ask)

| Ask | What happens |
|---|---|
| *"What do we know about the FCA launch?"* | `librarian` reads `vault/INDEX.md`, then only the 1-3 relevant notes — not a bulk vault read |
| *"Load context on h2-2026-perps"* | Same pattern — INDEX first, then the project MOC |
| *"Update the vault with this decision"* | `librarian` files it into `vault/decisions/` with the Decision/Date/Context/Options/Rationale/Sign-off template |

---

## What's genuinely proven vs. still theoretical

**Proven on real work:** `librarian`, `STATUS.md`, `/standup`, `/eod`, `market-briefing`,
`meeting-synthesis`, `weekly-report`, `pm-quality-gate`, `storm-research`, `competitive-intel-brief`,
`prd-authoring` (author mode).

**Built but not yet run for real:** `hop-brief`, `sop-builder`, `prd-authoring` (gap mode),
`report-from-images`, `ops-check-runbook`, `launch-conductor`, the transcription pipeline
(both manual and auto-record), inbox-triage routing logic.

Treat the second group as v0.1 hypotheses, not finished tools — per `SETUP.md`'s Agent Workflow
Optimization Loop, the first real run of each is a pilot: walk through it, correct anything wrong
in real time, then tell the agent to codify what worked into the skill body.
