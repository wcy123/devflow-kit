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

# Helper function: copy directory recursively, checking each file
# Args: source_dir target_dir description_prefix
copy_dir_if_different() {
    local src_dir="$1"
    local dst_dir="$2"
    local desc_prefix="$3"

    mkdir -p "$dst_dir"

    # Find all files in source directory
    find "$src_dir" -type f | while read -r src_file; do
        # Calculate relative path
        local rel_path="${src_file#$src_dir/}"
        local dst_file="$dst_dir/$rel_path"
        local desc="$desc_prefix/$rel_path"

        copy_if_different "$src_file" "$dst_file" "$desc"
    done
}

# Copy Claude skills and configuration
echo "📦 Syncing Claude Code skills and hooks..."
copy_dir_if_different "$SOURCE_DIR/.claude/skills" "$TARGET_DIR/.claude/skills" ".claude/skills"
copy_dir_if_different "$SOURCE_DIR/.claude/hooks" "$TARGET_DIR/.claude/hooks" ".claude/hooks"
copy_if_different "$SOURCE_DIR/.claude/settings.json" "$TARGET_DIR/.claude/settings.json" ".claude/settings.json"
copy_if_different "$SOURCE_DIR/.claude/README.md" "$TARGET_DIR/.claude/README.md" ".claude/README.md"

# Copy workflow documentation
echo ""
echo "📄 Syncing workflow documentation..."
copy_dir_if_different "$SOURCE_DIR/docs/workflows" "$TARGET_DIR/docs/workflows" "docs/workflows"
copy_if_different "$SOURCE_DIR/docs/README.md" "$TARGET_DIR/docs/README.md" "docs/README.md"

# Copy project templates
echo ""
echo "📋 Syncing issue templates..."
mkdir -p "$TARGET_DIR/docs/project/issues"
copy_if_different "$SOURCE_DIR/docs/project/issues/TEMPLATE.md" "$TARGET_DIR/docs/project/issues/TEMPLATE.md" "docs/project/issues/TEMPLATE.md"

# Only copy project-specific files if they don't exist (never overwrite these)
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

echo "Next steps:"
echo "  1. cd $TARGET_DIR"
echo "  2. Review synced files"
if [ ${#WARNED_FILES[@]} -gt 0 ]; then
    echo "  3. Manually merge files with local modifications if needed"
fi
echo ""
