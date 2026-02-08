<!--
Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
Licensed under the MIT License.
-->
# Multi-Project Architecture Design

**Created:** 2026-02-08
**Status:** Design Document

---

## Overview

This document describes the architecture for supporting multiple projects in devflow-kit. It captures design decisions and rationale from exploration and discussion.

---

## Two Supported Workflows

devflow-kit supports **two distinct workflows** for working with projects:

### Workflow 1: Traditional (Direct Work)

**Use case:** Main contributors who "live" in a project repository.

**Setup:**
```bash
~/morphizen.github.1/
├── .claude/skills/ → ~/devflow-kit/.claude/skills/  # Symlinked
├── docs/project/                                      # Project's own backlog
└── src/
```

**User experience:**
```bash
cd ~/morphizen.github.1
/create-issue   # Works in current directory
/fix-issue      # Works in current directory
```

**Characteristics:**
- User works directly in project clone
- Skills symlinked from devflow-kit (see Issue #002)
- Changes committed to project repo immediately
- Good for long-term, focused project work

### Workflow 2: Workspace Model (devflow-kit Hub)

**Use case:** Working on multiple projects, quick fixes, non-intrusive projects.

**Setup:**
```bash
~/devflow-kit/
├── .claude/skills/                    # Skills live here
├── docs/projects/                     # Multi-project tracking
│   ├── morphizen/
│   └── onnx-hipdnn-ep/
└── workspace/                         # Work happens here (gitignored)
    ├── cache/                         # Persistent clones (always main)
    │   ├── morphizen/                 # For browsing/selecting issues
    │   └── onnx-hipdnn-ep/
    └── issues/                        # Temporary work directories
        ├── morphizen-042/             # Clone for issue #042
        │   └── morphizen/             # Deleted after issue complete
        └── onnx-043/
            └── onnx-hipdnn-ep/
```

**User experience:**
```bash
cd ~/devflow-kit
/create-issue   # Tracks in docs/projects/{name}/
/fix-issue      # Clones to workspace/issues/{name}-{num}/
                # After PR merged: deletes workspace/issues/{name}-{num}/
```

**Characteristics:**
- User always works from devflow-kit
- Projects cloned into workspace/ subdirectories
- Parallel work on multiple issues (separate workspace dirs)
- Clean workspace after completion
- Zero intrusion on target projects

---

## Workflow Detection

**How skills detect which workflow to use:**

```python
# Detection logic
if current_directory_has("docs/projects/"):  # Plural
    workflow = "workspace"
    # Clone to workspace/, track in docs/projects/{name}/
else:
    workflow = "traditional"
    # Work in current directory, use local docs/project/
```

**Why this works:**
- devflow-kit has `docs/projects/` (plural) - multi-project tracking
- Projects have `docs/project/` (singular) - single project tracking
- Clear distinction prevents ambiguity

**Edge case:** If user is in a directory without `.claude/`, skills don't exist, so `/fix-issue` command won't work. No special handling needed - it's impossible to invoke.

---

## Workspace Structure (Workspace Model)

### Cache Directories (Persistent)

**Purpose:** Quick access to project code for browsing, selecting issues, reading context.

```
workspace/cache/
├── morphizen/              # git clone, persistent
└── onnx-hipdnn-ep/         # git clone, persistent
```

**Characteristics:**
- Persistent across issues
- Always tracks `origin/main` branch
- Auto-updated before each skill run (`git pull origin main`)
- Used for reading code, not making changes
- Never deleted

**Update strategy:**
```python
# Every skill run
try:
    git pull origin main
except GitError:
    # Warn user but continue with stale cache
    print("⚠️ Warning: Failed to update {project} cache. Using existing version.")
    # Don't block - user can still work
```

**Why warn but continue:**
- Network issues shouldn't block work
- Stale cache is better than no cache
- User can manually fix if needed

### Issue Directories (Temporary)

**Purpose:** Actual work on specific issues.

```
workspace/issues/
├── morphizen-042/          # Working on issue #042
│   └── morphizen/          # Fresh clone, feature branch
└── onnx-043/               # Working on issue #043
    └── onnx-hipdnn-ep/     # Parallel work possible
```

**Characteristics:**
- Created when starting issue (`/fix-issue`)
- Fresh clone from origin
- Feature branch created here
- Changes committed, pushed, PR created
- **Deleted after issue complete** (PR merged)
- Enables parallel work (multiple issue dirs)

**Lifecycle:**
```
/fix-issue
→ Clone to workspace/issues/{project}-{issue_num}/
→ Create feature branch
→ Make changes, commit, push
→ Create PR

(PR reviewed, merged)

→ Delete workspace/issues/{project}-{issue_num}/
```

---

## Project Metadata

**Location:** `devflow-kit/docs/projects/{name}/project.yaml`

### Minimal Metadata

```yaml
name: morphizen
git_url: https://github.com/ROCm/MorphiZen.git
```

**Why minimal:**
- More metadata = more maintenance burden
- Auto-detect instead of store when possible

### What's NOT Stored (and Why)

**❌ Workflow type**
- Reason: From devflow-kit perspective, always uses workspace model
- Traditional workflow is external (user's choice to set up symlinks)

**❌ has_own_backlog / backlog_mode**
- Reason: Auto-detect by checking `git show origin/main:docs/project/backlog.md`
- Dynamic check is more reliable than stale metadata

**❌ Fork URL**
- Reason: User-specific (everyone has their own fork)
- Should be in user's local config or auto-detected from git remotes

**❌ Local path**
- Reason: Users can have multiple clones, paths change
- Not reliable to store

**❌ Default branch**
- Reason: Convention is `main`, can detect from git remote

### Future Metadata (If Needed)

Could add later if use cases arise:
- `description`: Brief project description
- `team`: Owning team
- `access_level`: Public/Private/Internal
- `ci_system`: GitHub Actions / Jenkins / etc.

**Principle:** Start minimal, add only when proven necessary.

---

## Backlog Location Detection

Projects fall into two categories based on backlog location:

### Type 1: Projects with Own Backlog (e.g., MorphiZen)

**Backlog lives:** In the project's repo `docs/project/backlog.md`

**From devflow-kit workspace:**
```bash
# Check remote backlog
git show origin/main:docs/project/backlog.md

# Or from cache
cat workspace/cache/morphizen/docs/project/backlog.md
```

**Characteristics:**
- Source of truth: Project's repo
- devflow-kit reads from remote
- Changes go through PRs to project
- Good for projects that adopted devflow-kit workflow

### Type 2: Projects without Own Backlog (e.g., onnx-hipdnn-ep)

**Backlog lives:** In devflow-kit `docs/projects/onnx-hipdnn-ep/backlog.md`

**Location:**
```bash
devflow-kit/docs/projects/onnx-hipdnn-ep/
├── backlog.md
├── completed-issues.md
├── issue-dependency-analysis.md
└── issues/
```

**Characteristics:**
- Source of truth: devflow-kit repo
- Non-intrusive (nothing added to target project)
- Personal tracking or team-shared if devflow-kit is shared
- Good for contributing to projects without workflow changes

### Detection Logic

```python
def get_backlog_path(project):
    # Check if project has own backlog
    try:
        result = git_show(f"origin/main:docs/project/backlog.md")
        # Type 1: Use remote backlog
        return f"workspace/cache/{project}/docs/project/backlog.md"
    except FileNotFound:
        # Type 2: Use devflow-kit tracking
        return f"docs/projects/{project}/backlog.md"
```

**No metadata needed:** Detection happens dynamically.

---

## New Project Setup (Workspace Model)

### User Experience

```bash
cd ~/devflow-kit
/create-issue
# User explores code for a new project
```

**Skill behavior:**
1. Detects: No `docs/projects/new-project/` exists
2. Asks: "New project detected: 'new-project'. Create tracking structure? (y/n)"
3. If yes:
   - Ask: "Enter git URL: "
   - User: "https://github.com/org/new-project.git"
   - Create: `docs/projects/new-project/project.yaml`
   - Create: `docs/projects/new-project/backlog.md` (from template)
   - Create: `docs/projects/new-project/issues/TEMPLATE.md`
   - Clone to: `workspace/cache/new-project/`

### Project Name Extraction

**From git URL:**
```
https://github.com/org/new-project.git
→ Extract: "new-project"
```

**Rule:** Use repository name (last path component, remove `.git`)

### Metadata Created

```yaml
# docs/projects/new-project/project.yaml
name: new-project
git_url: https://github.com/org/new-project.git
```

### Files Created

```
docs/projects/new-project/
├── project.yaml              # Metadata
├── backlog.md                # Empty/template
├── completed-issues.md       # Empty
├── issue-dependency-analysis.md  # Template
└── issues/
    └── TEMPLATE.md

workspace/cache/new-project/  # Cloned from git_url
```

---

## User Experience Scenarios

### Scenario A: MorphiZen (Traditional Workflow)

**Setup:**
```bash
~/morphizen.github.1/.claude/skills/ → devflow-kit (symlinks)
```

**Usage:**
```bash
cd ~/morphizen.github.1
/create-issue
→ Brief message: "Working in: MorphiZen (local mode)"
→ Creates issues in: docs/project/issues/
→ Updates: docs/project/backlog.md
```

**Characteristics:**
- Skills detect: Not in devflow-kit (no docs/projects/)
- Work directly in current directory
- Commit to MorphiZen repo

### Scenario B: MorphiZen (Workspace Model)

**Setup:**
```bash
~/devflow-kit/
└── workspace/cache/morphizen/  # Persistent clone
```

**Usage:**
```bash
cd ~/devflow-kit
/fix-issue
→ Reads: workspace/cache/morphizen/docs/project/backlog.md
→ Clones to: workspace/issues/morphizen-042/
→ Works in: workspace/issues/morphizen-042/morphizen/
→ Creates PR to: ROCm/MorphiZen
→ After merge: Deletes workspace/issues/morphizen-042/
```

**Characteristics:**
- User never leaves devflow-kit
- Can work on multiple issues in parallel
- Clean workspace after completion

### Scenario C: onnx-hipdnn-ep (Workspace Model Only)

**Setup:**
```bash
~/devflow-kit/
├── docs/projects/onnx-hipdnn-ep/  # devflow-kit tracking
└── workspace/cache/onnx-hipdnn-ep/  # Persistent clone
```

**Usage:**
```bash
cd ~/devflow-kit
/create-issue
→ Creates issues in: docs/projects/onnx-hipdnn-ep/issues/
→ Updates: docs/projects/onnx-hipdnn-ep/backlog.md

/fix-issue
→ Reads: docs/projects/onnx-hipdnn-ep/backlog.md
→ Clones to: workspace/issues/onnx-043/
→ Creates PR to: org/onnx-hipdnn-ep
```

**Characteristics:**
- Zero intrusion on onnx-hipdnn-ep repo
- All tracking in devflow-kit
- Can contribute without modifying their workflow

---

## Design Principles

### 1. Auto-Detect Over Metadata

**Prefer:** Dynamic detection
**Over:** Stored configuration

**Reason:** Metadata becomes stale, detection is always current.

**Examples:**
- ✅ Check for `docs/projects/` to detect workspace mode
- ✅ Check `origin/main:docs/project/` to detect backlog location
- ❌ Store workflow_type in metadata

### 2. Minimal Metadata

**Principle:** Only store what can't be detected or derived.

**Current:** `name` + `git_url`
**Future:** Add only when proven necessary

**Reason:** Less to maintain, less to go wrong.

### 3. Fail Gracefully

**Principle:** Warn but continue when possible.

**Examples:**
- Cache update fails → warn, use stale cache
- Metadata missing → prompt to create
- Detection ambiguous → ask user

**Reason:** Don't block work over recoverable issues.

### 4. Support Both Workflows

**Principle:** Traditional and workspace models coexist.

**Reason:** Different use cases need different approaches.

**Implementation:** Detection logic routes to appropriate behavior.

### 5. Zero Intrusion Option

**Principle:** Always offer non-intrusive way to work with projects.

**Implementation:** Workspace model with devflow-kit tracking.

**Benefit:** Can contribute to any project without changing their setup.

---

## Implementation Notes

### Skills Changes Needed

**All skills need:**
- Workspace/traditional detection
- Cache management (workspace mode)
- Project metadata handling
- Backlog location detection

**Specific per skill:**
- `/create-issue`: Issue creation in correct location
- `/fix-issue`: Workspace setup, clone management
- `/resolve-ci`: Cleanup workspace after merge

### Git Operations

**Cache update:**
```bash
cd workspace/cache/{project}
git fetch origin
git reset --hard origin/main  # Always stay on main
```

**Issue clone:**
```bash
git clone {git_url} workspace/issues/{project}-{num}/{project}
cd workspace/issues/{project}-{num}/{project}
git checkout -b feature/issue-{num}
```

### File Structure

```
devflow-kit/
├── .claude/
│   └── skills/
├── docs/
│   ├── design/                    # This document
│   ├── projects/                  # Multi-project tracking
│   │   ├── devflow-kit/          # Meta-project
│   │   ├── morphizen/            # If centralized tracking
│   │   └── onnx-hipdnn-ep/       # Non-intrusive tracking
│   └── workflows/
└── workspace/                     # Gitignored
    ├── cache/                     # Persistent clones
    └── issues/                    # Temporary work dirs
```

---

## Future Considerations

### Team Collaboration

**Question:** How do teams share devflow-kit tracking?

**Options:**
- Shared devflow-kit repo (team clones same repo)
- Each developer has own devflow-kit (personal tracking)
- Hybrid: Shared tracking repo, personal devflow-kit

**Defer:** Until we have real team use case.

### Project Templates

**Question:** Different project types need different templates?

**Example:** Python projects vs C++ projects vs documentation projects

**Solution:** Could add `template` field to metadata, select appropriate issue/plan templates.

**Defer:** Start with one template, specialize later.

### Cache Management

**Questions:**
- How large can cache get? (Many projects)
- Automatic cleanup of unused cache?
- User command to manage cache?

**Defer:** Implement basic cache first, optimize later.

---

## Related Documents

- [Issue #001](../project/issues/001-restructure-and-rename-to-devflow-kit.md) - Restructure for multi-project
- [Issue #002](../project/issues/002-morphizen-integration-with-devflow-kit.md) - MorphiZen traditional workflow
- Skills multi-project support (TBD) - Implementation issues

---

## Revision History

- **2026-02-08:** Initial design document created from exploration discussion
