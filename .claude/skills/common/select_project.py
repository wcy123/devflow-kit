#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
# Licensed under the MIT License.
#

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
        if project_dir.is_dir() and (project_dir / "backlog.md").exists():
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
            ["git", "-C", str(cache_dir), "show", "origin/main:docs/projects/devflow-kit/backlog.md"],
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
                "backlog": str(cache_dir / "docs/projects/devflow-kit/backlog.md"),
                "issues_dir": str(cache_dir / "docs/projects/devflow-kit/issues/"),
                "completed": str(cache_dir / "docs/projects/devflow-kit/completed-issues.md"),
                "dependencies": str(cache_dir / "docs/projects/devflow-kit/issue-dependency-analysis.md"),
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
            "backlog": "docs/projects/devflow-kit/backlog.md",
            "issues_dir": "docs/projects/devflow-kit/issues/",
            "completed": "docs/projects/devflow-kit/completed-issues.md",
            "dependencies": "docs/projects/devflow-kit/issue-dependency-analysis.md",
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
