# Café Athena - Project Status & Active Context

Last Updated: 2026-05-18 (session 14)

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
