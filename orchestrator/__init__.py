#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
# Licensed under the MIT License.
#
"""
Orchestrator - Multi-session manager for Claude Code.

This package provides an interactive REPL interface for managing multiple
parallel Claude Code sessions working in different workspace directories.
"""

__version__ = '0.1.0'
__author__ = 'AMD'
__license__ = 'MIT'

from .orchestrator import OrchestratorShell, Session, Config

__all__ = ['OrchestratorShell', 'Session', 'Config']
