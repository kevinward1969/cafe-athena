# Café Athena — Infrastructure & Document Reorganization Plan

**Status:** Planning complete — ready for phased execution
**Last Updated:** 2026-06-24
**Owner:** Kevin Ward
**Approval surface:** Claude Code (this session or successor)

---

## Problem Statement

Project documentation is fragmented and duplicated. Agents have project knowledge baked into their system prompts rather than reading reference documents at runtime. The README is a developer reference, not a project scope document. The SKILLS_INDEX is orphaned — it exists but no agent reads it. CLAUDE.md has grown into a knowledge dump rather than a behavioral contract.

The goal of this reorganization is:

1. **One document per purpose** — no duplication, clear ownership per file
2. **README = public scope** — what the project is, not how to run it
3. **RAG setup** — agents READ reference documents for facts; system prompts contain only behavioral rules
4. **CLAUDE.md = behavioral contract** — slim, pointing outward to reference docs

---

## New Document Structure (Target State)

| Document | Purpose | Audience |
|----------|---------|---------|
| `README.md` | What Café Athena IS — scope, content arc, audience, site, why | Public / GitHub visitors |
| `Docs/TECHNICAL_REFERENCE.md` | How it works — build, deploy, scripts, agent system, skills map | Developers + agents |
| `CLAUDE.md` | Behavioral contract — Claude Code rules + pointers to reference docs | Claude Code only |
| `Brand/BRAND_GUIDELINES.md` | Brand rules — agents READ this at runtime | Brand Manager agent |
| `Brand/BRAND_SCOPE.md` | Project scope in detail — feeds README and agent context | Brand Manager + all agents |
| `Guidance/Recipe-Format-Standard.md` | Recipe formatting rules — agents READ this (Chef already does) | Chef agent |
| `Guidance/Taxonomy.md` | Controlled vocabulary — agents READ this | Chef + pipeline |

**Retired:** `.claude/SKILLS_INDEX.md` — content absorbed into `Docs/TECHNICAL_REFERENCE.md`

---

## Phase 1 — Rewrite README.md

**Status: Not started**
**Execution surface:** Brand Manager (Claude Desktop)
**Kevin approves:** Final README content before committing

### Scope

Rewrite `README.md` as a non-technical, public-facing scope document. No build commands, no slash commands, no scripts, no developer tooling.

### Deliverables

- What Café Athena is (one clear paragraph)
- The problem it solves and who it's for
- The four-part manuscript arc (Academy, Brigade, Larder, Expo) — high level
- The site: `cafeathenathemanual.com`
- The origin story (named for Athena, started as a personal project)
- A brief note that technical documentation is in `Docs/TECHNICAL_REFERENCE.md`

### What It Should NOT Contain

- Build commands or npm scripts
- Slash command reference
- Script documentation
- Image workflow details
- Mode 1/2/3 internal methodology
- Repository file tree (too technical / goes stale)

### Briefing for Execution Session

> Read the current `README.md` to understand what exists. Read `Brand/BRAND_GUIDELINES.md` §1 (positioning, mission, core values) and `Brand/Author/bio-short.md` for author voice. Read `CLAUDE.md`'s manuscript architecture section for the four-part arc. Rewrite `README.md` as a non-technical public scope document using the acquisition register voice from `Brand/BRAND_GUIDELINES.md` §6. The document should answer "what is this?" for a curious GitHub visitor who knows nothing about the project. Write to file but do NOT commit — Kevin approves first.

---

## Phase 2 — Create Docs/TECHNICAL_REFERENCE.md

**Status: Not started**
**Execution surface:** Technical Director (Claude Code session)
**Kevin approves:** File content before committing
**Dependency:** Can run in parallel with Phase 1

### Scope

Create a new file `Docs/TECHNICAL_REFERENCE.md` that consolidates all technical operational content currently scattered across `README.md` and `.claude/SKILLS_INDEX.md`. This becomes the single technical source of truth for humans and agents.

### Deliverables

- Repository structure (file tree with descriptions)
- Stack overview (Astro, Tailwind, Pagefind, FastComet)
- Build and deploy commands
- Content pipeline (`prepare-content.py`) — what it does, how to run it
- Script documentation (`audit.py`, markdownlint pipeline, etc.)
- Slash command index (all `/commands` with one-line descriptions)
- Agent system map — which agents exist, what they own, which surfaces they run on
- Skills map (absorbed from `SKILLS_INDEX.md`) — which skills each agent uses and when
- Image workflow (hero images, reference images, naming conventions)
- Mode 1/2/3 Chef methodology reference

### Briefing for Execution Session

> Read the current `README.md` in full — extract all technical content. Read `.claude/SKILLS_INDEX.md` in full — extract the skills-to-agent mapping. Read `CLAUDE.md`'s site and build notes sections. Read `Agents/MULTI_AGENT_ARCHITECTURE.md`. Synthesize all of this into a single `Docs/TECHNICAL_REFERENCE.md`. Create the `Docs/` directory if it doesn't exist. Write to file but do NOT commit — Kevin approves first.

---

## Phase 3 — Slim CLAUDE.md

**Status: Not started**
**Execution surface:** Technical Director (Claude Code session)
**Kevin approves:** Diff before committing
**Dependency:** Phase 2 must be complete (content must have a home before it's removed from CLAUDE.md)

### Scope

Strip `CLAUDE.md` of content now living in `Docs/TECHNICAL_REFERENCE.md`. What remains should be the behavioral contract for Claude Code — rules and protocols, not project facts.

### What Stays in CLAUDE.md

- Working style rules
- Human-in-the-loop protocol
- Status query protocol (which files to read, in what order)
- Documentation lifecycle rules
- Git workflow
- Slash command index (one-liner per command — details live in `.claude/commands/`)
- Skill auto-trigger rules
- Operational heuristics (learnings that shape behavior — not reference content)
- Site build notes that are behavior-critical (e.g., "never run astro build directly")
- Key files table (pointers to where things live)

### What Moves to TECHNICAL_REFERENCE.md

- Full site architecture description
- Content pipeline transform details
- Image placement workflow details
- Python script documentation
- Hero image prompt format
- Deploy workflow detail

### Briefing for Execution Session

> `Docs/TECHNICAL_REFERENCE.md` now exists and contains the technical reference content. Read `CLAUDE.md` in full. Remove any section whose content is now covered by `TECHNICAL_REFERENCE.md`. Do not remove behavioral rules, protocols, or auto-trigger rules — those stay. Where content is removed, replace with a one-line pointer: "See `Docs/TECHNICAL_REFERENCE.md`." Produce a diff for Kevin to review before committing.

---

## Phase 4 — Agent RAG Audit

**Status: Not started**
**Execution surface:** Technical Director (Claude Code session)
**Kevin approves:** Each agent file change before committing
**Dependency:** Phases 2 and 3 complete

### Scope

Audit each agent instruction file. Any content that is a project fact (not a behavioral rule) should be removed from the agent prompt and replaced with an explicit instruction to READ the relevant reference document. The Chef agent already does this correctly with `Recipe-Format-Standard.md` — replicate that pattern.

### Agents to Audit

**Café Athena Chef** (`.claude/agents/Cafe Athena Chef.agent.md`)

- Mode detection logic → stays (behavioral)
- Recipe format rules → should READ `Guidance/Recipe-Format-Standard.md` (already does)
- Taxonomy → should READ `Guidance/Taxonomy.md`
- Check: is there project knowledge baked in that should be a reference read?

**Café Athena Brand Manager** (`.claude/agents/Cafe Athena Brand Manager.agent.md`)

- Persona behavior → stays (behavioral)
- Brand rules, voice, tone → should READ `Brand/BRAND_GUIDELINES.md`
- Project scope → should READ `Brand/BRAND_SCOPE.md` (once written in Phase 5)
- Skills → should READ agent's section in `Docs/TECHNICAL_REFERENCE.md`

**Café Athena Technical Director** (`.claude/agents/Cafe Athena Technical Director.agent.md`)

- Behavior rules → stays
- Technical reference → should READ `Docs/TECHNICAL_REFERENCE.md`
- Site architecture → should READ `Docs/TECHNICAL_REFERENCE.md`

### Pattern to Apply

```
# BEFORE (baked-in)
The recipe format requires: Headnote, Mise en Place, Ingredients...

# AFTER (reference read)
At session start, read `Guidance/Recipe-Format-Standard.md` — this is the 
authoritative recipe format. Do not rely on any internally memorized version.
```

### Note on Secondary Surfaces

Any changes to canonical agent files must be propagated to secondary surfaces (Claude Desktop, Gemini Gem) per the agent propagation rule in `CLAUDE.md`. Kevin handles the UI paste steps.

### Briefing for Execution Session

> Read each agent file in `.claude/agents/`. For each one, identify content that is a project fact (format rules, taxonomy terms, skills lists, architecture descriptions) vs. behavioral instruction (how to interact, what mode to use, when to ask for confirmation). Replace fact content with explicit READ instructions pointing to the correct reference document. Follow the pattern established in the Chef agent for `Recipe-Format-Standard.md`. Produce a diff for each file. Do NOT commit — Kevin approves each agent file separately.

---

## Phase 5 — Write Brand/BRAND_SCOPE.md

**Status: Not started**
**Execution surface:** Brand Manager (Claude Desktop)
**Kevin approves:** Content before committing
**Dependency:** None — can run in parallel with Phases 1–4
**Note:** This is Phase 1 of `Brand/BRAND_DEVELOPMENT_PLAN.md`

### Scope

Write `Brand/BRAND_SCOPE.md` — the concrete definition of what Café Athena is and is not. This document feeds the README (Phase 1), the brand guidelines (referenced in §1), and the agent RAG setup (agents read this for project scope).

### Deliverables

- Scope statement — what the project covers (chapters, content types, technique range)
- Out-of-scope statement — what it explicitly does not cover
- Format and delivery — digital-first, how it is used, what it is not
- Problem/solution — the specific problem it solves for the reader
- Content boundaries — what makes something qualify for The Manual

### Briefing for Execution Session

> Read `Brand/BRAND_GUIDELINES.md` §1 in full (mission, positioning, core values). Read `CLAUDE.md`'s manuscript architecture section. Read `The Manual/CONTENT_PLAN.md` to understand what chapters exist and what they cover. Write `Brand/BRAND_SCOPE.md` as a concrete scope definition document. Use the acquisition register voice from §6. This is not marketing copy — it's a precise definition of what the project is and isn't. Write to file but do NOT commit — Kevin approves first.

---

## Execution Order

```
Phase 5 (Brand Scope)  ──────────────────────────────────┐
Phase 1 (README rewrite) ────────────────────────────────┤
Phase 2 (TECHNICAL_REFERENCE) ───────────────────────────┤── Kevin approves all
                                                          │   before committing
Phase 3 (Slim CLAUDE.md)  ← requires Phase 2 complete ──┤
Phase 4 (Agent RAG audit) ← requires Phases 2+3 ─────────┘
```

Phases 1, 2, and 5 can run in parallel. Phase 3 requires Phase 2. Phase 4 requires Phases 2 and 3.

---

## Approval Protocol

Each phase produces output (a new or modified file) that Kevin reviews in Claude Code before any commit happens. Nothing in this plan is committed until Kevin says so. The briefing for each execution session explicitly ends with "do NOT commit."

---

## Tracking

| Phase | Status | Session | Kevin Approved |
|-------|--------|---------|---------------|
| 1 — README rewrite | Complete ✅ | 2026-06-24 | ✅ |
| 2 — TECHNICAL_REFERENCE.md | Complete ✅ | 2026-06-24 | ✅ |
| 3 — Slim CLAUDE.md | Complete ✅ | 2026-06-24 | ✅ |
| 4 — Agent RAG audit | Complete ✅ | 2026-06-24 | ✅ |
| 5 — Brand/BRAND_SCOPE.md | Not started | — | — |
