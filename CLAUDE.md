# CLAUDE.md

@/Users/kevinward/.claude/code-rules/coding-style.md
@/Users/kevinward/.claude/code-rules/testing.md
@/Users/kevinward/.claude/code-rules/security.md
@/Users/kevinward/.claude/code-rules/patterns.md
@/Users/kevinward/.claude/code-rules/development-workflow.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Working Style

- Default to action. Explain only when the task is complex or you need clarification.
- Use the minimum tokens necessary to complete the task.

---

## Human-in-the-Loop Protocol

**Current mode: Development.** Autonomous action is the goal, not the current state.

Rules while in development mode:

1. **One action at a time.** Define what you are about to do, do it, stop.
2. **Report and wait.** After each action, summarize the result and wait for explicit approval before the next step.
3. **No pre-loading.** Do not define, queue, or describe multiple upcoming steps. The next step is defined only after the current one is approved.
4. **Tests one at a time.** Run one test. Document the result. Wait for "go ahead" before the next test.
5. **Errors stop the chain.** If anything fails or is uncertain, stop and report — do not work around it or proceed.

This mode is lifted only when Kevin explicitly says so.

---

## Commands

All `npm` commands run from `site/` — there is no root-level `package.json`.

```bash
# Site development
cd site && npm run dev           # local dev server (Astro, hot reload)
cd site && npm run build         # production build + Pagefind search index
cd site && npm run preview       # preview the production build locally

# Content pipeline (run from repo root)
python3 site/scripts/prepare-content.py   # Manual → site/src/content/recipes/ (no build)
bash site/scripts/deploy.sh               # full pipeline: prep + build + rsync to FastComet
```

`npm run build` runs `astro build` followed by `npx pagefind` — both must succeed for site search to work. Do not run `astro build` directly when building for deployment.

**Pushing to GitHub alone does NOT deploy the site** — only the rsync in `deploy.sh` updates the live site. Never report the site as deployed until rsync completes successfully.

See `Docs/TECHNICAL_REFERENCE.md` §3 (Build & Deploy Commands) for the full deploy sequence.

---

## Status Query Protocol

When the user asks for a status update, what's next, where we are, what's pending, or anything semantically equivalent, read these four sources **before answering** — never respond from memory alone:

1. `PROJECT_STATUS.md` — active work, bugs, pending items
2. `The Manual/IDEAS.md` — future/deferred backlog
3. `The Manual/recipes.json` — live per-recipe state (run `python3 scripts/audit.py --status` for the rollup)
4. `CLAUDE.md` — this file, for architectural context

Produce a rollup in this order: **active work first, then open issues, then backlog highlights.** Do not dump the full `The Manual/IDEAS.md` — surface only what's relevant to the current session's direction.

---

## Documentation Lifecycle

Never let active-work detail live in more than one place at a time:

1. **`The Manual/IDEAS.md`** — ideas not yet realized, or not yet completely acted on. Nothing active belongs here.
2. **`PROJECT_STATUS.md`** — work in progress, *or* existing/already-built systems with a functional status worth tracking. Not purely a "pending work" file. While an initiative is active, it gets only a single pointer row here — all working detail (architecture decisions, open questions, build checklist) consolidates into one dedicated tracker file for that initiative (e.g. `Expo/EXPO_TODO.md`). Do not fragment active work across multiple docs.
3. **On completion** — the durable operational knowledge (commands, agents, skills, how the pipeline runs end to end) gets written up as a new workflow in `Guidance/Cafe-Athena-Workflow-Guide.md`, in the same PHASE-style format as the existing workflows. The detailed tracker file is retired; `PROJECT_STATUS.md` keeps whatever ongoing functional-status line still applies rather than dropping the system from view entirely.

---

## Project Architecture

See `Docs/TECHNICAL_REFERENCE.md` for the full technical reference — repository structure, stack, content pipeline, image workflow, scripts, agent system map, and Chef agent modes.

---

## Key Files

| File | Role |
|------|------|
| `PROJECT_STATUS.md` | Session state — active recipes, strategic context, pending tasks. Check this at the start of each session. **Does not duplicate registry state** — hero image + format audit status live in `The Manual/recipes.json`. |
| `The Manual/CONTENT_PLAN.md` | Chapter-by-chapter content gap analysis — minimum recipe counts, category coverage gaps, RecipeIdeas assignments, and development sequence. Reference when planning new recipe development. |
| `The Manual/recipes.json` | Pipeline registry — single source of truth for per-recipe state. Each entry has `stages` (formatAudit, glossaryPull, heroImage, heroImageOptimized, deployed, etc.) and an `audit` block (`lastRun`, `status`, `issues[]`). Updated via `/register-recipe`, `/sync-registry`, and `scripts/audit.py`. Run `python3 scripts/audit.py --status` for a rollup. |
| `The Manual/IDEAS.md` | Future recipe, folio, technique, and editorial ideas — low-priority backlog. Not active work; drop new ideas here. |
| `Guidance/Recipe-Format-Standard.md` | Single source of truth for all recipe formatting rules |
| `Guidance/Taxonomy.md` | Canonical controlled vocabulary — all valid `cuisine:`, `style:`, `family:`, `course:`, and `dietary:` values. Referenced by agents, pipelines, and `audit.py`. Add new terms here first. |
| `Agents/AGENT_CHANGELOG.md` | Version history for all agent surfaces |
| `Agents/MULTI_AGENT_ARCHITECTURE.md` | Full architecture reference and improvement roadmap |
| `.claude/agents/Cafe Athena Chef.agent.md` | **Canonical master** for the culinary agent system prompt |
| `.claude/agents/Cafe Athena Brand Manager.agent.md` | **Canonical master** for the brand and marketing agent system prompt |
| `.claude/agents/Cafe Athena Technical Director.agent.md` | **Canonical master** for the Technical Director agent system prompt |
| `.claude/agents/Cafe Athena Writing Director.agent.md` | **Canonical master** for the Writing Director system prompt — all prose surfaces |
| `Brand/Author/writing-exemplars.md` | Approved paragraphs in the correct brand register — Writing Director reads this before every draft session |
| `Agents/Claude-Desktop/TECHNICAL_DIRECTOR_INSTRUCTIONS.md` | Secondary surface for Claude Desktop Technical Director project |
| `Brand/BRAND_GUIDELINES.md` | Master brand reference — typography, color, voice, visual system |
| `Brand/BRAND_STATUS.md` | Active brand work tracker |
| `Brand/Scorecards/` | Date-stamped brand strategy scorecards — new file per review cycle, never overwrite |
| `Marketing/MARKETING_STATUS.md` | Active marketing work tracker — points to current strategy and calendar |
| `Marketing/Marketing_Strategy/MARKETING_CALENDAR_2026.md` | Weekly content production tracker and posted content log |
| `Marketing/Marketing_Strategy/` | All strategy docs — active and archived. Archived folder is gitignored. |
| `Marketing/Marketing Content/Social/` | Channel setup, post templates, reel production assets |
| `Marketing/Marketing Content/NotebookLM/` | NotebookLM outputs — infographics, audio, PDFs, slide decks |
| `Marketing/Marketing Content/Site-Copy/` | Hero, CTA, footer copy drafts |
| `.claude/commands/` | Slash-command workflow definitions |
| `scripts/audit.py` | Local Ollama-powered audit & repair tool — scans all recipes for structural issues, generates glossary/keyword fixes, applies with user approval |
| `The Manual/Cafe-Athena-The-Manual-Current-Version.md` | **Master manuscript index** — the human-facing table of contents for every folio in the book. Must be updated every time a new recipe or technique folio is added. Updated by `/register-recipe` (automatic) or manually when bypassing that workflow. |
| `The Manual/Glossary/` | Split culinary glossary — one file per letter (`Café Athena  - Glossary [LETTER].md`, A–Z + 0-9) |
| `The Manual/` | Full cookbook manuscript (source files) |
| `site/src/content/recipes/` | Built recipe files consumed by the Astro site — ephemeral, never hand-edit |
| `~/Projects/Hugging Face/hugging_face/Projects/cafe-athena/` | **Writable.** Café Athena's project folder inside the HF workspace — tool registry, brand parameters, asset manifest, gap documentation, and handoff prompts all live here. |
| `~/Projects/Hugging Face/hugging_face/` (all other paths) | **Read-only.** The canonical HF workspace — skills, space docs, audits, roadmap. Never write to or modify anything outside the `Projects/cafe-athena/` subfolder. Reference canonical content by path only. |

---

## ⚠️ Version Bump Rule

**Whenever any agent file is modified, you must:**

1. Bump the version number in the file header (e.g. `Version: 1.1` → `Version: 1.2`)
2. Add an entry to `Agents/AGENT_CHANGELOG.md` describing what changed and why
3. Follow the propagation rule below for any changes that affect secondary surfaces

This applies to: `.claude/agents/Cafe Athena Chef.agent.md`, `.claude/agents/Cafe Athena Brand Manager.agent.md`, `.claude/agents/Cafe Athena Technical Director.agent.md`, `.claude/agents/Cafe Athena Writing Director.agent.md`, `Agents/Claude-Desktop/PROJECT_INSTRUCTIONS.md`, `Agents/Claude-Desktop/BRAND_MANAGER_INSTRUCTIONS.md`, `Agents/Claude-Desktop/TECHNICAL_DIRECTOR_INSTRUCTIONS.md`, `Agents/Gemini-Gems/CAFÉ ATHENA - VISUAL DIRECTOR GEM INSTRUCTIONS.md`, and any `.claude/commands/*.md` file.

---

## ⚠️ Agent Propagation Rule

**When the canonical master is modified, apply changes to secondary surfaces as follows. File edits are done directly — only UI pastes require manual action by Kevin.**

| File Changed | Action Required |
|-------------|----------------------|
| `.claude/agents/Cafe Athena Chef.agent.md` | **Edit directly:** port changes to `Agents/Claude-Desktop/PROJECT_INSTRUCTIONS.md`. **Remind Kevin:** paste updated `PROJECT_INSTRUCTIONS.md` content into Claude Desktop project settings, and port relevant changes to `Agents/Gemini-Gems/CAFÉ ATHENA - CHEF GEM INSTRUCTIONS.md` then paste into Gemini Gem 1 config. |
| `.claude/agents/Cafe Athena Brand Manager.agent.md` | **Edit directly:** port changes to `Agents/Claude-Desktop/BRAND_MANAGER_INSTRUCTIONS.md`. **Remind Kevin:** paste updated `BRAND_MANAGER_INSTRUCTIONS.md` content into Claude Desktop brand project settings. |
| `.claude/agents/Cafe Athena Technical Director.agent.md` | **Edit directly:** port changes to `Agents/Claude-Desktop/TECHNICAL_DIRECTOR_INSTRUCTIONS.md`. **Remind Kevin:** paste updated `TECHNICAL_DIRECTOR_INSTRUCTIONS.md` content into Claude Desktop Technical Director project settings. |
| `Guidance/Recipe-Format-Standard.md` | No action needed — Claude Desktop reads this file live from the filesystem via MCP |
| `.claude/commands/*.md` | No action needed — workflows run in Claude Code only |
| `Agents/Gemini-Gems/CAFÉ ATHENA - VISUAL DIRECTOR GEM INSTRUCTIONS.md` | **Remind Kevin:** paste updated content into the Gemini Gem 2 configuration |
| `Agents/Claude-Desktop/PROJECT_INSTRUCTIONS.md` | **Remind Kevin:** paste updated content into the Claude Desktop Chef project settings |
| `Agents/Claude-Desktop/BRAND_MANAGER_INSTRUCTIONS.md` | **Remind Kevin:** paste updated content into the Claude Desktop Brand Manager project settings |

After propagating changes, bump the version number in the modified file and add an entry to `Agents/AGENT_CHANGELOG.md`.

---

## ⚠️ New Recipe Mandatory Updates

Every time a new recipe or technique folio is added, **all four of these must be updated before committing**:

1. **The folio file** — `The Manual/Chapter N - Name/XX-YY Café Athena - [Recipe Title].md`
2. **`The Manual/recipes.json`** — register the entry with correct stage flags
3. **`The Manual/Cafe-Athena-The-Manual-Current-Version.md`** — append the entry under the correct chapter heading
4. **`PROJECT_STATUS.md`** — update the Last Updated date

`/register-recipe` handles items 2 and 3 automatically. Items 1 and 4 are always manual.

---

## Slash Commands

Run these in Claude Code. Full definitions in `.claude/commands/`.

| Command | Purpose |
|---------|---------|
| `/project-health [scope?]` | Full project health audit — registry, flags, images, deploy currency, docs, agents. Optional scope: `registry`, `images`, `deploy`, `docs`, `agents` |
| `/format-audit [id\|Chapter N]` | Audit recipe(s) against format standard |
| `/glossary-pull [id]` | Merge recipe glossary terms into main glossary |
| `/keyword-pull [id]` | Add missing Keywords + Category sections |
| `/audit-glossary` | Fix alphabetization + duplicates in main glossary |
| `/new-recipe` | Scaffold a new recipe through the full pipeline |
| `/recipe-update [id]` | Edit an already-deployed recipe — bumps version, sets needsRedeploy, re-evaluates affected pipeline stages. Use for any post-deploy content change |
| `/register-recipe [id]` | Register a new entry in `The Manual/recipes.json` **and** update the Current Version index after Claude Desktop Mode 2 |
| `/sync-registry` | Sync `The Manual/recipes.json` against live Manual directory — adds missing entries, corrects filesystem-derivable stages |
| `/session-handoff` | Update PROJECT_STATUS.md, commit, push, output summary |

---

## Git Workflow

- **Commit directly to main.** No feature branches, no PRs. All changes — format audits, content updates, site changes — go directly to main with a single commit and push.
- **Always one commit.** Bundle everything in the working tree into a single commit. Never split, never propose options, never ask. Exception: if the user says "commit only X," stage exactly those files.

---

## Operational Heuristics

Session-relevant learnings that shape how work should be done in this project.

- **Google Analytics (2026-06-22)**: GA4 property live on cafeathenathemanual.com. Measurement ID: `G-F8Y9NNYBNM`. Tag is in `BaseLayout.astro` `<head>`. Measurement ID is public (visible in page source) — safe to document here.
- **Project email (2026-06-28)**: Master email for all Café Athena platform accounts is `kevin@cafeathenathemanual.com`. Password in 1Password. Mail server settings: Incoming — `mail.cafeathenathemanual.com`, IMAP 993 / POP3 995. Outgoing — `mail.cafeathenathemanual.com`, SMTP 465. CalDAV: `https://mail.cafeathenathemanual.com:2080/calendars/kevin@cafeathenathemanual.com/calendar`. CardDAV: `https://mail.cafeathenathemanual.com:2080/addressbooks/kevin@cafeathenathemanual.com/addressbook`. All require authentication.
- **Filesystem Authority**: Always scan live directories for folio numbers — never infer from stale docs.
- **Scaling Nuance**: Ingredients scale linearly; reduction times do NOT (surface area constraints).
- **Formula Trust**: Use established adaptive hydration rates for pasta.
- **Tool Awareness**: Antigravity is used for local project orchestration. If unsure of its capabilities, ask.
- **Frico Method (2026-04-21)**: Baked frico is structurally superior to stovetop-pan frico — even browning, longer plastic-shaping window (~30–45 sec on counter vs. 5–10 sec off the pan), hands-free batching. Silpat beats parchment for structural/molded fricos (clean release protects lace; mat retains counter heat long enough to shape). Parchment only wins on pure flat tiles where bottom crispness matters more than shape-hold.
- **Built recipe files**: `site/src/content/recipes/` is ephemeral — fully regenerated by `prepare-content.py`. If those files show as bulk-modified in git, it means the script ran and overwrote them — that is a regression, not an improvement. Investigate the diff before staging; discard if lines are only being removed.
- **Adobe Express Project Folder (2026-06-28)**: Primary workspace for social template assembly, brand asset production, and video editing. URL: <https://express.adobe.com/your-stuff/projects/urn:aaid:sc:US:4a65052f-ef4a-4453-a231-0980da154d1c>
- **Generative tool routing**: Lane 1 (cookbook photography) = Gemini Gem 2 only — hero images and reference images for `site/public/images/`. Never route cookbook photography to any other tool. For all other creative and media needs — promotional stills, social graphics, video, audio — evaluate whether HF has a solution that improves the outcome. HF's distinct capabilities: atmospheric/editorial food stills (FLUX.1), text-in-image graphics (Ideogram 4), video clip generation and panel-to-panel consistency (Wan2.2), voiceovers (TTS tools), music beds (MusicGen/Stable Audio). These work alongside Adobe Firefly, Adobe Express, and Gemini image generation — the right tool is whichever produces the best result for the specific need. **Video generation:** Adobe Firefly (Kling 3.0 Omni) — 15 sec, 720p, 9:16, reference image support, Brand Manager owns. Assembly in Adobe Express. HF video tools (Wan2.1, Wan2.2) are backup only. **HF image/TTS tools cleared:** OmniGen2 (audited), ZONOS2/Qwen3-TTS (evaluated). FLUX.1 and Ideogram 4 audits still pending.

---

## Project Skills — Auto-Trigger Rules

Skills from `.claude/skills/` and installed plugins are invoked automatically when their trigger conditions are met — do not wait to be asked.

### Project Health

| Skill | Invoke when… |
|-------|-------------|
| `project-health` | Something feels off with the project — search not returning results, deploy flags inconsistent, images missing, docs stale, agents drifting. Also invoke at the start of any session that begins with "what's broken" or "let's audit". Supports scope flags: `registry`, `images`, `deploy`, `docs`, `agents` |

### Site & Content Skills

| Skill | Invoke when… |
|-------|-------------|
| `astro` | Working on any file in `site/` — `.astro` pages, `content.config.ts`, `prepare-content.py`, build errors, content collection schema changes, or routing questions |
| `avoid-ai-writing` | Reviewing or editing any prose in `The Manual/` — headnotes, technique descriptions, glossary entries, or any free-text web copy — before it is committed |
| `seo-aeo-schema-generator` | Adding a new recipe to the site, or when asked about schema, structured data, JSON-LD, or rich results |
| `fixing-metadata` | Editing `[...slug].astro`, layout files, `<head>` content, OG tags, or any site-wide metadata |
| `seo-images` | Processing or placing hero images, running the deploy pipeline, or auditing `site/public/images/` for missing/oversized files |
| `notebooklm-folio-explainer` | User mentions NotebookLM, a folio number (e.g. "01-02"), "video explainer", "infographic prompt", "slide deck prompt", or asks to prepare a folio for any NotebookLM Studio tool |

### Writing Director

Invoke the Writing Director sub-agent (not a skill — it is an agent) when the task involves prose that will be published on any surface.

| Trigger | Action |
|---------|--------|
| Author bio (any length or platform) | Invoke Writing Director |
| About page copy | Invoke Writing Director |
| Social captions or headlines | Invoke Writing Director |
| Promotional copy, advertising, email | Invoke Writing Director |
| Site hero copy or CTAs | Invoke Writing Director |
| Any Brand Manager task that produces prose output | Brand Manager invokes Writing Director as sub-agent |

Writing Director has no secondary surfaces — Claude Code only. Do not route these tasks to Brand Manager and expect prose output; Brand Manager redirects to Writing Director.

### PM Skills (pm-skills plugin)

These skills map to Phase 7 (Marketing Activation) and ongoing brand/GTM work. Suggest the relevant skill when the context matches — do not wait for Kevin to ask.

| Skill | Invoke when… |
|-------|-------------|
| `pm-go-to-market:plan-launch` | Planning any channel launch, social setup, or audience-building initiative |
| `pm-marketing-growth:value-prop-statements` | Writing or reviewing site hero copy, subheadlines, CTAs, or acquisition-register copy |
| `pm-marketing-growth:positioning-ideas` | Asked about how to differentiate Café Athena from other food/cookbook sites |
| `pm-marketing-growth:north-star-metric` | Defining what success looks like for the site, social, or audience growth |
| `pm-go-to-market:gtm-motions` | Deciding which social channels to prioritize or how to structure the channel mix |
| `pm-go-to-market:beachhead-segment` | Identifying which audience persona to lead with on which platform |
| `pm-market-research:competitive-analysis` | Asked about competing cookbooks, food content creators, or the culinary content landscape |
| `pm-execution:pre-mortem` | Before any major launch, deploy decision, or irreversible brand commitment |
