import asyncio
import json
import os
from openai import AsyncAzureOpenAI
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

async def main():
    """Azure OpenAI client that uses MCP tools for enhanced capabilities."""
    
    # Initialize Azure OpenAI client
    azure_client = AsyncAzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
    )

if __name__ == "__main__":
    asyncio.run(main())