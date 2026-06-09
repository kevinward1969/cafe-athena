# Café Athena - Project Status & Active Context

Last Updated: 2026-06-08 (session 39)

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
| ~~Resolve 09-03 (replace with Lemon Blackberry Tart)~~ | ✓ Done 2026-05-19 — new folio written, registry updated | — | 2026-05-15 |
| ~~12-24 → 12-16 Foundation Curd (new folio, renumbered)~~ | ✓ Done 2026-05-19 (written); renumbered 2026-05-26 — folio, hero image, built file, registry all updated. Deployed. | — | 2026-05-19 |
| ~~Verify Chef agent uses new family/course fields~~ | ✓ Done 2026-05-19 — confirmed on 08-11, `family: Brassica`, `course: Side` written correctly | — | 2026-05-19 |
| ~~Site IA Project Brief~~ | ✓ Done 2026-05-20 — all phases complete (1–5c). Brief deleted. 5d deferred to The Expo. | — | 2026-05-18 |
| ~~12-25 Fleur de Sel Crumble~~ | ✓ Done 2026-05-20 — content corrected, folio fixed | — | 2026-05-19 |
| ~~09-09 Crème Brûlée~~ | ✓ Done 2026-05-20 — folio written and registered | — | 2026-05-19 |
| ~~12-11 update — lemon crème pâtissière variant~~ | ✓ Done 2026-05-26 — lemon variant written, ref images (12-11a, 12-11b) placed and rendered, keywords updated, deployed v1.1. Ref image rendering bug also fixed site-wide (08-13). | — | 2026-05-19 |
| ~~PB tart crust — 12-02 variant vs. new 12-25 folio~~ | ✓ Done 2026-05-26 — added as Variant 7 (Peanut Butter Shell) in 12-02. Folio renamed to Seven Variants throughout. Deployed v1.3. | — | 2026-05-19 |
| Re-audit all recipes vs v3.2 template | `audit.py` updated for v3.2. Full re-audit pending. **Blocked until CONTENT_PLAN.md is complete** (Ch 5 +8, Ch 6 +6 still needed) — no point auditing a corpus still in flux. | Blocked on content plan | 2026-05-15 |
| Fix-It remediation plan | For recipes flagged non-conformant, bring to v3.2 format | Blocked on re-audit | 2026-05-15 |
| ~~v3.2 section split — Chef's Notes / Variations~~ | ✓ Done 2026-06-08 — all 65 combined headings split across 171 folios. audit.py updated with auto-fix handler. Taxonomy extended with Turkish, Lebanese, Persian, Moroccan, North African, Southern, Cajun. 165 clean, 6 non-critical issues remain (keywords_count, section_order). **Site built files need regeneration + deploy.** | — | 2026-06-08 |
| ~~Finish pipeline on 12-02, 12-15, 12-22~~ | ✓ Done 2026-05-26 — formatAudit and glossaryPull complete on all three. 11 new glossary terms added (A, B, D, F, P, S, W). 12-15 section header fixed (Chef's Notes / Variations → Chef's Notes). All deployed v1.1. | — | 2026-05-18 |
| ~~Architecture review — Ch. 1 & Ch. 12 placement~~ | ✓ Done 2026-05-26 — Ch. 1 clean. 12-16 Sesame Tuile Cylinders moved to Ch. 9 as 09-13 (Sesame Florentine Cylinders with Miso-Orange Dark Chocolate Ganache). Renamed, re-categorized (Confection/Dessert), 12-24 → 12-16 (Foundation Curd). All deployed. | — | 2026-05-25 |
| ~~Agent verbosity — lead with recommendation~~ | ✓ Done 2026-05-25 — Chef agent v1.12: Mode 1 reordered (recommendation first), Steelman conditional, confirmation echo scoped. PROJECT_INSTRUCTIONS.md updated. CLAUDE.md propagation rule fixed to edit files directly. | — | 2026-05-25 |
