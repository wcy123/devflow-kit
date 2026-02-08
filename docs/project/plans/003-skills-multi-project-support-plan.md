<!--
Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
Licensed under the MIT License.
-->
# Plan: Issue #003 - Skills Multi-project Support

**Created:** 2026-02-08
**Issue:** [#003](../issues/003-skills-multi-project-support.md)

---

## Overview

Implement multi-project support for all workflow skills (create-issue, fix-issue, resolve-ci) using a shared Python script for project detection, cache management, and path resolution.

---

## Prerequisites

- Issue #001 completed (devflow-kit restructure)
- Python 3.x available in environment
- Git available in environment

---

## Implementation Steps

### Phase 1: Create Shared Python Script

**File:** `.claude/skills/common/select_project.py`

```python
#!/usr/bin/env python3
"""
Project detection, cache management, and path resolution for multi-project workflow.
Used by all skills (create-issue, fix-issue, resolve-ci).
"""
import os
import sys
import json
import subprocess
from pathlib import Path

def detect_mode():
    """Detect workspace vs traditional mode"""
    if os.path.exists("docs/projects"):  # Plural
        return "workspace"
    else:
        return "traditional"

def list_projects():
    """List available projects in workspace mode"""
    projects_dir = Path("docs/projects")
    if not projects_dir.exists():
        return []

    projects = []
    for project_dir in projects_dir.iterdir():
        if project_dir.is_dir() and (project_dir / "project.yaml").exists():
            projects.append(project_dir.name)

    return sorted(projects)

def detect_from_git():
    """Detect project name from git remote URL in traditional mode"""
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            check=True
        )
        url = result.stdout.strip()
        # Extract project name from URL (last path component, remove .git)
        name = url.rstrip('/').split('/')[-1]
        if name.endswith('.git'):
            name = name[:-4]
        return name
    except subprocess.CalledProcessError:
        print("Error: Could not detect project name from git remote", file=sys.stderr)
        sys.exit(1)

def get_project(mode):
    """Get project name (ask in workspace, detect in traditional)"""
    if mode == "workspace":
        projects = list_projects()
        if not projects:
            print("Error: No projects found in docs/projects/", file=sys.stderr)
            sys.exit(1)

        # Ask user to select (Claude will handle this via AskUserQuestion)
        # For now, output projects and expect project name via arg
        if len(sys.argv) > 1:
            project = sys.argv[1]
            if project not in projects:
                print(f"Error: Project '{project}' not found. Available: {', '.join(projects)}", file=sys.stderr)
                sys.exit(1)
            return project
        else:
            print(json.dumps({"action": "select_project", "projects": projects}))
            sys.exit(0)
    else:
        return detect_from_git()

def update_cache(project):
    """Update cache to latest origin/main"""
    cache_dir = Path(f"workspace/cache/{project}")

    if not cache_dir.exists():
        print(f"Warning: Cache directory not found for {project}", file=sys.stderr)
        return

    try:
        subprocess.run(
            ["git", "-C", str(cache_dir), "pull", "origin", "main"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✓ Updated {project} cache to latest origin/main", file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Warning: Failed to update {project} cache. Using existing version.", file=sys.stderr)
        print(f"   Error: {e.stderr}", file=sys.stderr)

def check_backlog_location(project, cache_dir):
    """Check if project has own backlog (Type 1) or uses devflow-kit tracking (Type 2)"""
    # Try to check if backlog exists in project's origin/main
    try:
        result = subprocess.run(
            ["git", "-C", str(cache_dir), "show", "origin/main:docs/project/backlog.md"],
            capture_output=True,
            text=True,
            check=True
        )
        return "remote"  # Type 1: Project has own backlog
    except subprocess.CalledProcessError:
        return "local"  # Type 2: Use devflow-kit tracking

def resolve_paths(mode, project):
    """Resolve backlog and issue paths based on mode and project"""
    if mode == "workspace":
        cache_dir = Path(f"workspace/cache/{project}")

        # Detect backlog location
        location = check_backlog_location(project, cache_dir)

        if location == "remote":
            # Type 1: Project has own backlog
            paths = {
                "backlog": str(cache_dir / "docs/project/backlog.md"),
                "issues_dir": str(cache_dir / "docs/project/issues/"),
                "completed": str(cache_dir / "docs/project/completed-issues.md"),
                "dependencies": str(cache_dir / "docs/project/issue-dependency-analysis.md"),
                "location": "remote"
            }
        else:
            # Type 2: devflow-kit tracking
            paths = {
                "backlog": f"docs/projects/{project}/backlog.md",
                "issues_dir": f"docs/projects/{project}/issues/",
                "completed": f"docs/projects/{project}/completed-issues.md",
                "dependencies": f"docs/projects/{project}/issue-dependency-analysis.md",
                "location": "local"
            }
    else:
        # Traditional mode - work in current directory
        paths = {
            "backlog": "docs/project/backlog.md",
            "issues_dir": "docs/project/issues/",
            "completed": "docs/project/completed-issues.md",
            "dependencies": "docs/project/issue-dependency-analysis.md",
            "location": "local"
        }

    return paths

def main():
    # 1. Detect workflow mode
    mode = detect_mode()

    # 2. Select/detect project
    project = get_project(mode)

    # 3. Update cache (workspace mode only)
    if mode == "workspace":
        update_cache(project)

    # 4. Resolve paths
    paths = resolve_paths(mode, project)

    # 5. Return JSON
    result = {
        "mode": mode,
        "project": project,
        "paths": paths
    }

    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
```

**Tasks:**
1. Create directory: `mkdir -p .claude/skills/common/`
2. Create script file: `.claude/skills/common/select_project.py`
3. Make executable: `chmod +x .claude/skills/common/select_project.py`
4. Test with: `python .claude/skills/common/select_project.py` (should output JSON or request project selection)

---

### Phase 2: Update create-issue Skill

**File:** `.claude/skills/create-issue/SKILL.md`

**Changes:**

1. Add Phase 0 at the beginning:

```markdown
## Phase 0: Detect Project

Run project detection:
```bash
PROJECT_INFO=$(python .claude/skills/common/select_project.py)
```

If output contains `"action": "select_project"`, ask user to select from available projects using AskUserQuestion tool, then re-run with:
```bash
PROJECT_INFO=$(python .claude/skills/common/select_project.py PROJECT_NAME)
```

Parse JSON and extract paths:
```bash
BACKLOG=$(echo "$PROJECT_INFO" | jq -r '.paths.backlog')
ISSUES_DIR=$(echo "$PROJECT_INFO" | jq -r '.paths.issues_dir')
MODE=$(echo "$PROJECT_INFO" | jq -r '.mode')
PROJECT=$(echo "$PROJECT_INFO" | jq -r '.project')
```

Display brief mode message: "Working in: {PROJECT} ({MODE} mode)"
```

2. Update all hardcoded paths to use variables:
   - Change `docs/project/backlog.md` → `$BACKLOG`
   - Change `docs/project/issues/` → `$ISSUES_DIR`

**Tasks:**
1. Read current `.claude/skills/create-issue/SKILL.md`
2. Add Phase 0 section
3. Replace hardcoded paths with variables
4. Test skill in both traditional and workspace modes

---

### Phase 3: Update fix-issue Skill

**File:** `.claude/skills/fix-issue/SKILL.md`

**Changes:**

1. Add Phase 0 (same as create-issue)

2. Update Phase 1 (Setup) to handle workspace mode:

```markdown
## Phase 1: Setup

Based on detected mode:

**If traditional mode:**
- Work in current directory
- Backlog at: $BACKLOG
- Create feature branch in current repo

**If workspace mode:**
- Create workspace issue directory: `workspace/issues/{PROJECT}-{ISSUE_NUM}/`
- Clone project: `git clone {GIT_URL} workspace/issues/{PROJECT}-{ISSUE_NUM}/{PROJECT}`
- Change directory: `cd workspace/issues/{PROJECT}-{ISSUE_NUM}/{PROJECT}`
- Create feature branch
- All subsequent work happens in this directory
```

3. Add git_url extraction from project.yaml (workspace mode only)

4. Update all path references to use variables

**Tasks:**
1. Read current `.claude/skills/fix-issue/SKILL.md`
2. Add Phase 0 section
3. Update Phase 1 with workspace/traditional branching
4. Replace hardcoded paths with variables
5. Test skill in both modes

---

### Phase 4: Update resolve-ci Skill

**File:** `.claude/skills/resolve-ci/SKILL.md`

**Changes:**

1. Add Phase 0 (same as create-issue)

2. Add finalization phase for workspace cleanup:

```markdown
## Phase N: Finalization (Workspace Mode Only)

If workspace mode detected:

1. Return to devflow-kit root: `cd ~/devflow-kit` (or wherever devflow-kit is)
2. Clean up workspace issue directory: `rm -rf workspace/issues/{PROJECT}-{ISSUE_NUM}/`
3. Confirm cleanup: "✓ Cleaned up workspace/issues/{PROJECT}-{ISSUE_NUM}/"

This removes the temporary work directory after successful PR merge.
```

3. Update backlog/issue path references

**Tasks:**
1. Read current `.claude/skills/resolve-ci/SKILL.md`
2. Add Phase 0 section
3. Add workspace cleanup phase
4. Replace hardcoded paths with variables
5. Test skill in both modes

---

### Phase 5: Testing

**Test Cases:**

**1. Traditional Mode (in morphizen.github.1):**
```bash
cd ~/morphizen.github.1
/create-issue
# Should detect: mode=traditional, project=morphizen
# Should use: docs/project/backlog.md
```

**2. Workspace Mode (in devflow-kit, existing project):**
```bash
cd ~/devflow-kit
/create-issue
# Should ask to select project
# Should detect: mode=workspace
# Should update cache: git pull origin/main
# Should use: workspace/cache/{project}/docs/project/ (if Type 1) or docs/projects/{project}/ (if Type 2)
```

**3. Workspace Mode - fix-issue:**
```bash
cd ~/devflow-kit
/fix-issue
# Should clone to: workspace/issues/{project}-{num}/
# Should work in cloned directory
```

**4. Workspace Mode - resolve-ci:**
```bash
cd ~/devflow-kit
/resolve-ci
# Should clean up: workspace/issues/{project}-{num}/
```

**5. Cache Update:**
```bash
# Verify cache updates on every skill run
# Check for warning message if cache update fails
```

---

## Success Criteria

- ✅ Shared Python script exists and is executable
- ✅ Script correctly detects workspace vs traditional mode
- ✅ Script updates cache in workspace mode
- ✅ Script resolves correct paths for both modes
- ✅ All three skills (create-issue, fix-issue, resolve-ci) invoke shared script
- ✅ Skills work in traditional mode (e.g., from morphizen.github.1)
- ✅ Skills work in workspace mode (from devflow-kit)
- ✅ fix-issue clones to workspace/issues/ in workspace mode
- ✅ resolve-ci cleans up workspace/issues/ after completion
- ✅ Cache auto-updates on every skill run (with graceful failure)
- ✅ No hardcoded paths in skills (all use variables from script)

---

## Rollback Plan

If shared script approach causes issues:

1. Revert skill files to previous versions
2. Delete `.claude/skills/common/select_project.py`
3. Implement per-skill detection as fallback

---

## Notes

- Python script is deterministic (not LLM-based) for reliability
- Cache update happens automatically on every skill run
- Graceful degradation: warns but continues if cache update fails
- Backward compatible: traditional workflow still works exactly as before
- Future: Could add `/setup-project` skill to create new project structure
