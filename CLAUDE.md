# Café Athena — Claude Code Instructions

## What This Project Is

A culinary cookbook project with a published Astro site at `cookbook.kevinward.com`. The cookbook manuscript lives in `The Manual/`. The site is in `site/`. Recipes and technique folios are written in Markdown and processed through a build pipeline before deployment.

---

## How the AI Surfaces Are Divided

| Surface | Responsibilities |
|---------|-----------------|
| **Claude Desktop** | Recipe development (Mode 1), formatting (Mode 2), technique education (Mode 3) — all culinary creative work |
| **Claude Code** (you) | Format audits, glossary operations, web/site development, QA, deploys, image optimization |
| **Gemini Gem 1** | Alternative surface for recipe development; generates hero image briefs |
| **Gemini Gem 2** | Hero image and web image generation only |

---

## Key Files

| File | Role |
|------|------|
| `PROJECT_STATUS.md` | Session state — active recipes, pending tasks. Check this at the start of each session. |
| `recipes.json` | Pipeline registry — tracks stage completion (glossary, hero image, format audit, etc.) for every entry. Updated via `/register-recipe` and `/sync-registry`. |
| `Guidance/Recipe-Format-Standard.md` | Single source of truth for all recipe formatting rules |
| `AGENT_CHANGELOG.md` | Version history for all four agent surfaces |
| `MULTI_AGENT_ARCHITECTURE.md` | Full architecture reference and improvement roadmap |
| `.claude/agents/Cafe Athena Chef.agent.md` | **Canonical master** for the culinary agent system prompt |
| `.agents/workflows/` | Slash-command workflow definitions |
| `The Manual/` | Full cookbook manuscript (source files) |
| `site/src/content/recipes/` | Built recipe files consumed by the Astro site |

---

## ⚠️ Agent Propagation Rule

**When any of the following files are modified, stop and remind the user to manually update the corresponding external surfaces before committing.**

| File Changed | Manual Update Required |
|-------------|----------------------|
| `.claude/agents/Cafe Athena Chef.agent.md` | Copy changes to `Guidance/CAFÉ ATHENA - GEM INSTRUCTIONS.md` (Gemini Gem 1) and `Claude-Desktop/PROJECT_INSTRUCTIONS.md` (Claude Desktop) |
| `Guidance/Recipe-Format-Standard.md` | Re-attach the updated file in Claude Desktop (it is a file attachment, not pasted text); verify Gemini Gem 1 instructions still reference it correctly |
| `.agents/workflows/*.md` | No external update needed — workflows run in Claude Code only |
| `Guidance/CAFÉ ATHENA - HERO IMAGE GEM INSTRUCTIONS.md` | Paste updated content into the Gemini Gem 2 configuration |
| `Claude-Desktop/PROJECT_INSTRUCTIONS.md` | Paste updated content into the Claude Desktop project instructions |

After propagating changes, bump the version number in the modified file and add an entry to `AGENT_CHANGELOG.md`.

---

## Slash Commands

Run these in Claude Code. Full definitions in `.agents/workflows/`.

| Command | Purpose |
|---------|---------|
| `/format-audit [id\|Chapter N]` | Audit recipe(s) against format standard |
| `/glossary-pull [id]` | Merge recipe glossary terms into main glossary |
| `/keyword-pull [id]` | Add missing Keywords + Category sections |
| `/audit-glossary` | Fix alphabetization + duplicates in main glossary |
| `/recipe-hero-image [id]` | Build Gemini image prompt for a recipe |
| `/recipe-hero-image optimize [id\|chapter-N\|all]` | Convert PNG hero images to WebP |
| `/recipe-hero-image insert [id] "[position]" "[caption]"` | Insert image shortcode into a folio |
| `/new-recipe` | Scaffold a new recipe through the full pipeline |
| `/register-recipe [id]` | Register a new entry in `recipes.json` after Claude Desktop Mode 2 |
| `/sync-registry` | Sync `recipes.json` against live Manual directory — adds missing entries, corrects filesystem-derivable stages |
| `/session-handoff` | Update PROJECT_STATUS.md, commit, push, output summary |

---

## Site & Build Notes

- Recipe source files: `The Manual/Chapter N - Name/XX-YY.md`
- Built recipe files: `site/src/content/recipes/XX-YY.md`
- Hero images (source): `The Manual/Chapter N - Name/XX-YY.png` (or `.webp`)
- Hero images (site): `site/public/images/XX-YY.webp`
- Build pipeline: `site/scripts/prepare-content.py` processes Manual → site content
- Deploy: `site/deploy.sh`
