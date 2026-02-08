<!--
Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
Licensed under the MIT License.
-->
---
name: resolve-ci
description: Autonomous loop to resolve merge conflicts and CI failures until PR merges
allowed-tools: [Bash, Read, Grep, Glob, Edit, Write, AskUserQuestion]
---

# /resolve-ci - Autonomous Conflict and CI Failure Resolution

## Purpose

Autonomously resolve merge conflicts and CI failures until PR merges, then clean up workspace.

---

## Workflow

Call monitor-pr.py. It checks prerequisites and returns status codes.

### Prerequisites Checked by monitor-pr.py

The script validates:
1. PR is marked ready (not draft) - `STATUS:NEEDS_READY` if draft
2. PR is finalized (title doesn't contain `[WIP]`) - `STATUS:NEEDS_FINALIZATION` if still WIP

### Status Code: NEEDS_FINALIZATION

When monitor-pr.py returns `STATUS:NEEDS_FINALIZATION`, AI must complete Phase 0:

1. **Read issue file** - understand context from `docs/project/issues/{NUM}-*.md`

2. **Craft PR title** - Remove `[WIP]`, add proper type
   - Format: `Issue #{NUM}: {type}: {description}`
   - Example: `Issue #038: docs: document lazy symlink resolution const_cast`

3. **Write comprehensive PR body**
   - Read issue and plan files
   - Create sections: Summary, Problem, Context, Solution, Benefits, Changes
   - Include implementation details and rationale

4. **Update completed-issues.md:**
   - Add entry to top of current month's table
   - Format: `| #{NUM} | {AUTHOR} | #{PR} | {COMMIT} | {DATE} | {TITLE} |`
   - Use `TBD` for commit hash (will be updated after merge)

5. **Update backlog.md:**
   - Add to "Recent (last 5)" compact list (prepend, remove oldest if >5)
   - Delete from active backlog table
   - Remove from "Quick dependencies" section if referenced

6. **Delete files:**
   - `git rm docs/project/issues/{NUM}-*.md`
   - `git rm docs/project/plans/{NUM}-*.md` (if exists)

7. **Commit and push:**
   - `git add docs/project/backlog.md docs/project/completed-issues.md`
   - `git commit -m "docs: complete issue #{NUM}"`
   - `git push fork {BRANCH}`

8. **Re-run monitor-pr.py** to continue with monitoring

After finalization, monitor-pr.py will proceed to Main Loop.

---

## Main Loop

**Script runs autonomously, returns status when intervention needed:**

```bash
python .claude/skills/resolve-ci/monitor-pr.py --attempt 1
```

**Timeout:** 10 min. Retry up to 6 attempts (1 hour). After attempt 6: inform user "CI still running, check GitHub".

**Status codes:**

**STATUS:FORK_CONFLICT** - conflict with fork/branch, resolve and re-run

**STATUS:BASE_CONFLICT** - conflict with origin/main, resolve and re-run

**STATUS:NEEDS_FIX_CI** - complex CI failure, fix and re-run

**STATUS:AUTO_MERGE_FAILED** - inform user "Check PR settings"

**STATUS:CLEANUP_COMPLETE** - done!

---

## Conflict Resolution

When `STATUS:FORK_CONFLICT` or `STATUS:BASE_CONFLICT`:

1. **List conflicts:**
   ```bash
   git diff --name-only --diff-filter=U
   ```

2. **Read conflicting files** - use Read tool

3. **Resolve conflicts:**
   - Simple (whitespace/imports) → auto-merge with Edit tool
   - Complex → analyze and resolve intelligently
   - Too complex → AskUserQuestion

4. **Complete rebase:**
   ```bash
   git add <conflicting_file>
   git rebase --continue
   git push fork "{BRANCH_NAME}" --force-with-lease
   ```

---

## CI Failure Resolution

When `STATUS:NEEDS_FIX_CI`:

1. **Get CI logs:**
   ```bash
   RUN_ID=$(gh run list --branch "{BRANCH_NAME}" --limit 1 --json databaseId | python -c "import sys, json; print(json.load(sys.stdin)[0]['databaseId'])")
   gh run view $RUN_ID --log-failed > /tmp/ci_logs.txt
   ```

2. **Read logs** - use Read tool on /tmp/ci_logs.txt

3. **Categorize and fix:**
   - Build errors → fix syntax/types/includes
   - Test failures → fix logic bugs
   - Other → analyze and resolve

4. **Verify fix (if build error):**
   ```bash
   cmake --build ../../build/$(basename $PWD) --config Debug --parallel
   ```

5. **Commit and push:**
   ```bash
   git add <file> && git commit -m "fix: ..." && git push fork "{BRANCH_NAME}"
   ```
