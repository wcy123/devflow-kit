<!--
Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
Licensed under the MIT License.
-->
# Issue #003: create-issue - Multi-project Support

## Metadata
- **Type:** Feature
- **Priority:** HIGH
- **Created:** 2026-02-08
- **Dependencies:** #001 (devflow-kit restructure must be complete)

## Description

Add multi-project support to `/create-issue` skill. Enable working with multiple projects by detecting workflow mode (workspace vs traditional) and using correct backlog paths. This is a focused enhancement - just add detection and path selection on top of existing functionality.

## Problem

**Current design:**
```python
# Hardcoded in create-issue skill
backlog = "docs/project/backlog.md"
issues_dir = "docs/project/issues/"
```

**Why this is problematic:**
1. **Single project only** - Can't distinguish between projects
2. **No workspace support** - Assumes traditional workflow
3. **Hardcoded paths** - No flexibility for multi-project tracking
4. **Can't work from devflow-kit** - Must be in project directory

**Impact:**
- Can't create issues for onnx-hipdnn-ep from devflow-kit
- Can't track multiple projects
- Workspace model documented but not implemented

## Solution

**Proposed approach:**
Add detection at start of `/create-issue` skill:

```python
# Phase 0: Detect workflow mode
if current_directory_has("docs/projects/"):  # Plural
    mode = "workspace"
    project = ask_user_which_project()
    paths = get_workspace_paths(project)
else:
    mode = "traditional"
    project = detect_from_git_remote()
    paths = get_traditional_paths()

# Rest of skill uses paths.backlog, paths.issues_dir
# Everything else stays the same
```

**Path resolution:**

**Workspace mode:**
```python
# User in devflow-kit
project = "morphizen"  # User selected

# Check backlog location
if exists(f"workspace/cache/{project}/docs/project/backlog.md"):
    # Type 1: Project has own backlog
    paths = {
        'backlog': f'workspace/cache/{project}/docs/project/backlog.md',
        'issues_dir': f'workspace/cache/{project}/docs/project/issues/'
    }
else:
    # Type 2: Centralized tracking
    paths = {
        'backlog': f'docs/projects/{project}/backlog.md',
        'issues_dir': f'docs/projects/{project}/issues/'
    }
```

**Traditional mode:**
```python
# User in project directory (e.g., ~/morphizen.github.1)
paths = {
    'backlog': 'docs/project/backlog.md',
    'issues_dir': 'docs/project/issues/'
}
```

**Benefits:**
- ✅ **Multi-project support** - Works with any project
- ✅ **Workspace model** - Can work from devflow-kit hub
- ✅ **Backward compatible** - Traditional workflow still works
- ✅ **Simple change** - Just detection + path selection
- ✅ **No cache management** - Assumes projects already set up

**Trade-offs:**
- ⚠️ **Projects must exist** - Errors if project not set up (handled by separate /setup-project skill)
- ⚠️ **User must know project** - Can't auto-detect in workspace mode (asks explicitly)

## Plans

- [create-issue Multi-project Plan](../plans/003-create-issue-multi-project-support-plan.md) - Created 2026-02-08
