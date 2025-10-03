"""
How to Use Azure OpenAI API Key - Complete Example
This demonstrates the correct way to use your Azure OpenAI API key.
"""

import os
import sys
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent / "src"))

from mcpdemo.config import config

def example_1_basic_usage():
    """Example 1: Basic Azure OpenAI usage with proper configuration."""
    print("📝 Example 1: Basic Azure OpenAI Usage")
    print("=" * 50)
    
    try:
        from openai import AzureOpenAI
        
        # Create client using your configuration from .env
        client = AzureOpenAI(
            api_key=config.azure_openai_api_key,
            api_version=config.azure_openai_api_version,
            azure_endpoint=config.azure_openai_endpoint
        )
        
        print("✅ Azure OpenAI client created successfully!")
        print(f"🔗 Endpoint: {config.azure_openai_endpoint}")
        print(f"📅 API Version: {config.azure_openai_api_version}")
        
        return client
        
    except ImportError:
        print("❌ OpenAI package not installed. Install with: pip install openai")
        return None
    except Exception as e:
        print(f"❌ Error creating client: {e}")
        return None

def example_2_chat_completion(client):
    """Example 2: Using chat completions with Azure OpenAI."""
    if not client:
        return
        
    print("\n💬 Example 2: Chat Completion")
    print("=" * 50)
    
    try:
        # Simple chat completion
        response = client.chat.completions.create(
            model=config.azure_openai_gpt35_deployment,  # Use your deployment name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is Model Context Protocol (MCP)?"}
            ],
            max_tokens=150,
            temperature=0.7
        )
        
        print("✅ Chat completion successful!")
        print(f"🤖 Response: {response.choices[0].message.content}")
        
    except Exception as e:
        print(f"❌ Chat completion failed: {e}")
        if "DeploymentNotFound" in str(e):
            print("💡 Tip: Check your deployment name in Azure portal")
        elif "InvalidRequestError" in str(e):
            print("💡 Tip: Check your endpoint URL and API key")

def example_3_with_mcp_integration():
    """Example 3: Using Azure OpenAI with MCP data."""
    print("\n🔄 Example 3: Azure OpenAI + MCP Integration")
    print("=" * 50)
    
    # Simulate MCP server response
    mcp_data = {
        "tool": "list_directory",
        "result": ["file1.py", "file2.py", "config.json"],
        "timestamp": "2025-10-02T10:30:00Z"
    }
    
    try:
        from openai import AzureOpenAI
        
        client = AzureOpenAI(
            api_key=config.azure_openai_api_key,
            api_version=config.azure_openai_api_version,
            azure_endpoint=config.azure_openai_endpoint
        )
        
        # Use Azure OpenAI to analyze MCP data
        messages = [
            {
                "role": "system", 
                "content": "You are an assistant that helps interpret MCP server responses. Provide helpful insights about the data."
            },
            {
                "role": "user", 
                "content": f"Please analyze this MCP server response and provide insights: {mcp_data}"
            }
        ]
        
        response = client.chat.completions.create(
            model=config.azure_openai_gpt35_deployment,
            messages=messages,
            max_tokens=200
        )
        
        print("✅ MCP + Azure OpenAI integration successful!")
        print(f"🔍 Analysis: {response.choices[0].message.content}")
        
    except Exception as e:
        print(f"❌ Integration failed: {e}")

def check_configuration():
    """Check if Azure OpenAI is properly configured."""
    print("🔧 Configuration Check")
    print("=" * 50)
    
    issues = []
    
    # Check API key
    if not config.azure_openai_api_key:
        issues.append("❌ AZURE_OPENAI_API_KEY not set")
    else:
        print(f"✅ API Key: {'*' * 10}{config.azure_openai_api_key[-10:]}")
    
    # Check endpoint
    if not config.azure_openai_endpoint:
        issues.append("❌ AZURE_OPENAI_ENDPOINT not set")
    elif "your-resource-name" in config.azure_openai_endpoint:
        issues.append("❌ AZURE_OPENAI_ENDPOINT contains placeholder text")
    else:
        print(f"✅ Endpoint: {config.azure_openai_endpoint}")
    
    # Check deployments
    if not config.azure_openai_gpt35_deployment and not config.azure_openai_gpt4_deployment:
        issues.append("❌ No model deployments configured")
    else:
        if config.azure_openai_gpt4_deployment:
            print(f"✅ GPT-4 Deployment: {config.azure_openai_gpt4_deployment}")
        if config.azure_openai_gpt35_deployment:
            print(f"✅ GPT-3.5 Deployment: {config.azure_openai_gpt35_deployment}")
    
    print(f"✅ API Version: {config.azure_openai_api_version}")
    
    if issues:
        print("\n🚨 Configuration Issues:")
        for issue in issues:
            print(f"  {issue}")
        print("\n📝 To fix these issues:")
        print("1. Go to Azure Portal → Your OpenAI Resource → Keys and Endpoint")
        print("2. Update your .env file with the correct values")
        print("3. Make sure your model deployments exist in Azure")
        return False
    
    return True

def main():
    """Main function demonstrating Azure OpenAI usage."""
    print("🚀 Azure OpenAI Usage Examples")
    print("=" * 60)
    
    # Check configuration first
    if not check_configuration():
        print("\n❌ Please fix configuration issues before proceeding.")
        return
    
    # Run examples
    client = example_1_basic_usage()
    example_2_chat_completion(client)
    example_3_with_mcp_integration()
    
    print("\n🎉 Examples completed!")
    print("\n📚 Next Steps:")
    print("1. Update your .env file with your actual Azure resource name")
    print("2. Verify your model deployments in Azure portal")
    print("3. Test the connection with: python src/mcpdemo/azure_openai_client.py")

if __name__ == "__main__":
    main()