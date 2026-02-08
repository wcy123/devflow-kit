#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2023 - 2025 Advanced Micro Devices, Inc. All rights reserved.
# Licensed under the MIT License.
#
"""Setup script for devflow-kit orchestrator."""

from setuptools import setup, find_packages

with open('orchestrator/README.md', 'r') as f:
    long_description = f.read()

setup(
    name='devflow-kit-orchestrator',
    version='0.1.0',
    description='Multi-session manager for parallel workflow execution',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='AMD',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'PyYAML>=6.0',
    ],
    entry_points={
        'console_scripts': [
            'orchestrator=orchestrator.orchestrator:main',
        ],
    },
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
