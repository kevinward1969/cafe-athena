# AGENT CHANGELOG

Tracks version history for all four Café Athena AI agent surfaces. The canonical master for the culinary agent system prompt is `.claude/agents/Cafe Athena Chef.agent.md`. Update the master first; then port changes to secondary surfaces.

---

## Surface Version Concordance

| Release Date | Canonical Master | GEM Instructions | Claude Desktop | Markdownlint QA |
|--------------|-----------------|-----------------|----------------|-----------------|
| 2026-04-26 | v1.6 | v3.7 | v1.6 | v1.1 |
| 2026-04-23 | v1.5 | v3.7 | v1.6 | v1.1 |
| 2026-04-16b | v1.4 | v3.7 | v1.5 | v1.1 |
| 2026-04-16 | v1.3 | v3.6 | v1.4 | v1.1 |
| 2026-04-14 | v1.2 | v3.5 | v1.3 | v1.0 |
| 2026-04-04 | v1.1 | v3.4 | v1.2 | v1.0 |
| (initial) | v1.0 | v3.0 | v1.0 | v1.0 |

---

## Gemini Gem 1 — The Chef

**File:** `Guidance/CAFÉ ATHENA - GEM INSTRUCTIONS.md`  
**Current Version:** 3.7

| Version | Date | Changes |
|---------|------|---------|
| v3.0 | — | Initial release. Mode invoker system, consolidated format standard. |
| v3.1 | — | Added Stop Point Protocol, Troubleshooting Guide, Bad Output Examples, Decision Protocol, mode-specific completion criteria. |
| v3.2 | — | Updated SYSTEM ASSETS (removed 00-01 structure file). Added INDEX UPDATE PROTOCOL with mandatory INDEX DATA block format. Added chapter prefix validation to Stop Points. |
| v3.3 | — | Added Table of Contents, standardized STOP language, streamlined INDEX UPDATE PROTOCOL, clarified Mode 1 completion checklist, consolidated quality guidance, tightened cross-references. |
| v3.4 | 2026-04-04 | Added secondary surface notice and canonical master cross-reference to file header. |
| v3.5 | 2026-04-14 | Updated `/glossary-pull` and `/audit-glossary` descriptions to reference the split glossary structure (`The Manual/Glossary/`) instead of the deprecated monolithic file. |
| v3.6 | 2026-04-16 | Master audit pass. Added anti-sycophancy and uncertainty acknowledgment directives to ROLE & PERSONA. Hardened HACCP food safety stop to non-overridable hard block. Added MEMORY & STATE section with session-start PROJECT_STATUS read directive. Added devil's advocate clause to Mode 1 Stop Points. Added FORMATTING NOTES section (glossary format spec). Added OUT-OF-SCOPE REDIRECT. Added v3.5 entry to in-file VERSION HISTORY (was previously missing). |
| v3.7 | 2026-04-16 | Added Confidence Flagging four-level scale ([Established] / [Consensus] / [Judgment] / [Experimental]) to ROLE & PERSONA. Added Assumption Surfacing directive. Added Steelman Check to Mode 1 Stop Points (after proposing a direction, surface strongest counterargument in one sentence). |

---

## Claude Desktop Agent

**File:** `Claude-Desktop/PROJECT_INSTRUCTIONS.md`  
**Current Version:** 1.6

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | — | Initial release. Three-mode system prompt for Claude Desktop / Claude.ai Projects. |
| v1.1 | 2026-03-12 | Full audit pass (see `Claude-Desktop/CD-Audit.md` for details). Key changes: replaced keyword-based mode detection with intent classification; added Mode 2 INDEX VERIFICATION block; added multi-intent request handler; added folio index protocol to Mode 3; added persona tone directives per mode; added version header; fixed line-count discrepancy in COPY_PASTE_TEMPLATE.md. |
| v1.2 | 2026-04-04 | Added secondary surface notice and canonical master cross-reference to header. Added Mode 2 step 8: CLAUDE CODE HANDOFF block (`/register-recipe [XX-YY]`) output after user confirms recipe is written to The Manual. Added update reminder note to header. |
| v1.3 | 2026-04-14 | Updated `/glossary-pull` and `/audit-glossary` descriptions to reference the split glossary structure (`The Manual/Glossary/`) instead of the deprecated monolithic file. |
| v1.4 | 2026-04-16 | Master audit pass. Added No Sycophancy and Uncertainty Acknowledgment directives to PERSONA. Added session-start PROJECT_STATUS read directive to MEMORY & STATE. Added devil's advocate clause and Mode 1 response structure template. Added food safety HARD BLOCK to CRITICAL STOP POINTS. Added glossary format spec to FORMATTING STANDARDS. Added OUT-OF-SCOPE REDIRECT to CORE CONSTRAINTS. |
| v1.5 | 2026-04-16 | Added Confidence Flagging four-level scale ([Established] / [Consensus] / [Judgment] / [Experimental]) to PERSONA. Added Assumption Surfacing directive. Added Steelman Check as item 3 in Mode 1 response structure. |
| v1.6 | 2026-04-23 | Lowered Keywords minimum from 10 to 8 (Mode 2 step 4 and RECIPE STRUCTURE item 8). Clarified Category format split: recipe folios use `cuisine: X \| style: Y`; technique folios use `style: Technique Folio` only (no cuisine). Aligns with `Guidance/Recipe-Format-Standard.md` update and `scripts/audit.py` rule changes in same release. |

---

## Claude Code Sub-Agent — Café Athena Chef

**File:** `.claude/agents/Cafe Athena Chef.agent.md`  
**Current Version:** 1.6  
**Status:** Canonical master — update this first.

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | — | Initial release. Full three-mode system prompt adapted for Claude Code sub-agent with Read/Write/Edit/Grep/Glob/Bash tools. |
| v1.1 | 2026-04 | Added `version:` field to YAML frontmatter. Fixed `.claude/settings.local.json` paths to be project-root-relative. Fixed workflow files (`.agents/workflows/`) to use Claude Code tool names instead of Desktop Commander MCP names. Added canonical master designation and cross-references to secondary surfaces. |
| v1.2 | 2026-04-14 | Updated `/glossary-pull` description to reference the new split glossary structure (`The Manual/Glossary/Café Athena  - Glossary [LETTER].md`) instead of the deprecated monolithic `Café Athena  - Glossary.md`. |
| v1.3 | 2026-04-16 | Master audit pass. Added anti-sycophancy and uncertainty acknowledgment directives to PERSONA. Added session-start PROJECT_STATUS read directive to MEMORY & STATE. Added devil's advocate clause and Mode 1 response structure template. Added food safety HARD BLOCK to UNIVERSAL STOP POINTS. Added glossary format spec to FORMATTING STANDARDS. Added REFERENCE IMAGE SHORTCODE spec to CORE CONSTRAINTS (was CD-only). Added OUT-OF-SCOPE REDIRECT to CORE CONSTRAINTS. |
| v1.4 | 2026-04-16 | Added Confidence Flagging four-level scale ([Established] / [Consensus] / [Judgment] / [Experimental]) to PERSONA. Added Assumption Surfacing directive. Added Steelman Check as item 3 in Mode 1 response structure. |
| v1.5 | 2026-04-23 | Lowered Keywords minimum from 10 to 8 (Mode 2 step 1 and RECIPE STRUCTURE item 8). Clarified Category format split: recipe folios use `cuisine: X \| style: Y`; technique folios use `style: Technique Folio` only (no cuisine). Aligns with `Guidance/Recipe-Format-Standard.md` update and `scripts/audit.py` rule changes in same release. |
| v1.6 | 2026-04-26 | BUILT-IN WORKFLOWS section now lists `/register-recipe` and `/sync-registry` (previously omitted). Closes drift between canonical master and the `.agents/workflows/` directory. Workflow definitions themselves were already present — this fix surfaces them in the agent's documented capability set. |

### Companion workflow updates (`.agents/workflows/`)

These workflow files do not carry independent version numbers, but were updated alongside the v1.6 master:

- `glossary-pull.md` — corrected stale glossary heading reference (`### **Glossary**` → `## Glossary`); recipes use H2.
- `new-recipe.md` — corrected glossary heading; added `recipes.json` registration check in Phase 1; added stage-flag updates (`formatAudit`, `keywordPull`, `glossaryPull`, `deployed`) at each phase boundary; replaced `git add -A` guidance with by-name staging; corrected keyword count to 8–15 with foundation-folio note.
- `keyword-pull.md` — corrected keyword count to 8–15 (was 10–15) with foundation-folio note, aligning with canonical master.
- `format-audit.md` — same keyword-count correction for both Recipe and Technique Folio rule sets.
- `recipe-hero-image.md` — fixed deploy-script path (`bash scripts/deploy.sh` → `bash site/scripts/deploy.sh`); replaced `git add -A` in Phase 5 cleanup with by-name staging and a no-`-A` invariant note.

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
**Current Version:** 1.1
**Status:** Claude Code only — no secondary surfaces.

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-06 | Initial release. Four-mode pipeline agent (Scan, Safe Fix, Deep Fix, Full Pipeline) orchestrating `scripts/markdownlint_safe_fix.py` and `scripts/fix_markdown_with_ollama.py`. Authorization checkpoint before any file writes. Scope resolution from file ID, chapter name, site, or all. Model guidance for llama3.2 vs gemma3:4b. |
| v1.1 | 2026-04-16 | Added excluded scope table: `Guidance/`, `.claude/`, `.agents/`, `Claude-Desktop/`, `node_modules/` are now blocked from lint-repair with an explicit refusal message. Prevents LLM fixer from corrupting curated instruction and agent definition files. |

---

---

## VS Code Copilot Skill — Site Development

**File:** `.github/skills/cafe-athena-site-dev/SKILL.md`
**Current Version:** 1.0
**Status:** VS Code Copilot Chat only — no secondary surfaces. Not compatible with Claude Code sub-agents or `.agents/workflows/` slash commands.

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-14 | Initial release. Full Astro/Tailwind site development skill for cookbook.kevinward.com. Covers stack reference (Astro 6, Tailwind v4, Pagefind, GSAP), project layout, critical constraints (heroImage filename-only format, no tailwind.config.js), four-stage workflow (assess → plan → implement → test → commit → deploy), FastComet rsync deploy via SSH alias, content schema, pending site work (Part IV/Expo, banner images, SectionLayout bannerImage prop), and pre-completion checklist. |
| v1.1 | 2026-04-26 | Replaced `git add -A` in commit step with by-name staging, aligned with `CLAUDE.md` git-hygiene policy. Updated stale Ch. 12 entry count (10 → 20) in Pending Site Work. |

---

## VS Code Copilot Agent — Markdownlint QA

**File:** `.github/agents/markdownlint-qa.agent.md`
**Current Version:** 1.1
**Status:** VS Code Copilot Chat only. Mirrors the Claude Code Markdownlint QA sub-agent.

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-04-14 | Initial release. Four-mode lint pipeline (Scan, Safe Fix, Deep Fix, Full Pipeline) for Copilot Chat surface. Mirrors the Claude Code sub-agent's pipeline behavior and authorization gates. |
| v1.1 | 2026-04-26 | Added missing **Excluded scopes** safety table (`Guidance/`, `.claude/`, `.agents/`, `.github/`, `Claude-Desktop/`, `node_modules/`) — closes parity gap with the Claude Code sub-agent. Without this table, the Copilot agent could lint-repair curated instruction files and corrupt agent behavior. |

---

## Notes

- Dates marked `—` are not recorded in the original files. Use `git log` to approximate if needed.
- When updating any agent, bump the version number in both the file header and this changelog.
- The Visual Director (Gem 2) is independent of the culinary agent system prompt — it does not need to stay in sync with the master.
