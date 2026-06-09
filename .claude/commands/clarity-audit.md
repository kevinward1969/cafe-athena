---
description: Audits a recipe folio or all recipes in a chapter for instructional clarity issues — forward references, ambiguous cross-section parentheticals, method ingredients not listed, and multi-action steps. Stop point if issues found. Usage: /clarity-audit [id] or /clarity-audit [Chapter N]
---

# Clarity Audit Workflow

Invoked with: `/clarity-audit [id or Chapter N]`

Examples:
- `/clarity-audit 07-04`
- `/clarity-audit Chapter 7`

---

## Single Recipe

1. Invoke the **Recipe Clarity Auditor** agent on the folio file matching the given ID.
2. Display the full findings report.
3. **If issues found:** STOP. Do not proceed with any other work until every issue is resolved or explicitly excepted by the user.
4. **If clean:** report `✅ Clarity audit passed — [id]` and update `clarityAudit: true` in `recipes.json`.

---

## Chapter

1. Use Glob to find all `*.md` files under `The Manual/Chapter [N] - */`.
2. For each file, invoke the **Recipe Clarity Auditor** agent.
3. Collect all findings across the chapter.
4. Report a summary:

```
CLARITY AUDIT — Chapter [N]
───────────────────────────
Passed:  N recipes
Issues:  N recipes
  - [id] — [title]: [finding count] issue(s)
  - ...
───────────────────────────
```

5. **If any issues found:** STOP. Display full findings for each recipe with issues. Do not mark any as passed until all issues in the chapter are resolved or excepted.
6. **If all clean:** update `clarityAudit: true` for all entries in `recipes.json` and report `✅ Clarity audit passed — Chapter [N] ([N] recipes)`.
