from mcp.server.fastmcp import FastMCP
import os
import sys

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Math MCP server
app = FastMCP("Math MCP Server")

@app.tool()
def add(a: float, b: float) -> float:
    """Add two numbers"""
    return a + b

@app.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers"""
    return a - b

@app.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

@app.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Export ASGI app for gunicorn
def create_asgi_app():
    return app.streamable_http_app()

asgi_app = create_asgi_app()

if __name__ == "__main__":
    import os
    
    # Set environment variables for uvicorn host/port before running
    os.environ["HOST"] = "0.0.0.0" 
    os.environ["PORT"] = str(os.environ.get('PORT', 8000))
    
    app.run(transport="streamable-http")