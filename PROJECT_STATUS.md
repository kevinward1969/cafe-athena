# Café Athena - Project Status & Active Context

Last Updated: 2026-06-09 (session 44)

> **Scope:** This file holds *only* active work — in-progress folios, bugs being fixed, items deferred from the last session. Future ideas live in `IDEAS.md` and are promoted here when started. Per-recipe state (hero image, format audit, deploy flags) lives in `recipes.json` — run `python3 scripts/audit.py --status` or `/sync-registry` for live rollups.

---

## 🎯 Active Development

In-progress folios. Completed items are tracked via `recipes.json` and `git log`.

| Folio | Title | Status | Notes |
| :--- | :--- | :--- | :--- |
| *(none)* | — | — | — |

---

## 🐛 Active Issues / Fixes

Bugs, regressions, or registry drift being worked now.

| Issue | Context | Owner | Since |
| :--- | :--- | :--- | :--- |
| *(none)* | — | — | — |

---

## 🔖 Pending from Prior Sessions

Items deferred from earlier sessions. Session handoff writes here. Resolve or carry forward each session.

| Item | Context | Blocking Condition | Since |
| :--- | :--- | :--- | :--- |
| Re-audit all recipes vs v3.2 template | `audit.py` updated for v3.2. Full re-audit pending. **Blocked until CONTENT_PLAN.md is complete** (Ch 5 +8, Ch 6 +6 still needed) — no point auditing a corpus still in flux. | Blocked on content plan | 2026-05-15 |
| Fix-It remediation plan | For recipes flagged non-conformant, bring to v3.2 format | Blocked on re-audit | 2026-05-15 |
| Regenerate `banner-brigade.webp` | Current image is stock photo style with visible faces — violates Visual Director spec. Use Mode 2 brief. | Awaiting Gemini session | 2026-06-09 |
| Regenerate `section-glossary.webp` | Current image contains AI-hallucinated legible fake text in open book. Use Mode 3 brief. | Awaiting Gemini session | 2026-06-09 |
| Attach reference images to Gemini Gem 2 (Visual Director) | Attach 5 recipe heroes + 2 banner/section references in Gemini UI. Paste updated `CAFÉ ATHENA - VISUAL DIRECTOR GEM INSTRUCTIONS.md` v2.0. | Kevin action | 2026-06-09 |
