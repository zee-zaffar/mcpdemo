from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Zee Weather MCP Server")

@mcp.tool()
def get_weather(location: str) -> str:
    """
        Get the current weather for a given location.
        Args:
            location (str): The location to get the weather for.
            returns: str: The current weather description.
    """
    # In a real implementation, this would call a weather API.
    # Here, we'll return a mock response.
    mock_weather_data = {
        "New York": "Sunny, 75°F",
        "Los Angeles": "Cloudy, 68°F",
        "Chicago": "Rainy, 60°F",
        "Miami": "Sunny, 85°F"
    }
    return mock_weather_data.get(location, "Location not found") 

if __name__ == "__main__":
    import os
    transport = os.getenv("TRANSPORT", "http")  # Default to streamable-http
    port = int(os.getenv("PORT", "8001"))
    
    if transport == "http":
        mcp.run(transport="http", port=port, host="0.0.0.0")
    else:
        mcp.run(transport="stdio")