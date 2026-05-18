# Café Athena - Project Status & Active Context

Last Updated: 2026-05-18 (session 13)

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
| Propagate Recipe-Format-Standard.md v3.1 to Gemini Gem 1 | Re-attach updated `Guidance/Recipe-Format-Standard.md` in Claude Desktop (done); verify Gemini Gem 1 instructions still reference it correctly | Manual action required | 2026-05-15 |
| Re-audit all recipes vs new template | Deterministic structural audit (extend audit.py — not Ollama). Ollama only proposes Fix-It vs Exception with rationale for review | — | 2026-05-15 |
| Fix-It remediation plan | For recipes flagged non-conformant and not Exceptions, plan to bring them to template format | Re-audit complete | 2026-05-15 |
| Update audit.py for new template | `audit.py` must recognize `## Variations` and `## Chef's Notes` as valid separate sections (currently expects combined heading) | — | 2026-05-15 |
