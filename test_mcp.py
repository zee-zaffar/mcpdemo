#!/usr/bin/env python3
"""
Manual MCP Server Tester

Test MCP servers directly from VS Code terminal.
"""

import asyncio
import json
import sys
from pathlib import Path

# Add the src directory to Python path
sys.path.insert(0, str(Path(__file__).parent / "src"))

async def test_mcp_server():
    """Test the MCP server tools manually."""
    # This would require setting up an MCP client
    # For now, we'll just import and test the functions directly
    
    try:
        from mcpdemo.server import (
            read_file, write_file, list_directory, 
            get_file_info, search_files, get_current_directory, echo
        )
        
        print("🧪 Testing MCP Server Tools Directly")
        print("=" * 50)
        
        # Test echo
        print("1. Testing echo:")
        result = echo("Hello from VS Code!")
        print(f"   Result: {result}")
        
        # Test current directory
        print("\n2. Testing get_current_directory:")
        result = get_current_directory()
        print(f"   Result: {result}")
        
        # Test list directory
        print("\n3. Testing list_directory:")
        result = list_directory(".")
        print(f"   Result: {result[:200]}...")
        
        # Test search files
        print("\n4. Testing search_files:")
        result = search_files("*.py", ".")
        print(f"   Result: {result[:200]}...")
        
        print("\n✅ All tests completed successfully!")
        
    except Exception as e:
        print(f"❌ Error testing server: {e}")

if __name__ == "__main__":
    asyncio.run(test_mcp_server())