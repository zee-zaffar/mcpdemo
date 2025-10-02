#!/usr/bin/env python3
"""
MCP Inspector Helper

Simple script to test MCP server tools interactively.
"""

import json
import subprocess
import sys
import asyncio
from pathlib import Path

class MCPTester:
    """Simple MCP server tester."""
    
    def __init__(self):
        self.server_process = None
    
    def test_server_functions(self):
        """Test server functions directly."""
        print("🧪 MCP Server Function Tests")
        print("=" * 50)
        
        # Import the server functions directly
        sys.path.insert(0, str(Path(__file__).parent / "src"))
        
        try:
            from mcpdemo.server import (
                read_file, write_file, list_directory, 
                get_file_info, search_files, get_current_directory, echo
            )
            
            tests = [
                ("Echo Test", lambda: echo("Hello MCP Inspector!")),
                ("Current Directory", lambda: get_current_directory()),
                ("List Directory", lambda: list_directory(".")),
                ("Search Python Files", lambda: search_files("*.py", ".")),
                ("File Info", lambda: get_file_info("README.md")),
            ]
            
            for test_name, test_func in tests:
                print(f"\n🔸 {test_name}:")
                try:
                    result = test_func()
                    # Truncate long results
                    if len(result) > 200:
                        result = result[:200] + "..."
                    print(f"   ✅ {result}")
                except Exception as e:
                    print(f"   ❌ Error: {e}")
            
        except ImportError as e:
            print(f"❌ Could not import server functions: {e}")
            print("Make sure you're in the project directory and dependencies are installed.")
    
    def show_inspector_info(self):
        """Show how to use the web inspector."""
        print("\n🌐 MCP Inspector Web Interface")
        print("=" * 50)
        print("The MCP Inspector is running in your browser.")
        print("\n📋 Available Tools to Test:")
        tools = [
            ("echo", '{"message": "Hello Inspector!"}'),
            ("get_current_directory", "{}"),
            ("list_directory", '{"directory_path": "."}'),
            ("search_files", '{"pattern": "*.py", "directory": "."}'),
            ("read_file", '{"file_path": "README.md"}'),
            ("get_file_info", '{"file_path": "demo.py"}'),
        ]
        
        for tool, params in tools:
            print(f"   🔧 {tool}")
            print(f"      Parameters: {params}")
            print()
    
    def show_usage_tips(self):
        """Show usage tips for the inspector."""
        print("💡 Inspector Usage Tips:")
        print("=" * 30)
        print("1. 📊 In the web interface, you can:")
        print("   • See all available tools and their schemas")
        print("   • Test tools with different parameters")
        print("   • View request/response logs")
        print("   • Debug errors in real-time")
        print()
        print("2. 🧪 Test different scenarios:")
        print("   • Valid file paths vs invalid ones")
        print("   • Different search patterns")
        print("   • Empty vs filled parameters")
        print()
        print("3. 🔍 Debugging features:")
        print("   • Real-time request/response monitoring")
        print("   • JSON schema validation")
        print("   • Error stack traces")
        print("   • Performance timing")

def main():
    """Run the MCP tester."""
    tester = MCPTester()
    
    print("🚀 MCP Inspector Testing Helper")
    print("=" * 50)
    
    # Test functions directly
    tester.test_server_functions()
    
    # Show inspector info
    tester.show_inspector_info()
    
    # Show usage tips
    tester.show_usage_tips()
    
    print("\n🎯 Next Steps:")
    print("   1. Use the web interface that opened in your browser")
    print("   2. Or run: npx @modelcontextprotocol/inspector python examples/minimal_server.py")
    print("   3. Test different tools with various parameters")

if __name__ == "__main__":
    main()