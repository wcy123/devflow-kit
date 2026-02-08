<!--
Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
Licensed under the MIT License.
-->
# Orchestrator - Multi-Session Manager for Claude Code

Interactive REPL tool for managing multiple parallel Claude Code sessions working in different workspace directories.

## Features

- **Parallel Sessions**: Work on multiple issues simultaneously from one terminal
- **Auto-Collection**: Automatic output collection when processes complete
- **Persistent History**: Full conversation history saved to disk
- **Tab Completion**: Session names and commands auto-complete
- **State Management**: Clean lifecycle management (CREATED → RUNNING → IDLE → ARCHIVED)

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Make executable (Unix-like systems)
chmod +x orchestrator.py
```

## Quick Start

```bash
# Start orchestrator
python orchestrator.py

# Configure GitHub username (one-time setup)
orchestrator> config set github.username your-username

# Create a session for issue #042
orchestrator> create morphizen 042

# Send work to the session
orchestrator> send morphizen-042 "read issue and create implementation plan"

# List all sessions
orchestrator> list

# View history
orchestrator> history morphizen-042

# Show detailed response
orchestrator> show morphizen-042 1

# Exit
orchestrator> exit
```

## Commands

### Session Management

- `create <project> <name>` - Create new session with workspace
- `delete <session>` - Archive or permanently delete session
- `list` - Show all active sessions
- `config set/get <key> [value]` - Manage configuration

### Working with Sessions

- `send <session> "<prompt>"` - Send prompt to session
- `stop <session>` - Stop running process
- `history <session>` - Show prompt history
- `show <session> [n]` - Show detailed prompt/response

### Examples

```bash
# Issue-based session
orchestrator> create morphizen 042
orchestrator> send morphizen-042 "implement feature from plan"

# General workspace
orchestrator> create morphizen debug-auth
orchestrator> send morphizen-debug-auth "investigate authentication bug"

# View history (reverse numbered, latest = 1)
orchestrator> history morphizen-042
[3] commit changes
[2] run tests
[1] implement feature

# Show latest response (full)
orchestrator> show morphizen-042 1

# Show range with summary
orchestrator> show morphizen-042 1-3 --summary

# Stop if wrong prompt sent
orchestrator> stop morphizen-042
orchestrator> send morphizen-042 "correct prompt"

# Archive when done
orchestrator> delete morphizen-042
```

## Configuration

Configuration stored in `workspace/.orchestrator/config.json`

### GitHub Username

Required for auto-generating fork URLs:

```bash
orchestrator> config set github.username wcy123
```

### Project-Specific Fork Override

```bash
orchestrator> config set fork.morphizen https://github.com/org/custom-fork.git
```

## Session States

- **CREATED** - Workspace exists, never sent a prompt
- **IDLE** - Ready for new prompt, no running process
- **RUNNING** - Process actively working
- **ARCHIVED** - Workspace deleted, history preserved

## File Structure

```
workspace/
├── cache/
│   └── morphizen/              # Persistent clone (always main)
├── issues/
│   └── morphizen-042/
│       ├── .session.json       # Session metadata
│       └── morphizen/          # Git clone (working directory)
├── sessions/
│   ├── active/
│   │   └── morphizen-042.json  # Active session data
│   └── archived/
│       └── morphizen-041.json  # Archived session data
└── .orchestrator/
    ├── config.json             # User configuration
    └── history                 # Command history
```

## Design

See [docs/design/orchestrator-design.md](../docs/design/orchestrator-design.md) for detailed design documentation.

## Requirements

- Python 3.7+
- PyYAML
- readline (standard library, may need `python-readline` on some systems)
- Git
- Claude Code CLI

## License

MIT License - See LICENSE file for details
