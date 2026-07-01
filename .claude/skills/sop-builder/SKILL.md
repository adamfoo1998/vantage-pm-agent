---
name: sop-builder
description: Use when turning raw, messy knowledge into a structured Standard Operating Procedure (SOP) — especially from Caleb knowledge-drain sessions, recordings, handover notes, or scattered documentation. Also triggers when the user says "document how X works", "write a process for", "turn these notes into a guide", "what's the process for", or "create a step-by-step for". Priority use case: capturing institutional knowledge before it leaves the company.
---

# SOP Builder

Context: Vantage has critical undocumented institutional knowledge — pricing engine mechanics,
MT5 group/suffix setup, unlimited leverage configuration, plugin dependencies, tools and their
purpose, account types, and who the internal experts are. This skill turns raw captured input
(voice notes, bullet points, handover sessions, meeting notes) into usable SOPs before that
knowledge is lost.

## Two input modes

**Mode A — Raw capture (most common right now)**
You have messy, unstructured input: voice note transcript, bullet-point dump from a session with
Caleb, a screenshot of a config screen, scattered chat messages. The agent structures it.

**Mode B — Known process**
You know the process and want to document it cleanly. Walk the agent through it step by step;
it writes the SOP as you go.

---

## SOP output structure

### Header block (always include)
```
SOP Title:
Process Owner: [name + role]
Subject-matter expert / source: [who provided this knowledge]
Date captured: [date]
Last updated: [date]
Status: DRAFT / REVIEW / APPROVED
Confidence: HIGH (observed/confirmed) / MEDIUM (inferred from notes) / LOW (single source, unverified)
```

### Body sections

1. **Purpose** — one sentence: what this SOP enables and why it matters.

2. **Scope** — what this covers and explicitly what it does NOT cover (prevents scope creep
   and misuse of the SOP).

3. **Who this is for** — role(s) that need to execute this process.

4. **Prerequisites** — access, tools, system states, or prior steps required before starting.
   Include tool names, admin rights needed, MT5 server details where relevant.

5. **Step-by-step procedure** — numbered, atomic steps. Each step:
   - States exactly what to do (not just what outcome to achieve)
   - Names the system/tool/screen where the action happens
   - Flags decision points with: `IF [condition] → THEN [action] / ELSE [action]`
   - Marks any step with compliance/regulatory impact with ⚠️ `VERIFY`

6. **Expected output / success criteria** — what "done correctly" looks like. Testable.

7. **Common errors & how to fix them** — known failure modes and their resolution.
   If Caleb mentioned something that "usually breaks", it goes here.

8. **Escalation path** — if the process fails or hits an edge case: who to call, in what order.
   Use the stakeholder map: Amin (Risk), Andy Chang (Admin/MT5), Vincent Zhang (BIT),
   Vladimir (Plugin — note: back-end only). If no escalation path is known, write `TBC —
   identify expert` as an open item.

9. **Related SOPs / documents** — links or references to upstream/downstream processes.

10. **Open questions** — anything that could not be confirmed from the input, with a named
    owner to resolve it.

---

## Knowledge-drain extraction guide

When working from a Caleb session or similar raw input, structure the extraction using these
prompts before writing the SOP:

| Question | Why it matters |
|---|---|
| What does this process do / what problem does it solve? | Defines Purpose |
| Walk me through it step by step from the beginning | Body steps |
| What do you need before you start? | Prerequisites |
| What does it look like when it's done correctly? | Success criteria |
| What breaks most often and how do you fix it? | Common errors |
| What's the most critical thing NOT to get wrong? | Risk flags / ⚠️ steps |
| Who else understands this if you're not available? | Escalation path |
| Where does any existing documentation live, even partial? | Related docs |

---

## Confidence and gap handling

If the input is thin or from a single source (common in urgent handovers):
- Mark the SOP status as `DRAFT — single source`
- Tag uncertain steps with `[UNCONFIRMED — verify with [name]]`
- List all gaps in Open Questions with a suggested verifier
- Do NOT fill gaps with plausible-sounding invented steps

A partial SOP that is honest about its gaps is far safer than a complete-looking SOP that
contains unverified steps in a financial services context.

---

## Priority SOP topics to build first (Vantage-specific backlog)
These are the highest knowledge-cliff risk items. Work through them with Caleb before departure:
1. Pricing Engine — how it works, parameters, who configures it, what breaks
2. MT5 group/suffix structure — what suffixes exist, what each means, how groups are configured
3. Unlimited Leverage setup — step-by-step config for APAC and FCA variants
4. Plugin dependency map — what Vladimir's plugin does, how it's deployed, failure modes
5. New joiner setup — tools, access, systems, who to contact for each
6. Account type reference — all account types in MT4/MT5, their rules, and their MT5 group names

## Known failure modes (do not repeat)
- Writing a complete-looking SOP that contains invented steps in the middle.
- Using vague action language ("configure the settings") instead of specific steps
  ("in MT5 Manager, navigate to Groups > [group name] > Parameters > Leverage, set to...").
- Omitting the escalation path — in a company losing its expert, this is critical.
