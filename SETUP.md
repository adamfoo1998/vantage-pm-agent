# Vantage PM Agent — Setup & Operating Manual

A Claude Code starter kit for a Vantage Senior PM. Built on the **"less is more / progressive
disclosure"** model: a lean `AGENTS.md` plus a small set of Skills whose full instructions load
only when needed.

## What's in here
```
vantage-pm-agent/
├── AGENTS.md                         # loads every turn — keep it lean
├── SETUP.md                          # this file
└── .claude/
    └── skills/
        ├── competitive-intel-brief/SKILL.md
        ├── prd-authoring/SKILL.md
        ├── meeting-synthesis/SKILL.md
        └── hop-brief/SKILL.md
```

## Install
1. Copy `AGENTS.md` and the `.claude/` folder into the root of the repo/folder where you run
   Claude Code. (Project-level skills live in `.claude/skills/<name>/SKILL.md`. Confirm the path
   matches your Claude Code version; the convention is stable but verify with `/skills` or your
   docs.)
2. Start Claude Code in that folder. Run `/skills` (or your version's equivalent) to confirm all
   four skills are detected.
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
Start with this single agent and these four skills. Only add sub-agents once the primary agent is
reliable. Resist the urge to build a multi-agent system for fashion.

## Backlog — skills to grow next, experientially (not pre-written on purpose)
- `sop-builder` — codify any repeated workflow into a step-by-step SOP (your job explicitly
  requires maintaining SOPs; this is also the loop, productised).
- `roadmap-prioritisation` — RICE/WSJF scoring for roadmap items (CFD/perp, equities).
- `risk-policy-draft` — structured first-draft risk policy (e.g. pre-IPO perp), every line
  `VERIFY`-flagged for compliance review.
- `product-knowledge-library` — maintain the unified product knowledge base / user manuals.

Build each only after you've run the task manually with the agent a few times.
