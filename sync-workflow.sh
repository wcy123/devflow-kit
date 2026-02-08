#!/bin/bash
# sync-workflow.sh
# Sync workflow system to another project
# Usage: ./sync-workflow.sh /path/to/target-project

SOURCE_DIR="$(cd "$(dirname "$0")" && pwd)"
TARGET_DIR="$1"

if [ -z "$TARGET_DIR" ]; then
    echo "Usage: $0 /path/to/target-project"
    echo ""
    echo "Example:"
    echo "  $0 /path/to/my-project"
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

# Copy Claude skills and configuration
echo "📦 Copying Claude Code skills and hooks..."
mkdir -p "$TARGET_DIR/.claude"
cp -r "$SOURCE_DIR/.claude/skills" "$TARGET_DIR/.claude/"
cp -r "$SOURCE_DIR/.claude/hooks" "$TARGET_DIR/.claude/"
cp "$SOURCE_DIR/.claude/settings.json" "$TARGET_DIR/.claude/"
cp "$SOURCE_DIR/.claude/README.md" "$TARGET_DIR/.claude/"

# Copy workflow documentation
echo "📄 Copying workflow documentation..."
mkdir -p "$TARGET_DIR/docs/workflows"
cp -r "$SOURCE_DIR/docs/workflows"/* "$TARGET_DIR/docs/workflows/"
cp "$SOURCE_DIR/docs/README.md" "$TARGET_DIR/docs/"

# Copy project templates (don't overwrite existing backlog)
echo "📋 Copying issue templates..."
mkdir -p "$TARGET_DIR/docs/project/issues"
cp "$SOURCE_DIR/docs/project/issues/TEMPLATE.md" "$TARGET_DIR/docs/project/issues/"

# Only copy these if they don't exist (don't overwrite project data)
if [ ! -f "$TARGET_DIR/docs/project/backlog.md" ]; then
    echo "📝 Copying backlog.md (new file)"
    cp "$SOURCE_DIR/docs/project/backlog.md" "$TARGET_DIR/docs/project/"
else
    echo "⏭️  Skipping backlog.md (already exists)"
fi

if [ ! -f "$TARGET_DIR/docs/project/completed-issues.md" ]; then
    echo "📝 Copying completed-issues.md (new file)"
    cp "$SOURCE_DIR/docs/project/completed-issues.md" "$TARGET_DIR/docs/project/"
else
    echo "⏭️  Skipping completed-issues.md (already exists)"
fi

if [ ! -f "$TARGET_DIR/docs/project/issue-dependency-analysis.md" ]; then
    echo "📝 Copying issue-dependency-analysis.md (new file)"
    cp "$SOURCE_DIR/docs/project/issue-dependency-analysis.md" "$TARGET_DIR/docs/project/"
else
    echo "⏭️  Skipping issue-dependency-analysis.md (already exists)"
fi

echo ""
echo "✅ Sync complete!"
echo ""
echo "Synced:"
echo "  ✅ Claude skills (create-issue, fix-issue, resolve-ci)"
echo "  ✅ Claude hooks (workflow enforcement)"
echo "  ✅ Workflow documentation (issue-resolution, git workflows)"
echo "  ✅ Issue template"
echo "  ✅ docs/README.md"
echo ""
echo "Project-specific files (preserved if existing):"
echo "  📋 backlog.md"
echo "  📋 completed-issues.md"
echo "  📋 issue-dependency-analysis.md"
echo ""
echo "Next steps:"
echo "  1. cd $TARGET_DIR"
echo "  2. Review copied files"
echo "  3. Customize for your project as needed"
