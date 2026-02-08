<!--
Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
Licensed under the MIT License.
-->
# Issue #002: MorphiZen Integration with devflow-kit

## Metadata
- **Type:** Feature
- **Priority:** HIGH
- **Created:** 2026-02-08
- **Dependencies:** #001 (must complete restructure first)

## Description

Integrate MorphiZen with devflow-kit by symlinking shared skills from external devflow-kit repository. This allows MorphiZen to use the workflow automation while keeping skills maintained in devflow-kit (minimizing PRs to MorphiZen for infrastructure updates).

## Problem

**Current design:**
```
MorphiZen/.claude/
└── skills/
    ├── create-issue/         (Full copy - must PR to update)
    ├── fix-issue/            (Full copy - must PR to update)
    ├── resolve-ci/           (Full copy - must PR to update)
    └── build-and-test/       (MorphiZen-specific)
```

**Why this is problematic:**
1. **Duplication** - Skills copied from work_log, must manually sync
2. **Update friction** - Every skill improvement requires PR to ROCm/MorphiZen
3. **Maintenance burden** - Skills diverge between projects
4. **No single source of truth** - Changes propagate slowly

**Impact:**
- Workflow improvements don't reach MorphiZen automatically
- PRs to corporate repo for infrastructure changes (noisy)
- Bug fixes in skills need multiple PRs
- Team doesn't get latest automation features

## Solution

**Proposed structure:**
```
~/devflow-kit/.claude/                    (External - public GitHub)
└── skills/
    ├── create-issue/                     (Maintained here)
    ├── fix-issue/
    └── resolve-ci/

MorphiZen/.claude/                        (ROCm repo)
├── skills/
│   ├── create-issue/ → ~/devflow-kit/.claude/skills/create-issue/    (symlink - gitignored)
│   ├── fix-issue/ → ~/devflow-kit/.claude/skills/fix-issue/          (symlink - gitignored)
│   ├── resolve-ci/ → ~/devflow-kit/.claude/skills/resolve-ci/        (symlink - gitignored)
│   └── build-and-test/                   (Real dir - MorphiZen-specific)
├── hooks/                                (Keep as-is for now)
└── settings.json                         (MorphiZen-specific)
```

**Approach:**
1. **Update .gitignore** - Ignore symlinked skill directories
2. **Delete old skills** - Remove create-issue, fix-issue, resolve-ci copies
3. **Create symlinks** - Link to external devflow-kit skills
4. **Keep MorphiZen-specific** - build-and-test stays as real directory
5. **Update CONTRIBUTING.md** - Document devflow-kit setup for team
6. **Create PR** - Submit to ROCm/MorphiZen for review

**Benefits:**
- ✅ **Auto-updates** - Skill improvements immediately available
- ✅ **Zero PRs for infrastructure** - Workflow updates happen externally
- ✅ **Single source of truth** - Skills maintained in devflow-kit
- ✅ **Team optional** - Each developer chooses to set up devflow-kit
- ✅ **MorphiZen stays lean** - Only project-specific code committed

**Trade-offs:**
- ⚠️ **Per-developer setup** - Each team member sets up devflow-kit separately
- ⚠️ **Optional automation** - Not all team members may use it
- ⚠️ **External dependency** - Requires devflow-kit cloned locally

## Plans

- [MorphiZen Integration Plan](../plans/002-morphizen-integration-with-devflow-kit-plan.md) - Created 2026-02-08
