# Café Athena - Project Status & Active Context

Last Updated: 2026-06-25 (session 61)

> **Scope:** This file holds *only* active work — in-progress folios, bugs being fixed, items deferred from the last session. Future ideas live in `The Manual/IDEAS.md` and are promoted here when started. Per-recipe state (hero image, format audit, deploy flags) lives in `The Manual/recipes.json` — run `python3 scripts/audit.py --status` or `/sync-registry` for live rollups.

---

## 🎯 Active Development

In-progress folios. Completed items are tracked via `The Manual/recipes.json` and `git log`.

| Folio | Title | Status | Notes |
| :--- | :--- | :--- | :--- |
| 06-07 | Chicken and Dumplings — social content | ✅ Complete | Published as Facebook reel 2026-06-22. First multi-tool HF production run — all stages done. Assets in `Marketing/Social/Recipes/06-07/`. |
| — | Agent audit & doc alignment | 🟡 In Progress | Writing Director built + wired. TECHNICAL_REFERENCE.md partially updated. Full non-Chef agent audit (Phase 1) not yet run. See Pending. |

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
| Non-Chef agent audit — Phase 1 (read-only) | Session 61 built the Writing Director and updated Brand Manager + CD surface + TECHNICAL_REFERENCE.md (partially). Phase 1 audit still needed: compare Brand Manager canonical (v1.9) vs CD (v1.10) for functional gaps; Technical Director canonical (v1.4) vs CD (v1.5) — CD is AHEAD of canonical (wrong direction); CLAUDE.md Writing Director gaps (Key Files table, Version Bump Rule, Propagation Rule); TECHNICAL_REFERENCE.md Division of Labor table + Writing Director skills section (both still missing); MULTI_AGENT_ARCHITECTURE.md; support docs SYSTEM_OVERVIEW.md, SETUP_GUIDE.md, COPY_PASTE_TEMPLATE.md; README.md. DO NOT TOUCH: Chef, site/, scripts/, cookbook content. | Run in a fresh session — use Phase 1 handoff prompt from session 61. | 2026-06-25 |
| Non-Chef agent audit — Phase 2 (fix pass) | One file at a time, stop for approval between each. Scope defined after Phase 1 report. | Phase 1 complete | 2026-06-25 |
| bio-long.md — P3, P4, P5 repair | P1 and P2 are approved and seeded into writing-exemplars.md. P3 (Samsung Smart Fridge, AI Chef Agent in Gemini, broken final sentence), P4 (grammatically broken), P5 (back-cover pitch tone, not author bio voice) all need Writing Director rewrite. | Invoke Writing Director in a fresh session; read writing-exemplars.md first | 2026-06-25 |
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

- **Writing Director agent (2026-06-25):** New dedicated agent for all prose — author bios, About page, social captions, promotional copy, advertising, email. Three modes: Mode 1 Draft (pre-writing brief + paragraph-gate approval), Mode 2 Edit (diagnosis before rewrite), Mode 3 Standards Audit. Brand Manager v1.9 now redirects all write/draft/create keywords to Writing Director. Writing-exemplars.md seeded with two approved bio paragraphs as the voice baseline. Writing Director is Claude Code only — no CD or Gem surface by design (paragraph gate requires interactive session).
- **Agent version drift detected (2026-06-25):** Technical Director CD surface (`Agents/Claude-Desktop/TECHNICAL_DIRECTOR_INSTRUCTIONS.md`) is at v1.5 while canonical is v1.4 — CD is AHEAD of canonical, which is the wrong direction. Not yet resolved. Phase 1 audit will determine scope of fix. Chef canonical is v1.19, Chef CD is v1.18 — one ported update missing (out of scope for current audit).
- **TECHNICAL_REFERENCE.md partial update (2026-06-25):** Sub-agent surfaces table and Canonical Agent Files expanded to Surface Manifest (with CD and Gem columns) — both completed. Division of Labor table and Writing Director skills section still missing — to be completed in Phase 2 fix pass.

- **Canonical social video workflow (2026-06-22):** Voiceover: ZONOS2 → Video: Adobe Firefly Kling 3.0 Omni (720p, 9:16, 15s, seed 1847, reference image, 300 credits) → Assembly: Adobe Express base template (`https://express.adobe.com/design/userTemplate/urn:aaid:sc:US:7fa31834-9bb7-583f-83e5-49ee4deb977e`). Template reference: `Marketing/Social/Templates/template-social-reel.md`. WanWeb/FFmpeg/HF video tools are backup only. Brand Manager owns production. Confirmed working on 06-07 Chicken and Dumplings Facebook reel.
- **Plugin scope:** Plugins installed via `claude plugin install` at user scope are stored in `~/.claude/plugins/` and are shared across Claude Code CLI, Claude Desktop, and claude.ai. No separate Desktop install needed.
- **antigravity-awesome-skills:** Registered as a marketplace but individual plugins lack `plugin.json` manifests — cannot install via `claude plugin install`. Skills must be copied manually to `~/.claude/skills/`. Done for `context-window-management` and `claude-code-guide`.
- **Context degradation:** Session 59 showed clear signs of context-length-related errors. Next session with heavy workload should start with `/everything-claude-code:context-budget` audit before any substantive work.
- **Expo pipeline: live and operational (2026-06-16).** Phases 1–8 complete. Content model, routing, cross-linking, pipeline scripts, inline images, search/SEO, tags, categories, and validation all built and verified (262 pages). Operational reference: Workflow E in `Guidance/Cafe-Athena-Workflow-Guide.md`. First real post pending Chef delivery of 06-12 Quail walkthrough or Ortolan essay.
- **Author photo strategy (2026-06-23):** Two-asset approach. (1) Personal anchor — Kevin + Athena, Monterey — for About page origin story context. (2) Solo headshot — still needed, specs in `Brand/Author/photo-brief.md` — for press and manuscript bio use.
