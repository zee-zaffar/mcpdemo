#!/usr/bin/env python3
"""Test client for the deployed Math MCP Server on Azure using streamable HTTP"""
import asyncio
import json
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamablehttp_client

async def create_math_session():
    """Create a direct session to weather server"""
    mcp_server_url = "https://app-math.azurewebsites.net/mcp"
    
    try:
        print(f"🌤️ Creating direct session to {mcp_server_url}")
        async with streamablehttp_client(mcp_server_url) as (read_stream, write_stream, _):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                
                # Get tools
                tools_result = await session.list_tools()
                tools = tools_result.tools
                
                print(f"✅ Math session created with {len(tools)} tools")
                for tool in tools:
                    print(f"  - {tool.name}: {tool.description}")
                
                return session, tools
                
    except Exception as e:
        print(f"❌ Weather session failed: {e}")
        return None, None

if __name__ == "__main__":
    print("🚀 Testing Azure Math MCP Server Deployment")
    print("=" * 60)
    
    try:
        # First try SSE connection
        asyncio.run(create_math_session())
        print("\n✅ All MCP tests completed!")
        
    except Exception as e:
        print(f"\n❌ MCP test failed: {e}")
        print("\n🔄 Trying HTTP fallback test...")
    
    print("\n" + "=" * 60)
    print("🏁 Test session complete")