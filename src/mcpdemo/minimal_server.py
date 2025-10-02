#!/usr/bin/env python3
"""
Minimal FastMCP Server Example

This is the simplest possible MCP server using FastMCP.
"""

from fastmcp import FastMCP

# Create a minimal server
mcp = FastMCP("Minimal Demo Server")


@mcp.tool()
def hello(name: str = "World") -> str:
    """Say hello to someone.
    
    Args:
        name: Name to greet (default: "World")
        
    Returns:
        A greeting message
    """
    return f"Hello, {name}! 👋"


@mcp.tool()
def add_numbers(a: float, b: float) -> str:
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of the two numbers
    """
    result = a + b
    return f"{a} + {b} = {result}"


@mcp.tool()
def count_words(text: str) -> str:
    """Count words in a text.
    
    Args:
        text: Text to count words in
        
    Returns:
        Word count information
    """
    words = text.split()
    chars = len(text)
    return f"Text has {len(words)} words and {chars} characters"


if __name__ == "__main__":
   mcp.run()