---
name: project-health
description: Full project health audit for Café Athena. Checks registry integrity, pipeline flag logic, image integrity, deploy currency, search index staleness, doc alignment, and Expo registry. Produces a prioritized CRITICAL/MODERATE/MINOR report with auto-fix options. Invoke with /project-health or when something feels off.
---

# Project Health Audit

Invoked with: `/project-health`

Optional scope flags (run full audit if omitted):
- `/project-health registry` — registry and pipeline flags only
- `/project-health images` — image integrity only
- `/project-health deploy` — deploy currency + search index
- `/project-health docs` — doc alignment only
- `/project-health agents` — agent drift only (delegates to `/audit-agent-instructions`)
- `/project-health --full` — include Phase 5E (CONTENT_PLAN counts) and Phase 5F (Current Version Index), which require reading large additional files and are skipped by default

---

## Field Conventions (read before running checks)

**`stages.*` fields are canonical.** recipes.json entries have both top-level fields (`heroImage`, `heroImageOptimized`) and a `stages` block (`stages.heroImage`, `stages.heroImageOptimized`). The `stages` block is the source of truth. Top-level fields are legacy and may be stale. All flag logic in this audit reads from `stages.*`. If a top-level field contradicts its `stages` counterpart, that is a MODERATE alignment issue — fix the top-level field to match `stages`, not the other way around.

---

## Phase 0 — Load State

Read these files in parallel before any checks:

- `The Manual/recipes.json` — full recipe registry
- `Expo/expo.json` — full Expo registry
- `README.md` — doc alignment reference
- `PROJECT_STATUS.md` — last updated date

Collect:
- `registered_ids` — all `id` values in recipes.json
- `expo_registered_ids` — all `id` values in expo.json
- `deployed_ids` — all entries where `stages.deployed: true`
- `needs_deploy_ids` — all entries where `stages.deployed: false` AND `stages.heroImage: true` AND `stages.formatAudit: true`

---

## Phase 1 — Registry Integrity

### 1A — ID Format Validation

Before any file-matching, validate every id in recipes.json against the pattern `/^\d{2}-\d{2}$/`.

- **CRITICAL** if any entry has a non-standard id (e.g., `07-10_2`, `12-25b`, `foo`) — these will cause prepare-content.py and sync tools to misfire. Flag the id, its title, and the fact that it has no valid corresponding folio file.

### 1B — Manual ↔ recipes.json Sync

```bash
# List all folio files in The Manual
find "The Manual" -name "*.md" | grep -E "/[0-9]{2}-[0-9]{2}[^/]*\.md" | sort
```

For each file found:
- Extract the `XX-YY` id from the filename
- Check if that id exists in `registered_ids`
- **CRITICAL** if a folio file exists but has no registry entry

For each entry in `registered_ids` (standard-format ids only):
- Check if a corresponding folio file exists under `The Manual/Chapter N*/`
- **CRITICAL** if a registry entry has no corresponding folio file

### 1C — Expo Posts ↔ expo.json Sync

```bash
find "Expo/Posts" -name "*.md" | sort
```

- **MODERATE** if a post file has no entry in expo.json
- **MODERATE** if an expo.json entry has no corresponding post file

---

## Phase 2 — Pipeline Flag Logic

All checks read from `stages.*` fields. For each entry in recipes.json:

| Condition | Severity | Issue |
|---|---|---|
| `stages.deployed: true` AND `stages.heroImage: false` | CRITICAL | Deployed without hero image |
| `stages.deployed: true` AND `stages.formatAudit: false` | CRITICAL | Deployed with failed/skipped format audit |
| `stages.deployed: true` AND `stages.glossaryPull: false` | MODERATE | Deployed without glossary terms merged |
| `stages.deployed: true` AND `stages.clarityAudit: false` | MODERATE | Deployed without clarity audit |
| `stages.heroImage: true` AND `stages.heroImageOptimized: false` | MODERATE | Image confirmed but optimized flag not set |
| Top-level `heroImage` contradicts `stages.heroImage` | MODERATE | Stale top-level field — set top-level to match stages |
| Top-level `heroImageOptimized` contradicts `stages.heroImageOptimized` | MODERATE | Stale top-level field — set top-level to match stages |
| `stages.keywordPull: true` but folio has no `## Keywords` section | MODERATE | Flag set but section missing from source |
| `stages.glossaryPull: true` but folio has no `## Glossary` section | MODERATE | Flag set but section missing from source |
| `stages.clarityAudit: true` AND `stages.formatAudit: false` | MINOR | Clarity audited before format audit (ordering issue) |

**Note on CRITICAL vs MODERATE overlap:** The `deployed: false + heroImage/formatAudit missing` states (Phase 4A) are the mirror of these violations — same category, different direction. Cross-reference rather than duplicate in the report.

To check keyword/glossary sections, run:

```bash
grep -rL "## Keywords" "The Manual/Chapter"* --include="*.md"
grep -rL "## Glossary" "The Manual/Chapter"* --include="*.md"
```

Then cross-reference against entries with those stage flags set true.

---

## Phase 3 — Image Integrity

### 3A — Hero Image Files

For each entry where `stages.heroImage: true` OR `stages.heroImageOptimized: true`:

```bash
ls "site/public/images/[id].webp" 2>/dev/null
```

- **CRITICAL** if `stages.heroImage: true` but `site/public/images/[id].webp` is missing
- **CRITICAL** if `stages.heroImageOptimized: true` but file is missing

### 3B — Orphaned Images

```bash
ls site/public/images/*.webp | grep -E "[0-9]{2}-[0-9]{2}[a-z]?\.webp"
```

For each image file found, strip any trailing letter suffix to get the base id, then check if that id exists in recipes.json.
- **MINOR** if an image file has no corresponding registry entry (orphan — may be safe to delete, confirm before acting)

### 3C — Leftover Manual Images

```bash
find "The Manual" \( -name "*.webp" -o -name "*.png" \) | grep -E "[0-9]{2}-[0-9]{2}"
```

For each file found, check if the corresponding entry has `stages.heroImageOptimized: true`.
- **MODERATE** if `stages.heroImageOptimized: true` but source image still exists in The Manual (cleanup was missed)

---

## Phase 4 — Deploy Currency

### 4A — Recipes Ready to Deploy

`needs_deploy_ids` (from Phase 0): entries where `stages.deployed: false` AND `stages.heroImage: true` AND `stages.formatAudit: true`.

- **CRITICAL** if any such entry exists — pipeline-complete recipe sitting undeployed.

### 4B — Local Build State

```bash
cat site/dist/_pagefind/pagefind-entry.json 2>/dev/null
ls site/src/content/recipes/ | wc -l
```

If pagefind-entry.json exists, extract `page_count` and compare to content file count.
- **MODERATE** if `page_count` differs significantly from content file count (local index stale relative to local build)
- **MINOR** if `site/dist/` doesn't exist at all (no local build — run `npm run build` before next deploy)

### 4C — Post-Deploy Content Changes

```bash
# Find the last commit mentioning deploy
git log --oneline --grep="deploy" -5

# Files changed in The Manual after that commit
git diff [last-deploy-sha]..HEAD --name-only | grep "The Manual/Chapter"
```

- **MODERATE** if folio files were modified after the last deploy commit (live site does not reflect these changes)

---

## Phase 5 — Doc Alignment

### 5A — README Entry Count

Read `README.md`. Find `**Status:** Active — N entries`.
Compare N against `len(recipes.json entries)`.
- **MODERATE** if count is wrong

### 5B — README Last Updated

Check the `**Last Updated:**` field.
- **MINOR** if the month/year is more than 2 months ago

### 5C — README Route Table

Verify these routes are present in the README route table:
`/`, `/academy`, `/brigade`, `/larder`, `/expo`, `/categories`, `/glossary`, `/search`, `/about`
- **MINOR** for each missing route

### 5D — README Commands Table

```bash
ls .claude/commands/*.md | sed 's|.*/||; s|\.md||'
```

- **MINOR** if a command file exists but is absent from the README commands table
- **MINOR** if the README table lists a command with no corresponding `.md` file

### 5E — CONTENT_PLAN Counts *(--full only)*

Read `The Manual/CONTENT_PLAN.md`. For each chapter with a listed recipe count, compare against actual count of entries in recipes.json for that chapter.
- **MINOR** if counts are misaligned

### 5F — Current Version Index *(--full only)*

Read `The Manual/Cafe-Athena-The-Manual-Current-Version.md`. For each entry in recipes.json, check that its title appears under the correct chapter heading.
- **MODERATE** if a registered recipe is missing from the index

---

## Phase 6 — Agent Drift

Delegate entirely to the `audit-agent-instructions` skill. Run it inline and include its output in the report.

Skip this phase unless the scope is `agents` or unscoped (full audit).

---

## Phase 7 — Expo Registry

### 7A — Stage Flag Logic

For each entry in expo.json:
- `deployed: true` AND `formatAudit: false` → **MODERATE**
- `deployed: true` AND `keywordPull: false` → **MINOR**

### 7B — Tags Sanity

For each Expo post file, check frontmatter for a non-empty `tags[]` array.
- **MINOR** if `tags` is missing or empty and `keywordPull: true`

---

## Phase 8 — Report

Run all applicable phases before producing any output. Then produce:

```
Café Athena — Project Health Audit
Date: YYYY-MM-DD
═══════════════════════════════════════════════════════

Checked: N recipes | N expo posts | N images
Issues:  N critical / N moderate / N minor

━━━ CRITICAL ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[id] — [title]
Issue: [description]
Fix:   [exact action]

━━━ MODERATE ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[same format]

━━━ MINOR ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[same format]

━━━ CLEAN ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[list phases that passed with no issues]

━━━ SKIPPED ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[phases skipped and why — scope flag or --full required]

━━━ RECOMMENDED ACTIONS ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. [highest-priority action]
2. ...
```

---

## Phase 9 — Apply Fixes (optional)

If the user confirms, apply in this order:

**Auto-fixable (apply directly):**
1. Delete invalid-format registry entries (confirm title before deleting)
2. Align stale top-level `heroImage`/`heroImageOptimized` fields to match `stages.*`
3. README entry count and date corrections
4. README route/command table gaps
5. expo.json flag corrections
6. Delete The Manual images where `stages.heroImageOptimized: true` (cleanup)

**Requires user action:**
- Missing folio files — can't be created automatically
- Missing hero images — user must generate and place
- Format/glossary/clarity audits — run the relevant slash command per recipe
- Agent secondary surface updates — require Claude Desktop paste
- Deploy — always confirm before running `bash site/scripts/deploy.sh`

---

## Audit Rules

- **`stages.*` is canonical.** Never infer state from top-level fields. Never correct a `stages` flag to match a stale top-level field.
- **Never reset a `true` stage flag to `false`** — flags are append-only unless explicitly instructed.
- **Flag, don't assume** — if a check is ambiguous, report it as MINOR with the raw finding.
- **One report, one pass** — complete all phases before producing any output.
- **Deploy requires explicit confirmation** — even for CRITICAL deploy-ready entries, always prompt before running `deploy.sh`.
- **Agent drift is advisory** — never blocks other auto-fixes.
- **5E and 5F are opt-in** — skip unless `--full` flag is present; note them in the SKIPPED section.
