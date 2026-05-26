# Café Athena - Project Status & Active Context

Last Updated: 2026-05-26 (session 33)

> **Scope:** This file holds *only* active work — in-progress folios, bugs being fixed, items deferred from the last session. Future ideas live in `IDEAS.md` and are promoted here when started. Per-recipe state (hero image, format audit, deploy flags) lives in `recipes.json` — run `python3 scripts/audit.py --status` or `/sync-registry` for live rollups.

---

## 🎯 Active Development

In-progress folios. Completed items are tracked via `recipes.json` and `git log`.

| Folio | Title | Status | Notes |
| :--- | :--- | :--- | :--- |
| 08-13 | Glacé Carrots | ✅ Complete | Folio, hero image, and ref image (08-13a) all done |
| 14-01 | The Garnish Arsenal (The Power of Finish) | Pending | Ch. 14 first folio; Part IV now active |

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
| ~~Resolve 09-03 (replace with Lemon Blackberry Tart)~~ | ✓ Done 2026-05-19 — new folio written, registry updated | — | 2026-05-15 |
| ~~12-24 Foundation Curd (new folio)~~ | ✓ Done 2026-05-19 — folio written, registered in recipes.json | — | 2026-05-19 |
| ~~Verify Chef agent uses new family/course fields~~ | ✓ Done 2026-05-19 — confirmed on 08-11, `family: Brassica`, `course: Side` written correctly | — | 2026-05-19 |
| ~~Site IA Project Brief~~ | ✓ Done 2026-05-20 — all phases complete (1–5c). Brief deleted. 5d deferred to The Expo. | — | 2026-05-18 |
| ~~12-25 Fleur de Sel Crumble~~ | ✓ Done 2026-05-20 — content corrected, folio fixed | — | 2026-05-19 |
| ~~09-09 Crème Brûlée~~ | ✓ Done 2026-05-20 — folio written and registered | — | 2026-05-19 |
| ~~12-11 update — lemon crème pâtissière variant~~ | ✓ Done 2026-05-26 — lemon variant written, ref images tagged (12-11a, 12-11b), keywords updated, deployed v1.1 | — | 2026-05-19 |
| PB tart crust — 12-02 variant vs. new 12-25 folio | Decision pending: does PB tart crust earn its own folio (12-25) or become Variant 7 in 12-02? | Decision required before writing | 2026-05-19 |
| Re-audit all recipes vs v3.2 template | `audit.py` updated for v3.2. Full re-audit pending to catch any remaining order violations. | Run `python3 scripts/audit.py --scan-only` | 2026-05-15 |
| Fix-It remediation plan | For recipes flagged non-conformant, bring to v3.2 format | Blocked on re-audit | 2026-05-15 |
| Finish pipeline on 12-02, 12-15, 12-22 | 3 recipes with genuine outstanding stages (audit and/or glossary). | `/pipeline` or manual | 2026-05-18 |
| Architecture review — Ch. 1 & Ch. 12 placement | Audit Ch. 1 (The Lab) and Ch. 12 (Les Fonds) folios against Escoffier-style function logic. Some garnish/vessel elements may belong in Ch. 14 (Plating) once Part IV is built out. | Blocked on Ch. 14 scaffold | 2026-05-25 |
| ~~Agent verbosity — lead with recommendation~~ | ✓ Done 2026-05-25 — Chef agent v1.12: Mode 1 reordered (recommendation first), Steelman conditional, confirmation echo scoped. PROJECT_INSTRUCTIONS.md updated. CLAUDE.md propagation rule fixed to edit files directly. | — | 2026-05-25 |
