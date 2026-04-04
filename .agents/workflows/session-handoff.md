---
description: Updates PROJECT_STATUS.md with session progress, stages all changes, and commits to git with a descriptive message.
---

# Session Handoff Workflow

Invoked when the user says "Handoff," "Close out," "Goodbye," or `/session-handoff`.

---

## Phase 1 — Read Current State

1. Read `PROJECT_STATUS.md` using the Read tool to load the current active development, pending items, and strategic context.
2. Confirm which folios, recipes, or workflows were touched during this session.

---

## Phase 2 — Update PROJECT_STATUS.md

Update the following sections in place:

1. **Active Development table**: Change the status of any folio worked on this session (e.g., `In Progress` → `Completed`, or add `Pending:` notes for deferred items).
2. **Pending Items**: Document open questions or deferred decisions that need to be picked up next session.
3. **On the Horizon**: Append any new concepts, upcoming recipes, or improvement ideas that surfaced during the session.
4. **Strategic Context & Learnings**: Add any new technical learnings, discovered constraints, or scaling notes uncovered this session.

Write the updated file back to `PROJECT_STATUS.md` using the Write tool.

---

## Phase 3 — Git Commit *(STOP POINT)*

1. Run `git status` (via Bash) to show the user all staged and unstaged changes.
2. Present the list of changed files to the user and ask:
   > *"Ready to commit all changes? Proposed commit message: `Handoff: [brief description of session work]` — adjust or confirm?"*
3. **WAIT** for the user to confirm the commit message.

---

## Phase 4 — Stage, Commit, and Push

1. Run `git status` (via Bash) to get the list of modified files.
2. Stage each modified file by name using `git add [file]` — do NOT use `git add .` as it may capture unintended files.
3. Run `git commit -m "[confirmed commit message]"` (via Bash).
4. If the user wants to push, run `git push`.
5. Confirm success and output the commit hash.

---

## Phase 5 — Formal Handoff Summary

Output a formal handoff summary for the "Next Chef" — exactly **3 bullet points**:

- What was completed this session
- What is still in progress or pending
- What to tackle next (top priority)
