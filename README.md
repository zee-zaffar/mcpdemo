# MCP Demo with FastMCP

This is a demo repository to showcase Model Context Protocol (MCP) features using the FastMCP library in Python.

## Overview

The Model Context Protocol (MCP) is an open protocol that standardizes how applications can securely access content and resources in a user's environment. This project demonstrates creating MCP servers using FastMCP - a modern, simple library that makes building MCP servers easy and fast.

## Project Structure

```
mcpdemo/
├── src/mcpdemo/
│   ├── server.py            # Main MCP server with file tools
│   ├── client.py            # Demo client
│   └── __init__.py
├── examples/
│   ├── minimal_server.py    # Minimal FastMCP example
│   └── mcp_config.json      # Claude Desktop configuration
├── quickstart.py            # Quick start demo script
├── requirements.txt         # Dependencies
└── pyproject.toml          # Project configuration
```

## Features

### 🚀 FastMCP Server Features
- **Simple Setup**: Create MCP servers with just a few lines of code
- **File Operations**: Read, write, list files and directories
- **File Search**: Search for files using patterns
- **Utilities**: Echo, math operations, text analysis
- **Auto Documentation**: Tools are automatically documented
- **Type Safety**: Full type hints support

### 🔧 Available Tools
- `read_file(file_path)` - Read file contents
- `write_file(file_path, content)` - Write to files
- `list_directory(directory_path)` - List directory contents
- `get_file_info(file_path)` - Get file metadata
- `search_files(pattern, directory)` - Search files by pattern
- `get_current_directory()` - Get current working directory
- `echo(message)` - Echo messages (for testing)

## Quick Start

1. **Install dependencies**:
   ```powershell
   pip install fastmcp click
   ```

2. **Run the quick start demo**:
   ```powershell
   python quickstart.py
   ```

3. **Start the MCP server**:
   ```powershell
   python -m mcpdemo.server
   # or run the minimal example
   python examples/minimal_server.py
   ```

4. **Test the client**:
   ```powershell
   python -m mcpdemo.client --demo
   ```

## Using with Claude Desktop

1. **Copy the configuration**:
   Copy `examples/mcp_config.json` to your Claude Desktop MCP configuration file.

2. **Configuration location**:
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Linux**: `~/.config/Claude/claude_desktop_config.json`

3. **Restart Claude Desktop** and start using MCP tools!

## Example Usage

### Basic Server Example
```python
from fastmcp import FastMCP

app = FastMCP("My Server")

@app.tool()
def hello(name: str) -> str:
    """Say hello to someone."""
    return f"Hello, {name}!"

app.run()
```

### Using Tools in Claude
Once configured, you can ask Claude:
- "Please read the README.md file"
- "List all Python files in this directory"
- "Create a new file called test.txt with some sample content"
- "Search for all .json files"

## Development

### Project Installation
```powershell
# Install in development mode
pip install -e .

# Run the server
mcp-demo-server

# Run the client demo
mcp-demo-client --demo
```

### Adding New Tools
Simply add new functions with the `@mcp.tool()` decorator:

```python
@mcp.tool()
def my_new_tool(param: str) -> str:
    """Description of what this tool does."""
    return f"Result: {param}"
```

## Minimal Example

The simplest FastMCP server (`examples/minimal_server.py`):

```python
from fastmcp import FastMCP

app = FastMCP("Minimal Demo")

@app.tool()
def hello(name: str = "World") -> str:
    return f"Hello, {name}! 👋"

if __name__ == "__main__":
    app.run()
```

## Configuration Examples

### Claude Desktop Configuration
```json
{
  "mcpServers": {
    "mcp-demo-server": {
      "command": "python",
      "args": ["-m", "mcpdemo.server"],
      "env": {}
    }
  }
}
```

## Tips for Demo

1. **Start Simple**: Use the minimal_server.py first
2. **Test Tools**: Use the echo tool to verify connection
3. **File Operations**: Demonstrate reading and writing files
4. **Live Updates**: Modify tools and restart to show changes
5. **Error Handling**: Show how tools handle invalid inputs gracefully

## Why FastMCP?

- **🚀 Fast Setup**: Get an MCP server running in minutes
- **📝 Simple API**: Just add `@mcp.tool()` decorators to functions
- **🔧 Type Safe**: Full TypeScript-like type checking
- **📚 Auto Docs**: Tools are automatically documented
- **🔄 Live Reload**: Easy to update and test during development

## Troubleshooting

### Common Issues

1. **Import errors**: Install dependencies with `pip install fastmcp click`
2. **Server won't start**: Check that the port isn't already in use
3. **Claude can't find tools**: Verify the MCP configuration file path and restart Claude Desktop
4. **Permission errors**: Make sure Python has permission to read/write files

### Debugging

Run with verbose output:
```powershell
python -m mcpdemo.server --verbose
```

## Next Steps

- Add more sophisticated tools (database, APIs, etc.)
- Create domain-specific MCP servers
- Integrate with different AI applications
- Build tools for your specific workflow needs

## Resources

- [FastMCP Documentation](https://fastmcp.readthedocs.io/)
- [Model Context Protocol Specification](https://spec.modelcontextprotocol.io/)
- [Claude Desktop MCP Guide](https://docs.anthropic.com/claude/docs/mcp-model-context-protocol)
