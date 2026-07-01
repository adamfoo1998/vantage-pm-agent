# The Complete Guide to Claude Code Subagents

*From "what is this" to building your own fleet. Read top to bottom once, then keep it as a reference.*

---

## Part 1: The 30-Second Version

A subagent is a second Claude that your main Claude can hand a job to.

It runs in its own separate window, does the messy work (reading 40 files, searching the whole codebase, digging through logs), then hands back a short summary. All the noise stays in its window. Your main chat only sees the clean answer.

That is the whole idea. Everything else in this guide is detail on top of that one sentence.

Three things to lock in before we go deep:

1. **Subagents save your context.** The main chat stays clean because the grunt work happens somewhere else.
2. **There are built-in ones and ones you build yourself.** Claude ships with a few. You can write your own as little files.
3. **You can specialize them.** Each one can have its own job, its own tools, and its own (cheaper) model.

---

## Part 2: The Mental Model (Read This Twice)

Picture your main Claude session as **you, the general contractor** on a job site.

You do not personally read every spec sheet, count every nail, and inspect every weld. If you did, your head would be so full of detail you would lose track of the actual build. Instead you send specialists off: "Go inspect the foundation and report back." They go do the dirty, detailed work. They come back and say "Foundation's good, one crack on the north wall, here's the photo." You never had to hold all that detail in your own head.

That is exactly what a subagent is. A specialist you send off so your own head (the context window) stays clear.

### Why this matters: the context window problem

Claude has a limited memory for any single conversation. Every file it reads, every search result, every log line gets added to that memory and stays there for the rest of the chat. Do enough heavy work and the window fills up. When it fills up, Claude gets slower, more expensive, and starts forgetting things from earlier.

Heavy tasks are the worst offenders:

- Searching 200 files for one pattern dumps dozens of file contents into memory.
- Running a test suite dumps hundreds of lines of output.
- Researching a problem dumps pages of documentation.

A subagent does all of that in **its own** memory. When it finishes, only the final summary comes back to your main chat. The 200 file reads, the test output, the research pages all stay behind in the subagent's window and disappear when it is done.

**This is the number one reason subagents exist.** Not speed. Not even cost directly. Context preservation. Keep that front of mind and every other decision in this guide gets easier.

---

## Part 3: The Two Kinds of Subagent

### Kind 1: Built-in (native) subagents

These ship with Claude Code. You do not create them. Claude reaches for them automatically when a task fits. You will often see Claude say "Exploring..." or spin one up without you asking. The three that do real work:

| Built-in | Model | Tools | What it does |
|----------|-------|-------|--------------|
| **Explore** | Haiku (fast, cheap) | Read-only | Fast codebase search and file discovery. Skips your CLAUDE.md and git status to stay quick and cheap. Claude can tell it to be "quick," "medium," or "very thorough." |
| **Plan** | Inherits main model | Read-only | Gathers codebase context during Plan mode, before Claude presents a plan. |
| **General-purpose** | Inherits main model | All tools | Complex, multi-step jobs that need both exploration AND action. The Swiss Army knife. |

There are also small helper agents Claude uses behind the scenes (for example one that sets up your status line, one that answers questions about Claude Code itself). You will rarely think about those.

**Key point for beginners:** you get value from subagents on day one without building anything. The built-ins are already working for you. Building your own is the next level, not the entry fee.

### Kind 2: Custom subagents (the ones you build)

These are the ones you write. They live as little Markdown files in a folder. They are how you create a permanent "code reviewer," a "researcher," a "test runner," whatever recurring specialist you need. The rest of this guide is mostly about these.

---

## Part 4: What a Custom Subagent Actually Looks Like

A custom subagent is just **one Markdown file** with two parts:

1. A **frontmatter** block at the top (the settings, written in YAML between `---` lines).
2. A **body** below it (plain English instructions that become the subagent's entire personality and job description).

Here is a complete, real one:

```markdown
---
name: code-reviewer
description: Expert code review specialist. Use proactively after writing or modifying code. Also triggers on "review my changes" or "check this PR".
tools: Read, Grep, Glob, Bash
model: sonnet
---

You are a senior code reviewer ensuring high standards of code quality and security.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately without asking for clarification

Review checklist:
- Code clarity and readability
- Proper error handling
- No exposed secrets or API keys
- Input validation present
- Adequate test coverage

Provide feedback in three tiers:
- Critical (must fix before merge)
- Warnings (should fix)
- Suggestions (consider improving)

Include specific file paths and line references.
```

That is it. That file IS the subagent. Drop it in the right folder and Claude can now use it.

### Where these files live: project-level vs global-level

This is the part beginners get wrong most often, so go slow here. It comes down to one choice: **where you save the file.** That single choice decides two completely separate things:

1. **Where you can use the agent** (which projects it shows up in)
2. **Who else gets the agent** (just you, or your whole team)

There are two main spots to save a subagent. That is it. Pick one based on those two questions.

#### Option A: Project-level — `.claude/agents/` inside a specific project

The file lives in a `.claude/agents/` folder **inside one project's repo.**

- **Where you can use it:** ONLY when you are working inside that project. Open a different project and the agent is gone. It does not exist there. It is bolted to this one repo.
- **Who else gets it:** Your **whole team.** Because the file sits inside the project folder, it gets committed to git like any other file. When a teammate clones or pulls the repo, the agent comes with it automatically. They do not install anything. They open the project and the agent is just there, ready to invoke.
- **Think of it as:** a tool that belongs to the project, not to you. It ships with the codebase.

This is the right choice when the agent only makes sense for this codebase. A "run our specific test suite" agent, a reviewer that knows your project's conventions, a deploy helper for this app. Stuff a teammate on this project would also want.

#### Option B: Global-level (a.k.a. user-level) — `~/.claude/agents/` in your home folder

The file lives in the `.claude/agents/` folder in your **home directory** (the `~/` means your user folder, e.g. `C:\Users\Nate\.claude\agents\` on Windows).

- **Where you can use it:** **Every project on your machine.** It follows you everywhere. Open any repo, any folder, the agent is available.
- **Who else gets it:** **Nobody. Just you.** This folder is on your personal machine and is not part of any project's git repo. It is your private toolkit. A teammate has no idea it exists unless you send them the file by hand.
- **Think of it as:** a tool that belongs to YOU, not to any one project. It travels with your account, not with the code.

This is the right choice for your personal favorites: a general researcher, a "explain this code" helper, an agent you reach for constantly no matter what you are working on.

#### Side by side

| | **Project-level** (`.claude/agents/` in the repo) | **Global / user-level** (`~/.claude/agents/`) |
|---|---|---|
| **Lives in** | A specific project's folder | Your home folder |
| **Usable in** | Only that one project | Every project on your machine |
| **Shared with team?** | **Yes** — rides along in git automatically | **No** — private to you |
| **Travels with** | The codebase | Your machine / account |
| **Best for** | Project-specific specialists | Your personal everyday agents |

#### What "shared with the team" actually means in practice

Say you write a `code-reviewer` agent and save it project-level. You commit and push. Your teammate runs `git pull`. Now your teammate types `@agent-code-reviewer` and it works for them too, with the exact same instructions, tools, and model you set. You built it once, the whole team gets it, and it stays in sync through git. That is the entire reason project-level exists: agents become part of the project the same way code is.

A global agent does none of that. It is yours alone. If a teammate wants it, you have to literally hand them the `.md` file to drop in their own home folder.

#### When the same name exists in both

If you have a project-level agent and a global agent with the **same `name`**, the **project one wins** inside that project. This is on purpose: it lets a project override your personal default with a project-specific version. Everywhere else, your global one still applies.

#### Two smaller notes

- You can organize agents into subfolders (like `.claude/agents/review/security.md`). The folder path does not change anything. Only the `name` field inside the file matters, and it has to be unique.
- There are a couple of additional, more advanced scopes (plugins can ship agents, and enterprises can push org-wide managed agents). For 99% of use, project-level and global-level are the only two you need to think about.

> **Gotcha:** If you create or edit one of these files by hand, restart your Claude Code session so it picks up the change. The exception is the `/agents` command (covered below), which takes effect immediately.

---

## Part 5: How Claude Decides to Use One

You almost never call a subagent like a function. Claude picks them for you. There are four ways it happens, from most hands-off to most deliberate.

### 1. Automatic delegation (the default)

Claude reads the `description` field of every available subagent and routes to the matching one when your request fits. This is why the description is the single most important line in the whole file. It is not a label. It is the trigger rule.

- Weak description: `"Security expert"` (Claude has no idea when to use this)
- Strong description: `"Reviews code for security vulnerabilities. Use proactively after writing auth or data-handling code. Triggers on 'check this for security issues'."`

### 2. Proactive invocation

Put the literal phrase **"use proactively"** in the description and Claude will reach for the agent without you asking. Example: a code reviewer that fires automatically right after you change code, no prompt needed.

### 3. Explicit, by name

Just ask in plain English: *"Use the test-runner subagent to fix the failing tests."* Or guarantee a specific one runs by @-mentioning it: `@agent-code-reviewer check the auth changes`. The @-mention is the "I definitely want THIS one" button.

### 4. As the whole session's default

You can launch Claude so a subagent's personality runs the entire session: `claude --agent code-reviewer`. Most beginners never need this, but it exists.

### The `/agents` command

Type `/agents` in Claude Code to open a manager. From there you can:

- See which subagents are currently running.
- Browse every available agent (built-in, yours, your team's).
- **Create a new one** with a guided form, or by describing it and letting Claude write the file for you.
- Edit or delete existing ones.

For beginners this is the easiest way to make your first subagent. You do not have to hand-write the file. Changes here apply immediately, no restart.

---

## Part 6: The Settings (Frontmatter Fields)

You only need **two** fields to have a working subagent. Everything else is optional power.

### The two required fields

| Field | What it does |
|-------|--------------|
| `name` | The agent's ID. Lowercase, hyphens only (`code-reviewer`). Must be unique. |
| `description` | When Claude should use it. This is your trigger rule. Write it carefully. |

### The two you will use constantly

| Field | What it does |
|-------|--------------|
| `tools` | Which tools the agent is allowed to touch. Leave it out and it inherits everything. (See Part 7.) |
| `model` | Which model it runs on: `haiku`, `sonnet`, `opus`, or `inherit`. Leave it out and it inherits the main model. (See Part 8.) |

### The advanced fields (newer versions, nice to know)

These exist in recent Claude Code versions. You do not need them to start. Check `/agents` or the official docs if you want to confirm one is available in your version.

| Field | What it does |
|-------|--------------|
| `disallowedTools` | The opposite of `tools`. Inherit everything EXCEPT these. Handy for "give it everything but writing." |
| `maxTurns` | Caps how many steps the agent can take. Stops runaway agents from burning tokens on tangents. |
| `color` | The display color in the UI. Cosmetic. |
| `skills` | Preloads specific skills into the agent at startup. |
| `permissionMode` | Overrides how the agent handles permission prompts. |
| `isolation: worktree` | Gives the agent its own isolated copy of the repo so parallel agents do not collide when editing files. |
| `background: true` | Always run this one as a non-blocking background task. |

Start with the four. Reach for these later.

---

## Part 7: Tools (and Why You Restrict Them)

If you do not list any tools, your subagent inherits **everything** the main session has: reading, writing, running commands, web access, your connected services, all of it. That is usually too much.

Restricting tools is free, physical enforcement. A code reviewer that only has `Read, Grep, Glob` literally cannot modify your code, no matter what goes wrong. You are not trusting it to behave. You made misbehaving impossible.

Simple decision rule:

- **Look-but-don't-touch roles** (reviewer, auditor, researcher, explorer): `tools: Read, Grep, Glob, Bash`
  *(Bash is for running read-only things like `git diff` or tests, not for editing.)*
- **Fix-it roles** (debugger, implementer): add `Edit` and/or `Write`.
- **Web research roles**: `tools: WebSearch, WebFetch, Read`.

Two ways to control it:

- `tools:` is an **allowlist** (only these, nothing else).
- `disallowedTools:` is a **denylist** (everything except these).

For a reviewer, an allowlist is cleanest. For "give it the works but never let it write," a `disallowedTools: Write, Edit` denylist is faster.

---

## Part 8: Saving Money with Subagents

This is its own section because it is one of the biggest wins, and one of the easiest places to shoot yourself in the foot.

### Lever 1: Run cheap agents on cheap models

Every subagent can run on a different model. This is the main cost dial.

| Model | Rough cost (per million tokens) | Use it for |
|-------|-------------------------------|------------|
| **Haiku** | ~$1 in / $5 out | Scanning files, summarizing logs, simple search, documentation. The cheap workhorse. |
| **Sonnet** | ~$3 in / $15 out | Most implementation and review work. The default sweet spot. |
| **Opus** | Significantly higher | Deep reasoning only: subtle security audits, complex architecture, anywhere a wrong answer is expensive. |

*(Prices are approximate and change. Treat them as ratios, not gospel.)*

The pattern that wins: a smart model running the show, cheap models doing the legwork. Anthropic's own multi-agent research system used an Opus "lead" with Sonnet "workers" and beat a single Opus by a wide margin on hard research tasks. The model **mix** beats raw spend.

Quick wins:

- Set your codebase explorer and doc writer to `model: haiku`. They do not need deep reasoning.
- Keep reviewers and implementers on `sonnet`.
- Reserve `opus` for the security auditor and gnarly debugging.
- You can also set the `CLAUDE_CODE_SUBAGENT_MODEL` environment variable to force a cheap model on all subagents at once (great for automated/CI runs).

### Lever 2: Context offloading (the structural saving)

This is the saving you get just by using subagents at all. The subagent reads 50 files in its own window and hands back a 3-paragraph summary. You paid for those 50 file reads **once, over there**. They never enter your main chat, so you are not re-paying to carry them in context for the rest of your session. On a long session, this is enormous.

### The trap: subagents are NOT free

Here is the nuance most people miss until it costs them.

A subagent starts with a blank slate. It cannot see your conversation. So it has to re-gather context every time it spins up. There is real overhead in that. The numbers people throw around:

- Plain chat: 1x tokens
- Single-agent coding: ~4x
- Multi-agent (lots of subagents): **~15x**

That 15x is the price of parallelism and isolation. It is worth it when the task is big or when keeping your main context clean is the whole point. It is a **waste** on a 20-second task you could have done inline.

**The rule:** if the job would read 10+ files or spit out noise you will never need again, a subagent saves you money overall. If it is a small, targeted change, do it inline and skip the overhead.

Bonus lever: set `maxTurns` on any agent that might wander, so it cannot rack up a huge bill chasing tangents.

---

## Part 9: When To Actually Use One (The Most Important Section)

This is the question everyone asks: *"Okay, but when do I actually reach for a subagent?"* Here is how to know in the moment, every time.

### The one-question gut check

Before anything else, ask yourself one thing:

> **"Is this task about to dump a pile of stuff into my chat that I will never need to look at again?"**

If yes, that is a subagent. If no, it is probably not.

That is the whole heuristic, and it traces straight back to the core idea from Part 2: subagents exist to protect your main context. A subagent reads the pile in its own window and hands you back the one paragraph that matters. Almost every "should I use one" question is really this question in disguise.

Everything below is just the specific shapes that gut check takes in real life.

### The signals that say "use a subagent"

These are moments you will actually notice yourself in. When you catch one, that is your cue.

**1. "This is going to read a LOT of files."**
Searching the whole codebase, scanning 15 files to understand how something works, crawling a directory. *Why:* every one of those files would land in your main context and sit there for the rest of the session. The subagent absorbs all of it and returns a summary. This is the single most common trigger.

**2. "This is going to spit out a wall of output I'll glance at once."**
Running the test suite, parsing a giant log file, pulling pages of web research, a noisy build. *Why:* the raw output is throwaway. You want the verdict ("3 tests failed, all in auth"), not 400 lines of stack traces clogging your chat.

**3. "I keep doing this exact task over and over."**
Reviewing every PR, auditing every auth change, updating docs after every release. *Why:* package it once as a specialist and it is permanent. You stop re-explaining the job every time, and the standard stays consistent.

**4. "I've got several independent jobs and none needs another's output."**
*Why:* this is the parallel test. When the inputs do not rely on other steps' outputs (no required order), fire several subagents at once and they run at the same time. Auth module, database layer, API routes, all explored simultaneously, then you synthesize. Doing it inline means one slow step after another. If the pieces ARE ordered (step 2 needs step 1's result), it is not parallel work, so keep it inline.

**5. "I want a second opinion that isn't biased by how I just built this."**
*Why:* a fresh subagent reviewing your code never saw your reasoning. It judges the result on its own terms, the way an outside reviewer would. Your main chat, by contrast, is emotionally invested in the code it just wrote. The fresh context is the feature.

**6. "I do NOT want this thing to be able to change anything."**
*Why:* a subagent with only `Read, Grep, Glob` physically cannot edit or delete. For an auditor or an explorer turned loose on a repo, that lockdown is not a suggestion, it is enforced. You are not trusting it to behave; you removed the ability to misbehave.

**7. "My context is almost full but I'm not done."**
*Why:* offloading the next heavy chunk to a subagent lets you keep going without compacting or losing the thread of your main session.

A fast way to remember the top one: **10+ files, or output you'll never re-read = subagent.** Under that bar, stay inline.

### The signals that say "do NOT use a subagent"

Equally important, and the part people skip. Forcing a subagent where it does not fit makes things slower, more expensive, and more confusing.

**1. "This is small and quick."**
A subagent has real startup cost: it spins up a blank context and re-gathers what it needs. *Why it's wrong here:* if the task takes 30 seconds inline, you just paid setup overhead for zero benefit. This is the most common misuse, and it is why people sometimes complain subagents feel "slow" or "token-hungry." They were aimed at the wrong job.

**2. "I'm in a tight back-and-forth, refining as I go."**
Step 2 depends on the full detail of step 1, and step 3 on step 2. *Why it's wrong here:* subagents hand back a summary, not the full detail, and they run start-to-finish without checking in. Iterative work belongs inline where you can steer turn by turn.

**3. "This needs everything we've talked about so far."**
*Why it's wrong here:* a subagent starts blank. It does not see your conversation, only a short task brief. If the job needs the last 20 messages of context, either re-explain it in the task (clunky) or use a **fork** instead, which is a subagent that DOES inherit the full conversation (see Part 12).

**4. "It'll need to ask me a question partway through."**
*Why it's wrong here:* subagents cannot stop to ask you anything. Background ones auto-deny anything that would prompt you. If the task is ambiguous, clarify it BEFORE you delegate, not during.

**5. "I want this subagent to spin up its own subagents."**
*Why it's wrong here:* subagents cannot nest. Only your main chat can be the conductor. If you need a chain, run it from the main conversation (see Part 11).

**6. "The subagents would need to talk to each other."**
*Why it's wrong here:* a subagent only ever reports back to the main chat. Two subagents cannot message each other or share state. If the work needs agents to discuss, hand off, and react to each other in real time, that is an Agent Team, not subagents (see Part 15). With subagents, every result routes through the main chat and gets synthesized there.

### Two quick before/after gut checks

- *"Find every place we call the old payments API."* → Subagent. It will grep the whole repo and read a dozen files. You want the list, not the search noise. **Use one.**
- *"Rename this variable and update the three spots that use it."* → Tiny, targeted, you can see all of it. **Stay inline.**
- *"Review the 600-line PR I just opened for security issues."* → Lots of reading, plus you want an unbiased eye. **Use one.**
- *"Add a console.log here so I can check the value."* → One line. **Stay inline.**

### The escape hatch for quick questions

For a quick question about something already in your chat, do not even use a subagent. Use `/btw`. It sees your full context but has no tools, so it answers fast and cheap without spinning anything up. Reach for a subagent only when there is real, tool-using work to offload.

---

## Part 10: Build Your Own, Step by Step

Two ways. Start with the easy one.

### The easy way (recommended for your first)

1. Type `/agents` in Claude Code.
2. Choose to create a new agent.
3. Either fill in the form, or just **describe what you want** and let Claude write the file for you.
4. Pick its tools and model in the UI.
5. Save. It works immediately, no restart.

### The manual way (when you know what you want)

1. Decide the **one job** this agent does. One job. If you catch yourself writing "and also," split it into two agents.
2. Create the file: `.claude/agents/your-agent-name.md` (project) or `~/.claude/agents/your-agent-name.md` (personal).
3. Write the frontmatter:
   - `name`: matches the filename, lowercase-hyphenated.
   - `description`: the trigger rule. Say WHEN to use it, name the signal phrases, add "use proactively" if it should fire on its own.
   - `tools`: the minimum it needs. Read-only unless it must edit.
   - `model`: cheap if the job is simple, sonnet/opus if it needs to think.
4. Write the body (this becomes its whole brain):
   - **Role:** one sharp sentence. "You are a senior security engineer."
   - **Workflow:** numbered steps for what to do when it starts.
   - **Checklist/criteria:** exactly what to look for or what "done" means.
   - **Output format:** how to structure the answer (tiers, line refs, word limits).
   - **Constraints:** what NOT to do ("Do not modify files. Return a summary only.").
5. Keep the body short. Focused prompts beat long ones. A bloated body makes the agent lose track of its own rules.
6. Restart the session (if you wrote the file by hand), then test it: ask Claude to do the thing and watch whether it routes correctly. First runs often reveal a vague description; tighten it.

---

## Part 11: Six Ready-to-Copy Agents

**Pro move: borrow before you build.** Whole collections of battle-tested Claude Code subagents live on GitHub (search "claude code subagents"). Download the `.md`, drop it in `.claude/agents/`, and it works immediately. Starting from someone else's proven agent and tweaking it beats writing one from scratch.

Drop any of these into `.claude/agents/`. Adjust tools and model to taste.

### 1. Code Reviewer

```markdown
---
name: code-reviewer
description: Expert code review specialist. Use proactively immediately after writing or modifying code. Triggers on "review my changes" or "check this PR".
tools: Read, Grep, Glob, Bash
model: sonnet
---

You are a senior code reviewer ensuring high standards of code quality and security.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately without asking for clarification

Review checklist:
- Code clarity and readability
- Well-named functions and variables
- No duplicated logic
- Proper error handling
- No exposed secrets or API keys
- Input validation present
- Adequate test coverage

Provide feedback in three tiers:
- Critical (must fix before merge)
- Warnings (should fix)
- Suggestions (consider improving)

Include specific file paths, line references, and concrete fix examples.
```

### 2. Debugger

```markdown
---
name: debugger
description: Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any error message or failed test.
tools: Read, Edit, Bash, Grep, Glob
model: sonnet
---

You are an expert debugger specializing in root cause analysis.

When invoked:
1. Capture the full error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location in the code
4. Implement the minimal fix
5. Verify by running the failing test or reproducing the scenario

For each issue, return:
- Root cause (not the symptom)
- Evidence for your diagnosis
- The specific fix applied
- Verification result
- One-line prevention tip

Fix the underlying issue, not the surface symptom.
```

### 3. Web Researcher

```markdown
---
name: researcher
description: General-purpose research agent. Use when a task needs web search, reading documentation, or gathering external information before a decision. Do not use for questions already answerable from the codebase.
tools: WebSearch, WebFetch, Read
model: sonnet
---

You are a research analyst. Find accurate, current information and return clean briefs.

When invoked:
1. Pin down the exact question to answer
2. Search broadly, then read the best sources in depth
3. Cross-reference key claims across multiple sources
4. Flag where sources disagree

Return:
- Direct answer to the question
- Key supporting evidence (bullets)
- Source URLs for factual claims
- Important caveats or uncertainties

Return a summary only. Never dump raw search results or full page contents.
```

### 4. Codebase Explorer

```markdown
---
name: codebase-explorer
description: Explores and maps unfamiliar codebases. Use proactively before planning changes. Triggers on "how does X work" or "find where Y is implemented".
tools: Read, Grep, Glob, Bash
model: haiku
---

You are a codebase analyst. Understand codebases quickly and return structured maps.

When invoked:
1. Identify main entry points and top-level structure
2. Find the files relevant to the question or task
3. Map key dependencies and patterns
4. Note conventions (naming, error handling, testing)

Return:
- Key files and what they do (bullet list)
- Architecture summary (2-3 sentences)
- Relevant patterns or conventions
- Anything that would surprise an outsider

Keep your response under 500 words. Synthesize. Do not dump file contents.
```

### 5. Documentation Writer

```markdown
---
name: doc-maintainer
description: Keeps documentation synced with code. Use proactively after changes to public APIs, function signatures, or user-facing behavior. Triggers on "update the docs".
tools: Read, Write, Edit, Glob, Grep
model: haiku
---

You are a technical writer keeping documentation accurate and current.

When invoked:
1. Read the relevant code files
2. Read the existing documentation
3. Identify what changed or is undocumented
4. Write or update docs to match the current code

Standards:
- Match the tone and format of existing docs
- Include code examples for API or signature changes
- Skip internal/private functions unless asked
- Flag anything uncertain instead of guessing

Return a summary of what you changed and why.
```

### 6. Security Auditor

```markdown
---
name: security-auditor
description: Reviews code for security vulnerabilities. Use proactively after writing auth, authorization, payment, or data-handling code. Triggers on "security review" or "check for vulnerabilities".
tools: Read, Grep, Glob, Bash
model: opus
---

You are a senior security engineer. Find real vulnerabilities, not style issues.

When invoked:
1. Run git diff to see recent changes
2. Read files involved in auth, authorization, or data handling
3. Search for common vulnerability patterns

Check for:
- SQL injection, XSS, command injection
- Authentication and authorization flaws
- Hardcoded secrets, API keys, credentials
- Insecure deserialization
- Missing input validation
- Insecure direct object references
- Dependency vulnerabilities

Return:
- Critical findings (file path, line number, severity, exploit scenario)
- Suggested fix for each
- Confidence level on each

Only report findings you can trace to specific code. No theoretical issues.
```

Notice the model choices: the explorer and doc writer run on **Haiku** (cheap, simple work), the reviewer and debugger on **Sonnet** (balanced), the security auditor on **Opus** (a wrong answer here is expensive). That single column is most of your cost control.

---

## Part 12: Chaining and Orchestration

This is where subagents go from "handy" to "a system." A few rules first, then the patterns.

### The composition rules

- **Skills can call subagents.** A skill (a saved workflow) can hand a step off to a subagent.
- **Subagents can call skills.** As long as the agent has the `Skill` tool, it can run your skills. You can even preload skills into an agent with the `skills:` frontmatter field.
- **Subagents CANNOT call other subagents.** No nesting. This is on purpose, to prevent infinite loops. If you need a chain, the **main conversation** runs it: it calls agent A, gets the result, then calls agent B with that result. The main chat is always the conductor.

### The patterns

**Sequential chain.** Main chat runs a pipeline: researcher finds the files → reviewer checks the plan → main implements. Best for 2-3 step flows where each step feeds the next.

**Fan-out / fan-in (parallel).** Main chat fires several agents at once, waits for all, then combines. Example: one explorer per module (auth, database, API) running simultaneously, then synthesize. This is where the speed gains live. Anthropic's research system cut research time dramatically by fanning out 3-5 subagents at once.

> **When the fan-out outgrows a handful, reach for a dynamic workflow.** Doing the orchestration by hand from the main chat is fine for two or three agents. When the job needs dozens (a codebase-wide audit, a 500-file migration, cross-checked research), a *dynamic workflow* is the right tool: it is a JavaScript script the main agent writes that orchestrates and runs many subagents in parallel at scale, then merges the results. The trade-off is cost: more agents means meaningfully more tokens, so point it only at jobs that genuinely break into many independent pieces.

**Orchestrator-worker.** One session that does no work itself. It only plans, delegates, reviews, and routes to the next worker. Spec writer → architect review → implementer → code reviewer → final PR. Good for full feature pipelines. Put human checkpoints at the important handoffs so it cannot run off a cliff.

**Builder/validator.** A builder writes the code. A separate validator checks it in a fresh context with no memory of the reasoning, so it judges the result on its own terms. This is the strongest argument for subagents in serious work: the reviewer is not biased by having written the thing.

**Worktree isolation.** When several agents need to edit files at the same time, give each `isolation: worktree` so they work on separate copies and do not collide.

### How many agents?

Most good setups run **2 to 8** agents. Past that, descriptions start overlapping, Claude routes to the wrong one, and you spend more time debugging the fleet than doing the work. More agents is not better. Sharper agents is better.

---

## Part 13: Limitations and Gotchas

Keep this list handy. Most "why did my agent do that" moments are on it.

- **Fresh memory every time.** A subagent does not see your chat history, your read files, or anything from the main session. It gets a task brief, its own system prompt, and your CLAUDE.md project rules (those still load). That is it. (The built-in Explore and Plan agents even skip CLAUDE.md to stay fast.)
- **It cannot ask you questions.** It runs to completion. Background ones auto-deny anything that would prompt you. Clarify before delegating.
- **No nesting.** Subagents cannot spawn subagents. Chain from the main chat instead.
- **Only the final message comes back.** All the intermediate work is gone once it finishes. That is the feature, but it means you cannot go fish around in what it did.
- **Startup overhead is real.** Do not use one for a task you could finish inline in 30 seconds.
- **Hand-edited files need a session restart.** Files made via `/agents` do not.
- **They cannot talk to each other.** Two running agents are blind to each other. Everything routes through the main chat.
- **Model names are lowercase.** `sonnet`, not `Sonnet`. The field is `model`, not `Model`.

---

## Part 14: Common Mistakes (and the Fix)

| Mistake | Why it bites | Fix |
|---------|--------------|-----|
| No `tools` field | Agent inherits write access and everything else. Security gap, unfocused. | Always list the minimum tools it needs. |
| Vague `description` | It never triggers, or triggers at the wrong time. | Write a trigger rule, not a label. Name the signal phrases. |
| Subagent for trivial tasks | You pay startup overhead for no gain. Feels slow and token-hungry. | Do small targeted work inline. |
| Expecting it to know the chat | It starts blank. It will be "confused." | Put needed context in the task, or use a fork. |
| Using agents to WRITE big features | Fresh-context agents go blind to overall project state. | Use agents to gather and review. Let the main chat implement. |
| Too many agents (15+) | Overlapping triggers, wrong routing, hard to debug. | Keep it to a handful. Merge overlapping ones. |
| Overlapping descriptions | Two agents match the same request; Claude picks randomly. | Make trigger conditions mutually exclusive. |
| No `maxTurns` on open-ended agents | One can wander and burn tokens. | Cap turns on anything exploratory. |

---

## Part 15: Subagents vs. Everything Else

People mix these up constantly. Here is the clean version.

| Thing | What it is | Lives where | Use when |
|-------|-----------|-------------|----------|
| **Subagent** | A second Claude with its own context and tools. Returns only a summary. | `.claude/agents/*.md` | A task is verbose, recurring, parallel, or needs isolation. |
| **Skill** | Saved instructions/workflow loaded into your MAIN context. No separate window. | `.claude/skills/` | A reusable recipe you want Claude to follow in the current chat. |
| **Slash command** | A quick built-in or custom command you type (`/compact`, `/agents`). | Built-in or skill-backed | A fast, one-shot action. |
| **MCP server** | A connection to an outside tool or service (Slack, a database, GitHub). | External process | You need data or actions from another system. |
| **Fork** | A subagent that DOES inherit your full conversation history. | `/fork` | A side task that genuinely needs everything said so far. |
| **Agent teams** | Multiple full sessions with a lead and teammates that message each other. (Experimental.) | Separate sessions | A big project split across many agents that must coordinate. |
| **Dynamic workflow** | A JavaScript script the main agent writes that orchestrates subagents at scale: fan-out in parallel, pipeline stages, dozens to hundreds of agents. | `.claude/workflows/*` (once saved) | A job is too big for one conversation to coordinate by hand: a codebase-wide audit, a 500-file migration, cross-checked research. |

The one-line distinction to remember: **a skill runs in your current head; a subagent runs in a fresh head and mails you back a summary.**

---

## Part 16: Cheat Sheet

**The one sentence:** A subagent is a second Claude you send off to do the messy work in its own window so your main chat stays clean.

**The minimum file:**
```markdown
---
name: my-agent
description: What it does and exactly when to use it. Add "use proactively" to auto-fire.
tools: Read, Grep, Glob
model: haiku
---
You are a [role]. When invoked: [steps]. Return: [format]. Do not: [constraints].
```

**Where it goes:** `.claude/agents/` (team, shared via git) or `~/.claude/agents/` (just you).

**Make one fast:** type `/agents`.

**The four rules that matter most:**
1. One agent, one job.
2. The `description` is a trigger rule, not a label.
3. Give it the fewest tools it needs (read-only by default).
4. Cheap model for grunt work, smart model for thinking.

**Save money:** match model to task (Haiku for scanning, Sonnet for building, Opus for hard reasoning), let the agent absorb the noisy context, and never spin one up for a 30-second job.

**Remember the cost trap:** subagents start blank and re-gather context. Worth it for big or noisy work, wasteful for small tasks. Rule of thumb: 10+ files or throwaway output = use one.

**The composition rules:** skills can call agents, agents can call skills, agents cannot call agents. The main chat is always the conductor.

---

## Sources

Official:
- Claude Code subagents docs: https://code.claude.com/docs/en/sub-agents
- Claude Code best practices: https://code.claude.com/docs/en/best-practices
- How we built our multi-agent research system (Anthropic Engineering): https://www.anthropic.com/engineering/multi-agent-research-system
- How and when to use subagents (Anthropic): https://claude.com/blog/subagents-in-claude-code

Community deep-dives:
- Tembo: https://www.tembo.io/blog/claude-code-subagents
- PubNub: https://www.pubnub.com/blog/best-practices-for-claude-code-sub-agents/
- claudefast (orchestration patterns): https://claudefa.st/blog/guide/agents/agent-patterns
- Claudekit (common mistakes): https://claudekit.cc/blog/vc-04-subagents-from-basic-to-deep-dive-i-misunderstood
