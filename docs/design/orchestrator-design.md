<!--
Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
Licensed under the MIT License.
-->
# Orchestrator Design Document

**Created:** 2026-02-08
**Status:** Design Document

---

## Overview

The Orchestrator is an interactive REPL tool that manages multiple parallel Claude Code sessions working in different workspace directories. It solves the problem of managing multiple terminal tabs/windows when working on multiple issues or projects simultaneously.

**Mental Model:** Terminal multiplexer (like tmux/screen) for Claude Code sessions.

**Key Benefits:**
- Work on multiple issues in parallel from a single terminal
- Automatic session state management and output collection
- Persistent conversation history across orchestrator restarts
- Clean workspace management and lifecycle

---

## Core Concepts

### Session

**Definition:** Session = Working directory + optional Claude Code process + conversation state

**Components:**
- **session_id**: Unique identifier (e.g., "morphizen-042")
- **working_dir**: Where Claude works (e.g., "workspace/issues/morphizen-042/morphizen")
- **process**: Optional subprocess.Popen object (in-memory only)
- **claude_session_id**: Claude's conversation ID (persisted to disk)
- **history**: Full prompt/response pairs (persisted to disk)

**Example:**
```
Session: morphizen-042
├── Working directory: workspace/issues/morphizen-042/morphizen/
├── Claude session ID: 550e8400-...
├── Process: subprocess.Popen (PID 12345) or None
└── History: [
      {prompt: "...", response: "...", cost: 0.05},
      ...
    ]
```

### Session States

```
┌─────────┐
│ CREATED │ - Workspace exists, never sent a prompt
└────┬────┘
     │ send first prompt
     ↓
┌─────────┐
│ RUNNING │ - Process actively working
└────┬────┘
     │ process finishes (auto-collected)
     ↓
┌─────────┐
│  IDLE   │ - Ready for new prompt
└────┬────┘
     │ send another prompt
     └──→ RUNNING (cycle)

Any state:
     │ delete
     ↓
┌──────────┐
│ ARCHIVED │ - Workspace deleted, history preserved
└──────────┘
```

**State Detection:**
```python
def get_state(session):
    if session.archived:
        return 'ARCHIVED'
    if session.process and session.process.poll() is None:
        return 'RUNNING'
    if len(session.history) == 0:
        return 'CREATED'
    return 'IDLE'
```

**Note:** No FINISHED state - output is auto-collected when process completes.

---

## Architecture

### Interactive REPL Shell

**Long-running orchestrator process:**
- Keeps child Claude processes alive (especially important on Windows)
- Maintains in-memory session objects with live subprocess references
- Polls for completed processes before each command
- No threading (avoids race conditions)

**Benefits:**
- ✅ Simple architecture (no daemon, no IPC)
- ✅ No race conditions (single-threaded)
- ✅ Child processes survive (parent is alive)
- ✅ Natural interactive workflow

### In-Memory + Disk Persistence

**In-Memory (Session objects):**
```python
class Session:
    # Persistent fields (saved to disk)
    session_id: str
    project: str
    issue_num: str | None
    working_dir: str
    claude_session_id: str | None
    history: List[dict]
    archived: bool

    # Live fields (NOT saved to disk)
    process: subprocess.Popen | None
    current_prompt: str | None
    output_file: str | None
    process_start_time: float | None
```

**On-Disk (.session.json):**
```json
{
  "session_id": "morphizen-042",
  "project": "morphizen",
  "issue_num": "042",
  "working_dir": "workspace/issues/morphizen-042/morphizen",
  "claude_session_id": "550e8400-...",
  "history": [
    {
      "prompt": "implement feature from plan",
      "response": "Feature implemented...",
      "cost": 0.42
    }
  ],
  "archived": false
}
```

**Why separate?**
- subprocess.Popen objects cannot be serialized
- Process PIDs are meaningless after orchestrator restarts
- History is valuable and must persist
- Live state is ephemeral and reconstructed on load

### Auto-Collection Pattern

**Automatic output collection:**
```python
class OrchestratorShell(cmd.Cmd):
    def precmd(self, line):
        """Called before EVERY command"""
        self.check_all_sessions()
        return line

    def check_all_sessions(self):
        """Poll all running processes"""
        for session in self.sessions.values():
            if session.process and session.process.poll() is not None:
                # Process finished - auto-collect
                self.collect_output(session)
                print(f"\n[Session {session.session_id} completed]")
                print(session.history[-1]['response'][:200] + "...")

    def collect_output(self, session):
        """Read output file, update history, clean up"""
        output = json.load(open(session.output_file))

        if not session.claude_session_id:
            session.claude_session_id = output['session_id']

        session.history.append({
            'prompt': session.current_prompt,
            'response': output['result'],
            'cost': output.get('cost', 0)
        })

        os.remove(session.output_file)
        session.process = None
        session.current_prompt = None
        session.output_file = None
        session.process_start_time = None

        self.save_session(session)
```

**Benefits:**
- User doesn't need manual `get` command
- Responses appear automatically when ready
- Simple state machine (no FINISHED state)

---

## File Structure

```
workspace/
├── cache/
│   ├── morphizen/              # Persistent clone (always main branch)
│   └── onnx-hipdnn-ep/         # Updated before each create
│
├── issues/                     # Issue-based workspaces
│   ├── morphizen-042/
│   │   ├── .session.json       # Session metadata (NOT in git)
│   │   ├── .output.json        # Temp output (deleted after collection)
│   │   └── morphizen/          # Git clone (working directory)
│   │       ├── .git/
│   │       └── src/
│   └── morphizen-043/
│       └── ...
│
├── work/                       # General workspaces (non-issue)
│   └── morphizen-debug-auth/
│       └── ...
│
├── sessions/
│   ├── active/
│   │   ├── morphizen-042.json  # Active session metadata
│   │   └── morphizen-043.json
│   └── archived/
│       └── morphizen-041.json  # Archived (workspace deleted)
│
└── .orchestrator/
    └── config.json             # User configuration
```

**Cache Strategy:**
- Cache updated on every `create` command
- Clone from cache (fast local copy) instead of remote
- Remotes fixed after clone (origin → upstream, add fork)

---

## Configuration

**Location:** `workspace/.orchestrator/config.json`

**Schema:**
```json
{
  "github": {
    "username": "wcy123"
  },
  "fork": {
    "morphizen": "https://github.com/custom-org/fork-name.git"
  }
}
```

**Fork URL Resolution:**
1. Check project-specific override: `config.fork.{project}`
2. Auto-generate from username: `https://github.com/{username}/{project}.git`
3. If no username configured, error

**Setup:**
```bash
orchestrator> config set github.username wcy123
orchestrator> config set fork.morphizen https://github.com/org/custom.git
```

---

## Commands

### `create <project> <name>`

**Purpose:** Create a new session with workspace.

**Usage:**
```bash
create morphizen 042           # Issue-based (numeric)
create morphizen debug-auth    # General workspace
```

**Steps:**
1. Validate project exists in `docs/projects/{project}/project.yaml`
2. Generate session_id: `{project}-{name}`
3. Check session doesn't already exist
4. Determine workspace type:
   - Numeric name → `workspace/issues/{session_id}/`
   - Other name → `workspace/work/{session_id}/`
5. Update/create cache: `workspace/cache/{project}/`
6. Clone from cache to workspace
7. Setup remotes:
   - `origin` → upstream (from project.yaml)
   - `fork` → user's fork (from config)
8. Create feature branch:
   - Issue: `feature/issue-{name}`
   - General: `feature/{name}`
9. Create .session.json with initial state
10. Save to `workspace/sessions/active/{session_id}.json`

**Initial State:** CREATED

**Errors:**
- Project not found
- Session already exists
- Git clone fails
- Fork URL not configured

---

### `send <session> "<prompt>"`

**Purpose:** Send a prompt to a session, starts Claude Code process.

**Valid States:** CREATED, IDLE
**Invalid States:** RUNNING (error: busy), ARCHIVED (error: archived)

**Steps:**
1. Load session from memory
2. Validate state (not RUNNING, not ARCHIVED)
3. Build Claude command:
   ```bash
   claude -p "{prompt}" --output-format json
   [--resume {claude_session_id}]  # If not first prompt
   ```
4. Spawn process:
   - Working directory: `session.working_dir`
   - Stdout: `workspace/issues/{session_id}/.output.json`
   - Stderr: Combined with stdout
5. Update session:
   - `process` = subprocess.Popen object
   - `current_prompt` = prompt
   - `output_file` = path to output
   - `process_start_time` = current time
6. Save to disk
7. Print confirmation

**State Transition:** → RUNNING

**TODO:**
- Decide on `--allowedTools` usage
- Decide on `--max-turns` limit

---

### `list`

**Purpose:** Show all active sessions (excludes archived).

**Output:**
```
Session ID           State      Elapsed    Current Work
--------------------------------------------------------------------------------
morphizen-042        RUNNING    2m 35s     implement feature from plan...
morphizen-043        IDLE       -          Last: run all tests...
onnx-015             CREATED    -          (never used)
```

**Columns:**
- **Session ID:** Unique identifier
- **State:** CREATED | IDLE | RUNNING
- **Elapsed:** Time since process started (RUNNING only)
- **Current Work:**
  - RUNNING: Current prompt (truncated to 45 chars)
  - IDLE: Last prompt from history
  - CREATED: "(never used)"

**Elapsed Time Format:**
- < 60s: "35s"
- < 1h: "2m 35s"
- >= 1h: "1h 25m"

---

### `history <session>`

**Purpose:** Show chronological list of all prompts (reverse numbered).

**Output:**
```
=== History for morphizen-042 ===

[4] read issue #042 and create implementation plan  ← Oldest, shown first
[3] implement the feature from the plan
[2] run tests and fix any failures
[1] commit the changes with proper message          ← Latest, shown last

Total: 4 prompts
Use 'show morphizen-042 <n>' to view details
```

**Numbering:** Reverse (latest = 1) for easy reference
**Display:** Chronological (oldest first) for natural reading

---

### `show <session> [range] [--summary]`

**Purpose:** Show detailed prompt/response pairs.

**Usage:**
```bash
show morphizen-042           # Show last entry (full)
show morphizen-042 2         # Show entry #2 (full)
show morphizen-042 1-3       # Show entries 1 through 3 (full)
show morphizen-042 --all     # Show all entries (full)
show morphizen-042 2 --summary  # Truncate long responses
```

**Default:** Show full response (no truncation)

**Output:**
```
[2] Prompt:
    run tests and fix any failures

    Response:
    I've run the test suite. Results:
    - 15 tests passed
    - 2 tests failed in auth module

    Fixed the failures by updating...
    [Full response shown by default]
```

**--summary flag:** Truncate responses > 500 chars

---

### `stop <session>`

**Purpose:** Kill a running process.

**Valid States:** RUNNING
**Invalid States:** IDLE, CREATED (error: not running)

**Steps:**
1. Validate session is RUNNING
2. Terminate process (SIGTERM)
3. Wait up to 5 seconds
4. Force kill if still alive (SIGKILL)
5. Clean up:
   - Delete output file if exists
   - Clear process, current_prompt, output_file
6. Save to disk

**Use Cases:**
- Wrong prompt sent
- Want to cancel and restart
- Process hanging

**State Transition:** → IDLE

---

### `delete <session>`

**Purpose:** Archive session (delete workspace) or permanently delete archived session.

**For Active Sessions (CREATED/IDLE):**
```bash
orchestrator> delete morphizen-042
This will archive session morphizen-042:
  - Delete workspace: workspace/issues/morphizen-042/
  - Preserve history: 4 prompts
Archive? (y/n): y
Deleted workspace: workspace/issues/morphizen-042
Session morphizen-042 archived (history preserved)
```

**For Archived Sessions:**
```bash
orchestrator> delete morphizen-042
WARNING: This will permanently delete session morphizen-042
History will be lost (4 prompts)
Delete permanently? (y/n): y
Session morphizen-042 deleted permanently
```

**Invalid States:** RUNNING (error: must stop first)

**Archiving Steps:**
1. Confirm with user
2. Delete workspace directory (entire tree)
3. Mark `archived = true`
4. Move session file: `active/` → `archived/`

**Permanent Deletion Steps:**
1. Confirm with user (strong warning)
2. Delete archived session file
3. Remove from in-memory sessions

---

## Session Lifecycle Example

```bash
# Create session
orchestrator> create morphizen 042
Session morphizen-042 created (CREATED)

# Send first prompt
orchestrator> send morphizen-042 "read issue and create plan"
Session morphizen-042 started (RUNNING, PID 12345)

# Wait... (auto-collected when done)
[Session morphizen-042 completed]
I've read issue #042...

# Send more work
orchestrator> send morphizen-042 "implement the feature"
Session morphizen-042 started (RUNNING, PID 12399)

# Check status while running
orchestrator> list
Session ID           State      Elapsed    Current Work
morphizen-042        RUNNING    1m 23s     implement the feature

# View history
orchestrator> history morphizen-042
[2] implement the feature
[1] read issue and create plan

# Show details
orchestrator> show morphizen-042 1
[1] Prompt:
    read issue and create plan

    Response:
    I've read issue #042...
    [Full response]

# Archive when done
orchestrator> delete morphizen-042
Archive? (y/n): y
Session morphizen-042 archived
```

---

## Implementation Notes

### Startup Flow

```python
class OrchestratorShell(cmd.Cmd):
    def __init__(self):
        self.sessions = {}
        self.load_config()
        self.load_all_sessions()

    def load_all_sessions(self):
        """Load from disk on startup"""
        # Active sessions
        for json_file in glob('workspace/sessions/active/*.json'):
            data = json.load(open(json_file))
            session = Session(data)

            # Check for orphaned output files
            output_file = f"workspace/issues/{session.session_id}/.output.json"
            if os.path.exists(output_file):
                session.output_file = output_file
                # Will be collected on first command via precmd()

            self.sessions[session.session_id] = session

        # Archived sessions (for viewing history, deletion)
        for json_file in glob('workspace/sessions/archived/*.json'):
            data = json.load(open(json_file))
            session = Session(data)
            self.sessions[session.session_id] = session
```

### Save Strategy

**When to save:**
- After `create` (new session)
- After `send` (process started)
- After auto-collection (history updated)
- After `stop` (state changed)
- After `delete` (archived or deleted)
- On shell exit (save all modified)

**What to save:**
- Only persistent fields (exclude process, output_file, etc.)
- Full history (no truncation)
- JSON format with indent=2 (human-readable)

### Error Handling

**Graceful degradation:**
- Cache update fails → warn, use stale cache
- Clone fails → error, don't create session
- Process spawn fails → error, clean up partial state
- Output file missing → warn, skip collection

**User-friendly errors:**
- Always explain what went wrong
- Suggest remediation steps
- Never crash the shell

---

## Future Considerations

### Integration with /fix-issue Skill

**Option A:** Orchestrator wraps skill
```bash
orchestrator> fix-issue morphizen 042
# Internally: create session, send "/fix-issue" prompt
```

**Option B:** Skill creates session
```bash
# Inside Claude
/fix-issue
# Skill calls: orchestrator.create_session(...)
```

**Option C:** Independent (current design)
- User creates session manually
- Runs /fix-issue inside Claude prompt
- Orchestrator is just session management

**Defer:** Start with Option C (independent), integrate later if needed.

### Additional Commands

**Potential additions:**
- `attach <session>` - Interactive mode (full TTY takeover)
- `rename <session> <new-name>` - Change session ID
- `clone <session> <new-name>` - Duplicate session
- `export <session> <file>` - Export history
- `import <file>` - Import history

**Defer:** Only add when proven necessary.

### Multi-User / Team Collaboration

**Questions:**
- Shared orchestrator instance?
- Locking for concurrent access?
- Remote orchestrator (client/server)?

**Defer:** Single-user design first, extend later.

### Performance Optimization

**Current approach:**
- Load all sessions on startup
- Save after each state change
- Poll processes on every command

**Future optimizations (if needed):**
- Lazy loading (load session on first access)
- Batch saves (save every N seconds)
- Event-driven collection (signal handlers)

**Defer:** Simple approach first, optimize if slow.

---

## Design Principles

### 1. Simplicity First

**Prefer:**
- Single-threaded over multi-threaded
- In-memory over database
- JSON files over complex persistence
- REPL over daemon + IPC

**Reason:** Easier to understand, debug, and maintain.

### 2. User Experience

**Guidelines:**
- Full output by default (no truncation)
- Auto-collection (no manual get)
- Confirmations for destructive actions
- Clear error messages with remediation
- Natural command names and arguments

### 3. Fail Gracefully

**Principles:**
- Warn but continue when possible
- Never crash the shell
- Preserve user data (history) at all costs
- Clean up partial state on errors

### 4. Separation of Concerns

**Clear boundaries:**
- Orchestrator = session management
- Claude Code = actual work
- Skills = workflow automation
- Each layer independent

---

## Related Documents

- [Multi-Project Architecture](multi-project-architecture.md) - Workspace and cache design
- [Issue Resolution Workflow](../workflows/issue-resolution-workflow.md) - /fix-issue integration
- [Git Workflow](../workflows/git-workflow.md) - Branch and remote management

---

## Revision History

- **2026-02-08:** Initial design document created from interactive discussion
