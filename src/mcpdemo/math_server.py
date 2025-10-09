from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Zee Math MCP Server")

@mcp.tool()
def add_two_numbers(a: float, b: float) -> str: 
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of the two numbers
    """
    result = a + b
    return f"Zee Math MCP Server Result for addition is: {a} + {b} = {result}"

@mcp.tool()
def divide_two_numbers(a: float, b: float) -> str: 
    """Divide two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The division of the two numbers
    """
    result = a / b
    return f"Zee Math MCP Server Result is: {a} + {b} = {result}"

@mcp.tool()
def multipy_two_numbers(a: float, b: float) -> str: 
    """Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The multiplication of the two numbers
    """
    result = a * b
    return f"Zee Math MCP Server Result for multiplication is: {a} + {b} = {result}"


if __name__ == "__main__":
   mcp.run()