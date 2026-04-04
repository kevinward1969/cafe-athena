# AGENT CHANGELOG

Tracks version history for all four Café Athena AI agent surfaces. The canonical master for the culinary agent system prompt is `.claude/agents/Cafe Athena Chef.agent.md`. Update the master first; then port changes to secondary surfaces.

---

## Gemini Gem 1 — The Chef
**File:** `Guidance/CAFÉ ATHENA - GEM INSTRUCTIONS.md`  
**Current Version:** 3.3

| Version | Date | Changes |
|---------|------|---------|
| v3.0 | — | Initial release. Mode invoker system, consolidated format standard. |
| v3.1 | — | Added Stop Point Protocol, Troubleshooting Guide, Bad Output Examples, Decision Protocol, mode-specific completion criteria. |
| v3.2 | — | Updated SYSTEM ASSETS (removed 00-01 structure file). Added INDEX UPDATE PROTOCOL with mandatory INDEX DATA block format. Added chapter prefix validation to Stop Points. |
| v3.3 | — | Added Table of Contents, standardized STOP language, streamlined INDEX UPDATE PROTOCOL, clarified Mode 1 completion checklist, consolidated quality guidance, tightened cross-references. |

---

## Claude Desktop Agent
**File:** `Claude-Desktop/PROJECT_INSTRUCTIONS.md`  
**Current Version:** 1.1

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | — | Initial release. Three-mode system prompt for Claude Desktop / Claude.ai Projects. |
| v1.1 | 2026-03-12 | Full audit pass (see `Claude-Desktop/CD-Audit.md` for details). Key changes: replaced keyword-based mode detection with intent classification; added Mode 2 INDEX VERIFICATION block; added multi-intent request handler; added folio index protocol to Mode 3; added persona tone directives per mode; added version header; fixed line-count discrepancy in COPY_PASTE_TEMPLATE.md. |

---

## Claude Code Sub-Agent — Café Athena Chef
**File:** `.claude/agents/Cafe Athena Chef.agent.md`  
**Current Version:** 1.1  
**Status:** Canonical master — update this first.

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | — | Initial release. Full three-mode system prompt adapted for Claude Code sub-agent with Read/Write/Edit/Grep/Glob/Bash tools. |
| v1.1 | 2026-04 | Added `version:` field to YAML frontmatter. Fixed `.claude/settings.local.json` paths to be project-root-relative. Fixed workflow files (`.agents/workflows/`) to use Claude Code tool names instead of Desktop Commander MCP names. Added canonical master designation and cross-references to secondary surfaces. |

---

## Gemini Gem 2 — The Visual Director
**File:** `Guidance/CAFÉ ATHENA - HERO IMAGE GEM INSTRUCTIONS.md`  
**Current Version:** 1.0

| Version | Date | Changes |
|---------|------|---------|
| v1.0 | — | Initial release. Purpose-limited to hero image generation. Defines core aesthetic (warm editorial food photography), output constraints (one image, 16:9, ¾ overhead angle), and quality benchmarks. |

---

## Notes

- Dates marked `—` are not recorded in the original files. Use `git log` to approximate if needed.
- When updating any agent, bump the version number in both the file header and this changelog.
- The Visual Director (Gem 2) is independent of the culinary agent system prompt — it does not need to stay in sync with the master.
