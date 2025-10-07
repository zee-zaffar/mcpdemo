#!/usr/bin/env python3
import os
import uvicorn
from app import app

if __name__ == "__main__":
    # Get port from environment (Azure App Service sets this)
    port = int(os.environ.get("PORT", 8000))
    
    # Create the ASGI application
    from mcp.server.fastmcp.server import FastMCPServer
    
    # Get the FastMCP server instance
    server = app._server
    
    # Create ASGI app for streamable-http transport
    asgi_app = server.create_asgi_app(transport="streamable-http")
    
    # Run with uvicorn on all interfaces
    uvicorn.run(asgi_app, host="0.0.0.0", port=port, log_level="info")