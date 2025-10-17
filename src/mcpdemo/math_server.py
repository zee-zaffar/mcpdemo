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

# Add HTTP endpoints by modifying the ASGI app creation
def create_custom_asgi_app():
    """Create custom ASGI app with HTTP endpoints for Azure App Service."""
    from fastapi import FastAPI
    from fastapi.responses import JSONResponse
    
    # Get the base MCP ASGI app
    base_app = mcp.streamable_http_app()
    
    # Create FastAPI app for custom endpoints
    api_app = FastAPI(title="Zee Math MCP Server", version="1.0.0")
    
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