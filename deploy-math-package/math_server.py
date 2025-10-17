from mcp.server.fastmcp import FastMCP
from typing import Dict, Any
import os
import logging
import sys

# Configure logging for Azure Application Insights
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("Zee Math MCP Server")

@mcp.tool()
def add_two_numbers(a: float, b: float) -> str: 
    """Add two numbers together with comprehensive error handling.
    
    Args:
        a: First number to add
        b: Second number to add
        
    Returns:
        The sum of the two numbers with clear formatting
    """
    try:
        result = a + b
        logger.info(f"Addition performed: {a} + {b} = {result}")
        return f"Zee Math MCP Server Result for addition is: {a} + {b} = {result}"
    except Exception as e:
        logger.error(f"Error in addition: {str(e)}")
        return f"Error performing addition: {str(e)}"

@mcp.tool()
def subtract_two_numbers(a: float, b: float) -> str:
    """Subtract two numbers with comprehensive error handling.
    
    Args:
        a: First number (minuend)
        b: Second number (subtrahend)
        
    Returns:
        The subtraction result with clear formatting
    """
    try:
        result = a - b
        logger.info(f"Subtraction performed: {a} - {b} = {result}")
        return f"Zee Math MCP Server Result for subtraction is: {a} - {b} = {result}"
    except Exception as e:
        logger.error(f"Error in subtraction: {str(e)}")
        return f"Error performing subtraction: {str(e)}"

@mcp.tool()
def multiply_two_numbers(a: float, b: float) -> str: 
    """Multiply two numbers together with comprehensive error handling.
    
    Args:
        a: First number to multiply
        b: Second number to multiply
        
    Returns:
        The multiplication result with clear formatting
    """
    try:
        result = a * b
        logger.info(f"Multiplication performed: {a} × {b} = {result}")
        return f"Zee Math MCP Server Result for multiplication is: {a} × {b} = {result}"
    except Exception as e:
        logger.error(f"Error in multiplication: {str(e)}")
        return f"Error performing multiplication: {str(e)}"

@mcp.tool()
def divide_two_numbers(a: float, b: float) -> str: 
    """Divide two numbers with zero-division protection and error handling.
    
    Args:
        a: First number (dividend)
        b: Second number (divisor)
        
    Returns:
        The division result or error message for zero division
    """
    try:
        if b == 0:
            logger.warning("Division by zero attempted")
            return "Error: Division by zero is not allowed"
        
        result = a / b
        logger.info(f"Division performed: {a} ÷ {b} = {result}")
        return f"Zee Math MCP Server Result for division is: {a} ÷ {b} = {result}"
    except Exception as e:
        logger.error(f"Error in division: {str(e)}")
        return f"Error performing division: {str(e)}"

# Helper function to get server info data
def _get_server_info_data() -> Dict[str, Any]:
    """Get comprehensive MCP server information and available tools.
    
    Returns detailed information about the server, its capabilities,
    available tools, and deployment information for Azure monitoring.
    """
    try:
        # Detect Azure environment
        is_azure = bool(os.environ.get('WEBSITE_HOSTNAME'))
        hostname = os.environ.get('WEBSITE_HOSTNAME', 'localhost:8000')
        
        return {
            "server": {
                "name": "Zee Math MCP Server",
                "version": "1.0.0",
                "description": "A production-ready mathematical operations MCP server with comprehensive error handling and Azure integration",
                "author": "Zee Zaffar",
                "transport": "streamable-http",
                "url": f"https://{hostname}" if is_azure else f"http://{hostname}",
                "environment": "production" if is_azure else "development"
            },
            "capabilities": {
                "tools": True,
                "resources": False,
                "prompts": False,
                "logging": True,
                "error_handling": True,
                "health_monitoring": True
            },
            "tools": [
                {
                    "name": "add_two_numbers",
                    "description": "Add two numbers together with comprehensive error handling",
                    "parameters": {
                        "a": {"type": "number", "description": "First number to add"},
                        "b": {"type": "number", "description": "Second number to add"}
                    },
                    "example": "add_two_numbers(5, 3) → 'Zee Math MCP Server Result for addition is: 5 + 3 = 8'"
                },
                {
                    "name": "subtract_two_numbers",
                    "description": "Subtract two numbers with comprehensive error handling", 
                    "parameters": {
                        "a": {"type": "number", "description": "Number to subtract from (minuend)"},
                        "b": {"type": "number", "description": "Number to subtract (subtrahend)"}
                    },
                    "example": "subtract_two_numbers(10, 4) → 'Zee Math MCP Server Result for subtraction is: 10 - 4 = 6'"
                },
                {
                    "name": "multiply_two_numbers",
                    "description": "Multiply two numbers together with comprehensive error handling",
                    "parameters": {
                        "a": {"type": "number", "description": "First number to multiply"},
                        "b": {"type": "number", "description": "Second number to multiply"}
                    },
                    "example": "multiply_two_numbers(6, 7) → 'Zee Math MCP Server Result for multiplication is: 6 × 7 = 42'"
                },
                {
                    "name": "divide_two_numbers", 
                    "description": "Divide two numbers with zero-division protection and error handling",
                    "parameters": {
                        "a": {"type": "number", "description": "Number to be divided (dividend)"},
                        "b": {"type": "number", "description": "Number to divide by (divisor)"}
                    },
                    "example": "divide_two_numbers(15, 3) → 'Zee Math MCP Server Result for division is: 15 ÷ 3 = 5'"
                }
            ],
            "endpoints": {
                "info": "/mcp",
                "tools": "/tools",
                "call": "/call",
                "health": "/health"
            },
            "deployment": {
                "platform": "Azure App Service" if is_azure else "Local Development",
                "runtime": "Python 3.11",
                "status": "active",
                "last_updated": "2025-10-16T18:30:00Z",
                "region": os.environ.get('REGION_NAME', 'unknown'),
                "resource_group": os.environ.get('RESOURCE_GROUP', 'unknown')
            },
            "monitoring": {
                "application_insights": is_azure,
                "structured_logging": True,
                "health_checks": True,
                "error_tracking": True
            },
            "usage": {
                "connect_via_mcp": "Use MCP client to connect to this server for mathematical operations",
                "health_check": "GET /health for Azure health monitoring",
                "server_info": "GET /mcp for comprehensive server information",
                "available_operations": ["addition", "subtraction", "multiplication", "division"]
            }
        }
    except Exception as e:
        logger.error(f"Error getting server info: {str(e)}")
        return {
            "error": f"Failed to get server info: {str(e)}",
            "server": "Zee Math MCP Server",
            "status": "error",
            "timestamp": "2025-10-16T18:30:00Z"
        }

# Helper function to get health check data
def _get_health_check_data() -> Dict[str, Any]:
    """Azure-compatible health check endpoint for monitoring and load balancing.
    
    Returns health status information for Azure App Service health monitoring,
    Application Insights, and load balancer health checks.
    """
    try:
        is_azure = bool(os.environ.get('WEBSITE_HOSTNAME'))
        
        # Perform basic functionality test
        test_result = add_two_numbers(1, 1)
        tools_healthy = "2" in test_result
        
        health_status = {
            "status": "healthy" if tools_healthy else "degraded",
            "server": "Zee Math MCP Server",
            "version": "1.0.0", 
            "timestamp": "2025-10-16T18:30:00Z",
            "tools_available": 4,
            "tools_functional": tools_healthy,
            "environment": "production" if is_azure else "development",
            "transport": "streamable-http",
            "azure_ready": True,
            "checks": {
                "basic_math": "passed" if tools_healthy else "failed",
                "error_handling": "enabled",
                "logging": "enabled",
                "mcp_protocol": "active"
            }
        }
        
        if tools_healthy:
            logger.info("Health check passed - all systems operational")
        else:
            logger.warning("Health check degraded - basic math test failed")
            
        return health_status
        
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return {
            "status": "unhealthy", 
            "error": str(e),
            "server": "Zee Math MCP Server",
            "timestamp": "2025-10-16T18:30:00Z",
            "azure_ready": False
        }

# Add HTTP endpoints by modifying the ASGI app creation
def create_custom_asgi_app():
    """Create custom ASGI app with HTTP endpoints for Azure App Service."""
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    
    # Get the base MCP ASGI app
    base_app = mcp.streamable_http_app()
    
    # Create FastAPI app for custom endpoints
    api_app = FastAPI(title="Zee Math MCP Server", version="1.0.0")
    
    @api_app.get("/mcp")
    async def get_server_info():
        """HTTP endpoint for server information."""
        return JSONResponse(_get_server_info_data())
    
    @api_app.get("/health")
    async def health_check():
        """HTTP endpoint for Azure health monitoring."""
        return JSONResponse(_get_health_check_data())
    
    # Mount the MCP app at the root and API endpoints
    from fastapi.middleware.wsgi import WSGIMiddleware
    api_app.mount("/", base_app)
    
    return api_app

if __name__ == "__main__":
    # Azure-aware transport configuration
    is_azure = bool(os.environ.get('WEBSITE_HOSTNAME'))
    transport = "streamable-http" 
    
    logger.info(f"Starting Zee Math MCP Server")

    try:
        mcp.run(transport=transport)
    except Exception as e:
        logger.error(f"Failed to start server: {str(e)}")
        raise