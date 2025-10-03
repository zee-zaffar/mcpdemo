#!/usr/bin/env python3
"""
FastMCP Demo Server

A simple Zee MCP server using FastMCP that provides basic file operations and utilities.
"""

import os
import json
from pathlib import Path
from fastmcp import FastMCP

# Create the FastMCP server instance
mcp = FastMCP("Zee MCP Directory Server")

@mcp.tool()
def read_file(file_path: str) -> str:
    """Read the contents of a file.
    
    Args:
        file_path: Path to the file to read
        
    Returns:
        File contents as a string
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return f"Error: File not found: {file_path}"
        
        if not path.is_file():
            return f"Error: Path is not a file: {file_path}"
            
        return path.read_text(encoding='utf-8')
    except Exception as e:
        return f"Error reading file: {str(e)}"


@mcp.tool()
def write_file(file_path: str, content: str) -> str:
    """Write content to a file.
    
    Args:
        file_path: Path to the file to write
        content: Content to write to the file
        
    Returns:
        Success message or error description
    """
    try:
        path = Path(file_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding='utf-8')
        return f"Successfully wrote {len(content)} characters to {file_path}"
    except Exception as e:
        return f"Error writing file: {str(e)}"


@mcp.tool()
def list_directory(directory_path: str = ".") -> str:
    """List the contents of a directory.
    
    Args:
        directory_path: Path to the directory to list (default: current directory)
        
    Returns:
        Directory listing as formatted string
    """
    try:
        path = Path(directory_path)
        if not path.exists():
            return f"Error: Directory not found: {directory_path}"
        
        if not path.is_dir():
            return f"Error: Path is not a directory: {directory_path}"
        
        items = []
        for item in sorted(path.iterdir()):
            item_type = "📁 DIR " if item.is_dir() else "📄 FILE"
            size = f"{item.stat().st_size:>8} bytes" if item.is_file() else "        -"
            items.append(f"{item_type} {size} {item.name}")
        
        return f"Contents of {directory_path}:\\n\\n" + "\\n".join(items)
    except Exception as e:
        return f"Error listing directory: {str(e)}"


@mcp.tool()
def get_file_info(file_path: str) -> str:
    """Get detailed information about a file or directory.
    
    Args:
        file_path: Path to the file or directory
        
    Returns:
        File information as JSON string
    """
    try:
        path = Path(file_path)
        if not path.exists():
            return f"Error: Path not found: {file_path}"
        
        stat = path.stat()
        info = {
            "name": path.name,
            "path": str(path.absolute()),
            "type": "directory" if path.is_dir() else "file",
            "size": stat.st_size,
            "created": stat.st_ctime,
            "modified": stat.st_mtime,
            "permissions": oct(stat.st_mode)[-3:]
        }
        
        return json.dumps(info, indent=2)
    except Exception as e:
        return f"Error getting file info: {str(e)}"


@mcp.tool()
def search_files(pattern: str, directory: str = ".") -> str:
    """Search for files matching a pattern.
    
    Args:
        pattern: File name pattern (supports wildcards like *.py)
        directory: Directory to search in (default: current directory)
        
    Returns:
        List of matching files
    """
    try:
        path = Path(directory)
        if not path.exists():
            return f"Error: Directory not found: {directory}"
        
        matches = list(path.glob(pattern))
        if not matches:
            return f"No files found matching pattern '{pattern}' in {directory}"
        
        results = []
        for match in sorted(matches):
            match_type = "📁" if match.is_dir() else "📄"
            results.append(f"{match_type} {match.relative_to(path)}")
        
        return f"Files matching '{pattern}' in {directory}:\\n\\n" + "\\n".join(results)
    except Exception as e:
        return f"Error searching files: {str(e)}"

@mcp.tool()
def get_current_directory() -> str:
    """Get the current working directory.
    
    Returns:
        Current working directory path
    """
    return f"Current directory: {os.getcwd()}"

@mcp.tool()
def echo(message: str) -> str:
    """Echo a message back (useful for testing).
    
    Args:
        message: Message to echo back
        
    Returns:
        The input message with a greeting
    """
    return f"Hello! You said: {message}"

if __name__ == "__main__":
   mcp.run()