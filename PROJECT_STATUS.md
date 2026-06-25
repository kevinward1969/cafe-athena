# Café Athena - Project Status & Active Context

Last Updated: 2026-06-25 (session 62)

> **Scope:** This file holds *only* active work — in-progress folios, bugs being fixed, items deferred from the last session. Future ideas live in `The Manual/IDEAS.md` and are promoted here when started. Per-recipe state (hero image, format audit, deploy flags) lives in `The Manual/recipes.json` — run `python3 scripts/audit.py --status` or `/sync-registry` for live rollups.

---

## 🎯 Active Development

In-progress folios. Completed items are tracked via `The Manual/recipes.json` and `git log`.

| Folio | Title | Status | Notes |
| :--- | :--- | :--- | :--- |
| 06-07 | Chicken and Dumplings — social content | ✅ Complete | Published as Facebook reel 2026-06-22. First multi-tool HF production run — all stages done. Assets in `Marketing/Social/Recipes/06-07/`. |
| — | Agent audit & doc alignment | ✅ Complete | Phase 1 audit complete (session 62). All gaps closed. See Strategic Context. bio-long.md P3–P5 deferred — separate task, see Pending. |

---

## 🐛 Active Issues / Fixes

*No active issues.*

---

## 🏗️ Infrastructure Reorganization — Complete ✅

All 5 phases complete as of 2026-06-24. See `INFRA_REORG_PLAN.md` for full record.

- README.md — non-technical public scope document
- Docs/TECHNICAL_REFERENCE.md — single technical reference (replaces SKILLS_INDEX)
- CLAUDE.md — slimmed to behavioral contract
- Agent RAG audit — all agents now READ reference docs at session start
- Brand/BRAND_SCOPE.md — concrete project scope definition

---

## 🔖 Pending from Prior Sessions

Items deferred from earlier sessions. Session handoff writes here. Resolve or carry forward each session.

| Item | Context | Blocking Condition | Since |
| :--- | :--- | :--- | :--- |
| AI setup health audit | Context degradation and repeated errors observed 2026-06-14 session. `context-window-management` and `claude-code-guide` skills installed. `everything-claude-code:context-budget` and `harness-optimizer` available. | Start fresh session; run context-budget + harness-optimizer to audit full setup | 2026-06-14 |
| bio-long.md — P3, P4, P5 repair | P1 and P2 are approved and seeded into writing-exemplars.md. P3 violations resolved in session 62 (Samsung → smart refrigerator; AI Chef Agent/Gemini cut; OneNote retained as earned brand name per updated rule). Writing Director drafted P3 but Kevin closed out before approval — start fresh with Writing Director, read writing-exemplars.md and the updated brand-names rule first. | Invoke Writing Director in a dedicated prose session | 2026-06-25 |
| HF tool integration | Integration entry point: `hugging_face/Projects/cafe-athena/hugging-face-agent.md`. **Integration test complete (2026-06-22):** All tools confirmed working in production run. Wan2.2 I2V (zerogpu-aoti fast) is the primary animated still tool — AUDIT-008 passed. ZONOS2 is preferred TTS; Qwen3-TTS is backup. **Remaining gaps:** ZONOS2 formal integration incomplete (no standalone Tool Registry entry, no workflow section, no audit at `hugging_face/audit/zonos2-audit.md`). FLUX and Ideogram audits (AUDIT-004, AUDIT-005 by original numbering) still pending. | Next: formally integrate ZONOS2 per skill-implementation.md, then FLUX/Ideogram audits. | 2026-06-20 |
| Install pm-skills in Claude Desktop | pm-skills plugins installed at user scope (~/.claude) — already globally available. Confirm they appear in Claude Desktop. | Open Claude Desktop and verify plugins are active | 2026-06-14 |
| Social account setup — Pinterest, YouTube | Briefs in `Marketing/Social/`. Instagram profile live (@cafeathena_themanual) — first post pending. Pinterest and YouTube not yet set up. | Kevin-driven — no blocking condition | 2026-06-16 |

---

## 🎯 Pending New Work

| Item | Notes |
| :--- | :--- |
| Google Analytics integration | ✅ Complete (2026-06-22). GA4 property created, tag added to BaseLayout.astro, deployed. Measurement ID: G-F8Y9NNYBNM. |
| Social media video/reel workflow | ✅ Complete (2026-06-22). Documented in `Marketing/Social/Templates/template-social-reel.md`. Zonos2 → Firefly Kling 3.0 Omni → Adobe Express. |
| Domain change | ✅ Complete (2026-06-23). Code, config, agents, skills, DNS, cPanel, and Claude Desktop agent instructions all updated by Kevin. |
| Author photo brief | ✅ Complete (2026-06-23). `Brand/Author/photo-brief.md` written. Personal anchor photo documented. Solo headshot specs defined — see Pending above. |

---

## 📐 Strategic Context & Learnings

- **Phase 1 agent audit complete (2026-06-25, session 62):** All non-Chef agent documentation gaps closed. `TECHNICAL_REFERENCE.md` §8 Division of Labor and §9 Skills Map both updated with Writing Director. `CLAUDE.md` updated: Writing Director in Key Files table, `writing-exemplars.md` in Key Files table, Writing Director in Version Bump Rule list, Writing Director auto-trigger section added. Technical Director canonical bumped to v1.5 (was behind CD at v1.5); CD restored to v1.6 with full ECC skills table (9 entries were missing from compact port). `MULTI_AGENT_ARCHITECTURE.md` updated to v1.4 — agent inventory, architecture diagram, and quick reference all reflect current 11-surface system.
- **Writing Director brand names rule (2026-06-25):** Rule updated from "cut all brand names" to "use brand names well and appropriately." Earned, narrative-serving brand names (e.g., "OneNote" as the specific archiving tool) may stay. Brand names functioning as product placement or tech-industry shorthand (Samsung, Gemini, "AI Chef Agent") get cut. Writing Director bumped to v1.1. Feedback saved to memory.
- **Writing Director agent (2026-06-25):** New dedicated agent for all prose — author bios, About page, social captions, promotional copy, advertising, email. Three modes: Mode 1 Draft (pre-writing brief + paragraph-gate approval), Mode 2 Edit (diagnosis before rewrite), Mode 3 Standards Audit. Brand Manager v1.9 now redirects all write/draft/create keywords to Writing Director. Writing-exemplars.md seeded with two approved bio paragraphs as the voice baseline. Writing Director is Claude Code only — no CD or Gem surface by design (paragraph gate requires interactive session).
- **Canonical social video workflow (2026-06-22):** Voiceover: ZONOS2 → Video: Adobe Firefly Kling 3.0 Omni (720p, 9:16, 15s, seed 1847, reference image, 300 credits) → Assembly: Adobe Express base template (`https://express.adobe.com/design/userTemplate/urn:aaid:sc:US:7fa31834-9bb7-583f-83e5-49ee4deb977e`). Template reference: `Marketing/Social/Templates/template-social-reel.md`. WanWeb/FFmpeg/HF video tools are backup only. Brand Manager owns production. Confirmed working on 06-07 Chicken and Dumplings Facebook reel.
- **Plugin scope:** Plugins installed via `claude plugin install` at user scope are stored in `~/.claude/plugins/` and are shared across Claude Code CLI, Claude Desktop, and claude.ai. No separate Desktop install needed.
- **antigravity-awesome-skills:** Registered as a marketplace but individual plugins lack `plugin.json` manifests — cannot install via `claude plugin install`. Skills must be copied manually to `~/.claude/skills/`. Done for `context-window-management` and `claude-code-guide`.
- **Context degradation:** Session 59 showed clear signs of context-length-related errors. Next session with heavy workload should start with `/everything-claude-code:context-budget` audit before any substantive work.
- **Expo pipeline: live and operational (2026-06-16).** Phases 1–8 complete. Content model, routing, cross-linking, pipeline scripts, inline images, search/SEO, tags, categories, and validation all built and verified (262 pages). Operational reference: Workflow E in `Guidance/Cafe-Athena-Workflow-Guide.md`. First real post pending Chef delivery of 06-12 Quail walkthrough or Ortolan essay.
- **Author photo strategy (2026-06-23):** Two-asset approach. (1) Personal anchor — Kevin + Athena, Monterey — for About page origin story context. (2) Solo headshot — still needed, specs in `Brand/Author/photo-brief.md` — for press and manuscript bio use.
