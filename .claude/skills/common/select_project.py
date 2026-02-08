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
    """Detect workspace vs traditional mode

    workspace: docs/projects/ exists (plural)
    traditional: docs/projects/ doesn't exist
    """
    return "workspace" if os.path.exists("docs/projects") else "traditional"

def list_projects():
    """List available projects in workspace mode

    Type 1 projects: have project.yaml (backlog in their own repo)
    Type 2 projects: have backlog.md (devflow-kit tracking)
    """
    projects_dir = Path("docs/projects")
    if not projects_dir.exists():
        return []

    projects = []
    for project_dir in projects_dir.iterdir():
        # Valid project if has either project.yaml (Type 1) or backlog.md (Type 2)
        if project_dir.is_dir() and (
            (project_dir / "project.yaml").exists() or
            (project_dir / "backlog.md").exists()
        ):
            projects.append(project_dir.name)

    return sorted(projects)

def update_cache(project):
    """Update cache to latest origin/main (workspace mode only)

    Cache is needed for both Type 1 and Type 2 projects to browse code.
    If cache doesn't exist, clone from git_url in project.yaml.
    """
    cache_dir = Path(f"workspace/cache/{project}")

    # If cache doesn't exist, create it by cloning
    if not cache_dir.exists():
        project_yaml = Path(f"docs/projects/{project}/project.yaml")

        # Need project.yaml with git_url to clone
        if not project_yaml.exists():
            print(f"Warning: No project.yaml found for {project}, cannot create cache", file=sys.stderr)
            return

        # Read git_url and clone
        try:
            import yaml
            with open(project_yaml) as f:
                config = yaml.safe_load(f)
            git_url = config.get("git_url")
            if not git_url:
                print(f"Warning: No git_url in {project_yaml}", file=sys.stderr)
                return

            # Create cache directory and clone
            cache_dir.parent.mkdir(parents=True, exist_ok=True)
            print(f"Cloning {project} to cache...", file=sys.stderr)
            subprocess.run(
                ["git", "clone", git_url, str(cache_dir)],
                capture_output=True,
                text=True,
                check=True
            )
            print(f"✓ Cloned {project} cache", file=sys.stderr)
            return
        except Exception as e:
            print(f"⚠️ Warning: Failed to clone {project} cache: {e}", file=sys.stderr)
            return

    # Cache exists - update it
    try:
        subprocess.run(
            ["git", "-C", str(cache_dir), "pull", "origin", "main"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✓ Updated {project} cache to latest origin/main", file=sys.stderr)
    except subprocess.CalledProcessError:
        print(f"⚠️ Warning: Failed to update {project} cache. Using existing version.", file=sys.stderr)

def check_backlog_location(project, cache_dir):
    """Check if project has own backlog (Type 1) or uses devflow-kit tracking (Type 2)"""
    # Check if backlog exists in project's repo at docs/project/ (singular!)
    try:
        subprocess.run(
            ["git", "-C", str(cache_dir), "show", "origin/main:docs/project/backlog.md"],
            capture_output=True,
            text=True,
            check=True
        )
        return "remote"  # Type 1: Project has own backlog
    except subprocess.CalledProcessError:
        return "local"  # Type 2: Use devflow-kit tracking

def resolve_paths(mode, project):
    """Resolve backlog and issue paths based on mode and project

    Traditional mode: docs/project/ (singular - fixed paths)
    Workspace Type 1: workspace/cache/{project}/docs/project/ (singular - project has own backlog)
    Workspace Type 2: docs/projects/{project}/ (plural - devflow-kit tracking)
    """
    if mode == "traditional":
        # Traditional mode - fixed paths at docs/project/ (singular!)
        return {
            "backlog": "docs/project/backlog.md",
            "issues_dir": "docs/project/issues/",
            "completed": "docs/project/completed-issues.md",
            "dependencies": "docs/project/issue-dependency-analysis.md",
            "location": "local"
        }

    # Workspace mode - detect Type 1 vs Type 2
    cache_dir = Path(f"workspace/cache/{project}")
    location = check_backlog_location(project, cache_dir)

    if location == "remote":
        # Type 1: Project has own backlog at docs/project/ (singular!)
        return {
            "backlog": str(cache_dir / "docs/project/backlog.md"),
            "issues_dir": str(cache_dir / "docs/project/issues/"),
            "completed": str(cache_dir / "docs/project/completed-issues.md"),
            "dependencies": str(cache_dir / "docs/project/issue-dependency-analysis.md"),
            "location": "remote"
        }
    else:
        # Type 2: devflow-kit tracking at docs/projects/{project}/ (plural!)
        return {
            "backlog": f"docs/projects/{project}/backlog.md",
            "issues_dir": f"docs/projects/{project}/issues/",
            "completed": f"docs/projects/{project}/completed-issues.md",
            "dependencies": f"docs/projects/{project}/issue-dependency-analysis.md",
            "location": "local"
        }

def main():
    mode = detect_mode()

    # TRADITIONAL MODE: Return everything in one call
    if mode == "traditional":
        paths = resolve_paths("traditional", "current")
        result = {
            "mode": "traditional",
            "project": "current",
            "paths": paths
        }
        print(json.dumps(result, indent=2))
        return 0

    # WORKSPACE MODE: Check if project arg provided
    # Get all available projects (needed for both Call 1 and Call 2 validation)
    projects = list_projects()
    if not projects:
        print("Error: No projects found in docs/projects/", file=sys.stderr)
        sys.exit(1)

    # CALL 1: No project arg - return project list
    if len(sys.argv) < 2:
        result = {
            "mode": "workspace",
            "projects": projects
        }
        print(json.dumps(result, indent=2))
        return 0

    # CALL 2: Project arg provided - validate and return paths
    project = sys.argv[1]
    if project not in projects:
        print(f"Error: Project '{project}' not found. Available: {', '.join(projects)}", file=sys.stderr)
        sys.exit(1)

    # Update cache before resolving paths
    update_cache(project)

    # Resolve paths for selected project
    paths = resolve_paths("workspace", project)

    result = {
        "mode": "workspace",
        "project": project,
        "paths": paths
    }
    print(json.dumps(result, indent=2))
    return 0

if __name__ == "__main__":
    sys.exit(main())
