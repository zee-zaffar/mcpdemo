#!/usr/bin/env python3
"""
Pure Python MCP Server Tester

Test your FastMCP server without any external dependencies.
No npm packages required - 100% Python!
"""

import json
import sys
import traceback
from pathlib import Path
from typing import Any, Dict

class PythonMCPInspector:
    """Pure Python MCP server inspector."""
    
    def __init__(self):
        # Add src to path so we can import our server
        sys.path.insert(0, str(Path(__file__).parent / "src"))
    
    def test_tool(self, tool_name: str, **kwargs) -> Dict[str, Any]:
        """Test a single tool with given parameters."""
        try:
            # Import the server module
            from mcpdemo.server import (
                read_file, write_file, list_directory, 
                get_file_info, search_files, get_current_directory, echo
            )
            
            # Map tool names to functions
            tools = {
                "echo": echo,
                "read_file": read_file,
                "write_file": write_file,
                "list_directory": list_directory,
                "get_file_info": get_file_info,
                "search_files": search_files,
                "get_current_directory": get_current_directory
            }
            
            if tool_name not in tools:
                return {"error": f"Tool '{tool_name}' not found", "available_tools": list(tools.keys())}
            
            # Call the tool
            result = tools[tool_name](**kwargs)
            return {"success": True, "result": result}
            
        except Exception as e:
            return {
                "error": str(e),
                "traceback": traceback.format_exc(),
                "tool": tool_name,
                "parameters": kwargs
            }
    
    def run_interactive_tests(self):
        """Run interactive testing session."""
        print("🔧 Pure Python MCP Inspector")
        print("=" * 50)
        print("Testing your FastMCP server tools without npm dependencies!")
        print()
        
        # Test cases
        test_cases = [
            {
                "name": "Echo Test",
                "tool": "echo",
                "params": {"message": "Hello from Python Inspector!"}
            },
            {
                "name": "Current Directory",
                "tool": "get_current_directory",
                "params": {}
            },
            {
                "name": "List Directory",
                "tool": "list_directory",
                "params": {"directory_path": "."}
            },
            {
                "name": "Search Python Files",
                "tool": "search_files",
                "params": {"pattern": "*.py", "directory": "."}
            },
            {
                "name": "File Info - README",
                "tool": "get_file_info",
                "params": {"file_path": "README.md"}
            },
            {
                "name": "Read Demo File",
                "tool": "read_file",
                "params": {"file_path": "demo.py"}
            }
        ]
        
        for i, test_case in enumerate(test_cases, 1):
            print(f"{i}. 🧪 {test_case['name']}")
            print(f"   Tool: {test_case['tool']}")
            print(f"   Params: {json.dumps(test_case['params'], indent=2)}")
            
            result = self.test_tool(test_case['tool'], **test_case['params'])
            
            if result.get('success'):
                output = result['result']
                if len(str(output)) > 150:
                    output = str(output)[:150] + "..."
                print(f"   ✅ Result: {output}")
            else:
                print(f"   ❌ Error: {result.get('error', 'Unknown error')}")
            print()
    
    def interactive_mode(self):
        """Run in interactive mode for custom testing."""
        print("\n🎮 Interactive Mode")
        print("=" * 30)
        print("Type tool commands to test them directly!")
        print("Examples:")
        print("  echo Hello World!")
        print("  list_directory .")
        print("  search_files *.json")
        print("  read_file README.md")
        print("  quit (to exit)")
        print()
        
        while True:
            try:
                command = input("🔧 MCP> ").strip()
                
                if command.lower() in ['quit', 'exit', 'q']:
                    print("👋 Goodbye!")
                    break
                
                if not command:
                    continue
                
                # Parse command
                parts = command.split(' ', 1)
                tool_name = parts[0]
                
                # Handle different tools
                if tool_name == "echo":
                    message = parts[1] if len(parts) > 1 else "Hello!"
                    result = self.test_tool("echo", message=message)
                
                elif tool_name == "list_directory":
                    directory = parts[1] if len(parts) > 1 else "."
                    result = self.test_tool("list_directory", directory_path=directory)
                
                elif tool_name == "search_files":
                    pattern = parts[1] if len(parts) > 1 else "*"
                    result = self.test_tool("search_files", pattern=pattern, directory=".")
                
                elif tool_name == "read_file":
                    if len(parts) < 2:
                        print("   ❌ Usage: read_file <filename>")
                        continue
                    result = self.test_tool("read_file", file_path=parts[1])
                
                elif tool_name == "get_file_info":
                    if len(parts) < 2:
                        print("   ❌ Usage: get_file_info <filename>")
                        continue
                    result = self.test_tool("get_file_info", file_path=parts[1])
                
                elif tool_name == "get_current_directory":
                    result = self.test_tool("get_current_directory")
                
                else:
                    print(f"   ❌ Unknown tool: {tool_name}")
                    print("   Available tools: echo, list_directory, search_files, read_file, get_file_info, get_current_directory")
                    continue
                
                # Display result
                if result.get('success'):
                    output = result['result']
                    print(f"   ✅ {output}")
                else:
                    print(f"   ❌ Error: {result.get('error')}")
                
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"   ❌ Error: {e}")

def main():
    """Run the Python MCP Inspector."""
    inspector = PythonMCPInspector()
    
    print("🚀 Welcome to Pure Python MCP Inspector!")
    print("🔒 No npm packages - 100% Python security!")
    print()
    
    # Run automated tests
    inspector.run_interactive_tests()
    
    # Ask if user wants interactive mode
    try:
        choice = input("🎮 Enter interactive mode? (y/n): ").lower().strip()
        if choice in ['y', 'yes']:
            inspector.interactive_mode()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

if __name__ == "__main__":
    main()