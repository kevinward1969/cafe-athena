# Café Athena - Project Status & Active Context

Last Updated: 2026-05-15 (session 11)

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
| Template: define optional Variations section | Update Recipe-Format-Standard.md — scope, placement (before Chef's Notes), optional status; resolve combined `## Chef's Notes / Variations` sections (e.g. 09-05). Version bump + propagation reminder | — | 2026-05-15 |
| Scan recipes for existing Variations content | Find recipes that already contain variation content; consolidate into the new `## Variations` section | Template defined | 2026-05-15 |
| recipes.json: flag files with Variations | Add an indicator showing which recipes contain a Variations section | Scan complete | 2026-05-15 |
| Re-audit all recipes vs new template | Deterministic structural audit (extend audit.py — not Ollama). Ollama only proposes Fix-It vs Exception with rationale for review | Template defined; flip + Variations done first so audit isn't all noise | 2026-05-15 |
| recipes.json: `formatException` field | Record intentional template deviations (collection folios e.g. 10-25) so future audits/scripts skip them declaratively | Classification done | 2026-05-15 |
| Fix-It remediation plan | For recipes flagged non-conformant and not Exceptions, plan to bring them to template format | Classification done | 2026-05-15 |
| Update audit + pipeline tools for new template | audit.py and any pipeline checks must reflect Ingredients-before-Mise + Variations section | Template defined | 2026-05-15 |
