# AGENT CHANGELOG

Tracks version history for all Café Athena AI agent surfaces. Update the canonical master first; then port changes to secondary surfaces.

---

## Surface Version Concordance

> **Note:** Gemini Gem 1 (The Chef) is maintained as a fallback surface. Updates to the canonical master should be ported here when practical.

| Release Date | Canonical Master (Chef) | GEM Instructions | Claude Desktop (Chef) | Visual Director Gem | Markdownlint QA | Recipe Clarity Auditor | Brand Manager | Brand Manager (CD) | Technical Director | Technical Director (CD) | Writing Director |
|--------------|------------------------|-----------------|----------------------|---------------------|-----------------|------------------------|---------------|--------------------|----------------|---------------------|-----------------|
| 2026-06-28b | v1.19 | v3.12 | v1.18 | v2.3 | v1.2 | v1.0 | v2.0 | v1.11 | v1.5 | v1.6 | v1.2 |
| 2026-06-28 | v1.19 | v3.12 | v1.18 | v2.3 | v1.2 | v1.0 | v1.9 | v1.10 | v1.5 | v1.6 | v1.2 |
| 2026-06-25c | v1.19 | v3.12 | v1.18 | v2.3 | v1.2 | v1.0 | v1.9 | v1.10 | v1.5 | v1.6 | v1.1 |
| 2026-06-25b | v1.19 | v3.12 | v1.18 | v2.3 | v1.2 | v1.0 | v1.9 | v1.10 | v1.5 | v1.6 | v1.0 |
| 2026-06-25 | v1.19 | v3.12 | v1.18 | v2.3 | v1.2 | v1.0 | v1.9 | v1.10 | v1.4 | v1.5 | v1.0 |
| 2026-06-24 | v1.19 | v3.12 | v1.18 | v2.3 | v1.2 | v1.0 | v1.8 | v1.9 | v1.4 | v1.5 | — |
| 2026-06-22f | v1.18 | v3.12 | v1.18 | v2.3 | v1.2 | v1.0 | v1.7 | v1.8 | v1.3 | v1.4 | — |
| 2026-06-22e | v1.18 | v3.12 | v1.18 | v2.3 | v1.2 | v1.0 | v1.6 | v1.7 | v1.3 | v1.4 | — |
| 2026-06-22d | v1.18 | v3.12 | v1.18 | v2.3 | v1.2 | v1.0 | v1.5 | v1.6 | v1.3 | v1.4 | — |
| 2026-06-22c | v1.18 | v3.12 | v1.18 | v2.3 | v1.2 | v1.0 | v1.4 | v1.5 | v1.3 | v1.4 | — |
| 2026-06-22b | v1.18 | v3.12 | v1.18 | v2.3 | v1.2 | v1.0 | v1.3 | v1.4 | v1.3 | v1.4 | — |
| 2026-06-22 | v1.18 | v3.12 | v1.18 | v2.2 | v1.2 | v1.0 | v1.3 | v1.4 | v1.3 | v1.4 | — |
| 2026-06-14b | v1.18 | v3.12 | v1.18 | v2.2 | v1.2 | v1.0 | v1.2 | v1.3 | v1.2 | v1.3 | — |
| 2026-06-14 | v1.18 | v3.12 | v1.17 | v2.2 | v1.2 | v1.0 | v1.2 | v1.2 | v1.2 | v1.2 | — |
| 2026-06-11c | v1.18 | v3.12 | v1.17 | v2.2 | v1.2 | v1.0 | v1.1 | v1.1 | v1.2 | v1.2 | — |
| 2026-06-11b | v1.18 | v3.11 | v1.17 | v2.2 | v1.2 | v1.0 | v1.1 | v1.1 | v1.2 | v1.2 | — |
| 2026-06-11 | v1.18 | v3.10 | v1.17 | v2.2 | v1.2 | v1.0 | v1.1 | v1.1 | v1.2 | v1.2 | — |
| 2026-06-10h | v1.18 | v3.10 | v1.17 | v2.1 | v1.2 | v1.0 | v1.1 | v1.1 | v1.1 | v1.1 | — |
| 2026-06-10g | v1.17 | v3.10 | v1.16 | v2.1 | v1.2 | v1.0 | v1.0 | v1.0 | v1.1 | v1.1 | — |
| 2026-06-10f | v1.16 | v3.10 | v1.16 | v2.1 | v1.2 | v1.0 | v1.0 | v1.0 | v1.1 | v1.1 | — |
| 2026-06-10e | v1.15 | v3.10 | v1.15 | v2.1 | v1.2 | v1.0 | v1.0 | v1.0 | v1.0 | v1.0 | — |
| 2026-06-10d | v1.14 | v3.10 | v1.14 | v2.1 | v1.2 | v1.0 | v1.0 | v1.0 | v1.0 | v1.0 | — |
| 2026-06-10c | v1.14 | v3.10 | v1.14 | v2.1 | v1.2 | v1.0 | v1.0 | v1.0 | — | — | — |
| 2026-06-10b | v1.14 | v3.10 | v1.14 | v2.1 | v1.2 | v1.0 | — | — | — | — | — |
| 2026-06-10 | v1.13 | v3.10 | v1.14 | v2.1 | v1.1 | v1.0 | — | — | — | — | — |
| 2026-06-09d | v1.13 | v3.10 | v1.14 | v2.0 | v1.1 | v1.0 | — | — | — | — | — |
| 2026-06-09c | v1.13 | v3.10 | v1.14 | v1.3 | v1.1 | v1.0 | — | — | — | — | — |
| 2026-06-09b | v1.13 | v3.10 | v1.14 | v1.2 | v1.1 | v1.0 | — | — | — | — | — |
| 2026-06-09 | v1.12 | v3.9 | v1.13 | v1.1 | v1.0 | — | — | — | — | — | — |
| 2026-05-25 | v1.12 | v3.8 | v1.9 | v1.1 | — | — | — | — | — | — | — |
| 2026-05-19e | v1.11 | v3.8 | v1.9 | v1.1 | — | — | — | — | — | — | — |
| 2026-05-19d | v1.11 | v3.7 | v1.9 | v1.1 | — | — | — | — | — | — | — |
| 2026-05-19c | v1.10 | v3.7 | v1.9 | v1.1 | — | — | — | — | — | — | — |
| 2026-05-19b | v1.9 | v3.7 | v1.9 | v1.1 | — | — | — | — | — | — | — |
| 2026-05-19 | v1.8 | v3.7 | v1.9 | v1.1 | — | — | — | — | — | — | — |
| 2026-05-18c | v1.7 | v3.7 | v1.9 | v1.1 | — | — | — | — | — | — | — |
| 2026-05-18b | v1.6 | v3.7 | v1.8 | v1.1 | — | — | — | — | — | — | — |
| 2026-05-18 | v1.6 | v3.7 | v1.8 | v1.1 | — | — | — | — | — | — | — |
| 2026-05-15 | v1.6 | v3.7 | v1.7 | v1.1 | — | — | — | — | — | — | — |
| 2026-04-26 | v1.6 | v3.7 | v1.6 | v1.1 | — | — | — | — | — | — | — |
| 2026-04-23 | v1.5 | v3.7 | v1.6 | v1.1 | — | — | — | — | — | — | — |
| 2026-04-16b | v1.4 | v3.7 | v1.5 | v1.1 | — | — | — | — | — | — | — |
| 2026-04-16 | v1.3 | v3.6 | v1.4 | v1.1 | — | — | — | — | — | — | — |
| 2026-04-14 | v1.2 | v3.5 | v1.3 | v1.0 | — | — | — | — | — | — | — |
| 2026-04-04 | v1.1 | v3.4 | v1.2 | v1.0 | — | — | — | — | — | — | — |
| (initial) | v1.0 | v3.0 | v1.0 | v1.0 | — | — | — | — | — | — | — |

---

## Gemini Gem 1 — The Chef *(Fallback Surface)*

**File:** `Agents/Gemini-Gems/CAFÉ ATHENA - CHEF GEM INSTRUCTIONS.md`  
**Status:** Maintained as a fallback surface. Not the primary creative surface (Claude Desktop holds that role), but kept in sync with canonical master updates when practical.  
**Current Version:** 3.12

| Version | Date | Changes |
|---------|------|---------|
| v3.12 | 2026-06-11 | Renamed file from `CAFÉ ATHENA - GEM INSTRUCTIONS.md` to `CAFÉ ATHENA - CHEF GEM INSTRUCTIONS.md`. Updated internal title. All tracking documents updated. |
| v3.11 | 2026-06-11 | Ported collection folio keyword range from canonical master v1.18 — RECIPE STRUCTURE item 9 updated from "8–15 comma-separated tags" to "8–15 for standard folios, up to 20 for collection folios." Backfilled missing v3.9 and v3.10 entries into the in-file VERSION HISTORY. |
| v3.0 | — | Initial release. Mode invoker system, consolidated format standard. |
| v3.1 | — | Added Stop Point Protocol, Troubleshooting Guide, Bad Output Examples, Decision Protocol, mode-specific completion criteria. |
| v3.2 | — | Updated SYSTEM ASSETS (removed 00-01 structure file). Added INDEX UPDATE PROTOCOL with mandatory INDEX DATA block format. Added chapter prefix validation to Stop Points. |
| v3.3 | — | Added Table of Contents, standardized STOP language, streamlined INDEX UPDATE PROTOCOL, clarified Mode 1 completion checklist, consolidated quality guidance, tightened cross-references. |
| v3.4 | 2026-04-04 | Added secondary surface notice and canonical master cross-reference to file header. |
| v3.5 | 2026-04-14 | Updated `/glossary-pull` and `/audit-glossary` descriptions to reference the split glossary structure (`The Manual/Glossary/`) instead of the deprecated monolithic file. |
| v3.6 | 2026-04-16 | Master audit pass. Added anti-sycophancy and uncertainty acknowledgment directives to ROLE & PERSONA. Hardened HACCP food safety stop to non-overridable hard block. Added MEMORY & STATE section with session-start PROJECT_STATUS read directive. Added devil's advocate clause to Mode 1 Stop Points. Added FORMATTING NOTES section (glossary format spec). Added OUT-OF-SCOPE REDIRECT. Added v3.5 entry to in-file VERSION HISTORY (was previously missing). |
| v3.10 | 2026-06-09 | Added mandatory clarity audit to Mode 2 Stop Points. After generating any recipe draft, the agent must run four checks (forward references, ambiguous parentheticals, unlisted method ingredients, multi-action steps) and fix all issues before outputting. |
| v3.9 | 2026-06-09 | Updated slash-command workflow path from `.agents/workflows/` to `.claude/commands/` following project structure consolidation. |
| v3.8 | 2026-05-19 | Added explicit RECIPE STRUCTURE ordered list (10 sections). Added Category format block to FORMATTING NOTES: all four mandatory fields (`cuisine`, `style`, `family`, `course`), `dietary:` as comma-separable optional, technique folio exception, and reference to `Guidance/Taxonomy.md`. Aligns with canonical master v1.9 and `Recipe-Format-Standard.md` v3.3. |
| v3.7 | 2026-04-16 | Added Confidence Flagging four-level scale ([Established] / [Consensus] / [Judgment] / [Experimental]) to ROLE & PERSONA. Added Assumption Surfacing directive. Added Steelman Check to Mode 1 Stop Points (after proposing a direction, surface strongest counterargument in one sentence). |

---

## Claude Desktop Agent

**File:** `Agents/Claude-Desktop/PROJECT_INSTRUCTIONS.md`  
**Current Version:** 1.18

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | — | Initial release. Three-mode system prompt for Claude Desktop / Claude.ai Projects. |
| v1.1 | 2026-03-12 | Full audit pass (see `Claude-Desktop/CD-Audit.md` for details). Key changes: replaced keyword-based mode detection with intent classification; added Mode 2 INDEX VERIFICATION block; added multi-intent request handler; added folio index protocol to Mode 3; added persona tone directives per mode; added version header; fixed line-count discrepancy in COPY_PASTE_TEMPLATE.md. |
| v1.2 | 2026-04-04 | Added secondary surface notice and canonical master cross-reference to header. Added Mode 2 step 8: CLAUDE CODE HANDOFF block (`/register-recipe [XX-YY]`) output after user confirms recipe is written to The Manual. Added update reminder note to header. |
| v1.3 | 2026-04-14 | Updated `/glossary-pull` and `/audit-glossary` descriptions to reference the split glossary structure (`The Manual/Glossary/`) instead of the deprecated monolithic file. |
| v1.4 | 2026-04-16 | Master audit pass. Added No Sycophancy and Uncertainty Acknowledgment directives to PERSONA. Added session-start PROJECT_STATUS read directive to MEMORY & STATE. Added devil's advocate clause and Mode 1 response structure template. Added food safety HARD BLOCK to CRITICAL STOP POINTS. Added glossary format spec to FORMATTING STANDARDS. Added OUT-OF-SCOPE REDIRECT to CORE CONSTRAINTS. |
| v1.5 | 2026-04-16 | Added Confidence Flagging four-level scale ([Established] / [Consensus] / [Judgment] / [Experimental]) to PERSONA. Added Assumption Surfacing directive. Added Steelman Check as item 3 in Mode 1 response structure. |
| v1.18 | 2026-06-14 | Added Mode 2 Output Protocol step 1: "Read Guidance/Recipe-Format-Standard.md to confirm current format rules." Renumbered steps 2–10 accordingly. Brings secondary surface in sync with canonical master v1.18. |
| v1.17 | 2026-06-10 | Ported collection folio keyword range from canonical master v1.18. |
| v1.16 | 2026-06-10 | Updated OUT-OF-SCOPE REDIRECT to reference "Technical Director" following agent rename. Ported from canonical master v1.16. |
| v1.15 | 2026-06-10 | Updated OUT-OF-SCOPE REDIRECT to name the Café Athena Technical Director agent. Ported from canonical master v1.15. |
| v1.14 | 2026-06-09 | Added mandatory clarity audit as step 2 of Mode 2 OUTPUT PROTOCOL. Four checks baked in: forward references, ambiguous parentheticals, unlisted method ingredients, multi-action steps. Renumbered steps 3–9 accordingly. |
| v1.13 | 2026-06-09 | Updated slash-command workflow path from `.agents/workflows/` to `.claude/commands/` following project structure consolidation. |
| v1.9 | 2026-05-18 | Phase 1.5 update. Category format updated to 4 mandatory fields: `cuisine`, `style`, `family`, `course`. Vocabulary now references `Guidance/Taxonomy.md`. `dietary:` comma-separable. Technique folio Category: `style: Technique Folio \| family: [value]` only. Recipe structure item 10 updated. |
| v1.8 | 2026-05-18 | Updated RECIPE STRUCTURE to v3.2 order: Ingredients (3) now precedes Mise en Place (4). Added Variations and Chef's Notes inline definitions (significant departures only vs. minor options). Updated REFERENCE IMAGE SHORTCODE: single-location rule — all images in `site/public/images/` only, no Manual chapter folder. Added `/pipeline [index]` as primary post-session entry point to CLAUDE CODE WORKFLOWS. Updated `/format-audit` and `/glossary-pull` descriptions to reflect v3.2 checks. Removed deprecated `/recipe-hero-image optimize` sub-mode. |
| v1.7 | 2026-05-15 | Split recipe structure item 6 (Chef's Notes / Variations) into two separate optional sections: item 6 = Variations, item 7 = Chef's Notes. Items 8–10 renumbered (Glossary, Keywords, Category). Updated Mode 2 steps 4–5 section references (Section 8→9 for Keywords, Section 9→10 for Category). Aligns with `Guidance/Recipe-Format-Standard.md` v3.1. |
| v1.6 | 2026-04-23 | Lowered Keywords minimum from 10 to 8 (Mode 2 step 4 and RECIPE STRUCTURE item 8). Clarified Category format split: recipe folios use `cuisine: X \| style: Y`; technique folios use `style: Technique Folio` only (no cuisine). Aligns with `Guidance/Recipe-Format-Standard.md` update and `scripts/audit.py` rule changes in same release. |

---

## Claude Code Sub-Agent — Recipe Clarity Auditor

**File:** `.claude/agents/Recipe Clarity Auditor.agent.md`
**Current Version:** 1.0
**Status:** Read-only audit agent. Does not modify files.

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | 2026-06-09 | Initial release. Four checks: forward references in ingredient sections, ambiguous cross-section parentheticals, method ingredients not listed, multi-action steps. |

---

## Claude Code Sub-Agent — Café Athena Chef

**File:** `.claude/agents/Cafe Athena Chef.agent.md`  
**Current Version:** 1.14
**Status:** Canonical master — update this first.

| Version | Date | Changes |
|---------|------|---------|
| v1.19 | 2026-06-24 | Phase 4 RAG audit. Added `Guidance/Taxonomy.md` to SYSTEM ASSETS as item 2 with explicit READ instruction. Updated Mode 2 Output Protocol step 1 to include Taxonomy.md alongside Recipe-Format-Standard.md. No behavior changes — Taxonomy.md was already referenced inline in step 9; this makes the read instruction explicit. |
| v1.18 | 2026-06-10 | Added collection folio keyword range to Mode 2 Output Protocol step 8 and RECIPE STRUCTURE item 9: standard range remains 8–15, collection folios may use up to 20. Ported to `Agents/Claude-Desktop/PROJECT_INSTRUCTIONS.md` v1.17. |
| v1.17 | 2026-06-10 | Housekeeping fixes from agent audit: (1) corrected BUILT-IN WORKFLOWS path from `.agents/workflows/` to `.claude/commands/` (two occurrences — live failure mode); (2) updated secondary surface version reference in file header from v1.9 to v1.16 (stale). Also fixed stale "site developer" language in CLAUDE.md Key Files and Propagation Rule tables; removed 5 Technical Director skills mis-attributed to the Chef section in SKILLS_INDEX. No behavior changes. |
| v1.16 | 2026-06-10 | Updated OUT-OF-SCOPE REDIRECT to reference "Technical Director" following agent rename from "Site Developer." Ported to `Agents/Claude-Desktop/PROJECT_INSTRUCTIONS.md` v1.16. |
| v1.15 | 2026-06-10 | Updated OUT-OF-SCOPE REDIRECT to name the Café Athena Technical Director agent explicitly. Old redirect pointed to Claude Code CLI slash commands; new redirect names the Technical Director as the owner of site development, pipeline, deploy, image optimization, and agent work. Ported to `Agents/Claude-Desktop/PROJECT_INSTRUCTIONS.md` v1.15. |
| v1.14 | 2026-06-10 | Updated all internal file path references to reflect project restructure: `AGENT_CHANGELOG.md` → `Agents/AGENT_CHANGELOG.md`, `Claude-Desktop/` → `Agents/Claude-Desktop/`, `Gemini-Gems/` → `Agents/Gemini-Gems/`, `recipes.json` → `The Manual/recipes.json`. No behavior changes. |
| v1.13 | 2026-06-09 | Added clarity audit as step 3 of Mode 2 Output Protocol. Four checks run automatically after draft generation: forward references in ingredient sections, ambiguous cross-section parentheticals, method steps referencing unlisted ingredients, multi-action steps. Recipe not output until all checks pass. Renumbered Output Protocol steps 4–11 accordingly. |
| v1.12 | 2026-05-25 | Fixed Mode 1 verbosity: reordered response structure to lead with recommendation (proposed direction first, supporting logic second), made Steelman check conditional on consequential/contentious direction rather than mandatory every turn, and scoped confirmation echo to genuinely ambiguous mode detection only. |
| v1.11 | 2026-05-19 | Applied analyzer-aligned wording for factual-correction persona guidance and removed duplicate Mode 2 correction sentence to keep one concise correction policy with mode-specific priority handling. |
| v1.10 | 2026-05-19 | Further diagnostics hardening: moved correction priority logic out of PERSONA into explicit Mode 1/Mode 2 behavior rules, added per-mode priority order lines, and clarified that false premises are never preserved while mode sections define execution style. |
| v1.9 | 2026-05-19 | Resolved Chat Customizations diagnostics by clarifying authority vs exploration priority in the PERSONA section and tightening the Mode 2 critical-input stop point to explicitly require all three fields (yield, cooking method, ingredient list). |
| v1.0 | — | Initial release. Full three-mode system prompt adapted for Claude Code sub-agent with Read/Write/Edit/Grep/Glob/Bash tools. |
| v1.1 | 2026-04 | Added `version:` field to YAML frontmatter. Fixed `.claude/settings.local.json` paths to be project-root-relative. Fixed workflow files (`.agents/workflows/`) to use Claude Code tool names instead of Desktop Commander MCP names. Added canonical master designation and cross-references to secondary surfaces. |
| v1.2 | 2026-04-14 | Updated `/glossary-pull` description to reference the new split glossary structure (`The Manual/Glossary/Café Athena  - Glossary [LETTER].md`) instead of the deprecated monolithic `Café Athena  - Glossary.md`. |
| v1.3 | 2026-04-16 | Master audit pass. Added anti-sycophancy and uncertainty acknowledgment directives to PERSONA. Added session-start PROJECT_STATUS read directive to MEMORY & STATE. Added devil's advocate clause and Mode 1 response structure template. Added food safety HARD BLOCK to UNIVERSAL STOP POINTS. Added glossary format spec to FORMATTING STANDARDS. Added REFERENCE IMAGE SHORTCODE spec to CORE CONSTRAINTS (was CD-only). Added OUT-OF-SCOPE REDIRECT to CORE CONSTRAINTS. |
| v1.4 | 2026-04-16 | Added Confidence Flagging four-level scale ([Established] / [Consensus] / [Judgment] / [Experimental]) to PERSONA. Added Assumption Surfacing directive. Added Steelman Check as item 3 in Mode 1 response structure. |
| v1.5 | 2026-04-23 | Lowered Keywords minimum from 10 to 8 (Mode 2 step 1 and RECIPE STRUCTURE item 8). Clarified Category format split: recipe folios use `cuisine: X \| style: Y`; technique folios use `style: Technique Folio` only (no cuisine). Aligns with `Guidance/Recipe-Format-Standard.md` update and `scripts/audit.py` rule changes in same release. |
| v1.8 | 2026-05-19 | Retired Gemini Gem 1 as secondary surface. Removed `Guidance/CAFÉ ATHENA - GEM INSTRUCTIONS.md` from the secondary surfaces list in the file header. Updated Claude Desktop version reference from v1.6 to v1.9. Claude Desktop is now the sole secondary surface. |
| v1.7 | 2026-05-18 | Phase 1.5 update. Category format updated to 4 mandatory fields: `cuisine`, `style`, `family`, `course`. Vocabulary now references `Guidance/Taxonomy.md` instead of inline list. `dietary:` documented as comma-separable. Technique folio Category updated to `style: Technique Folio \| family: [value]` (no cuisine/course). Recipe structure: fixed Ingredients before Mise (was reversed), split Chef's Notes/Variations, fixed section numbers (Keywords §9, Category §10). |
| v1.6 | 2026-04-26 | BUILT-IN WORKFLOWS section now lists `/register-recipe` and `/sync-registry` (previously omitted). Closes drift between canonical master and the `.agents/workflows/` directory. Workflow definitions themselves were already present — this fix surfaces them in the agent's documented capability set. |

### Companion workflow updates (`.agents/workflows/`)

These workflow files do not carry independent version numbers, but were updated alongside the v1.6 master:

- `glossary-pull.md` — corrected stale glossary heading reference (`### **Glossary**` → `## Glossary`); recipes use H2.
- `new-recipe.md` — corrected glossary heading; added `recipes.json` registration check in Phase 1; added stage-flag updates (`formatAudit`, `keywordPull`, `glossaryPull`, `deployed`) at each phase boundary; replaced `git add -A` guidance with by-name staging; corrected keyword count to 8–15 with foundation-folio note.
- `keyword-pull.md` — corrected keyword count to 8–15 (was 10–15) with foundation-folio note, aligning with canonical master.
- `format-audit.md` — same keyword-count correction for both Recipe and Technique Folio rule sets.
- `recipe-hero-image.md` — fixed deploy-script path (`bash scripts/deploy.sh` → `bash site/scripts/deploy.sh`); replaced `git add -A` in Phase 5 cleanup with by-name staging and a no-`-A` invariant note.
- `register-recipe.md` (2026-05-01) — Phase 5 now appends the new entry to `The Manual/Cafe-Athena-The-Manual-Current-Version.md` (the human-facing TOC) immediately after writing to `recipes.json`. Closes a process gap where 8 folios (01-22, 01-23, 05-03, 10-24, 12-17 through 12-20) had drifted out of the TOC over ~3 weeks.
- `register-recipe.md` (2026-05-18) — Phase 3 expanded to extract `cuisine`, `style`, `family`, `course`, `dietary` from `## Category` and `keywords[]` from `## Keywords`. Phase 4 summary updated to display all metadata fields. Phase 5 now writes these fields into the registry entry (canonical field order: id, title, chapter, chapterName, type, cuisine, style, family, course, keywords, dietary, added, stages, audit). Part of Site IA Phase 3.
- `sync-registry.md` (2026-05-01) — Phase 1 now also reads the Current-Version doc into a doc set; Phase 3 adds **Doc drift** detection (registered indices not present in the TOC); Phase 5 appends drifted/missing entries to the TOC, preserving each chapter's existing list-style convention. `_` and `.` are normalized as equivalent variant separators (registry uses `07-10_2`; doc uses `07-10.2`).
- `format-audit.md` and `keyword-pull.md` (2026-05-02) — Keyword count rule extended to allow **8–20 terms for collection folios** (multi-recipe bundles like 10-23 Asian Dipping Sauces, 10-25 Emulsion Sauces of the Mediterranean, 12-08 Gnocchi 201). Single-recipe folios stay at 8–15. Surfaced when 10-25 (4 sauces, 3 cuisines) legitimately required 18 terms — every term load-bearing for distinct sub-recipe / sub-cuisine / sub-mechanism. `Guidance/Recipe-Format-Standard.md` Section 8 carries the canonical rule.

---

## Recipe Format Standard

**File:** `Guidance/Recipe-Format-Standard.md`
**Current Version:** 3.3

| Version | Date | Changes |
|---------|------|---------|
| v3.3 | 2026-05-18 | Section 10 (Category): added `family:` and `course:` as mandatory fields for finished recipes. Vocabulary removed from inline — all valid values now live in `Guidance/Taxonomy.md` (single source of truth). `dietary:` documented as supporting comma-separated values. One-value-per-field rule documented. Technique Folio Category spec updated to include `family:` (no `cuisine:` or `course:`). |
| v3.2 | 2026-05-18 | Ingredients (3) now precedes Mise en Place (4). Split Variations / Chef's Notes into separate optional sections (items 6–7). Items 8–10 renumbered. |
| v3.1 | 2026-05-15 | Extended Keywords to allow 8–20 terms for collection folios. |
| v3.0 | 2026-04-23 | Keywords minimum lowered to 8. Category format split: recipe folios vs. technique folios clarified. |

---

## Gemini Gem 2 — The Visual Director

**File:** `Agents/Gemini-Gems/CAFÉ ATHENA - VISUAL DIRECTOR GEM INSTRUCTIONS.md`  
**Current Version:** 2.3

| Version | Date | Changes |
|---------|------|---------|
| v2.3 | 2026-06-22 | Updated site URL reference from cookbook.kevinward.com to cafeathenathemanual.com. |
| v2.2 | 2026-06-11 | Fixed broken markdown table separator in Mode 3 section-specific guidance (`---- ----` → `----`). Added reference image fallback to Mode 1: if Gem UI attachments are missing, written style descriptions serve as the fallback standard — do not interpolate generic food photography defaults. |
| v2.1 | 2026-06-10 | Revised people/faces rules. Mode 1 (recipe heroes): "No people or hands" replaced with "no faces/full figures; hands actively engaging with cookware or food are permitted." Mode 2 (banners): removed "No people or hands" restriction — people including faces are acceptable. Mode 3 (section landing): removed face exclusion rule — full figures including faces are permitted. Added Glossary exception to Mode 3 text suppression: legible text in open books/notebooks is acceptable and encouraged. |
| v2.0 | 2026-06-09 | Expanded scope from recipe hero images only to full Visual Director covering all three image types. Added MODE 1 (Recipe Hero), MODE 2 (Chapter Banner), and MODE 3 (Section Landing Page) sections, each with distinct composition rules, surface guidance, suppress lists, and brief input formats. Renamed file from `CAFÉ ATHENA - HERO IMAGE GEM INSTRUCTIONS.md` to `CAFÉ ATHENA - VISUAL DIRECTOR GEM INSTRUCTIONS.md`. Moved from `Guidance/` to `Gemini-Gems/`. Banners: 1920×480 ultra-wide (4:1), ingredient/process focus, no plated dishes. Section landing: 1920×1080 (16:9), hands/people permitted for action shots (faces excluded), cinematic editorial style. Per-section guidance table added for all four site sections (Academy, Brigade, Larder, Glossary). "No people or hands" constraint now scoped to Mode 1 recipe heroes only. |
| v1.3 | 2026-06-09 | Added REFERENCE STYLE IMAGES section. Five canonical hero images designated as visual anchors — one per style zone: `07-09.webp` (default bistro braise), `07-03.webp` (grilled/smoked), `05-02.webp` (seafood/Fishmonger), `09-03.webp` (pastry/Pâtissier), `10-17.webp` (larder/foundational). Images should be attached directly in the Gemini Gem UI. |
| v1.2 | 2026-06-08 | Added `Output: 16:9 widescreen, 1920×1080, landscape orientation` as a required field in the INPUT FORMAT brief template. Fixes aspect ratio drift — Gemini's image generation defaults do not reliably honor the 16:9 crop spec in the Camera & Composition section alone. |
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

## Claude Code Sub-Agent — Café Athena Brand Manager

**File:** `.claude/agents/Cafe Athena Brand Manager.agent.md`
**Current Version:** 2.0
**Status:** Canonical master — update this first, then port to Claude Desktop secondary surface.

Secondary surface: `Agents/Claude-Desktop/BRAND_MANAGER_INSTRUCTIONS.md`

| Version | Date | Changes |
|---------|------|---------|
| v2.0 | 2026-06-28 | Added `Brand/Scorecards/` to SESSION START PROTOCOL (item 6) — read most recent date-stamped scorecard when assessing brand progress, KPI targets, or channel performance. Added `Brand/Scorecards/` to OWNED DOCUMENTS — new date-stamped file per review cycle, never overwrite previous. Ported to BRAND_MANAGER_INSTRUCTIONS.md v1.11. |
| v1.8 | 2026-06-24 | Phase 4 RAG audit. Removed "Brand context you must always carry" block from ROLE & PERSONA — 4 baked-in bullets about origin story, website purpose, personality, and Kevin's role now replaced with an explicit instruction to read `Brand/BRAND_GUIDELINES.md`. Removed "*(once it exists)*" caveat from SESSION START PROTOCOL item 5 — BRAND_GUIDELINES.md exists and must be read unconditionally. Updated OWNED DOCUMENTS row for BRAND_GUIDELINES.md: "Create it" removed; now says "Maintain as master brand reference — read at every session." Updated BRAND GUIDELINES DEVELOPMENT PROTOCOL framing from "when file does not exist" to "when expanding or revising." Ported to BRAND_MANAGER_INSTRUCTIONS.md v1.9. |
| v1.5 | 2026-06-22 | Mode 4 renamed from "HF Asset Production" to "Asset Production." Added Adobe Firefly (Kling 3.0 Omni) as primary video tool: locked settings (720p, 9:16, 24fps, 15s, seed 1847, reference image, 300 credits), prompt pattern with 06-07 example, step-by-step workflow. Added Adobe Express as primary assembly tool (replaces WanWeb/FFmpeg). Tool routing table added. FFmpeg retained as backup only. Mode disambiguation and greeting updated to include Firefly/Adobe Express triggers. OUT-OF-SCOPE redirect clarified: cookbook hero images (Lane 1) → Visual Director Gem 2; promotional stills, social video, animated clips → Brand Manager Mode 4. Ported to BRAND_MANAGER_INSTRUCTIONS.md v1.6. |
| v1.4 | 2026-06-22 | Added Mode 4 (HF Asset Production): pre-production brief writing, output approval against brand parameters, FFmpeg post-processing commands (audio trim/compress/normalize, video merge/trim/compress, frame extraction). Brand Manager's role as HF production partner and approval gate is now explicit in the agent. Ported to BRAND_MANAGER_INSTRUCTIONS.md v1.5. |
| v1.3 | 2026-06-22 | Domain change — updated site URL from `cookbook.kevinward.com` to `cafeathenathemanual.com` in role description. Ported to BRAND_MANAGER_INSTRUCTIONS.md v1.4. |
| v1.2 | 2026-06-14 | Added PM Skills section to SKILLS — 8 skills from the pm-skills plugin (pm-go-to-market, pm-marketing-growth, pm-market-research, pm-execution) with per-mode trigger conditions. Skills are Claude Code–only; note added to inform agent of the constraint. CLAUDE.md auto-trigger table also updated with matching PM Skills subsection. Secondary surface updated to v1.2 with a PM Skills reference table and Claude-Desktop-only caveat. |
| v1.1 | 2026-06-10 | Three structural improvements from agent audit: (1) Added Mode disambiguation tie-breaker — "write/draft/create" + topic → Mode 3; planning verbs → Mode 2; resolves Mode 2/3 overlap on "post," "copy," "bio." (2) Added OUT-OF-SCOPE REDIRECT section — Chef for culinary, Technical Director for site/pipeline, Visual Director Gem for images. (3) Added SESSION HANDOFF PROTOCOL — trigger: "Handoff/Close out/Goodbye/Save and wrap"; updates status docs, commits, outputs 3-bullet summary. Ported to BRAND_MANAGER_INSTRUCTIONS.md v1.1. |
| v1.0 | 2026-06-10 | Initial release. Three-mode system (Brand Development, Marketing Execution, Content Creation). Owns Brand/ and Marketing/ folder documents. Session startup reads BRAND_STATUS.md, MARKETING_STATUS.md, and both Resources/INDEX.md files. Build sequence for BRAND_GUIDELINES.md defined. Resource library with trigger conditions. Skills: brand-voice, audience-persona-builder, copywriting, landing-page-copywriter, social-content, marketing-psychology, avoid-ai-writing, beautiful-prose. |

---

## Claude Desktop Agent — Café Athena Brand Manager

**File:** `Agents/Claude-Desktop/BRAND_MANAGER_INSTRUCTIONS.md`
**Current Version:** 1.11

| Version | Date | Changes |
|---------|------|---------|
| v1.11 | 2026-06-28 | Added `Brand/Scorecards/` to SESSION START (item 6) and KEY FILES table. Ported from canonical master v2.0. |
| v1.9 | 2026-06-24 | Phase 4 RAG audit port from canonical master v1.8. BRAND CONTEXT section renamed to BRAND REFERENCE — baked-in bullets removed, replaced with explicit instruction to read `Brand/BRAND_GUIDELINES.md`. SESSION START item 5: removed "*(once it exists)*" caveat. KEY FILES table: BRAND_GUIDELINES.md row updated to "Maintain as master brand reference — read at every session." BRAND GUIDELINES BUILD SEQUENCE: framing updated to "when expanding or revising." |
| v1.6 | 2026-06-22 | Mode 4 renamed to "Asset Production." Added Firefly (Kling 3.0 Omni) as primary video tool with settings table and prompt pattern. Added Adobe Express as primary assembly tool with workflow steps. Tool routing table added. FFmpeg retained as backup. Disambiguation and Out-of-Scope redirect updated. Ported from canonical master v1.5. |
| v1.5 | 2026-06-22 | Added Mode 4 (HF Asset Production) to MODE DETECTION section: structured brief writing, approval gate criteria, FFmpeg command reference, disambiguation tie-breaker update, ambiguous greeting update. Ported from canonical master v1.4. |
| v1.4 | 2026-06-22 | Domain change — updated site URL from `cookbook.kevinward.com` to `cafeathenathemanual.com`. Ported from canonical master v1.3. |
| v1.3 | 2026-06-14 | Added BRAND & COPY SKILLS table (8 skills: brand-voice, audience-persona-builder, copywriting, landing-page-copywriter, social-content, marketing-psychology, avoid-ai-writing, beautiful-prose) — was absent from secondary surface. Added items 3–4 to SESSION START (Brand/Resources/INDEX.md, Marketing/Resources/INDEX.md) — closes gap from agent audit. |
| v1.2 | 2026-06-14 | Added PM Skills Reference section with 8 pm-skills entries. Ported from canonical master v1.2. |
| v1.1 | 2026-06-10 | Ported from canonical master v1.1: mode disambiguation tie-breaker, OUT-OF-SCOPE REDIRECT, and SESSION HANDOFF PROTOCOL. |
| v1.0 | 2026-06-10 | Initial release. Secondary surface port of canonical master v1.0. |

---

## Claude Code Sub-Agent — Café Athena Technical Director

**File:** `.claude/agents/Cafe Athena Technical Director.agent.md`
**Current Version:** 1.5
**Status:** Canonical master — update this first, then port to Claude Desktop secondary surface.

Secondary surface: `Agents/Claude-Desktop/TECHNICAL_DIRECTOR_INSTRUCTIONS.md`

| Version | Date | Changes |
|---------|------|---------|
| v1.5 | 2026-06-25 | Phase 1 audit fix — canonical bumped to match CD v1.5 (CD had been edited directly on 2026-06-24, wrong direction). No content changes to canonical. Ported full ECC skills table to CD v1.6 (9 entries were missing from the compact CD port). |
| v1.4 | 2026-06-24 | Phase 4 RAG audit. SESSION START PROTOCOL item 4: replaced stale `.claude/SKILLS_INDEX.md` (retired in Phase 2) with `Docs/TECHNICAL_REFERENCE.md` with explicit read instruction. SYSTEM ASSETS table: replaced `.claude/SKILLS_INDEX.md` row with `Docs/TECHNICAL_REFERENCE.md`; updated CLAUDE.md row description to reflect it is now the behavioral contract, not the architecture reference. Ported to TECHNICAL_DIRECTOR_INSTRUCTIONS.md v1.5. |
| v1.3 | 2026-06-22 | Domain change — updated site URL from `cookbook.kevinward.com` to `cafeathenathemanual.com` in role description. Ported to TECHNICAL_DIRECTOR_INSTRUCTIONS.md v1.4. |
| v1.2 | 2026-06-11 | Added SESSION HANDOFF PROTOCOL — trigger: "Handoff/Close out/Goodbye/Save and wrap"; reads and updates PROJECT_STATUS.md, commits, outputs 3-bullet summary. Ported to TECHNICAL_DIRECTOR_INSTRUCTIONS.md v1.2 (also added condensed SKILLS table, SYSTEM ASSETS table). |
| v1.1 | 2026-06-10 | Renamed from "Café Athena Site Developer" to "Café Athena Technical Director." File renamed to `.claude/agents/Cafe Athena Technical Director.agent.md`; secondary surface renamed to `TECHNICAL_DIRECTOR_INSTRUCTIONS.md`. No behavior changes. |
| v1.0 | 2026-06-10 | Initial release. Three-mode system (Site Development, Pipeline & Deploy, Agent & Tooling Development). Owns site/, scripts/, site/scripts/, site/public/images/, .claude/agents/, .claude/commands/, .claude/skills/, and Agents/. Session startup reads PROJECT_STATUS.md, BRAND_STATUS.md, MARKETING_STATUS.md, .claude/SKILLS_INDEX.md. Deploy, heroImage, and agent version bump constraints documented as critical constraints. Skills: astro, cafe-athena-site-dev, seo-aeo-schema-generator, fixing-metadata, seo-images, and multiple everything-claude-code: agent tools. |

---

## Claude Desktop Agent — Café Athena Technical Director

**File:** `Agents/Claude-Desktop/TECHNICAL_DIRECTOR_INSTRUCTIONS.md`
**Current Version:** 1.6

| Version | Date | Changes |
|---------|------|---------|
| v1.6 | 2026-06-25 | Phase 1 audit fix — restored 9 ECC skills missing from compact CD port: `architect`, `blueprint`, `agentic-engineering`, `python-reviewer`, `code-reviewer`, `security-review`, `tdd`, `context-budget`, `claude-api`. CD skills table now matches canonical. |
| v1.5 | 2026-06-24 | Phase 4 RAG audit port from canonical master v1.4. SESSION START item 4: replaced `.claude/SKILLS_INDEX.md` with `Docs/TECHNICAL_REFERENCE.md`. SYSTEM ASSETS table: added `Docs/TECHNICAL_REFERENCE.md` row; updated CLAUDE.md row description. |
| v1.4 | 2026-06-22 | Domain change — updated site URL from `cookbook.kevinward.com` to `cafeathenathemanual.com`. Ported from canonical master v1.3. |
| v1.3 | 2026-06-14 | Added AGENT PROPAGATION RULE section — closes gap from agent audit. Ensures Claude Desktop Technical Director knows propagation steps (port changes, remind Kevin to paste, version bump, changelog update) when agent files are modified in Mode 3. |
| v1.2 | 2026-06-11 | Ported from canonical v1.2: SESSION HANDOFF PROTOCOL. Added condensed SKILLS table (5 project skills) and SYSTEM ASSETS table (7 key files). |
| v1.1 | 2026-06-10 | File renamed from `SITE_DEVELOPER_INSTRUCTIONS.md` to `TECHNICAL_DIRECTOR_INSTRUCTIONS.md`. Agent renamed to "Technical Director." No behavior changes. |
| v1.0 | 2026-06-10 | Initial release. Secondary surface port of canonical master v1.0. |

---

## Claude Code Sub-Agent — Café Athena Writing Director

**File:** `.claude/agents/Cafe Athena Writing Director.agent.md`
**Current Version:** 1.2
**Status:** Canonical master — no secondary surfaces by design (paragraph approval gate requires interactive session).

| Version | Date | Changes |
|---------|------|---------|
| v1.2 | 2026-06-28 | Added three editorial principles to Writing Standards, derived from WIRED-editor review of bio-long.md: (1) Narrative order — emotional anchor before mechanical explanation in any origin story or arc; (2) Authority and concession — never retreat into a self-deprecating list after establishing credentials; close the authority-building move with a statement, not a concession; (3) Closing sentences earn the paragraph — the final sentence must match or exceed the paragraph's best moment; a weak close is worse than an honest functional close. |
| v1.1 | 2026-06-25 | Replaced absolute "cut all brand names" rule with judgment-based guidance: brand names are not banned — they require judgment and must be used well and appropriately. Earned, narrative-serving brand names (specific personal tools, story-grounding details) may stay; brand names functioning as product placement or tech-industry shorthand are still cut. |
| v1.0 | 2026-06-25 | Initial release. Three-mode system (Draft, Edit, Standards Audit). Owns all prose surfaces — author bios, About page, social captions, promotional copy, email, site hero copy. Pre-writing brief mandatory in Mode 1; paragraph-by-paragraph approval gate in all modes; no file writes until full piece approved. Session start reads BRAND_GUIDELINES.md §5–§6 and writing-exemplars.md before every session. |

---

## Notes

- Dates marked `—` are not recorded in the original files. Use `git log` to approximate if needed.
- When updating any agent, bump the version number in both the file header and this changelog.
- The Visual Director (Gem 2) is independent of the culinary agent system prompt — it does not need to stay in sync with the master.
