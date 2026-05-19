# Café Athena - Project Status & Active Context

Last Updated: 2026-05-18 (session 18)

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
| Resolve 09-03 (replace with Lemon Blackberry Tart) | 09-03 is a duplicate of 09-02 cookie recipe. Replacement planned: Lemon Blackberry Tart referencing 12-02 (shell) and pending 12-24 Foundation Curd. Deferred until Site IA Phase 2 complete. | Site IA Phase 2 | 2026-05-15 |
| Re-audit all recipes vs v3.2 template | `audit.py` updated for v3.2 (Ingredients before Mise, split Variations/Chef's Notes, broadened combined-heading detection). 12-21, 12-23, 09-06 fixed. Full re-audit of all 152 recipes still pending to catch any remaining order violations. | Run `python3 scripts/audit.py --scan-only` | 2026-05-15 |
| Fix-It remediation plan | For recipes flagged non-conformant, plan to bring to v3.2 format | Re-audit complete | 2026-05-15 |
| `/pipeline [id]` slash command | Built and validated on 09-06 (audit-only) and 12-21 (full run incl. glossary + deploy). Ready for first new recipe test. | Awaiting new recipe | 2026-05-18 |
| Finish pipeline on 12-02, 12-15, 12-22 | 3 recipes with genuine outstanding stages (audit and/or glossary). | `/pipeline` or manual | 2026-05-18 |
| Re-attach Recipe-Format-Standard.md v3.2 in Claude Desktop | Ingredients before Mise en Place; Variations = significant departures only; Chef's Notes = minor options. Must re-attach as file attachment in Claude Desktop project. | Manual action required | 2026-05-18 |
| Site IA & Taxonomy Upgrade — Phase 4 | Phases 1–3 complete. Next: update `prepare-content.py` to extract `family` and `course` → Astro frontmatter; update `content.config.ts` schema. Full spec in `PROJECT_BRIEF_SITE_IA.md`. | — | 2026-05-18 |
