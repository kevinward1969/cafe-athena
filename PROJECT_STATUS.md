# Café Athena - Project Status & Active Context

Last Updated: 2026-05-18 (session 15)

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
| Resolve 09-03 (delete or merge into 09-02) | 09-03 is a near-duplicate of 09-02 with only minor keyword/glossary wording differences — no substantive recipe changes justify a separate folio | Decision on whether to delete or fold changes into 09-02 | 2026-05-15 |
| Re-audit all recipes vs new template | Deterministic structural audit — `audit.py` now updated for v3.1 template (split Variations/Chef's Notes). Run `python3 scripts/audit.py --scan-only` to get full picture before remediation. | — | 2026-05-15 |
| Fix-It remediation plan | For recipes flagged non-conformant and not Exceptions, plan to bring them to template format | Re-audit complete | 2026-05-15 |
| Build `/pipeline [id]` slash command | Orchestrates full recipe pipeline from recipes.json state — registry-driven cascade, prompts before deploy. **Image spec:** 1920×1080, WebP at 80% quality, warn if >500KB. Check via `sips` (macOS built-in). Gemini generates → Photoshop removes star watermark + exports → `site/public/images/`. Pipeline checks that folder only (single location). If absent: stop and prompt. CLAUDE.md "Two Image Workflows" section needs simplifying to single-location. Validate on 09-06 then on first new recipe. | In design — build next session | 2026-05-18 |
| Finish pipeline on 09-06, 12-02, 12-15, 12-21, 12-22 | These 5 recipes have genuine outstanding stages (audit and/or glossary). Run supervised once `/pipeline` is built, or manually as needed. | `/pipeline` built or manual | 2026-05-18 |
