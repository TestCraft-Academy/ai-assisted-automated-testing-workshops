"""Minimal teaching policy; not a security sandbox or MCP implementation."""

from typing import Optional


def approve_tool(tool: str, data: Optional[str] = None) -> bool:
    """Allow only one read-only tool without payloads; everything else is denied."""
    return tool == "read_test_summary" and data is None