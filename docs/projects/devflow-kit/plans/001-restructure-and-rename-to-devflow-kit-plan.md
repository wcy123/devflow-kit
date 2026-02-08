<!--
Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
Licensed under the MIT License.
-->
# Plan: Restructure and Rename to devflow-kit

**Issue:** #001
**Created:** 2026-02-08
**Type:** Detailed implementation guide

---

## Overview

This plan provides step-by-step instructions to restructure the project for multi-project support and rename to `devflow-kit` with public GitHub hosting.

**Goal:** Transform `work_log` into `devflow-kit` with multi-project structure and public GitHub presence.

---

## Prerequisites

- [x] On main branch with no uncommitted changes
- [x] Have GitHub account (wcy123)
- [x] Have gh CLI installed and authenticated

---

## Phase 1: Restructure docs/ for Multi-Project

### Step 1.1: Create new directory structure

```bash
cd ~/work_log  # (or wherever work_log is located)

# Create new multi-project structure
mkdir -p docs/projects/devflow-kit
```

### Step 1.2: Move existing project tracking

```bash
# Move all files from docs/project/ to docs/projects/devflow-kit/
mv docs/project/backlog.md docs/projects/devflow-kit/
mv docs/project/completed-issues.md docs/projects/devflow-kit/
mv docs/project/issue-dependency-analysis.md docs/projects/devflow-kit/
mv docs/project/issues docs/projects/devflow-kit/

# Verify the move
ls -la docs/projects/devflow-kit/
# Should show: backlog.md, completed-issues.md, issue-dependency-analysis.md, issues/

# Remove old directory (should be empty)
rmdir docs/project
```

### Step 1.3: Verify structure

```bash
tree docs/ -L 3
# Should show:
# docs/
# ├── projects/
# │   └── devflow-kit/
# │       ├── backlog.md
# │       ├── completed-issues.md
# │       ├── issue-dependency-analysis.md
# │       └── issues/
# ├── workflows/
# │   ├── git-workflow.md
# │   ├── git-workflow-reference.md
# │   └── issue-resolution-workflow.md
# └── README.md
```

### Step 1.4: Update references in docs

Check if any files reference `docs/project/`:

```bash
# Search for references
grep -r "docs/project/" docs/

# Update any references to docs/projects/devflow-kit/
# Common places:
# - docs/README.md
# - docs/workflows/issue-resolution-workflow.md
```

**Files to update:**
- `docs/README.md` - Update paths from `docs/project/` to `docs/projects/devflow-kit/`
- Any workflow docs that reference the backlog location

### Step 1.5: Test skills still work

```bash
# Test that skills can still find files
# (They may not work yet until we update them in Phase 3)
ls .claude/skills/
```

**Note:** Skills will need updates later to support multi-project detection, but that's a separate issue.

---

## Phase 2: Rename Directory

### Step 2.1: Determine current location

```bash
pwd
# Note the parent directory
# Example: /c/Develop/m/source/work_log
```

### Step 2.2: Rename work_log → devflow-kit

```bash
cd ..  # Go to parent directory
mv work_log devflow-kit
cd devflow-kit
```

### Step 2.3: Verify rename

```bash
pwd
# Should show: /path/to/devflow-kit

git status
# Should still show git repo working normally
```

---

## Phase 3: Create Public GitHub Repository

### Step 3.1: Create repo on GitHub

```bash
# Create public repository on GitHub
gh repo create wcy123/devflow-kit \
  --public \
  --description "Developer workflow toolkit with Claude Code skills for multi-project issue tracking and automation" \
  --source=. \
  --remote=origin

# This creates the repo and sets origin remote
```

**Alternative (if gh repo create fails):**
1. Go to https://github.com/new
2. Repository name: `devflow-kit`
3. Description: "Developer workflow toolkit with Claude Code skills"
4. Public
5. Don't initialize with README (we have one)
6. Create repository
7. Then set remote manually:
   ```bash
   git remote remove origin  # If exists
   git remote add origin https://github.com/wcy123/devflow-kit.git
   ```

### Step 3.2: Verify remote

```bash
git remote -v
# Should show:
# origin  https://github.com/wcy123/devflow-kit.git (fetch)
# origin  https://github.com/wcy123/devflow-kit.git (push)
```

### Step 3.3: Update branch tracking

```bash
# Set upstream for main branch
git branch --set-upstream-to=origin/main main
```

---

## Phase 4: Commit and Push Restructure

### Step 4.1: Stage restructure changes

```bash
git status
# Should show moved files: docs/project/* → docs/projects/devflow-kit/*

git add docs/
```

### Step 4.2: Commit restructure

```bash
git commit -m "refactor: restructure for multi-project support

- Move docs/project/ to docs/projects/devflow-kit/
- Enables tracking multiple projects independently
- Prepares for MorphiZen integration and other projects
- Keep all existing issues and backlog as-is

This establishes devflow-kit as the meta-project tracking
improvements to the workflow system itself."
```

### Step 4.3: Push to GitHub

```bash
# Push main branch to public GitHub
git push -u origin main
```

### Step 4.4: Verify on GitHub

Visit: https://github.com/wcy123/devflow-kit

Should see:
- ✅ Repository is public
- ✅ README.md displayed
- ✅ docs/ directory with new structure
- ✅ .claude/ directory with skills

---

## Phase 5: Update Documentation

### Step 5.1: Update README.md

```bash
# Edit README or docs/README.md to reflect new name
# Update any references to "work_log" → "devflow-kit"
```

**Files to check:**
- `README.md` (if exists at root)
- `docs/README.md`
- `.claude/README.md`
- `docs/workflows/*.md`

**Find references:**
```bash
grep -r "work.log" . --exclude-dir=.git
grep -r "work_log" . --exclude-dir=.git
```

### Step 5.2: Commit documentation updates

```bash
git add .
git commit -m "docs: update references from work_log to devflow-kit"
git push origin main
```

---

## Phase 6: Verification

### Step 6.1: Verify directory structure

```bash
pwd
# Should show: /path/to/devflow-kit

ls -la docs/projects/devflow-kit/
# Should show:
# - backlog.md
# - completed-issues.md
# - issue-dependency-analysis.md
# - issues/
```

### Step 6.2: Verify GitHub repo

- [ ] Repo is public: https://github.com/wcy123/devflow-kit
- [ ] README displays correctly
- [ ] docs/projects/devflow-kit/ structure visible
- [ ] .claude/skills/ directory exists
- [ ] Can clone: `git clone https://github.com/wcy123/devflow-kit.git /tmp/test-clone`

### Step 6.3: Verify skills (basic check)

```bash
# Check skills exist
ls .claude/skills/
# Should show: create-issue, fix-issue, resolve-ci

# Note: Skills will need updates to support multi-project
# That's tracked in separate issue
```

---

## Success Criteria

- ✅ Directory renamed: `work_log` → `devflow-kit`
- ✅ Structure updated: `docs/project/` → `docs/projects/devflow-kit/`
- ✅ All existing issues preserved in new location
- ✅ Public GitHub repo created: `github.com/wcy123/devflow-kit`
- ✅ Git remote points to GitHub
- ✅ Code pushed and visible on GitHub
- ✅ Documentation references updated
- ✅ Skills still accessible (even if not yet multi-project aware)

---

## Rollback Plan

If something goes wrong:

```bash
# 1. Rollback git commits
git reset --hard <commit-before-restructure>

# 2. Rename back
cd ..
mv devflow-kit work_log
cd work_log

# 3. Restore old remote (if needed)
git remote remove origin
git remote add origin <old-remote-url>

# 4. Delete GitHub repo (if created)
gh repo delete wcy123/devflow-kit --yes
```

---

## Notes

- This issue focuses on restructure and rename only
- Skills modification for multi-project support is separate issue
- MorphiZen integration is separate issue
- Keep this focused on foundation work
