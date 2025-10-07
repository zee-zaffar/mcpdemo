# Startup script for Weather MCP Server on Azure App Service
import os
import sys

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Import and run the weather server
from mcpdemo.weather_server import mcp

if __name__ == "__main__":
    # Get port from environment (App Service provides this)
    port = int(os.environ.get('PORT', 8000))
    
    # Run with HTTP transport for App Service
    print(f"Starting Weather MCP Server on port {port}")
    mcp.run(transport="http", port=port, host="0.0.0.0")