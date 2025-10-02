# FastMCP Demo Project

## 🎯 What You Just Created

✅ **Complete MCP Demo Project** with FastMCP library  
✅ **Working MCP Server** with 7 useful tools  
✅ **Demo Client** to test functionality  
✅ **Minimal Example** for learning  
✅ **Claude Desktop Configuration** ready to use  
✅ **Virtual Environment** with all dependencies  

## 🚀 Quick Demo

```powershell
# 1. Start the server
python -m mcpdemo.server

# 2. Test the client (in new terminal)
python -m mcpdemo.client --demo

# 3. Try minimal example
python examples/minimal_server.py
```

## 🔧 Available Tools

| Tool | Description |
|------|------------|
| `read_file` | Read file contents |
| `write_file` | Write to files |
| `list_directory` | List directory contents |
| `get_file_info` | Get file metadata |
| `search_files` | Search files by pattern |
| `get_current_directory` | Get current working directory |
| `echo` | Echo messages (for testing) |

## ⚙️ Use with Claude Desktop

1. Copy `examples/mcp_config.json` to:
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

2. Restart Claude Desktop

3. Ask Claude: *"Can you list the files in this directory?"*

## 🎨 Adding New Tools

Super simple with FastMCP:

```python
@mcp.tool()
def my_new_tool(param: str) -> str:
    """Description of what this tool does."""
    return f"Result: {param}"
```

## 📚 Learn More

- [FastMCP Documentation](https://gofastmcp.com)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- Run `python quickstart.py` for detailed setup guide
- Run `python demo.py` for complete project overview

---

**🎉 Your FastMCP demo project is ready! Start building amazing MCP tools!**