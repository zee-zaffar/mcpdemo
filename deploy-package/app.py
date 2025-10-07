from mcp.server.fastmcp import FastMCP
import os
import sys

# Add the src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Simple weather MCP server
app = FastMCP("Weather MCP Server")

@app.tool()
def get_weather(location: str) -> str:
    """Get weather for a location"""
    weather_data = {
        "New York": "Sunny, 75°F",
        "Los Angeles": "Cloudy, 68°F", 
        "Chicago": "Rainy, 60°F",
        "Miami": "Sunny, 85°F"
    }
    return weather_data.get(location, "Location not found")

if __name__ == "__main__":
    app.run(transport="streamable-http")