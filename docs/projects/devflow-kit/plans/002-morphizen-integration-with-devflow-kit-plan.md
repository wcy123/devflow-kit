<!--
Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
Licensed under the MIT License.
-->
# Plan: MorphiZen Integration with devflow-kit

**Issue:** #002
**Created:** 2026-02-08
**Type:** Detailed implementation guide

---

## Overview

This plan integrates MorphiZen with devflow-kit by replacing copied skills with symlinks to external devflow-kit repository.

**Goal:** MorphiZen uses devflow-kit skills via symlinks, minimizing PRs for infrastructure updates.

---

## Prerequisites

- [x] Issue #001 completed (devflow-kit restructured and on GitHub)
- [x] devflow-kit cloned: `~/devflow-kit/` (or known location)
- [x] MorphiZen cloned: `../morphizen.github.1/`
- [x] Have fork: `wcy123/MorphiZen` on GitHub

---

## Phase 1: Update MorphiZen .gitignore

### Step 1.1: Navigate to MorphiZen

```bash
cd ../morphizen.github.1
git checkout main
git pull origin main
```

### Step 1.2: Create feature branch

```bash
git checkout -b feature/integrate-devflow-kit
```

### Step 1.3: Update .gitignore

Add entries to ignore symlinked skills:

```bash
# Edit .gitignore
cat >> .gitignore << 'EOF'

# devflow-kit automation (symlinked skills - personal setup)
.claude/skills/create-issue/
.claude/skills/fix-issue/
.claude/skills/resolve-ci/
EOF
```

**Verify:**
```bash
tail .gitignore
# Should show the new entries
```

---

## Phase 2: Replace Skills with Symlinks

### Step 2.1: Backup current skills (optional)

```bash
cd .claude/skills

# Optional: backup existing skills
mkdir -p ~/morphizen-skills-backup
cp -r create-issue fix-issue resolve-ci ~/morphizen-skills-backup/
```

### Step 2.2: Delete old skill directories

```bash
cd ../morphizen.github.1/.claude/skills

# Delete copied skills (keep build-and-test)
rm -rf create-issue/
rm -rf fix-issue/
rm -rf resolve-ci/

# Verify only build-and-test remains
ls -la
# Should show only: build-and-test/
```

### Step 2.3: Create symlinks to devflow-kit

**Determine devflow-kit path:**
```bash
# Adjust path based on where devflow-kit is located relative to MorphiZen
# If structure is:
#   /c/Develop/m/source/devflow-kit/
#   /c/Develop/m/source/morphizen.github.1/
# Then relative path from morphizen.github.1 is: ../devflow-kit

DEVFLOW_KIT_PATH="../devflow-kit"  # Adjust if needed
```

**Create symlinks:**
```bash
cd ../morphizen.github.1/.claude/skills

ln -s ../../../devflow-kit/.claude/skills/create-issue create-issue
ln -s ../../../devflow-kit/.claude/skills/fix-issue fix-issue
ln -s ../../../devflow-kit/.claude/skills/resolve-ci resolve-ci
```

**Verify symlinks:**
```bash
ls -la
# Should show:
# lrwxrwxrwx ... create-issue -> ../../../devflow-kit/.claude/skills/create-issue
# lrwxrwxrwx ... fix-issue -> ../../../devflow-kit/.claude/skills/fix-issue
# lrwxrwxrwx ... resolve-ci -> ../../../devflow-kit/.claude/skills/resolve-ci
# drwxr-xr-x ... build-and-test/

# Test symlink target exists
ls create-issue/
# Should show contents of devflow-kit's create-issue skill
```

---

## Phase 3: Update CONTRIBUTING.md

### Step 3.1: Read current CONTRIBUTING.md

```bash
cd ../morphizen.github.1/docs/project
head -20 CONTRIBUTING.md
```

### Step 3.2: Add devflow-kit setup section

Add section after existing content explaining how to set up automation:

```markdown
## Optional: Workflow Automation with devflow-kit

MorphiZen uses workflow automation skills for issue tracking and development workflow.
These skills are maintained in the external [devflow-kit](https://github.com/wcy123/devflow-kit) repository.

### Manual Workflow (Always Available)

You can work with the issue system manually:
- **Backlog:** See [backlog.md](backlog.md)
- **Create issues:** Copy [issues/TEMPLATE.md](issues/TEMPLATE.md)
- **Workflows:** See [../workflows/](../workflows/)

### Automated Workflow (Optional Setup)

For automation, set up devflow-kit:

**One-time setup:**
```bash
# 1. Clone devflow-kit (parallel to MorphiZen)
cd /path/to/parent-directory
git clone https://github.com/wcy123/devflow-kit.git

# 2. Create symlinks in MorphiZen (from MorphiZen root)
cd /path/to/MorphiZen/.claude/skills
ln -s ../../../devflow-kit/.claude/skills/create-issue create-issue
ln -s ../../../devflow-kit/.claude/skills/fix-issue fix-issue
ln -s ../../../devflow-kit/.claude/skills/resolve-ci resolve-ci

# 3. Verify setup
ls -la
# Should show symlinks to devflow-kit
```

**Available skills:**
- `/create-issue` - Interactive issue creation and exploration
- `/fix-issue` - Automated issue implementation (selection → PR)
- `/resolve-ci` - CI monitoring and auto-merge

**Note:** The `.claude/skills/` symlinks are gitignored, so this setup stays local to your machine.

### Updating devflow-kit

To get latest workflow improvements:
```bash
cd /path/to/devflow-kit
git pull origin main
# Changes are immediately available in MorphiZen (via symlinks)
```
```

### Step 3.3: Save CONTRIBUTING.md

```bash
# After editing CONTRIBUTING.md
git add docs/projects/devflow-kit/CONTRIBUTING.md
```

---

## Phase 4: Commit and Push Changes

### Step 4.1: Review changes

```bash
cd ../morphizen.github.1
git status

# Should show:
# Modified: .gitignore
# Modified: docs/projects/devflow-kit/CONTRIBUTING.md
# Deleted: .claude/skills/create-issue/
# Deleted: .claude/skills/fix-issue/
# Deleted: .claude/skills/resolve-ci/
```

### Step 4.2: Verify symlinks are gitignored

```bash
git status .claude/skills/
# Should NOT show the symlinks (they're gitignored)
```

### Step 4.3: Stage changes

```bash
git add .gitignore docs/projects/devflow-kit/CONTRIBUTING.md
git add .claude/skills/  # Stages deletions only (symlinks ignored)
```

### Step 4.4: Commit

```bash
git commit -m "feat: integrate with devflow-kit for workflow automation

- Add .gitignore entries for symlinked skills
- Replace skills with symlinks to external devflow-kit
- Update CONTRIBUTING.md with setup instructions
- Keep build-and-test skill (MorphiZen-specific)

This enables automatic skill updates without PRs to MorphiZen.
Team members can optionally set up devflow-kit for automation.

Related: devflow-kit issue #002"
```

### Step 4.5: Push to fork

```bash
git push fork feature/integrate-devflow-kit
```

---

## Phase 5: Create Pull Request

### Step 5.1: Create draft PR

```bash
gh pr create --draft \
  --repo ROCm/MorphiZen \
  --title "feat: Integrate with devflow-kit for workflow automation" \
  --body "$(cat <<'EOF'
## Summary

Integrate MorphiZen with external [devflow-kit](https://github.com/wcy123/devflow-kit) by symlinking shared workflow skills. This minimizes PRs to MorphiZen for infrastructure updates while providing optional automation for team members.

## Changes

- **Updated `.gitignore`** - Ignore symlinked skill directories
- **Replaced skills with symlinks** - `create-issue`, `fix-issue`, `resolve-ci` now symlink to devflow-kit
- **Updated `CONTRIBUTING.md`** - Added setup instructions for team
- **Kept `build-and-test`** - MorphiZen-specific skill remains as real directory

## Benefits

- ✅ Skill improvements happen externally (zero PRs to MorphiZen)
- ✅ Single source of truth for workflow automation
- ✅ Team members opt-in (not forced)
- ✅ MorphiZen repo stays focused on project code

## Setup for Reviewers

To test the automation (optional):

1. Clone devflow-kit: `git clone https://github.com/wcy123/devflow-kit.git`
2. Create symlinks as documented in updated CONTRIBUTING.md
3. Test skills: `/create-issue`, `/fix-issue`, `/resolve-ci`

## Testing

- [x] Symlinks created and point to correct devflow-kit paths
- [x] Symlinks are gitignored (not committed)
- [x] CONTRIBUTING.md includes setup instructions
- [x] build-and-test skill still works (MorphiZen-specific)

## Related

- devflow-kit issue #002
- External repo: https://github.com/wcy123/devflow-kit
EOF
)"
```

### Step 5.2: Verify PR created

```bash
gh pr view --repo ROCm/MorphiZen
# Should show the draft PR
```

---

## Phase 6: Verification

### Step 6.1: Verify local setup

```bash
cd ../morphizen.github.1

# Check .gitignore
grep "devflow-kit" .gitignore
# Should show the new entries

# Check symlinks
ls -la .claude/skills/
# Should show:
# - create-issue → devflow-kit (symlink)
# - fix-issue → devflow-kit (symlink)
# - resolve-ci → devflow-kit (symlink)
# - build-and-test (real directory)

# Test symlink works
cat .claude/skills/create-issue/SKILL.md | head -5
# Should show content from devflow-kit
```

### Step 6.2: Verify git status

```bash
git status
# Should be clean (symlinks gitignored, changes committed)
```

### Step 6.3: Test skills (optional)

```bash
# If Claude Code is running in MorphiZen
/create-issue
# Should load skill from devflow-kit via symlink
```

---

## Success Criteria

- ✅ `.gitignore` updated with symlinked skill paths
- ✅ Old skill directories deleted from MorphiZen
- ✅ Symlinks created pointing to devflow-kit
- ✅ `build-and-test` skill preserved (MorphiZen-specific)
- ✅ Symlinks gitignored (not committed)
- ✅ `CONTRIBUTING.md` updated with setup instructions
- ✅ Changes committed to feature branch
- ✅ Draft PR created to ROCm/MorphiZen
- ✅ Skills accessible via symlinks

---

## Rollback Plan

If issues arise:

```bash
# 1. Delete symlinks
cd ../morphizen.github.1/.claude/skills
rm create-issue fix-issue resolve-ci

# 2. Restore from backup (if created)
cp -r ~/morphizen-skills-backup/* .

# 3. Or restore from git
git checkout main .claude/skills/

# 4. Close PR
gh pr close <PR_NUMBER> --repo ROCm/MorphiZen

# 5. Delete feature branch
git branch -D feature/integrate-devflow-kit
```

---

## Notes

- This integrates MorphiZen only; other projects handled separately
- Hooks and settings.json strategy deferred to separate issue (#026)
- Skills multi-project detection deferred to separate issue (#020)
- Focus: minimal intrusion, optional automation, zero ongoing PRs
