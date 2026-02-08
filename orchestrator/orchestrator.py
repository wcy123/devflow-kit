#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
# Licensed under the MIT License.
#
"""
Orchestrator - Interactive session manager for multiple parallel Claude Code sessions.

This module provides a REPL interface for managing multiple Claude Code sessions
working in different workspace directories. It enables parallel work on multiple
issues or projects from a single terminal session.
"""

import cmd
import json
import os
import readline
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple


class Session:
    """Represents a single Claude Code session with its workspace and state.

    A session combines a working directory, an optional running Claude Code process,
    and the conversation history. Sessions can be in different states (CREATED, IDLE,
    RUNNING, ARCHIVED) based on their process status and history.

    Attributes:
        session_id: Unique identifier (e.g., "morphizen-042")
        project: Project name (e.g., "morphizen")
        issue_num: Issue number or None for general workspaces
        working_dir: Absolute path to git clone working directory
        claude_session_id: Claude's conversation ID (None until first prompt)
        history: List of prompt/response pairs with costs
        archived: Whether workspace has been deleted
        process: Live subprocess.Popen object (not persisted)
        current_prompt: Current prompt being processed (not persisted)
        output_file: Path to temporary output file (not persisted)
        process_start_time: When current process started (not persisted)
    """

    def __init__(self, data: dict):
        """Initialize session from persisted data.

        Args:
            data: Dictionary loaded from .session.json file
        """
        # Persistent fields (saved to disk)
        self.session_id: str = data['session_id']
        self.project: str = data['project']
        self.issue_num: Optional[str] = data.get('issue_num')
        self.working_dir: str = data['working_dir']
        self.claude_session_id: Optional[str] = data.get('claude_session_id')
        self.history: List[dict] = data.get('history', [])
        self.archived: bool = data.get('archived', False)

        # Live fields (NOT saved to disk)
        self.process: Optional[subprocess.Popen] = None
        self.current_prompt: Optional[str] = None
        self.output_file: Optional[str] = None
        self.process_start_time: Optional[float] = None

    def to_dict(self) -> dict:
        """Serialize session for disk persistence.

        Returns:
            Dictionary with only persistent fields (excludes live process objects)
        """
        return {
            'session_id': self.session_id,
            'project': self.project,
            'issue_num': self.issue_num,
            'working_dir': self.working_dir,
            'claude_session_id': self.claude_session_id,
            'history': self.history,
            'archived': self.archived
        }

    def get_state(self) -> str:
        """Determine current session state.

        Returns:
            One of: 'ARCHIVED', 'RUNNING', 'CREATED', 'IDLE'
        """
        if self.archived:
            return 'ARCHIVED'

        # Check if process is alive
        if self.process and self.process.poll() is None:
            return 'RUNNING'

        # Check if output file exists (process finished but not collected)
        if self.output_file and os.path.exists(self.output_file):
            # This shouldn't happen due to auto-collection, but check anyway
            return 'RUNNING'  # Will be collected on next precmd()

        # Never sent a prompt
        if len(self.history) == 0:
            return 'CREATED'

        # Ready for new prompt
        return 'IDLE'


class Config:
    """Manages orchestrator configuration (GitHub username, fork URLs, etc.)."""

    def __init__(self, config_file: str = 'workspace/.orchestrator/config.json'):
        """Initialize configuration.

        Args:
            config_file: Path to configuration file
        """
        self.config_file = config_file
        self.data = self._load()

    def _load(self) -> dict:
        """Load configuration from disk or create default."""
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                return json.load(f)

        # Default configuration
        return {
            'github': {},
            'fork': {}
        }

    def save(self):
        """Save configuration to disk."""
        os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
        with open(self.config_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def get(self, key: str, default=None):
        """Get configuration value by dot-notation key.

        Args:
            key: Dot-separated key path (e.g., "github.username")
            default: Default value if key doesn't exist

        Returns:
            Configuration value or default
        """
        keys = key.split('.')
        value = self.data
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

    def set(self, key: str, value):
        """Set configuration value by dot-notation key.

        Args:
            key: Dot-separated key path (e.g., "github.username")
            value: Value to set
        """
        keys = key.split('.')
        data = self.data

        # Navigate to parent dict
        for k in keys[:-1]:
            if k not in data:
                data[k] = {}
            data = data[k]

        # Set value
        data[keys[-1]] = value
        self.save()

    def get_fork_url(self, project: str) -> Optional[str]:
        """Get fork URL for a project.

        First checks for project-specific override, then auto-generates
        from GitHub username.

        Args:
            project: Project name

        Returns:
            Fork URL or None if username not configured
        """
        # Check project-specific override
        override = self.get(f'fork.{project}')
        if override:
            return override

        # Auto-generate from username
        username = self.get('github.username')
        if username:
            return f"https://github.com/{username}/{project}.git"

        return None


class OrchestratorShell(cmd.Cmd):
    """Interactive REPL shell for managing Claude Code sessions.

    Provides commands for creating sessions, sending prompts, viewing history,
    and managing session lifecycle. Automatically collects completed process
    outputs before each command.
    """

    intro = "Orchestrator - Multi-session manager for Claude Code\nType 'help' for commands, 'exit' to quit\n"
    prompt = 'orchestrator> '

    def __init__(self):
        """Initialize the orchestrator shell."""
        super().__init__()

        self.sessions: Dict[str, Session] = {}
        self.config = Config()

        # Setup readline
        self._setup_readline()

        # Load existing sessions
        self._load_all_sessions()

        print(f"Loaded {len([s for s in self.sessions.values() if not s.archived])} active sessions")

    def _setup_readline(self):
        """Configure readline for tab completion and history."""
        # Configure tab completion
        readline.set_completer_delims(' \t\n')
        readline.parse_and_bind('tab: complete')

        # Load command history
        self.history_file = 'workspace/.orchestrator/history'
        if os.path.exists(self.history_file):
            readline.read_history_file(self.history_file)

        # Limit history size
        readline.set_history_length(1000)

    def _load_all_sessions(self):
        """Load all sessions from disk (both active and archived)."""
        # Load active sessions
        active_dir = Path('workspace/sessions/active')
        if active_dir.exists():
            for json_file in active_dir.glob('*.json'):
                self._load_session(json_file)

        # Load archived sessions (for history viewing and deletion)
        archived_dir = Path('workspace/sessions/archived')
        if archived_dir.exists():
            for json_file in archived_dir.glob('*.json'):
                self._load_session(json_file)

    def _load_session(self, json_file: Path):
        """Load a single session from JSON file.

        Args:
            json_file: Path to .session.json file
        """
        with open(json_file, 'r') as f:
            data = json.load(f)

        session = Session(data)

        # Check for orphaned output files (process died while orchestrator was closed)
        if not session.archived:
            workspace_base = self._get_workspace_base(session.session_id)
            output_file = os.path.join(workspace_base, '.output.json')
            if os.path.exists(output_file):
                # Will be collected on first precmd()
                session.output_file = output_file

        self.sessions[session.session_id] = session

    def _get_workspace_base(self, session_id: str) -> str:
        """Get workspace base directory for a session.

        Args:
            session_id: Session identifier

        Returns:
            Path to workspace directory (issues/ or work/)
        """
        # Check if it exists in issues/
        issues_path = f"workspace/issues/{session_id}"
        if os.path.exists(issues_path):
            return issues_path

        # Otherwise assume work/
        return f"workspace/work/{session_id}"

    def _save_session(self, session: Session):
        """Save session to disk.

        Args:
            session: Session to save
        """
        # Determine directory
        if session.archived:
            session_dir = 'workspace/sessions/archived'
        else:
            session_dir = 'workspace/sessions/active'

        os.makedirs(session_dir, exist_ok=True)

        # Write JSON
        json_file = os.path.join(session_dir, f'{session.session_id}.json')
        with open(json_file, 'w') as f:
            json.dump(session.to_dict(), f, indent=2)

    def precmd(self, line: str) -> str:
        """Hook called before each command - check for completed processes.

        This is where auto-collection happens: we poll all running processes
        and collect output for any that have finished.

        Args:
            line: Command line entered by user

        Returns:
            The command line (unchanged)
        """
        self._check_all_sessions()
        return line

    def _check_all_sessions(self):
        """Check all sessions for completed processes and auto-collect."""
        for session in self.sessions.values():
            # Skip if no process
            if not session.process:
                continue

            # Check if process finished
            if session.process.poll() is not None:
                # Process completed - collect output
                self._collect_output(session)

                # Notify user
                print(f"\n[Session {session.session_id} completed]")
                if session.history:
                    response = session.history[-1]['response']
                    # Show preview (first 200 chars)
                    preview = response[:200]
                    if len(response) > 200:
                        preview += "..."
                    print(preview)
                print()

    def _collect_output(self, session: Session):
        """Collect output from finished process and update session.

        Args:
            session: Session with finished process
        """
        try:
            # Read output file
            with open(session.output_file, 'r') as f:
                output = json.load(f)

            # Extract claude_session_id if first prompt
            if not session.claude_session_id and 'session_id' in output:
                session.claude_session_id = output['session_id']

            # Add to history
            session.history.append({
                'prompt': session.current_prompt,
                'response': output.get('result', ''),
                'cost': output.get('cost', 0)
            })

            # Clean up
            os.remove(session.output_file)

        except Exception as e:
            print(f"Warning: Failed to collect output for {session.session_id}: {e}")

        finally:
            # Always clear process state
            session.process = None
            session.current_prompt = None
            session.output_file = None
            session.process_start_time = None

            # Save updated session
            self._save_session(session)

    def _format_duration(self, seconds: float) -> str:
        """Format elapsed time as human-readable string.

        Args:
            seconds: Elapsed seconds

        Returns:
            Formatted string like "2m 35s" or "1h 25m"
        """
        if seconds < 60:
            return f"{int(seconds)}s"
        elif seconds < 3600:
            minutes = int(seconds / 60)
            secs = int(seconds % 60)
            return f"{minutes}m {secs}s"
        else:
            hours = int(seconds / 3600)
            minutes = int((seconds % 3600) / 60)
            return f"{hours}h {minutes}m"

    # ========================================================================
    # Tab completion methods
    # ========================================================================

    def complete_send(self, text: str, line: str, begidx: int, endidx: int) -> List[str]:
        """Tab completion for send command - suggests active session IDs."""
        active = [s for s in self.sessions.keys() if not self.sessions[s].archived]
        return [sid for sid in active if sid.startswith(text)]

    def complete_show(self, text: str, line: str, begidx: int, endidx: int) -> List[str]:
        """Tab completion for show command."""
        return self.complete_send(text, line, begidx, endidx)

    def complete_history(self, text: str, line: str, begidx: int, endidx: int) -> List[str]:
        """Tab completion for history command."""
        return self.complete_send(text, line, begidx, endidx)

    def complete_stop(self, text: str, line: str, begidx: int, endidx: int) -> List[str]:
        """Tab completion for stop command."""
        return self.complete_send(text, line, begidx, endidx)

    def complete_delete(self, text: str, line: str, begidx: int, endidx: int) -> List[str]:
        """Tab completion for delete command - includes archived sessions."""
        return [sid for sid in self.sessions.keys() if sid.startswith(text)]

    # ========================================================================
    # Command implementations
    # ========================================================================

    def do_create(self, args: str):
        """Create a new session with workspace.

        Usage: create <project> <name>

        Examples:
            create morphizen 042           # Issue-based workspace
            create morphizen debug-auth    # General workspace
        """
        parts = args.split()
        if len(parts) != 2:
            print("Usage: create <project> <name>")
            return

        project, name = parts
        session_id = f"{project}-{name}"

        # Check if session already exists
        if session_id in self.sessions:
            print(f"Error: Session {session_id} already exists")
            return

        # Check if project exists
        project_yaml = f"docs/projects/{project}/project.yaml"
        if not os.path.exists(project_yaml):
            print(f"Error: Project {project} not found (missing {project_yaml})")
            return

        # Load project configuration
        try:
            import yaml
            with open(project_yaml, 'r') as f:
                project_config = yaml.safe_load(f)
            git_url = project_config.get('git_url')
            if not git_url:
                print(f"Error: No git_url in {project_yaml}")
                return
        except Exception as e:
            print(f"Error: Failed to load project config: {e}")
            return

        # Determine workspace type
        if name.isdigit():
            workspace_base = f"workspace/issues/{session_id}"
            branch_name = f"feature/issue-{name}"
        else:
            workspace_base = f"workspace/work/{session_id}"
            branch_name = f"feature/{name}"

        # Check if workspace already exists
        if os.path.exists(workspace_base):
            print(f"Error: Workspace directory already exists: {workspace_base}")
            return

        print(f"Creating session {session_id}...")

        # Update/create cache
        cache_dir = f"workspace/cache/{project}"
        if not os.path.exists(cache_dir):
            print(f"Cloning {project} to cache...")
            try:
                subprocess.run(['git', 'clone', git_url, cache_dir], check=True,
                             capture_output=True, text=True)
                print(f"✓ Created cache")
            except subprocess.CalledProcessError as e:
                print(f"Error: Failed to clone repository: {e.stderr}")
                return
        else:
            print(f"Updating cache...")
            try:
                subprocess.run(['git', '-C', cache_dir, 'pull', 'origin', 'main'],
                             check=True, capture_output=True, text=True)
                print(f"✓ Updated cache")
            except subprocess.CalledProcessError as e:
                print(f"Warning: Failed to update cache: {e.stderr}")
                print("Continuing with existing cache...")

        # Create workspace directory
        os.makedirs(workspace_base, exist_ok=True)

        # Clone from cache
        working_dir = os.path.join(workspace_base, project)
        print(f"Cloning from cache...")
        try:
            subprocess.run(['git', 'clone', cache_dir, working_dir], check=True,
                         capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to clone from cache: {e.stderr}")
            shutil.rmtree(workspace_base)
            return

        # Fix remotes
        print(f"Setting up remotes...")
        try:
            # Set origin to upstream
            subprocess.run(['git', '-C', working_dir, 'remote', 'set-url', 'origin', git_url],
                         check=True, capture_output=True, text=True)

            # Add fork remote
            fork_url = self.config.get_fork_url(project)
            if not fork_url:
                print(f"Warning: No fork URL configured. Set with: config set github.username <username>")
            else:
                subprocess.run(['git', '-C', working_dir, 'remote', 'add', 'fork', fork_url],
                             check=True, capture_output=True, text=True)
                print(f"✓ Added fork remote: {fork_url}")
        except subprocess.CalledProcessError as e:
            print(f"Warning: Failed to setup remotes: {e.stderr}")

        # Create feature branch
        print(f"Creating branch {branch_name}...")
        try:
            subprocess.run(['git', '-C', working_dir, 'checkout', '-b', branch_name],
                         check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            print(f"Error: Failed to create branch: {e.stderr}")
            shutil.rmtree(workspace_base)
            return

        # Create session object
        session = Session({
            'session_id': session_id,
            'project': project,
            'issue_num': name if name.isdigit() else None,
            'working_dir': working_dir,
            'claude_session_id': None,
            'history': [],
            'archived': False
        })

        # Save session
        self.sessions[session_id] = session
        self._save_session(session)

        print(f"\n✓ Session {session_id} created (CREATED)")
        print(f"  Workspace: {workspace_base}")
        print(f"  Branch: {branch_name}")

    def do_send(self, args: str):
        """Send a prompt to a session.

        Usage: send <session> "<prompt>"

        Example:
            send morphizen-042 "implement feature from plan"
        """
        # Parse session ID and prompt
        parts = args.split(maxsplit=1)
        if len(parts) != 2:
            print("Usage: send <session> \"<prompt>\"")
            return

        session_id, prompt = parts

        # Strip quotes if present
        if prompt.startswith('"') and prompt.endswith('"'):
            prompt = prompt[1:-1]
        elif prompt.startswith("'") and prompt.endswith("'"):
            prompt = prompt[1:-1]

        # Validate session exists
        if session_id not in self.sessions:
            print(f"Error: Session '{session_id}' not found")
            return

        session = self.sessions[session_id]
        state = session.get_state()

        # Check state
        if state == 'RUNNING':
            print(f"Error: Session {session_id} is busy. Wait or run: stop {session_id}")
            return

        if state == 'ARCHIVED':
            print(f"Error: Session {session_id} is archived")
            return

        # Build Claude command
        cmd = ['claude', '-p', prompt, '--output-format', 'json']

        # Resume existing session if not first prompt
        if session.claude_session_id:
            cmd.extend(['--resume', session.claude_session_id])

        # Setup output file
        workspace_base = self._get_workspace_base(session_id)
        output_file = os.path.join(workspace_base, '.output.json')

        # Spawn process
        try:
            with open(output_file, 'w') as f:
                proc = subprocess.Popen(
                    cmd,
                    cwd=session.working_dir,
                    stdout=f,
                    stderr=subprocess.STDOUT
                )
        except Exception as e:
            print(f"Error: Failed to spawn Claude process: {e}")
            return

        # Update session state
        session.process = proc
        session.current_prompt = prompt
        session.output_file = output_file
        session.process_start_time = time.time()

        # Save session
        self._save_session(session)

        print(f"Session {session_id} started (RUNNING, PID {proc.pid})")

    def do_list(self, args: str):
        """List all active sessions.

        Usage: list
        """
        # Filter active sessions
        active = [s for s in self.sessions.values() if not s.archived]

        if not active:
            print("No active sessions")
            return

        # Print header
        print(f"{'Session ID':<20} {'State':<10} {'Elapsed':<10} {'Current Work'}")
        print("-" * 80)

        # Print each session
        for session in active:
            state = session.get_state()

            # Calculate elapsed time for RUNNING sessions
            if state == 'RUNNING' and session.process_start_time:
                elapsed = time.time() - session.process_start_time
                elapsed_str = self._format_duration(elapsed)
            else:
                elapsed_str = "-"

            # Determine info column
            if state == 'RUNNING':
                info = session.current_prompt
                if len(info) > 45:
                    info = info[:45] + "..."
            elif state == 'IDLE':
                if session.history:
                    last = session.history[-1]['prompt']
                    info = f"Last: {last[:35]}"
                    if len(last) > 35:
                        info += "..."
                else:
                    info = "-"
            elif state == 'CREATED':
                info = "(never used)"
            else:
                info = "-"

            print(f"{session.session_id:<20} {state:<10} {elapsed_str:<10} {info}")

    def do_history(self, args: str):
        """Show prompt history for a session.

        Usage: history <session>
        """
        session_id = args.strip()

        if not session_id:
            print("Usage: history <session>")
            return

        if session_id not in self.sessions:
            print(f"Error: Session '{session_id}' not found")
            return

        session = self.sessions[session_id]

        if not session.history:
            print(f"Session {session_id} has no history")
            return

        print(f"\n=== History for {session_id} ===\n")

        # Display chronologically (oldest first) but numbered in reverse (latest = 1)
        total = len(session.history)
        for i, entry in enumerate(session.history):
            reverse_num = total - i
            prompt = entry['prompt']
            if len(prompt) > 60:
                prompt = prompt[:60] + "..."
            print(f"[{reverse_num}] {prompt}")

        print(f"\nTotal: {total} prompts")
        print(f"Use 'show {session_id} <n>' to view details")

    def do_show(self, args: str):
        """Show detailed prompt/response.

        Usage:
            show <session>              Show last entry (full)
            show <session> <n>          Show entry #n (full)
            show <session> <start>-<end> Show range (full)
            show <session> --all        Show all entries (full)
            show <session> ... --summary Truncate long responses
        """
        parts = args.split()
        if len(parts) < 1:
            print("Usage: show <session> [range] [--summary]")
            return

        session_id = parts[0]
        summary = '--summary' in parts
        if summary:
            parts.remove('--summary')

        if session_id not in self.sessions:
            print(f"Error: Session '{session_id}' not found")
            return

        session = self.sessions[session_id]

        if not session.history:
            print(f"Session {session_id} has no history")
            return

        total = len(session.history)

        # Determine what to show
        if len(parts) == 1:
            # Show last entry
            entries = [1]
        elif parts[1] == '--all':
            # Show all
            entries = range(1, total + 1)
        elif '-' in parts[1]:
            # Range: 1-3
            try:
                start, end = parts[1].split('-')
                entries = range(int(start), int(end) + 1)
            except ValueError:
                print(f"Error: Invalid range '{parts[1]}'")
                return
        else:
            # Single entry
            try:
                entries = [int(parts[1])]
            except ValueError:
                print(f"Error: Invalid entry number '{parts[1]}'")
                return

        # Display entries
        for reverse_idx in entries:
            if reverse_idx < 1 or reverse_idx > total:
                print(f"Error: Entry {reverse_idx} out of range (1-{total})")
                continue

            # Convert reverse index to actual index
            actual_idx = total - reverse_idx
            entry = session.history[actual_idx]

            print(f"\n[{reverse_idx}] Prompt:")
            print(f"    {entry['prompt']}\n")
            print(f"    Response:")

            response = entry['response']
            if summary and len(response) > 500:
                print(f"    {response[:500]}...")
                print(f"    (truncated, {len(response)} chars total)")
            else:
                # Indent each line of response
                for line in response.split('\n'):
                    print(f"    {line}")
            print()

    def do_stop(self, args: str):
        """Stop a running session.

        Usage: stop <session>
        """
        session_id = args.strip()

        if not session_id:
            print("Usage: stop <session>")
            return

        if session_id not in self.sessions:
            print(f"Error: Session '{session_id}' not found")
            return

        session = self.sessions[session_id]

        if not session.process or session.process.poll() is not None:
            print(f"Error: Session {session_id} is not running")
            return

        # Terminate process
        print(f"Stopping session {session_id}...")
        session.process.terminate()

        try:
            session.process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            # Force kill if still alive
            print(f"Force killing...")
            session.process.kill()
            session.process.wait()

        # Clean up
        if session.output_file and os.path.exists(session.output_file):
            os.remove(session.output_file)

        session.process = None
        session.current_prompt = None
        session.output_file = None
        session.process_start_time = None

        self._save_session(session)

        print(f"Session {session_id} stopped")

    def do_delete(self, args: str):
        """Archive or permanently delete a session.

        Usage: delete <session>

        For active sessions: Archives (deletes workspace, preserves history)
        For archived sessions: Permanently deletes (after confirmation)
        """
        session_id = args.strip()

        if not session_id:
            print("Usage: delete <session>")
            return

        if session_id not in self.sessions:
            print(f"Error: Session '{session_id}' not found")
            return

        session = self.sessions[session_id]

        # Can't delete running session
        if session.process and session.process.poll() is None:
            print(f"Error: Session {session_id} is running. Stop it first.")
            return

        # Already archived - confirm permanent deletion
        if session.archived:
            print(f"WARNING: This will permanently delete session {session_id}")
            print(f"History will be lost ({len(session.history)} prompts)")
            confirm = input("Delete permanently? (y/n): ")
            if confirm.lower() != 'y':
                print("Cancelled")
                return

            # Permanent deletion
            archived_file = f"workspace/sessions/archived/{session_id}.json"
            if os.path.exists(archived_file):
                os.remove(archived_file)
            del self.sessions[session_id]
            print(f"Session {session_id} deleted permanently")
            return

        # Archive - confirm workspace deletion
        print(f"This will archive session {session_id}:")
        workspace_base = self._get_workspace_base(session_id)
        print(f"  - Delete workspace: {workspace_base}")
        print(f"  - Preserve history: {len(session.history)} prompts")
        confirm = input("Archive? (y/n): ")
        if confirm.lower() != 'y':
            print("Cancelled")
            return

        # Delete workspace
        if os.path.exists(workspace_base):
            shutil.rmtree(workspace_base)
            print(f"Deleted workspace: {workspace_base}")

        # Mark as archived
        session.archived = True

        # Move session file
        active_file = f"workspace/sessions/active/{session_id}.json"
        archived_file = f"workspace/sessions/archived/{session_id}.json"
        os.makedirs(os.path.dirname(archived_file), exist_ok=True)

        if os.path.exists(active_file):
            shutil.move(active_file, archived_file)

        self._save_session(session)

        print(f"Session {session_id} archived (history preserved)")

    def do_config(self, args: str):
        """Get or set configuration values.

        Usage:
            config set <key> <value>    Set configuration value
            config get <key>            Get configuration value

        Examples:
            config set github.username wcy123
            config set fork.morphizen https://github.com/org/fork.git
            config get github.username
        """
        parts = args.split(maxsplit=2)
        if len(parts) < 2:
            print("Usage: config set <key> <value>  OR  config get <key>")
            return

        command = parts[0]
        key = parts[1]

        if command == 'set':
            if len(parts) < 3:
                print("Usage: config set <key> <value>")
                return
            value = parts[2]
            self.config.set(key, value)
            print(f"Set {key} = {value}")

        elif command == 'get':
            value = self.config.get(key)
            if value is None:
                print(f"{key} is not set")
            else:
                print(f"{key} = {value}")

        else:
            print(f"Unknown command: {command}")
            print("Usage: config set <key> <value>  OR  config get <key>")

    def do_exit(self, args: str):
        """Exit the orchestrator.

        Usage: exit
        """
        # Save command history
        os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
        readline.write_history_file(self.history_file)

        print("Goodbye!")
        return True

    def do_quit(self, args: str):
        """Exit the orchestrator (alias for exit).

        Usage: quit
        """
        return self.do_exit(args)

    def do_EOF(self, args: str):
        """Handle Ctrl+D to exit."""
        print()  # New line
        return self.do_exit(args)


def main():
    """Entry point for orchestrator."""
    shell = OrchestratorShell()
    try:
        shell.cmdloop()
    except KeyboardInterrupt:
        print("\nUse 'exit' to quit")
        shell.cmdloop()


if __name__ == '__main__':
    main()
