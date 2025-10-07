# Startup script for Weather MCP Server on Azure App Service
import os
import sys

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the weather server
from mcpdemo.weather_server import mcp

if __name__ == "__main__":
    # Run with HTTP transport for App Service
    print("Starting Weather MCP Server with streamable-http transport")
    mcp.run(transport="streamable-http")