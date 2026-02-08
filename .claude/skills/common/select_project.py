#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
# Licensed under the MIT License.
#

"""
Project detection, cache management, and path resolution for multi-project workflow.
Used by all skills (create-issue, fix-issue, resolve-ci).

PATH STRUCTURE:
    Traditional mode:  docs/project/backlog.md            (singular - fixed)
    Workspace Type 1:  workspace/cache/{project}/docs/project/backlog.md  (singular - project's own)
    Workspace Type 2:  docs/projects/{project}/backlog.md (plural - devflow-kit tracking)

SMART CALL DESIGN FOR TOKEN EFFICIENCY:

TRADITIONAL MODE (one call):
    Working in project repo (e.g., ~/morphizen.github.1/)

    python select_project.py

    Output: {
        "mode": "traditional",
        "project": "current",
        "paths": {
            "backlog": "docs/project/backlog.md",    # Singular!
            ...
        }
    }
    Token cost: ~150 tokens
    No selection needed - paths are fixed.

WORKSPACE MODE (two calls):
    Working in devflow-kit hub (~/devflow-kit/)

    Call 1 (no args): Get project list
        python select_project.py

        Output: {"mode": "workspace", "projects": ["devflow-kit", "morphizen"]}
        Token cost: ~40 tokens

        AI asks user to select project, then...

    Call 2 (with project arg): Get paths for selected project
        python select_project.py morphizen

        Output: {
            "mode": "workspace",
            "project": "morphizen",
            "paths": {
                "backlog": "workspace/cache/morphizen/docs/project/backlog.md"  # Type 1
                # OR "docs/projects/morphizen/backlog.md"  # Type 2
            }
        }
        Token cost: ~150 tokens

        Total: ~190 tokens

WHY THIS DESIGN:
- Traditional mode: One call (no selection needed, fixed paths)
- Workspace mode: Two calls (only when selection needed)
- Scales well (100 projects doesn't bloat first call)
- Script handles complexity (Type 1/2 detection, cache updates)
- No git detection needed in traditional mode
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
        if project_dir.is_dir() and (project_dir / "backlog.md").exists():
            projects.append(project_dir.name)

    return sorted(projects)


def get_project(mode):
    """Get project name (select from list in workspace, N/A in traditional)"""
    if mode == "workspace":
        projects = list_projects()
        if not projects:
            print("Error: No projects found in docs/projects/", file=sys.stderr)
            sys.exit(1)

        # Workspace mode requires project name as argument
        if len(sys.argv) > 1:
            project = sys.argv[1]
            if project not in projects:
                print(f"Error: Project '{project}' not found. Available: {', '.join(projects)}", file=sys.stderr)
                sys.exit(1)
            return project
        else:
            # No argument - return project list for AI to present to user
            return None  # Signal that we need user selection
    else:
        # Traditional mode - project name not needed (paths are fixed)
        return "current"

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
    # Try to check if backlog exists in project's origin/main (singular path!)
    try:
        result = subprocess.run(
            ["git", "-C", str(cache_dir), "show", "origin/main:docs/project/backlog.md"],
            capture_output=True,
            text=True,
            check=True
        )
        return "remote"  # Type 1: Project has own backlog at docs/project/
    except subprocess.CalledProcessError:
        return "local"  # Type 2: Use devflow-kit tracking

def resolve_paths(mode, project):
    """Resolve backlog and issue paths based on mode and project

    Traditional mode: docs/project/ (singular - fixed paths)
    Workspace Type 1: workspace/cache/{project}/docs/project/ (singular - project has own backlog)
    Workspace Type 2: docs/projects/{project}/ (plural - devflow-kit tracking)
    """
    if mode == "workspace":
        cache_dir = Path(f"workspace/cache/{project}")

        # Detect backlog location
        location = check_backlog_location(project, cache_dir)

        if location == "remote":
            # Type 1: Project has own backlog at docs/project/ (singular!)
            paths = {
                "backlog": str(cache_dir / "docs/project/backlog.md"),
                "issues_dir": str(cache_dir / "docs/project/issues/"),
                "completed": str(cache_dir / "docs/project/completed-issues.md"),
                "dependencies": str(cache_dir / "docs/project/issue-dependency-analysis.md"),
                "location": "remote"
            }
        else:
            # Type 2: devflow-kit tracking at docs/projects/{project}/ (plural!)
            paths = {
                "backlog": f"docs/projects/{project}/backlog.md",
                "issues_dir": f"docs/projects/{project}/issues/",
                "completed": f"docs/projects/{project}/completed-issues.md",
                "dependencies": f"docs/projects/{project}/issue-dependency-analysis.md",
                "location": "local"
            }
    else:
        # Traditional mode - work in current directory, docs/project/ (singular!)
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
    #    - "workspace": Running from devflow-kit hub (docs/projects/ exists)
    #    - "traditional": Running from project directory (docs/projects/ doesn't exist)
    mode = detect_mode()

    # 2. Select/detect project name
    #    - Workspace mode: Returns None if no arg (need user selection)
    #    - Traditional mode: Auto-detect from git remote URL
    project = get_project(mode)

    # CALL 1: No project selected yet (workspace mode, no args)
    # Return minimal JSON with project list for AI to present to user
    if project is None:
        projects = list_projects()
        result = {
            "mode": mode,
            "projects": projects
        }
        print(json.dumps(result, indent=2))
        return 0

    # CALL 2: Project selected (traditional mode or workspace mode with arg)
    # 3. Update cache to latest origin/main (workspace mode only)
    #    - Ensures backlog/issues are always current before skills run
    #    - Gracefully handles cache update failures (warns but continues)
    if mode == "workspace":
        update_cache(project)

    # 4. Resolve paths based on mode and backlog location
    #    - Returns correct paths to backlog.md, issues/, completed-issues.md
    #    - Handles both Type 1 (remote backlog) and Type 2 (local tracking)
    paths = resolve_paths(mode, project)

    # 5. Return JSON result to stdout
    #    - Format: {"mode": "...", "project": "...", "paths": {...}}
    result = {
        "mode": mode,
        "project": project,
        "paths": paths
    }

    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
