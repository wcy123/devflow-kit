# Work Log Documentation

This directory contains a generic backlog system and workflow documentation for tracking work items, issues, and improvements across projects.

---

## Directory Structure

```
docs/
├── README.md                          # This file
├── workflows/                         # Workflow documentation
│   ├── issue-resolution-workflow.md   # Complete issue lifecycle workflow
│   ├── git-workflow.md               # Git branching and commit practices
│   └── git-workflow-reference.md     # Detailed git workflow reference
└── project/                          # Project tracking
    ├── backlog.md                    # Active issues index
    ├── completed-issues.md           # Completed issues archive
    ├── issue-dependency-analysis.md  # Issue dependencies and planning
    └── issues/                       # Individual issue files
        └── TEMPLATE.md               # Issue template
```

**Note:** This is a generic, shareable backlog system. Project-specific files like PR workflows, build workflows, and contributing guidelines have been removed to make it portable across different projects.

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

## How to Share Across Projects

This backlog system is designed to be shared across multiple projects. Here are the recommended approaches:

### Option 1: Copy to New Project (Simplest)

When starting a new project, copy the entire system:

```bash
# From the work-log-2026 repository
cd /path/to/work-log-2026

# Copy to new project
cp -r .claude /path/to/new-project/.claude
cp -r docs /path/to/new-project/docs

# Clean up project-specific data in new project
cd /path/to/new-project
# Edit docs/project/backlog.md - remove old issues, keep template structure
# Keep docs/project/issues/TEMPLATE.md
# Remove old issue files if any
```

**What gets copied:**
- ✅ `.claude/` - Claude Code skills and hooks
- ✅ `docs/workflows/` - Generic workflow documentation
- ✅ `docs/project/backlog.md` - Backlog template (edit to remove old issues)
- ✅ `docs/project/completed-issues.md` - Template (start fresh)
- ✅ `docs/project/issue-dependency-analysis.md` - Template
- ✅ `docs/project/issues/TEMPLATE.md` - Issue template

### Option 2: Sync Script (For Multiple Projects)

Use the provided sync script to update multiple projects:

```bash
# From work-log-2026 repository
./scripts/sync-workflow.sh /path/to/target-project
```

**The sync script (`scripts/sync-workflow.sh`):**

```bash
#!/bin/bash
# sync-workflow.sh
# Usage: ./scripts/sync-workflow.sh /path/to/target-project

SOURCE_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_DIR="$1"

if [ -z "$TARGET_DIR" ]; then
    echo "Usage: $0 /path/to/target-project"
    exit 1
fi

echo "Syncing workflow system to: $TARGET_DIR"

# Copy Claude skills
mkdir -p "$TARGET_DIR/.claude"
cp -r "$SOURCE_DIR/.claude/skills" "$TARGET_DIR/.claude/"
cp -r "$SOURCE_DIR/.claude/hooks" "$TARGET_DIR/.claude/"
cp "$SOURCE_DIR/.claude/settings.json" "$TARGET_DIR/.claude/"
cp "$SOURCE_DIR/.claude/README.md" "$TARGET_DIR/.claude/"

# Copy workflow documentation
mkdir -p "$TARGET_DIR/docs/workflows"
cp -r "$SOURCE_DIR/docs/workflows"/* "$TARGET_DIR/docs/workflows/"

# Copy project templates (don't overwrite existing backlog)
mkdir -p "$TARGET_DIR/docs/project/issues"
cp "$SOURCE_DIR/docs/project/issues/TEMPLATE.md" "$TARGET_DIR/docs/project/issues/"

# Only copy these if they don't exist (don't overwrite project data)
[ ! -f "$TARGET_DIR/docs/project/backlog.md" ] && \
    cp "$SOURCE_DIR/docs/project/backlog.md" "$TARGET_DIR/docs/project/"
[ ! -f "$TARGET_DIR/docs/project/completed-issues.md" ] && \
    cp "$SOURCE_DIR/docs/project/completed-issues.md" "$TARGET_DIR/docs/project/"
[ ! -f "$TARGET_DIR/docs/project/issue-dependency-analysis.md" ] && \
    cp "$SOURCE_DIR/docs/project/issue-dependency-analysis.md" "$TARGET_DIR/docs/project/"

echo "✅ Sync complete!"
echo ""
echo "Synced:"
echo "  - Claude skills and hooks"
echo "  - Workflow documentation"
echo "  - Issue template"
echo ""
echo "Not overwritten (if exists):"
echo "  - backlog.md (project-specific)"
echo "  - completed-issues.md (project-specific)"
echo "  - issue-dependency-analysis.md (project-specific)"
```

### Option 3: Git Submodule (Advanced)

For centralized updates across all projects:

```bash
# Create a shared workflow repository
mkdir workflow-tools
cd workflow-tools
git init
# Copy .claude/ and docs/ here
git add .
git commit -m "Initial workflow tools"
git remote add origin <your-repo-url>
git push -u origin main

# In each project
cd /path/to/project
git submodule add <workflow-tools-repo-url> .workflow-tools

# Create symlinks
ln -s .workflow-tools/.claude .claude
ln -s .workflow-tools/docs/workflows docs/workflows

# Copy templates for project-specific data
cp .workflow-tools/docs/project/backlog.md docs/project/backlog.md
cp .workflow-tools/docs/project/issues/TEMPLATE.md docs/project/issues/TEMPLATE.md
```

### What to Share vs Keep Separate

**✅ Share Across Projects:**
- `.claude/skills/` - Generic workflow automation skills
- `.claude/hooks/` - Workflow enforcement hooks
- `.claude/settings.json` - Hook configuration
- `docs/workflows/` - All workflow documentation
- `docs/project/issues/TEMPLATE.md` - Issue template

**⚠️ Keep Project-Specific:**
- `docs/project/backlog.md` - Each project has its own issues
- `docs/project/completed-issues.md` - Project history
- `docs/project/issues/*.md` - Actual issue files
- `docs/project/issue-dependency-analysis.md` - Project dependencies
- `.claude/settings.local.json` - User/project overrides

---

## Key Workflows

### Issue Resolution Workflow

Complete lifecycle from issue creation to completion:

```
/create-issue → /fix-issue → Author Review → /resolve-ci → Merged
```

See [issue-resolution-workflow.md](workflows/issue-resolution-workflow.md) for details.

### Git Workflow

Feature branch workflow:

```
main → feature/issue-NNN-name → implementation → review → merged
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

### Claude Code Skills

If using Claude Code, the following skills are available:

- **`/create-issue`** - Interactive issue discovery and documentation
- **`/fix-issue`** - Implementation from issue selection to draft PR
- **`/resolve-ci`** - PR finalization, CI monitoring, and merge

See [issue-resolution-workflow.md](workflows/issue-resolution-workflow.md) for skill usage.

### Manual Workflow

Without Claude Code skills, follow these steps:

1. **Create issue**: Copy template, fill details, update backlog
2. **Implement**: Create feature branch, implement, test, commit
3. **Review**: Create PR, get review, address feedback
4. **Merge**: Merge when approved
5. **Complete**: Update docs, delete issue file, commit changes

---

## Customization

This backlog system can be adapted to your needs:

- **Adjust categories**: Change "Group" values in backlog table
- **Priority levels**: Modify priority scheme (C/H/M/L) as needed
- **Time estimates**: Use your preferred time units
- **Additional fields**: Add columns to backlog table
- **Custom sections**: Add sections to issue template
- **Project workflows**: Add project-specific workflows alongside the generic ones

---

## Related Documentation

- [Issue Resolution Workflow](workflows/issue-resolution-workflow.md) - Complete lifecycle automation
- [Git Workflow](workflows/git-workflow.md) - Branch and commit practices
- [Git Workflow Reference](workflows/git-workflow-reference.md) - Detailed git reference

---

## Maintenance

### Updating the Shared System

When you improve the workflow system in one project:

1. Update in work-log-2026 (the master template)
2. Commit and push changes
3. Sync to other projects using your chosen sharing method
4. Test in target projects

### Version Control

Consider tagging releases of the workflow system:

```bash
cd work-log-2026
git tag -a v1.0 -m "Stable backlog system release"
git push origin v1.0
```

This allows projects to pin to specific versions.

---

## Questions?

This is a generic, shareable backlog system. Adapt it to your project's needs and workflow.
