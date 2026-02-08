<!--
Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
Licensed under the MIT License.
-->
# Plan: create-issue - Multi-project Support

**Issue:** #003
**Created:** 2026-02-08
**Type:** Detailed implementation guide

---

## Overview

Add multi-project support to `/create-issue` skill by adding detection logic and path selection. This is a focused enhancement on top of existing functionality.

**Goal:** Enable create-issue to work in both workspace and traditional modes with correct path selection.

---

## Prerequisites

- [x] Issue #001 completed (devflow-kit restructured)
- [x] Multi-project architecture documented (docs/design/multi-project-architecture.md)
- [ ] Projects already set up (use existing or /setup-project for new ones)

---

## Architecture Reference

See [Multi-Project Architecture Design](../../design/multi-project-architecture.md) for:
- Workflow detection logic
- Path resolution strategy
- Backlog location detection

---

## Phase 1: Add Detection Logic

### Step 1.1: Add workflow mode detection

**Location:** Near the start of `/create-issue` SKILL.md

**Add detection section:**

```markdown
## Phase 0.5: Detect Workflow Mode

Before starting exploration, detect which workflow mode:

### Check for workspace mode

```python
import os

def is_workspace_mode():
    """Check if running in devflow-kit workspace"""
    return os.path.exists("docs/projects")  # Plural indicates devflow-kit
```

### Determine mode

```python
if is_workspace_mode():
    mode = "workspace"
    print("Working in: devflow-kit (workspace mode)")
else:
    mode = "traditional"
    print("Working in: [project] (traditional mode)")
```
```

### Step 1.2: Add project selection (workspace mode)

**For workspace mode, ask which project:**

```markdown
### Select project (workspace mode only)

If workspace mode:

```python
# List available projects
projects = os.listdir("docs/projects")
projects = [p for p in projects if os.path.isdir(f"docs/projects/{p}")]

# Show to user
print("Available projects:")
for i, proj in enumerate(projects, 1):
    print(f"{i}. {proj}")

# Ask user
choice = input("Which project? (number or name): ")

# Validate
if choice.isdigit():
    project = projects[int(choice) - 1]
else:
    project = choice

# Verify exists
if not os.path.exists(f"docs/projects/{project}"):
    print(f"Error: Project '{project}' not found in docs/projects/")
    print("Run /setup-project to create a new project.")
    exit(1)
```
```

### Step 1.3: Add project detection (traditional mode)

**For traditional mode, detect from git:**

```markdown
### Detect project (traditional mode only)

If traditional mode:

```python
import subprocess

def detect_project_from_git():
    """Detect project name from git remote"""
    try:
        result = subprocess.run(
            ['git', 'remote', 'get-url', 'origin'],
            capture_output=True, text=True, check=True
        )
        remote_url = result.stdout.strip()
        # Extract project name: https://github.com/ROCm/MorphiZen.git → MorphiZen
        project = remote_url.rstrip('/').split('/')[-1].replace('.git', '')
        return project
    except:
        # Fallback: use directory name
        return os.path.basename(os.getcwd())

project = detect_project_from_git()
print(f"Working in: {project} (traditional mode)")
```
```

---

## Phase 2: Path Resolution

### Step 2.1: Add backlog location detection (workspace mode)

**For workspace mode, check where backlog lives:**

```markdown
### Determine backlog location (workspace mode)

```python
def get_workspace_paths(project):
    """Get paths for workspace mode"""

    # Check if project has own backlog (Type 1)
    cache_backlog = f"workspace/cache/{project}/docs/project/backlog.md"

    if os.path.exists(cache_backlog):
        # Type 1: Project has own backlog
        return {
            'backlog': cache_backlog,
            'issues_dir': f'workspace/cache/{project}/docs/project/issues/',
            'completed': f'workspace/cache/{project}/docs/project/completed-issues.md',
            'dependencies': f'workspace/cache/{project}/docs/project/issue-dependency-analysis.md',
            'location': 'remote'
        }
    else:
        # Type 2: Centralized tracking in devflow-kit
        return {
            'backlog': f'docs/projects/{project}/backlog.md',
            'issues_dir': f'docs/projects/{project}/issues/',
            'completed': f'docs/projects/{project}/completed-issues.md',
            'dependencies': f'docs/projects/{project}/issue-dependency-analysis.md',
            'location': 'local'
        }

paths = get_workspace_paths(project)
```
```

### Step 2.2: Add path resolution (traditional mode)

**For traditional mode, use local paths:**

```markdown
### Determine paths (traditional mode)

```python
def get_traditional_paths():
    """Get paths for traditional mode"""
    return {
        'backlog': 'docs/project/backlog.md',
        'issues_dir': 'docs/project/issues/',
        'completed': 'docs/project/completed-issues.md',
        'dependencies': 'docs/project/issue-dependency-analysis.md',
        'location': 'local'
    }

paths = get_traditional_paths()
```
```

### Step 2.3: Verify paths exist

**Before proceeding, check paths are valid:**

```markdown
### Verify paths

```python
if not os.path.exists(paths['backlog']):
    if mode == "workspace":
        print(f"Error: Backlog not found for project '{project}'")
        print(f"Expected: {paths['backlog']}")
        print("\nPossible causes:")
        print("1. Project not set up - run /setup-project")
        print("2. Cache not created - project may need initial clone")
    else:
        print(f"Error: No backlog found at {paths['backlog']}")
        print("This directory doesn't appear to have the workflow system set up.")
    exit(1)
```
```

---

## Phase 3: Update Skill to Use Paths

### Step 3.1: Replace hardcoded paths

**Find and replace all hardcoded paths in create-issue skill:**

**Before:**
```python
Read("docs/project/backlog.md")
```

**After:**
```python
Read(paths['backlog'])
```

**Before:**
```python
issue_file = f"docs/project/issues/{issue_num}-{name}.md"
```

**After:**
```python
issue_file = f"{paths['issues_dir']}{issue_num}-{name}.md"
```

**All occurrences to update:**
- Reading backlog
- Writing issue files
- Updating backlog
- Reading/writing completed-issues.md
- Git operations (commit paths)

### Step 3.2: Update git operations (workspace mode)

**For workspace mode with remote backlog (Type 1):**

Git operations need special handling:

```markdown
### Git operations for remote backlog

If workspace mode AND paths['location'] == 'remote':

**Issue creation workflow:**
1. Issue exists only in cache (not committed)
2. User creates PR to project repo with issue file
3. Issue gets committed to project repo through PR

**This is complex - defer to Phase 4 (optional enhancement)**

For now: Only support Type 2 (centralized) in workspace mode.
```

### Step 3.3: Update PR creation

**Update PR description to reference correct repo:**

**Traditional mode:**
```python
# PR goes to current repo (morphizen)
git push fork feature/exploration-session-{issue_num}
gh pr create --repo <current-repo>
```

**Workspace mode:**
```python
# PR goes to devflow-kit
git push fork feature/{project}-issues-{issue_num}
gh pr create --repo wcy123/devflow-kit
```

---

## Phase 4: Testing

### Test Case 1: Traditional Mode (MorphiZen)

```bash
# Setup
cd ~/morphizen.github.1
# (Has .claude/ symlinked, docs/project/ exists)

# Run skill
/create-issue

# Expected output
Working in: MorphiZen (traditional mode)
[Continue with normal flow]

# Expected files created
docs/project/issues/042-new-issue.md
docs/project/backlog.md (updated)

# Expected git
Commits to morphizen.github.1 repo
PR to ROCm/MorphiZen
```

### Test Case 2: Workspace Mode - Type 2 (onnx-hipdnn-ep)

```bash
# Setup
cd ~/devflow-kit
# docs/projects/onnx-hipdnn-ep/ exists
# No workspace/cache/onnx-hipdnn-ep/docs/project/ (Type 2)

# Run skill
/create-issue

# Expected prompts
Working in: devflow-kit (workspace mode)
Available projects:
1. devflow-kit
2. onnx-hipdnn-ep
Which project? (number or name): 2

[User explores onnx code]

# Expected files created
docs/projects/onnx-hipdnn-ep/issues/001-new-issue.md
docs/projects/onnx-hipdnn-ep/backlog.md (updated)

# Expected git
Commits to devflow-kit repo
PR to wcy123/devflow-kit
```

### Test Case 3: Workspace Mode - Type 1 (morphizen with cache)

```bash
# Setup
cd ~/devflow-kit
# workspace/cache/morphizen/docs/project/backlog.md exists (Type 1)

# Run skill
/create-issue

# Expected prompts
Working in: devflow-kit (workspace mode)
Which project?: morphizen

# Expected behavior
ERROR: Remote backlog (Type 1) not yet supported in workspace mode.
Please work in traditional mode for projects with their own backlogs.

# This is OK for now - Type 1 workspace support can be added later
```

### Test Case 4: Error - Project Not Found

```bash
cd ~/devflow-kit
/create-issue

Which project?: nonexistent

# Expected error
Error: Project 'nonexistent' not found in docs/projects/
Run /setup-project to create a new project.
```

---

## Success Criteria

- ✅ Detects workspace mode (docs/projects/ exists)
- ✅ Detects traditional mode (no docs/projects/)
- ✅ Asks which project in workspace mode
- ✅ Detects project from git in traditional mode
- ✅ Resolves correct paths for each mode
- ✅ Handles Type 2 (centralized) workspace mode
- ✅ Creates issues in correct location
- ✅ Updates correct backlog
- ✅ Git operations target correct repo
- ✅ Error handling for missing projects
- ✅ Traditional mode unchanged (backward compatible)

---

## Out of Scope (Future Enhancements)

**Not included in this issue:**

- ❌ Cache management (assume cache exists)
- ❌ New project setup (use /setup-project)
- ❌ Type 1 workspace support (remote backlog)
- ❌ Auto-project detection in workspace mode
- ❌ Project templates or customization

**These can be added in future issues if needed.**

---

## Rollback Plan

If issues arise:

```bash
# Revert create-issue skill changes
git checkout main .claude/skills/create-issue/

# Test traditional mode still works
cd ~/morphizen.github.1
/create-issue
```

---

## Notes

- Keep changes focused - just detection and path selection
- Don't change core create-issue workflow
- Document any limitations clearly
- Type 1 workspace support (remote backlog) deferred to future
- Reference design document for architecture decisions

---

## Related

- [Multi-Project Architecture Design](../../design/multi-project-architecture.md)
- [Issue #001](../issues/001-restructure-and-rename-to-devflow-kit.md) - Foundation
- [Issue #004](../issues/004-fix-issue-multi-project-support.md) - fix-issue multi-project (next)
