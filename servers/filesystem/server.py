#!/usr/bin/env python3
"""
Simple filesystem MCP server
"""

import asyncio
from mcp import Server
from mcp.types import Tool, TextContent

server = Server("filesystem-server")

@server.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="read_file",
            description="Read contents of a file",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {"type": "string", "description": "File path to read"}
                },
                "required": ["path"]
            }
        )
    ]

@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "read_file":
        try:
            with open(arguments["path"], "r", encoding="utf-8") as f:
                content = f.read()
            return [TextContent(type="text", text=content)]
        except Exception as e:
            return [TextContent(type="text", text=f"Error reading file: {str(e)}")]
    
    raise ValueError(f"Unknown tool: {name}")

if __name__ == "__main__":
    asyncio.run(server.run())
