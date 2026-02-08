<!--
Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
Licensed under the MIT License.
-->
# Issue #003: Skills - Multi-project Support

## Metadata
- **Type:** Feature
- **Priority:** HIGH
- **Created:** 2026-02-08
- **Updated:** 2026-02-08 (Revised to include all skills + shared script)
- **Dependencies:** #001 (devflow-kit restructure must be complete)

## Description

Add multi-project support to all workflow skills (create-issue, fix-issue, resolve-ci) by creating a shared Python script for project detection, cache management, and path resolution. This enables working with multiple projects in both workspace and traditional modes.

## Problem

**Current design:**
```python
# Hardcoded in all skills
backlog = "docs/projects/devflow-kit/backlog.md"
issues_dir = "docs/projects/devflow-kit/issues/"
```

**Why this is problematic:**
1. **Single project only** - Can't distinguish between projects
2. **No workspace support** - Assumes traditional workflow only
3. **Hardcoded paths** - No flexibility for multi-project tracking
4. **Duplicated logic** - Each skill would need same detection code
5. **No cache management** - Can't keep workspace cache up-to-date
6. **Can't work from devflow-kit** - Must be in project directory

**Impact:**
- Can't create issues for multiple projects from devflow-kit
- Can't track non-intrusive projects (like onnx-hipdnn-ep)
- Workspace model documented but not implemented
- Code duplication if we add detection to each skill separately

## Solution

**Proposed architecture:**

### 1. Shared Python Script

Create `.claude/skills/common/select_project.py`:

```python
#!/usr/bin/env python3
"""
Project detection, cache management, and path resolution for multi-project workflow.
Used by all skills (create-issue, fix-issue, resolve-ci).
"""

def main():
    # 1. Detect workflow mode
    mode = detect_mode()

    # 2. Select/detect project
    project = get_project(mode)

    # 3. Update cache (workspace mode only)
    if mode == "workspace":
        update_cache(project)  # git pull origin/main

    # 4. Resolve paths
    paths = resolve_paths(mode, project)

    # 5. Return JSON
    return {
        "mode": mode,
        "project": project,
        "paths": paths
    }

def detect_mode():
    """Detect workspace vs traditional mode"""
    return "workspace" if os.path.exists("docs/projects") else "traditional"

def get_project(mode):
    """Get project name (ask in workspace, detect in traditional)"""
    if mode == "workspace":
        # List projects, ask user to select
        projects = list_projects()
        return ask_user_select(projects)
    else:
        # Detect from git remote
        return detect_from_git()

def update_cache(project):
    """Update cache to latest origin/main"""
    cache_dir = f"workspace/cache/{project}"
    if os.path.exists(cache_dir):
        try:
            subprocess.run(["git", "-C", cache_dir, "pull", "origin", "main"])
        except:
            print(f"⚠️ Warning: Failed to update {project} cache. Using existing version.")

def resolve_paths(mode, project):
    """Resolve backlog and issue paths based on mode and project"""
    # Implementation details in plan
```

**Output (JSON):**
```json
{
  "mode": "workspace",
  "project": "morphizen",
  "paths": {
    "backlog": "workspace/cache/morphizen/docs/projects/devflow-kit/backlog.md",
    "issues_dir": "workspace/cache/morphizen/docs/projects/devflow-kit/issues/",
    "completed": "workspace/cache/morphizen/docs/projects/devflow-kit/completed-issues.md",
    "dependencies": "workspace/cache/morphizen/docs/projects/devflow-kit/issue-dependency-analysis.md",
    "location": "remote"
  }
}
```

### 2. Update All Skills

**Each skill invokes shared script:**

```markdown
## Phase 0: Detect Project

Run project detection:
```bash
PROJECT_INFO=$(python .claude/skills/common/select_project.py)
```

Parse JSON and use paths throughout skill.
```

**Skills updated:**
- `/create-issue` - Use detected paths for issue creation
- `/fix-issue` - Use detected paths for backlog, clone to workspace/issues/
- `/resolve-ci` - Use detected paths for finalization, cleanup workspace/issues/

**Benefits:**
- ✅ **Single source of truth** - Detection logic in one place
- ✅ **Deterministic** - Python script, not LLM interpretation
- ✅ **Auto-cache-update** - Every skill run updates cache to latest
- ✅ **Testable** - Can unit test the Python script
- ✅ **Consistent** - All skills get same detection results
- ✅ **Multi-project support** - Works with any number of projects
- ✅ **Workspace model** - Can work from devflow-kit hub
- ✅ **Backward compatible** - Traditional workflow still works
- ✅ **Fast** - No LLM overhead for detection

**Trade-offs:**
- ⚠️ **Python dependency** - Requires Python 3.x available
- ⚠️ **Projects must exist** - Errors if project not set up (handled by separate /setup-project skill)
- ⚠️ **Type 1 workspace** - Remote backlog (Type 1) support limited initially

## Plans

- [Skills Multi-project Plan](../plans/003-skills-multi-project-support-plan.md) - Created 2026-02-08
