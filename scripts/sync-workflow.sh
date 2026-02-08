#!/bin/bash
# sync-workflow.sh
# Sync workflow system to another project
# Usage: ./sync-workflow.sh /path/to/target-project [--force]

SOURCE_DIR="$(cd "$(dirname "$0")/.." && pwd)"
TARGET_DIR="$1"
FORCE_MODE=false

# Parse arguments
if [ "$2" = "--force" ]; then
    FORCE_MODE=true
fi

if [ -z "$TARGET_DIR" ]; then
    echo "Usage: $0 /path/to/target-project [--force]"
    echo ""
    echo "Options:"
    echo "  --force    Overwrite modified files without prompting"
    echo ""
    echo "Example:"
    echo "  $0 /path/to/my-project"
    echo "  $0 /path/to/my-project --force"
    exit 1
fi

if [ ! -d "$TARGET_DIR" ]; then
    echo "Error: Target directory does not exist: $TARGET_DIR"
    exit 1
fi

echo "=== Syncing Workflow System ==="
echo "Source: $SOURCE_DIR"
echo "Target: $TARGET_DIR"
echo ""

# Track what was synced
SYNCED_FILES=()
SKIPPED_FILES=()
WARNED_FILES=()

# Helper function: copy file if different
# Args: source_file target_file description
copy_if_different() {
    local src="$1"
    local dst="$2"
    local desc="$3"

    if [ ! -f "$dst" ]; then
        # Target doesn't exist, copy it
        mkdir -p "$(dirname "$dst")"
        cp "$src" "$dst"
        SYNCED_FILES+=("$desc (new)")
        return 0
    fi

    # Check if files are different
    if cmp -s "$src" "$dst"; then
        # Files are identical, skip
        SKIPPED_FILES+=("$desc (unchanged)")
        return 0
    fi

    # Files are different
    if [ "$FORCE_MODE" = true ]; then
        cp "$src" "$dst"
        SYNCED_FILES+=("$desc (updated)")
        return 0
    else
        # Warn user
        echo "⚠️  WARNING: $desc has local modifications"
        echo "   Source: $src"
        echo "   Target: $dst"
        echo ""
        read -p "   Overwrite? [y/N/d(iff)] " -n 1 -r
        echo ""
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            cp "$src" "$dst"
            SYNCED_FILES+=("$desc (overwritten)")
        elif [[ $REPLY =~ ^[Dd]$ ]]; then
            echo "   --- Differences ---"
            diff -u "$dst" "$src" || true
            echo "   --- End of diff ---"
            echo ""
            read -p "   Overwrite after seeing diff? [y/N] " -n 1 -r
            echo ""
            if [[ $REPLY =~ ^[Yy]$ ]]; then
                cp "$src" "$dst"
                SYNCED_FILES+=("$desc (overwritten)")
            else
                WARNED_FILES+=("$desc (kept local)")
            fi
        else
            WARNED_FILES+=("$desc (kept local)")
        fi
    fi
}

# Helper function: copy file only if exists in source
copy_file() {
    local rel_path="$1"
    local desc="$2"
    local src="$SOURCE_DIR/$rel_path"
    local dst="$TARGET_DIR/$rel_path"

    if [ -f "$src" ]; then
        copy_if_different "$src" "$dst" "$desc"
    else
        echo "⚠️  Warning: Source file not found: $src"
    fi
}

echo "📦 Syncing Claude Code configuration..."
echo ""

# Claude configuration files
copy_file ".claude/README.md" ".claude/README.md"
copy_file ".claude/settings.json" ".claude/settings.json"

# Claude hooks
echo ""
echo "🪝 Syncing Claude hooks..."
copy_file ".claude/hooks/pre-bash.py" ".claude/hooks/pre-bash.py"
copy_file ".claude/hooks/post-bash.py" ".claude/hooks/post-bash.py"
copy_file ".claude/hooks/post-file-edit.py" ".claude/hooks/post-file-edit.py"

# Claude skills
echo ""
echo "🛠️  Syncing Claude skills..."
echo ""
echo "  create-issue skill:"
copy_file ".claude/skills/create-issue/SKILL.md" ".claude/skills/create-issue/SKILL.md"

echo ""
echo "  fix-issue skill:"
copy_file ".claude/skills/fix-issue/SKILL.md" ".claude/skills/fix-issue/SKILL.md"
copy_file ".claude/skills/fix-issue/README.md" ".claude/skills/fix-issue/README.md"
copy_file ".claude/skills/fix-issue/setup-workspace.py" ".claude/skills/fix-issue/setup-workspace.py"
copy_file ".claude/skills/fix-issue/TEST_REPORT.md" ".claude/skills/fix-issue/TEST_REPORT.md"

echo ""
echo "  resolve-ci skill:"
copy_file ".claude/skills/resolve-ci/SKILL.md" ".claude/skills/resolve-ci/SKILL.md"
copy_file ".claude/skills/resolve-ci/README.md" ".claude/skills/resolve-ci/README.md"
copy_file ".claude/skills/resolve-ci/monitor-pr.py" ".claude/skills/resolve-ci/monitor-pr.py"

# Workflow documentation
echo ""
echo "📄 Syncing workflow documentation..."
copy_file "docs/README.md" "docs/README.md"
copy_file "docs/workflows/issue-resolution-workflow.md" "docs/workflows/issue-resolution-workflow.md"
copy_file "docs/workflows/git-workflow.md" "docs/workflows/git-workflow.md"
copy_file "docs/workflows/git-workflow-reference.md" "docs/workflows/git-workflow-reference.md"

# Project templates
echo ""
echo "📋 Syncing project templates..."
copy_file "docs/project/issues/TEMPLATE.md" "docs/project/issues/TEMPLATE.md"

# Project-specific files (only if they don't exist)
echo ""
echo "📝 Checking project-specific files..."
if [ ! -f "$TARGET_DIR/docs/project/backlog.md" ]; then
    cp "$SOURCE_DIR/docs/project/backlog.md" "$TARGET_DIR/docs/project/"
    SYNCED_FILES+=("docs/project/backlog.md (new)")
else
    SKIPPED_FILES+=("docs/project/backlog.md (project-specific, preserved)")
fi

if [ ! -f "$TARGET_DIR/docs/project/completed-issues.md" ]; then
    cp "$SOURCE_DIR/docs/project/completed-issues.md" "$TARGET_DIR/docs/project/"
    SYNCED_FILES+=("docs/project/completed-issues.md (new)")
else
    SKIPPED_FILES+=("docs/project/completed-issues.md (project-specific, preserved)")
fi

if [ ! -f "$TARGET_DIR/docs/project/issue-dependency-analysis.md" ]; then
    cp "$SOURCE_DIR/docs/project/issue-dependency-analysis.md" "$TARGET_DIR/docs/project/"
    SYNCED_FILES+=("docs/project/issue-dependency-analysis.md (new)")
else
    SKIPPED_FILES+=("docs/project/issue-dependency-analysis.md (project-specific, preserved)")
fi

# Summary
echo ""
echo "========================================"
echo "✅ Sync Complete!"
echo "========================================"
echo ""

if [ ${#SYNCED_FILES[@]} -gt 0 ]; then
    echo "✅ Synced (${#SYNCED_FILES[@]} files):"
    for file in "${SYNCED_FILES[@]}"; do
        echo "   ✅ $file"
    done
    echo ""
fi

if [ ${#SKIPPED_FILES[@]} -gt 0 ]; then
    echo "⏭️  Skipped (${#SKIPPED_FILES[@]} files):"
    for file in "${SKIPPED_FILES[@]}"; do
        echo "   ⏭️  $file"
    done
    echo ""
fi

if [ ${#WARNED_FILES[@]} -gt 0 ]; then
    echo "⚠️  Kept local modifications (${#WARNED_FILES[@]} files):"
    for file in "${WARNED_FILES[@]}"; do
        echo "   ⚠️  $file"
    done
    echo ""
    echo "💡 Tip: Review these files manually or use --force to overwrite all"
    echo ""
fi

echo "Files synced:"
echo "  📦 Claude configuration: README.md, settings.json"
echo "  🪝 Claude hooks: pre-bash.py, post-bash.py, post-file-edit.py"
echo "  🛠️  Claude skills: create-issue, fix-issue, resolve-ci"
echo "  📄 Workflow docs: issue-resolution, git-workflow, git-workflow-reference"
echo "  📋 Templates: issue TEMPLATE.md"
echo ""
echo "Next steps:"
echo "  1. cd $TARGET_DIR"
echo "  2. Review synced files"
if [ ${#WARNED_FILES[@]} -gt 0 ]; then
    echo "  3. Manually merge files with local modifications if needed"
fi
echo ""
