<!--
Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
Licensed under the MIT License.
-->
# Issue #001: Restructure and Rename to devflow-kit

## Metadata
- **Type:** Refactoring
- **Priority:** HIGH
- **Created:** 2026-02-08
- **Dependencies:** None

## Description

Restructure the project to support multi-project tracking and rename from `work_log` to `devflow-kit` for public sharing. This establishes the foundation for managing multiple projects (MorphiZen, onnx-hipdnn-ep, etc.) from a single workflow framework.

## Problem

**Current design:**
```
work_log/
└── docs/
    └── project/          # Single project tracking
        ├── backlog.md
        └── issues/
```

**Why this is problematic:**
1. **Single project limitation** - Cannot track multiple projects simultaneously
2. **Misleading name** - "work_log" doesn't describe the workflow automation purpose
3. **Not shareable** - Generic name doesn't convey value to other teams
4. **No public presence** - Only exists locally/on GHE, not discoverable

**Impact:**
- Cannot integrate with MorphiZen while maintaining devflow-kit's own backlog
- Difficult to share with teams - name doesn't explain purpose
- No way to track non-intrusive projects (like onnx-hipdnn-ep)
- Missing public portfolio piece

## Solution

**Proposed structure:**
```
devflow-kit/                              # Renamed from work_log
└── docs/
    ├── projects/                         # Multi-project support
    │   ├── devflow-kit/                  # Meta: issues about devflow-kit itself
    │   │   ├── backlog.md                # (migrated from docs/project/)
    │   │   ├── completed-issues.md
    │   │   ├── issue-dependency-analysis.md
    │   │   └── issues/
    │   ├── onnx-hipdnn-ep/               # (future: non-intrusive project)
    │   └── ...
    └── workflows/                        # Generic workflow docs (unchanged)
```

**Approach:**
1. **Restructure** - Move `docs/project/` → `docs/projects/devflow-kit/`
2. **Rename** - Rename directory `work_log` → `devflow-kit`
3. **Public repo** - Create `github.com/wcy123/devflow-kit` (public)
4. **Git setup** - Update remote to point to public GitHub
5. **Push** - Make public for sharing
6. **Verify** - Test that skills still work

**Benefits:**
- ✅ **Multi-project support** - Can track MorphiZen, onnx-hipdnn-ep separately
- ✅ **Clear naming** - "devflow-kit" describes developer workflow toolkit
- ✅ **Shareable** - Public repo for team adoption
- ✅ **Discoverable** - Portfolio piece on GitHub
- ✅ **Foundation** - Enables all future multi-project work

## Plans

- [Restructure and Rename Plan](../plans/001-restructure-and-rename-to-devflow-kit-plan.md) - Created 2026-02-08
