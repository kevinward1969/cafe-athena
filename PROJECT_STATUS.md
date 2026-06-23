# Café Athena - Project Status & Active Context

Last Updated: 2026-06-22 (session 59)

> **Scope:** This file holds *only* active work — in-progress folios, bugs being fixed, items deferred from the last session. Future ideas live in `The Manual/IDEAS.md` and are promoted here when started. Per-recipe state (hero image, format audit, deploy flags) lives in `The Manual/recipes.json` — run `python3 scripts/audit.py --status` or `/sync-registry` for live rollups.

---

## 🎯 Active Development

In-progress folios. Completed items are tracked via `The Manual/recipes.json` and `git log`.

| Folio | Title | Status | Notes |
| :--- | :--- | :--- | :--- |
| 06-07 | Chicken and Dumplings — social content | ✅ Complete | Published as Facebook reel 2026-06-22. First multi-tool HF production run — all stages done. Assets in `Marketing/Social/Recipes/06-07/`. |

---

## 🐛 Active Issues / Fixes

Bugs, regressions, or registry drift being worked now.

| Issue | Context | Owner | Since |
| :--- | :--- | :--- | :--- |
| Domain change | **Complete (2026-06-22).** All code, config, agent, skill, command, and marketing files updated. FastComet path updated to `~/Public_HTML/cafeathenathemanual`. Pending: Kevin to redeploy site (`bash site/scripts/deploy.sh`), update DNS/cPanel, and paste updated agent instructions into Claude Desktop Brand Manager and Technical Director projects. | Kevin / Technical Director | 2026-06-21 |

---

## 🔖 Pending from Prior Sessions

Items deferred from earlier sessions. Session handoff writes here. Resolve or carry forward each session.

| Item | Context | Blocking Condition | Since |
| :--- | :--- | :--- | :--- |
| AI setup health audit | Context degradation and repeated errors observed this session. `context-window-management` and `claude-code-guide` skills installed. `everything-claude-code:context-budget` and `harness-optimizer` available. | Start fresh session; run context-budget + harness-optimizer to audit full setup | 2026-06-14 |
| HF tool integration | Integration entry point: `hugging_face/Projects/cafe-athena/hugging-face-agent.md`. **Integration test complete (2026-06-22):** All tools confirmed working in production run. Wan2.2 I2V (zerogpu-aoti fast) is the primary animated still tool — AUDIT-008 passed. ZONOS2 is preferred TTS; Qwen3-TTS is backup. **Remaining gaps:** ZONOS2 formal integration incomplete (no standalone Tool Registry entry, no workflow section, no audit at `hugging_face/audit/zonos2-audit.md`). FLUX and Ideogram audits (AUDIT-004, AUDIT-005 by original numbering) still pending. | Next: Stage 4 video assembly (06-07), then formally integrate ZONOS2 per skill-implementation.md. | 2026-06-20 |
| Install pm-skills in Claude Desktop | pm-skills plugins installed at user scope (~/.claude) — already globally available. Confirm they appear in Claude Desktop. | Open Claude Desktop and verify plugins are active | 2026-06-14 |
| Social account setup — Instagram, Pinterest, YouTube | Briefs in `Marketing/Social/`, templates in `Marketing/Social/Templates/`. Kevin is handling account creation manually using Claude (Chrome) for guidance. | No blocking condition — Kevin-driven | 2026-06-16 |

---

## 🎯 Pending New Work (added 2026-06-22)

| Item | Notes |
| :--- | :--- |
| Google Analytics integration | Add GA4 to the Astro site so the project can eventually use Google Ads. Technical Director task — add tracking script to site layout. |
| Social media video/reel skill | Write a `/social-video` skill (or equivalent) documenting the full workflow: Zonos2 TTS → Adobe Firefly Kling 3.0 Omni (video) → Adobe Express (assembly). Based on 06-07 production run pattern. Brand Manager owns; Technical Director builds the skill file. |

---

## 📐 Strategic Context & Learnings

- **Canonical social video workflow (2026-06-22):** Voiceover: ZONOS2 → Video: Adobe Firefly Kling 3.0 Omni (720p, 9:16, 15s, seed 1847, reference image, 300 credits) → Assembly: Adobe Express. WanWeb/FFmpeg/HF video tools are backup only. Brand Manager owns production. Confirmed working on 06-07 Chicken and Dumplings Facebook reel.
- **Plugin scope:** Plugins installed via `claude plugin install` at user scope are stored in `~/.claude/plugins/` and are shared across Claude Code CLI, Claude Desktop, and claude.ai. No separate Desktop install needed.
- **antigravity-awesome-skills:** Registered as a marketplace but individual plugins lack `plugin.json` manifests — cannot install via `claude plugin install`. Skills must be copied manually to `~/.claude/skills/`. Done for `context-window-management` and `claude-code-guide`.
- **Context degradation:** This session showed clear signs of context-length-related errors (repeated wrong claims, incomplete fixes). Handoff triggered early. Next session should start with `/everything-claude-code:context-budget` audit before any substantive work.
- **Memory system:** Feedback memory `feedback_verify_before_stating.md` added — verify before stating claims about systems, platforms, or fix completeness.
- **Expo pipeline: live and operational (2026-06-16).** Phases 1–8 complete. Content model, routing, cross-linking, pipeline scripts, inline images, search/SEO, tags, categories, and validation all built and verified (262 pages). Operational reference: Workflow E in `Guidance/Cafe-Athena-Workflow-Guide.md`. First real post pending Chef delivery of 06-12 Quail walkthrough or Ortolan essay.
