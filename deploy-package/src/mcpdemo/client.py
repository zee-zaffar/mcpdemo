#!/usr/bin/env python3
"""
FastMCP Demo Client

A simple client to interact with FastMCP servers.
"""

import asyncio
import json
import sys
from pathlib import Path
import click


class SimpleMCPClient:
    """A simple MCP client for demonstration purposes."""
    
    def __init__(self, server_url: str = "http://localhost:8000"):
        self.server_url = server_url
        self.session = None
    
    def demo_usage(self):
        """Show demo usage examples."""
        print("🔧 MCP Demo Client")
        print("=" * 50)
        print()
        print("This is a demonstration client for FastMCP servers.")
        print("In a real implementation, this would connect to an MCP server")
        print("and interact with its tools.")
        print()
        print("📋 Example tools that would be available:")
        print("   - read_file(file_path)")
        print("   - write_file(file_path, content)")
        print("   - list_directory(directory_path)")
        print("   - get_file_info(file_path)")
        print("   - search_files(pattern, directory)")
        print("   - get_current_directory()")
        print("   - echo(message)")
        print()
        print("💡 To use this with a real MCP server:")
        print("   1. Start the server: python -m mcpdemo.server")
        print("   2. Configure your MCP client (like Claude Desktop)")
        print("   3. Use the tools through the MCP protocol")
        print()
    
    def show_sample_interactions(self):
        """Show sample interactions that could be performed."""
        print("📝 Sample Interactions:")
        print("-" * 30)
        print()
        
        # Sample file operations
        print("1. Reading the README file:")
        try:
            readme_path = Path("README.md")
            if readme_path.exists():
                content = readme_path.read_text()[:200] + "..."
                print(f"   📄 Content preview: {content}")
            else:
                print("   📄 README.md not found")
        except Exception as e:
            print(f"   ❌ Error: {e}")
        print()
        
        # Sample directory listing
        print("2. Listing current directory:")
        try:
            current_dir = Path(".")
            items = list(current_dir.iterdir())[:5]  # Show first 5 items
            for item in items:
                icon = "📁" if item.is_dir() else "📄"
                print(f"   {icon} {item.name}")
            if len(list(current_dir.iterdir())) > 5:
                print("   ... and more")
        except Exception as e:
            print(f"   ❌ Error: {e}")
        print()
        
        # Sample search
        print("3. Searching for Python files:")
        try:
            py_files = list(Path(".").rglob("*.py"))[:3]
            for py_file in py_files:
                print(f"   🐍 {py_file}")
            if len(list(Path(".").rglob("*.py"))) > 3:
                print("   ... and more")
        except Exception as e:
            print(f"   ❌ Error: {e}")
        print()
    
    def show_mcp_config(self):
        """Show sample MCP configuration."""
        config = {
            "mcpServers": {
                "mcp-demo-server": {
                    "command": "python",
                    "args": ["-m", "mcpdemo.server"],
                    "env": {}
                }
            }
        }
        
        print("⚙️  Sample MCP Configuration (for Claude Desktop):")
        print("-" * 50)
        print(json.dumps(config, indent=2))
        print()
        print("💾 Save this to your MCP configuration file to use with Claude Desktop")
        print()


@click.command()
@click.option('--server-url', default='http://localhost:8000', 
              help='URL of the MCP server')
@click.option('--demo', is_flag=True, 
              help='Show demonstration output')
@click.option('--config', is_flag=True, 
              help='Show MCP configuration example')
def main(server_url, demo, config):
    """Run the FastMCP demo client."""
    client = SimpleMCPClient(server_url)
    
    if config:
        client.show_mcp_config()
        return
    
    if demo:
        client.demo_usage()
        client.show_sample_interactions()
        client.show_mcp_config()
    else:
        print("🔧 MCP Demo Client")
        print("Use --demo to see demonstration output")
        print("Use --config to see MCP configuration")
        print("Use --help for more options")


if __name__ == "__main__":
    main()