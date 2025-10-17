from mcp.server.fastmcp import FastMCP
import os
import sys
import logging

# Configure logging for Azure
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    # Import the enhanced math server
    from mcpdemo.math_server import mcp as math_mcp, create_custom_asgi_app
    logger.info("Successfully imported enhanced math server with custom endpoints")
except ImportError as e:
    logger.error(f"Failed to import math server: {e}")
    # Fallback to basic import
    try:
        from mcpdemo.math_server import mcp as math_mcp
        logger.info("Imported basic math server")
        create_custom_asgi_app = None
    except ImportError as e2:
        logger.error(f"Failed to import any math server: {e2}")
        raise

# Create Azure-optimized ASGI app with HTTP endpoints
def create_asgi_app():
    """Create ASGI application optimized for Azure App Service with HTTP endpoints.
    
    Follows Azure best practices for:
    - Fast cold start times
    - Proper error handling
    - HTTP endpoints for monitoring
    - Scalability configuration
    """
    try:
        logger.info("Creating ASGI app for Azure deployment")
        
        # Try to use custom ASGI app with HTTP endpoints
        if create_custom_asgi_app:
            logger.info("Using custom ASGI app with /mcp and /health endpoints")
            asgi_app = create_custom_asgi_app()
        else:
            logger.info("Using standard MCP ASGI app")
            asgi_app = math_mcp.streamable_http_app()
            
        logger.info("ASGI app created successfully")
        return asgi_app
    except Exception as e:
        logger.error(f"Failed to create ASGI app: {e}")
        raise

# Export ASGI app for gunicorn/uvicorn
asgi_app = create_asgi_app()

if __name__ == "__main__":
    # Local development mode
    logger.info("Starting in local development mode")
    math_mcp.run(transport="streamable-http")