# Work Log Documentation

This directory contains the backlog system and workflow documentation for tracking work items, issues, and improvements.

---

## Directory Structure

```
docs/
├── README.md                          # This file
├── workflows/                         # Workflow documentation
│   ├── issue-resolution-workflow.md   # Complete issue lifecycle workflow
│   ├── git-workflow.md               # Git branching and commit practices
│   ├── git-workflow-reference.md     # Detailed git workflow reference
│   ├── pr-workflow.md                # Pull request workflow
│   └── build-workflow.md             # Build and test workflow
└── project/                          # Project tracking
    ├── backlog.md                    # Active issues index
    ├── completed-issues.md           # Completed issues archive
    ├── issue-dependency-analysis.md  # Issue dependencies and planning
    ├── CONTRIBUTING.md               # Issue quality guidelines
    ├── issues/                       # Individual issue files
    │   └── TEMPLATE.md               # Issue template
    ├── plans/                        # Implementation plans (optional)
    └── todos/                        # Quick todos (optional)
```

---

## Quick Start

### View Active Work

```bash
# View backlog
cat docs/project/backlog.md

# View completed issues
cat docs/project/completed-issues.md
```

### Create a New Issue

1. Copy the template:
   ```bash
   cp docs/project/issues/TEMPLATE.md docs/project/issues/001-my-issue.md
   ```

2. Fill in the required sections:
   - Description
   - Problem
   - Solution
   - Evidence (optional but recommended)

3. Add to backlog table in `docs/project/backlog.md`

4. Update `docs/project/issue-dependency-analysis.md` if there are dependencies

### Complete an Issue

When implementation is done:

1. Add entry to `completed-issues.md`
2. Update "Recent (last 5)" in `backlog.md`
3. Remove from backlog table in `backlog.md`
4. Delete issue file: `git rm docs/project/issues/NNN-*.md`
5. Commit: `git commit -m "docs: complete issue #NNN"`

See [backlog.md](project/backlog.md) for detailed completion workflow.

---

## Key Workflows

### Issue Resolution Workflow

Complete lifecycle from issue creation to merge:

```
/create-issue → /fix-issue → Author Review → /resolve-ci → Merged
```

See [issue-resolution-workflow.md](workflows/issue-resolution-workflow.md) for details.

### Git Workflow

Feature branch workflow with PR-based development:

```
main → feature/issue-NNN-name → draft PR → review → ready → merged
```

See [git-workflow.md](workflows/git-workflow.md) for details.

---

## File Formats

### Backlog Table Format

| # | Title | Pri | Est | Group | Blocked | Files |
|---|-------|-----|-----|-------|---------|-------|
| [#NNN](issues/NNN-name.md) | Issue Title | M | 1h | Category | - | affected_files.cpp |

**Legend:**
- **Pri**: C=Critical, H=High, M=Medium, L=Low
- **Est**: Time estimate (15m, 1h, 2d, etc.)
- **Group**: Feature area or category
- **Blocked**: Issue numbers that must complete first
- **Files**: Key files affected

### Completed Issues Format

| # | Author | PR | Commit | Date | Title |
|---|--------|----|---------|----|-------|
| #NNN | @username | [#PR](link) | `hash` | YYYY-MM-DD | Brief title |

---

## Best Practices

### Issue Quality

- **Clear problem statement**: What is broken or missing?
- **Concrete solution**: What specifically will be done?
- **Evidence**: Code references, error logs, examples
- **Scope**: Keep issues focused and achievable
- **Dependencies**: Document what blocks or is blocked by this issue

See [CONTRIBUTING.md](project/CONTRIBUTING.md) for detailed guidelines.

### Dependency Management

- Document all dependencies in `issue-dependency-analysis.md`
- Update dependency graph when adding/completing issues
- Use "Blocked" column in backlog table for quick reference
- Consider dependency depth when estimating effort

### Numbering Scheme

- Use 3-digit zero-padded numbers: 001, 002, ..., 099, 100, etc.
- Numbers are sequential and never reused
- Gaps in sequence are normal (from deleted/abandoned issues)

---

## Tools and Automation

### Skills (if available)

If using Claude Code with skills:

- `/create-issue` - Interactive issue discovery and documentation
- `/fix-issue` - Implementation from issue selection to draft PR
- `/resolve-ci` - PR finalization, CI monitoring, and merge

See [issue-resolution-workflow.md](workflows/issue-resolution-workflow.md) for skill usage.

### Manual Workflow

Without skills, follow these steps:

1. **Create issue**: Copy template, fill details, update backlog
2. **Implement**: Create feature branch, implement, test, commit
3. **PR**: Create draft PR, get review, address feedback
4. **Merge**: Mark ready, wait for CI, merge when approved
5. **Complete**: Update docs, delete issue file, commit changes

---

## Customization

This backlog system can be adapted to your needs:

- **Adjust categories**: Change "Group" values in backlog table
- **Priority levels**: Modify priority scheme (C/H/M/L) as needed
- **Time estimates**: Use your preferred time units
- **Additional fields**: Add columns to backlog table
- **Custom sections**: Add sections to issue template

---

## Related Documentation

- [Issue Resolution Workflow](workflows/issue-resolution-workflow.md) - Complete lifecycle automation
- [Git Workflow](workflows/git-workflow.md) - Branch and commit practices
- [PR Workflow](workflows/pr-workflow.md) - Pull request process
- [Build Workflow](workflows/build-workflow.md) - Build and test procedures
- [Contributing Guidelines](project/CONTRIBUTING.md) - Issue quality standards

---

## Questions?

This is a template backlog system. Adapt it to your project's needs and workflow.
