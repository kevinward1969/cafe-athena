# Café Athena — Multi-Agent Architecture

**Version:** 1.0  
**Last Updated:** April 2026  
**Status:** Active  

This document describes the full multi-agent ecosystem for the Café Athena cookbook project, including each agent's role, the relationships between them, identified improvement opportunities, and recommended next steps.

---

## 1. How the Agents Are Actually Used

Each AI surface has a distinct role in the day-to-day workflow. They are not interchangeable — each is chosen for what it does best.

| Surface | Used For | Why |
| ------- | -------- | --- |
| **Claude Desktop** | Recipe development (Mode 1 — The Lab), recipe formatting (Mode 2 — The Manual), technique education (Mode 3 — The MasterClass) | Easier conversational interface; can write directly to the filesystem via MCP |
| **Claude Code (sub-agent)** | Development, format audits, QA, web functions, glossary pulls, deploys | Full tool access (Read/Write/Edit/Grep/Glob/Bash); slash-command workflows; best for agentic file operations |
| **Gemini Gem 1** | Alternative surface for recipe development when preferred | Useful for exploratory ideation; generates image briefs for Gem 2 |
| **Gemini Gem 2** | Hero image creation for recipes and web images | Purpose-built for image generation; consumes briefs from Gem 1 or `/recipe-hero-image` |

**The division is intentional.** Claude Desktop handles the creative and culinary work. Claude Code handles the technical and operational work. Gemini handles all image generation. They share the same cookbook manuscript (`The Manual/`) and format standard (`Guidance/Recipe-Format-Standard.md`) as the common source of truth.

---

## 2. Agent Inventory

The system currently has **four distinct AI agent surfaces**, each targeting a different deployment context:

| Agent | File | Platform | Tools | Primary Role |
| ----- | ---- | -------- | ----- | ------------ |
| **Gemini Gem 1 — The Chef** | `Guidance/CAFÉ ATHENA - GEM INSTRUCTIONS.md` | Google Gemini Gems | Chat only | All three modes (Lab / Manual / MasterClass) |
| **Gemini Gem 2 — The Visual Director** | `Guidance/CAFÉ ATHENA - HERO IMAGE GEM INSTRUCTIONS.md` | Google Gemini Gems (Imagen) | Image generation | Hero image creation for recipes |
| **Claude Desktop Agent** | `Claude-Desktop/PROJECT_INSTRUCTIONS.md` | Claude Desktop / Claude.ai Projects | Chat + optional filesystem MCP | All three modes, portability-first |
| **Claude Code Sub-Agent — Café Athena Chef** | `.claude/agents/Cafe Athena Chef.agent.md` | Claude Code (Antigravity) | Read, Write, Edit, Grep, Glob, Bash | All three modes + agentic file operations |

Plus **seven slash-command workflows** (`.agents/workflows/`) that the Claude Code sub-agent executes:

| Workflow | Command | Purpose |
| -------- | ------- | ------- |
| `new-recipe.md` | `/new-recipe [id]` | Full onboarding pipeline: format audit → keyword pull → glossary pull → deploy |
| `format-audit.md` | `/format-audit [id\|chapter]` | Validate recipe/folio structure against the format standard |
| `glossary-pull.md` | `/glossary-pull [id]` | Merge recipe glossary terms into the main glossary |
| `keyword-pull.md` | `/keyword-pull [id]` | Generate and append Keywords + Category sections |
| `audit-glossary.md` | `/audit-glossary` | Fix formatting, alphabetization, and duplicates in main glossary |
| `recipe-hero-image.md` | `/recipe-hero-image [id]` | Create Gemini image prompt, optimize PNGs, insert reference shortcodes |
| `session-handoff.md` | `/session-handoff` | Update `PROJECT_STATUS.md`, commit, push, and output handoff summary |

---

## 3. Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CAFÉ ATHENA AI ECOSYSTEM                             │
└─────────────────────────────────────────────────────────────────────────────┘

  ┌──────────────────────────┐       ┌──────────────────────────────────────┐
  │   GEMINI GEM 1           │       │   GEMINI GEM 2                       │
  │   The Chef               │       │   The Visual Director                │
  │   (All 3 Modes)          │       │   (Image generation only)            │
  │   v3.3                   │       │   v1.0                               │
  └──────────┬───────────────┘       └──────────────────────┬───────────────┘
             │ Generates recipe brief                        │ Consumes brief
             │ + image prompt                                │ → outputs hero image
             └───────────────────────────────────────────────┘

  ┌──────────────────────────────────────────────────────────────────────────┐
  │   CLAUDE DESKTOP AGENT (Claude.ai Projects / Desktop)                    │
  │   PROJECT_INSTRUCTIONS.md v1.1                                           │
  │   All 3 modes | GitHub connector (read) | MCP filesystem (read+write)    │
  └──────────────────────────────────────────────────────────────────────────┘

  ┌──────────────────────────────────────────────────────────────────────────┐
  │   CLAUDE CODE SUB-AGENT (Antigravity CLI)                                │
  │   .claude/agents/Cafe Athena Chef.agent.md                               │
  │   All 3 modes + Read/Write/Edit/Grep/Glob/Bash tools                     │
  │                                                                           │
  │   Executes workflows from .agents/workflows/:                            │
  │     /new-recipe  /format-audit  /glossary-pull  /keyword-pull            │
  │     /audit-glossary  /recipe-hero-image  /session-handoff                │
  └──────────────────────────────────────────────────────────────────────────┘

  ┌──────────────────────────────────────────────────────────────────────────┐
  │   SHARED KNOWLEDGE BASE (project filesystem)                             │
  │   Guidance/Recipe-Format-Standard.md   ← formatting truth               │
  │   Guidance/Cafe-Athena-Workflow-Guide.md                                 │
  │   The Manual/ (chapters + live index)  ← XX-YY assignment truth         │
  │   PROJECT_STATUS.md                    ← session state bridge            │
  └──────────────────────────────────────────────────────────────────────────┘
```

---

## 4. Agent Relationships & Data Flow

```
Concept / Idea
     │
     ▼
[Gemini Gem 1 — Mode 1]   ←→   [Claude Desktop / Claude Code — Mode 1]
  Iterative development           (Alternative surface for same work)
     │
     │ User says "Finalize"
     ▼
[Gemini Gem 1 — Mode 2]   ←→   [Claude Code — Mode 2 via /new-recipe]
  Manuscript formatting           Automated: format audit + keywords + glossary
  + XX-YY index assignment         + deploy + commit
     │
     │ File written to The Manual/
     ▼
[Claude Code — /recipe-hero-image]  →  brief →  [Gemini Gem 2]
  Build image prompt                              Generate hero image
     │                                            (save as PNG in chapter folder)
     │ /recipe-hero-image optimize
     ▼
  PNG → WebP conversion
     │
     │ deploy.sh
     ▼
  Site: cookbook.kevinward.com
```

---

## 5. Evaluated Strengths

The current architecture is well-designed in several important ways:

- **Source-of-truth discipline**: Live filesystem scanning (not cached index documents) for XX-YY number assignment prevents duplicates.
- **Stop-point protocol**: Critical decisions (food safety, index conflicts, missing data) are always gated by human confirmation before the agent proceeds.
- **Zero-citation protocol**: Manuscript-ready output by design — no AI citations bleed into the cookbook.
- **Format standard portability**: `Recipe-Format-Standard.md` is the single source of truth consumed by all four agents, so format changes propagate automatically.
- **Separation of concerns**: The Visual Director Gem is purpose-limited — it has no recipe-development or indexing responsibilities, reducing risk of scope confusion.
- **Mode-specific reasoning**: Each mode has an explicit reasoning posture (exploratory / precise / pedagogical), reducing persona drift.

---

## 6. Identified Improvement Opportunities

### 5.1 Agent Redundancy & Divergence Risk

**Issue:** The same three-mode system prompt is maintained in three separate files:
- `Guidance/CAFÉ ATHENA - GEM INSTRUCTIONS.md` (v3.3)
- `Claude-Desktop/PROJECT_INSTRUCTIONS.md` (v1.1)
- `.claude/agents/Cafe Athena Chef.agent.md` (v1.1)

Each surface has diverged slightly. Changes to one do not automatically propagate to the others. Over time, the agents will give inconsistent advice.

**Recommendation:** Designate `.claude/agents/Cafe Athena Chef.agent.md` as the **canonical master** (it is the most recent and most capable version). When updating the system prompt, update the master first and port changes to the other two. Note the version number in a shared changelog.

**Status:** Complete — `version: "1.1"` added to sub-agent YAML frontmatter. `AGENT_CHANGELOG.md` created with retroactive entries for all four agents. Canonical master declared via cross-reference notes at the top of each agent file.

---

### 5.2 Missing Agent: The Image Pipeline Coordinator

**Issue:** The handoff from Gemini Gem 1 (which generates the image brief) to Gemini Gem 2 (which generates the image) is entirely manual. The user must copy/paste between two separate chat surfaces.

**Recommendation:** Add a dedicated Claude Code workflow `/generate-image-brief [id]` that generates the full Gemini image prompt in one command. The user can then paste it directly into Gemini Gem 2 without opening the recipe file themselves.

**Status:** Already implemented. `/recipe-hero-image` Create mode serves exactly this purpose and is documented as the Gem 1→Gem 2 bridge in the sub-agent's BUILT-IN WORKFLOWS section and in README.md. No additional workflow needed unless a standalone brief-only command is desired.

---

### 5.3 No Agent for Bulk Operations

**Issue:** Workflows operate on one recipe at a time. `PROJECT_STATUS.md` lists 85+ recipes with no hero images and all 11 chapters needing format audits. There is no mechanism to run these operations in batch.

**Recommendation:** Add a `/batch-audit [Chapter N]` workflow variant to `format-audit.md` that runs format checks across an entire chapter and produces a consolidated report (rather than stopping after each file). This already exists in the workflow invocation syntax (`/format-audit Chapter 4`) but the current workflow description implies file-by-file authorization stops — clarify whether authorization is per-recipe or per-batch-result.

---

### 5.4 No Shared Agent Changelog

**Issue:** There is no CHANGELOG for agent instruction versions. The CD-Audit.md document tracks changes to the Claude Desktop instructions, but there is no equivalent for the Gem Instructions (v3.0 → v3.1 → v3.2 → v3.3) and no record for the Claude Code sub-agent.

**Recommendation:** Create `AGENT_CHANGELOG.md` with entries for all four agents, listing what changed at each version. This enables debugging ("the agent stopped doing X — when did the instructions change?") and makes handoff to future contributors easier.

---

### 5.5 Gemini Gem 2 Aesthetic Drift

**Issue:** The Hero Image Gem (v1.0) references "Nano Banana" as the Gemini interface name (Phase 3, step 1 of Create Mode in `recipe-hero-image.md`). This is an informal name for a Gemini interface that may change. Additionally, the Hero Image Gem has no version history and no link to any Gemini-specific configuration.

**Recommendation:** Replace the "Nano Banana" reference with a generic instruction ("Open Gemini image generation"). Consider adding versioning to the Hero Image Gem instructions and linking to a reference image folder to show the agent what the established visual style looks like in practice.

**Status:** Complete — `recipe-hero-image.md` Phase 3 already reads "Open Gemini (image generation)" with no platform-specific UI references. No further action needed.

---

### 5.6 No Error Recovery Playbook

**Issue:** The stop-point protocol specifies what errors to raise ("CRITICAL ERROR: Live Directory Scan Failed") but provides no guidance on how to recover from them. Users hitting these errors for the first time have no path forward.

**Recommendation:** Add a "Troubleshooting" appendix to the Claude Code sub-agent or a `TROUBLESHOOTING.md` file listing the common errors, their causes, and recovery steps. (The Claude Desktop README has a partial version of this — extend it to cover Claude Code scenarios.)

---

### 5.7 Settings Portability

**Issue:** The `.claude/settings.local.json` file contained hardcoded macOS absolute paths (`/Users/kevinward/...`). These have been corrected in this update but were a latent bug for any collaborator or CI environment.

**Status:** Fixed in this update — paths are now project-root-relative.

---

### 5.8 Workflow Tool Names

**Issue:** Several `.agents/workflows/` files used Desktop Commander MCP tool names (`find_by_name`, `view_file`, `replace_file_content`, `multi_replace_file_content`) instead of the Claude Code sub-agent's actual tools (`Glob`, `Read`, `Edit`, `Write`). This would cause workflow execution failures.

**Status:** Fixed in this update — all workflow files now use correct Claude Code tool names.

---

## 7. Multi-Agent Improvement Roadmap

Listed in priority order:

| Status | Item | Notes |
| ------ | ---- | ----- |
| ✅ Done | Add `AGENT_CHANGELOG.md` | Created with retroactive entries for all four agents |
| ✅ Done | Designate canonical master + add version header | Sub-agent is canonical master; cross-references added to all agent files |
| ✅ Done | Update Hero Image Gem — remove "Nano Banana" reference | Already removed in `recipe-hero-image.md`; no further action needed |
| ✅ Done | Fix settings portability (absolute paths) | Fixed in a prior session |
| ✅ Done | Fix workflow tool names (Desktop Commander → Claude Code) | Fixed in a prior session |
| ⏸ Deferred | Create `TROUBLESHOOTING.md` for Claude Code error recovery | Defer until there are recurring errors worth documenting |
| ⏸ Skipped | Enhance `/format-audit` for single-authorization batch output | Current per-recipe authorization is intentional quality control — do not change |
| ⏸ Skipped | Retire Claude Desktop `Claude-Desktop/` folder | Claude Desktop is still in active use for Modes 1–3; folder stays |
| 🔲 Future | Add batch `/generate-all-briefs [chapter]` workflow | Only useful for a bulk image sprint; revisit when needed |

---

## 8. Recommended Next Steps

1. **Run format audit on all chapters** — Use Claude Code with `/format-audit Chapter N` starting with Chapter 1. All 11 chapters are pending. This clears formatting debt before adding new content.

2. **Bulk image optimization** — Run `/recipe-hero-image optimize all` to convert any remaining PNG hero images to WebP before the next deploy.

3. **Keep `AGENT_CHANGELOG.md` current** — When updating any agent file, bump the version number in the file header and add a changelog entry. This is the only ongoing maintenance item from the architecture review.

---

## 9. Agent File Quick Reference

| What you need | Where it lives |
| ------------- | -------------- |
| Master recipe formatting rules | `Guidance/Recipe-Format-Standard.md` |
| Claude Code sub-agent system prompt | `.claude/agents/Cafe Athena Chef.agent.md` |
| Claude Desktop / Claude.ai system prompt | `Claude-Desktop/PROJECT_INSTRUCTIONS.md` |
| Gemini Gem 1 instructions (culinary AI) | `Guidance/CAFÉ ATHENA - GEM INSTRUCTIONS.md` |
| Gemini Gem 2 instructions (image AI) | `Guidance/CAFÉ ATHENA - HERO IMAGE GEM INSTRUCTIONS.md` |
| Slash-command workflow definitions | `.agents/workflows/` |
| Active session state | `PROJECT_STATUS.md` |
| Full cookbook manuscript | `The Manual/` |
| Published cookbook site | `site/` |
