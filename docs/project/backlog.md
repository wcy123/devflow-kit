# Project Backlog

Issue tracking: `backlog.md` (index) + `issues/NNN-name.md` (detailed files)

---

## Backlog

**Quick dependencies:**
- Example: **#003 relates to #001, #002** - Brief explanation of relationship

See [issue-dependency-analysis.md](issue-dependency-analysis.md) for details.

| # | Title | Pri | Est | Group | Blocked | Files |
|---|-------|-----|-----|-------|---------|-------|
| [#001](issues/001-example-issue.md) | Example Issue Title | M | 1h | Example Group | - | example_file.cpp |

**Legend:**
- **Pri**: Priority (C=Critical, H=High, M=Medium, L=Low)
- **Est**: Estimated time (15m=15 minutes, 1h=1 hour, etc.)
- **Group**: Feature area grouping
- **Blocked**: Issue numbers that must complete first (`-` if none)
- **Files**: Key files affected (see issue file for complete list)

---

## Completed Issues

See **[completed-issues.md](completed-issues.md)** for full archive of all completed issues.

**Recent (last 5):**
- No completed issues yet

---

## Completing an Issue

When implementation is done (code complete, tests pass), update the backlog:

1. Add to completed-issues.md - Add entry to top of current month's table with: #, Author, PR, Commit, Date, Title
2. Update backlog.md - Add to "Recent (last 5)" list in compact format, remove oldest if >5
3. Remove from backlog.md - Delete from active backlog table
4. Delete issue file: `git rm docs/project/issues/042-*.md`
5. Remove from dependencies - Clean up any references in "Quick dependencies" section
6. Commit: `git commit -m "docs: complete issue #042"`

**CRITICAL: PR Title Must Include Issue Number**

When creating PRs for backlog issues, ALWAYS include the issue number in the PR title:

- ✅ CORRECT: `Issue #006: Remove legacy cache_dir system (~220-280 LOC)`
- ❌ WRONG: `Remove legacy cache_dir system (~220-280 LOC)`

This ensures PR is easily linked to the issue and makes tracking easier.

---

## Creating an Issue

1. Copy `issues/TEMPLATE.md` to `issues/NNN-name.md`
2. Fill required sections: Description, Problem, Solution, Evidence
3. Delete empty optional sections (Plans/Sessions/Notes)
4. Add link to backlog.md

Numbering: 001, 002, 003, etc.
