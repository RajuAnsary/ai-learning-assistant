#!/usr/bin/env python3
"""
Setup script for Custom Diagram MCP Server
"""

from setuptools import setup, find_packages

setup(
    name="custom-diagram-mcp-server",
    version="1.0.0",
    description="Custom MCP Server for generating architecture diagrams",
    author="AI Assistant",
    python_requires=">=3.8",
    install_requires=[
        "diagrams>=0.25.0",
        "graphviz>=0.20.0",
    ],
    py_modules=["diagram_mcp_server"],
    entry_points={
        "console_scripts": [
            "diagram-mcp-server=diagram_mcp_server:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)