# AGENT CHANGELOG

Tracks version history for all four Café Athena AI agent surfaces. The canonical master for the culinary agent system prompt is `.claude/agents/Cafe Athena Chef.agent.md`. Update the master first; then port changes to secondary surfaces.

---

## Gemini Gem 1 — The Chef

**File:** `Guidance/CAFÉ ATHENA - GEM INSTRUCTIONS.md`  
**Current Version:** 3.5

| Version | Date | Changes |
|---------|------|---------|
| v3.0 | — | Initial release. Mode invoker system, consolidated format standard. |
| v3.1 | — | Added Stop Point Protocol, Troubleshooting Guide, Bad Output Examples, Decision Protocol, mode-specific completion criteria. |
| v3.2 | — | Updated SYSTEM ASSETS (removed 00-01 structure file). Added INDEX UPDATE PROTOCOL with mandatory INDEX DATA block format. Added chapter prefix validation to Stop Points. |
| v3.3 | — | Added Table of Contents, standardized STOP language, streamlined INDEX UPDATE PROTOCOL, clarified Mode 1 completion checklist, consolidated quality guidance, tightened cross-references. |
| v3.4 | 2026-04-04 | Added secondary surface notice and canonical master cross-reference to file header. |
| v3.5 | 2026-04-14 | Updated `/glossary-pull` and `/audit-glossary` descriptions to reference the split glossary structure (`The Manual/Glossary/`) instead of the deprecated monolithic file. |

---

## Claude Desktop Agent

**File:** `Claude-Desktop/PROJECT_INSTRUCTIONS.md`  
**Current Version:** 1.3

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | — | Initial release. Three-mode system prompt for Claude Desktop / Claude.ai Projects. |
| v1.1 | 2026-03-12 | Full audit pass (see `Claude-Desktop/CD-Audit.md` for details). Key changes: replaced keyword-based mode detection with intent classification; added Mode 2 INDEX VERIFICATION block; added multi-intent request handler; added folio index protocol to Mode 3; added persona tone directives per mode; added version header; fixed line-count discrepancy in COPY_PASTE_TEMPLATE.md. |
| v1.2 | 2026-04-04 | Added secondary surface notice and canonical master cross-reference to header. Added Mode 2 step 8: CLAUDE CODE HANDOFF block (`/register-recipe [XX-YY]`) output after user confirms recipe is written to The Manual. Added update reminder note to header. |
| v1.3 | 2026-04-14 | Updated `/glossary-pull` and `/audit-glossary` descriptions to reference the split glossary structure (`The Manual/Glossary/`) instead of the deprecated monolithic file. |

---

## Claude Code Sub-Agent — Café Athena Chef

**File:** `.claude/agents/Cafe Athena Chef.agent.md`  
**Current Version:** 1.2  
**Status:** Canonical master — update this first.

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | — | Initial release. Full three-mode system prompt adapted for Claude Code sub-agent with Read/Write/Edit/Grep/Glob/Bash tools. |
| v1.1 | 2026-04 | Added `version:` field to YAML frontmatter. Fixed `.claude/settings.local.json` paths to be project-root-relative. Fixed workflow files (`.agents/workflows/`) to use Claude Code tool names instead of Desktop Commander MCP names. Added canonical master designation and cross-references to secondary surfaces. |
| v1.2 | 2026-04-14 | Updated `/glossary-pull` description to reference the new split glossary structure (`The Manual/Glossary/Café Athena  - Glossary [LETTER].md`) instead of the deprecated monolithic `Café Athena  - Glossary.md`. |

---

## Gemini Gem 2 — The Visual Director

**File:** `Guidance/CAFÉ ATHENA - HERO IMAGE GEM INSTRUCTIONS.md`  
**Current Version:** 1.1

| Version | Date | Changes |
|---------|------|---------|
| v1.1 | 2026-04-15 | Added Ch. 12 (Les Fonds) to chapter style table — architectural/elemental style for structural bases (doughs, pastry creams, tuile, pasta). Updated marble surface exception to include Ch. 12 alongside Ch. 9. |
| v1.0 | — | Initial release. Purpose-limited to hero image generation. Defines core aesthetic (warm editorial food photography), output constraints (one image, 16:9, ¾ overhead angle), and quality benchmarks. |

---

## Claude Code Sub-Agent — Markdownlint QA

**File:** `.claude/agents/Markdownlint QA.agent.md`
**Current Version:** 1.0
**Status:** Claude Code only — no secondary surfaces.

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-06 | Initial release. Four-mode pipeline agent (Scan, Safe Fix, Deep Fix, Full Pipeline) orchestrating `scripts/markdownlint_safe_fix.py` and `scripts/fix_markdown_with_ollama.py`. Authorization checkpoint before any file writes. Scope resolution from file ID, chapter name, site, or all. Model guidance for llama3.2 vs gemma3:4b. |

---

---

## VS Code Copilot Skill — Site Development

**File:** `.github/skills/cafe-athena-site-dev/SKILL.md`
**Current Version:** 1.0
**Status:** VS Code Copilot Chat only — no secondary surfaces. Not compatible with Claude Code sub-agents or `.agents/workflows/` slash commands.

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-14 | Initial release. Full Astro/Tailwind site development skill for cookbook.kevinward.com. Covers stack reference (Astro 6, Tailwind v4, Pagefind, GSAP), project layout, critical constraints (heroImage filename-only format, no tailwind.config.js), four-stage workflow (assess → plan → implement → test → commit → deploy), FastComet rsync deploy via SSH alias, content schema, pending site work (Part IV/Expo, banner images, SectionLayout bannerImage prop), and pre-completion checklist. |

---

## Notes

- Dates marked `—` are not recorded in the original files. Use `git log` to approximate if needed.
- When updating any agent, bump the version number in both the file header and this changelog.
- The Visual Director (Gem 2) is independent of the culinary agent system prompt — it does not need to stay in sync with the master.
