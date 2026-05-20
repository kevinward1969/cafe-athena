# Café Athena - Project Status & Active Context

Last Updated: 2026-05-19 (session 22)

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
| Resolve 09-03 (replace with Lemon Blackberry Tart) | 09-03 is a duplicate of 09-02 cookie recipe. Replacement planned: Lemon Blackberry Tart referencing 12-02 (shell) and pending 12-24 Foundation Curd. | Awaiting 12-24 Foundation Curd folio | 2026-05-15 |
| 12-24 Foundation Curd (new folio) | Lemon base with citrus variants. Multi-use Ch.12 building block; required before 09-03 tart can be written. | New folio | 2026-05-19 |
| 12-11 update — lemon crème pâtissière variant | Add lemon-flavored variant to existing 12-11 Crème Pâtissière folio. | After 12-24 is written | 2026-05-19 |
| PB tart crust — 12-02 variant vs. new 12-25 folio | Decision pending: does PB tart crust earn its own folio (12-25) or become Variant 7 in 12-02? | Decision required before writing | 2026-05-19 |
| Re-audit all recipes vs v3.2 template | `audit.py` updated for v3.2. Full re-audit of all 152 recipes pending to catch any remaining order violations. | Run `python3 scripts/audit.py --scan-only` | 2026-05-15 |
| Fix-It remediation plan | For recipes flagged non-conformant, bring to v3.2 format | Re-audit complete | 2026-05-15 |
| `/pipeline [id]` slash command | Built and validated. Ready for first new recipe test. | Awaiting new recipe | 2026-05-18 |
| Finish pipeline on 12-02, 12-15, 12-22 | 3 recipes with genuine outstanding stages (audit and/or glossary). | `/pipeline` or manual | 2026-05-18 |
| ~~Verify Chef agent uses new family/course fields~~ | Confirmed on 08-11 — `family: Brassica`, `course: Side` written correctly. | ✓ Done 2026-05-19 | 2026-05-19 |
| Site IA Phase 5 — 5d Collection Pages | 5a–5c complete. 5d (collection pages) deferred to The Expo editorial blog. No blocking condition — awaits Part IV content work. | Part IV / The Expo | 2026-05-19 |
