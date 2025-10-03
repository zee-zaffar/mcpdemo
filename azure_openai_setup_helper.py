"""
Azure OpenAI Setup Helper
This script helps you find the correct configuration for your Azure OpenAI resource.
"""

from src.mcpdemo.config import config

def check_azure_openai_config():
    """Check and validate Azure OpenAI configuration."""
    print("🔍 Azure OpenAI Configuration Check")
    print("=" * 50)
    
    # Check API Key
    api_key = config.azure_openai_api_key
    if api_key:
        print(f"✅ API Key: {'*' * 20}{api_key[-10:]}")
    else:
        print("❌ API Key: Not configured")
        return False
    
    # Check Endpoint
    endpoint = config.azure_openai_endpoint
    print(f"🔗 Endpoint: {endpoint}")
    
    if not endpoint or "your-resource-name" in endpoint:
        print("❌ Endpoint needs to be updated!")
        print("\n📋 How to find your endpoint:")
        print("1. Go to Azure Portal (portal.azure.com)")
        print("2. Navigate to your Azure OpenAI resource")
        print("3. Go to 'Keys and Endpoint' section")
        print("4. Copy the 'Endpoint' value")
        print("5. It should look like: https://YOUR-RESOURCE-NAME.openai.azure.com/")
        print("\n💡 Your resource name is typically what you named your Azure OpenAI service")
        return False
    
    # Check deployments
    print(f"🤖 GPT-4 Deployment: {config.azure_openai_gpt4_deployment}")
    print(f"🤖 GPT-3.5 Deployment: {config.azure_openai_gpt35_deployment}")
    print(f"🔤 Embedding Deployment: {config.azure_openai_embedding_deployment}")
    
    print(f"📅 API Version: {config.azure_openai_api_version}")
    
    return True

def get_endpoint_instructions():
    """Provide instructions for finding the correct endpoint."""
    print("\n🛠 How to Update Your Endpoint:")
    print("=" * 40)
    print("1. Open Azure Portal: https://portal.azure.com")
    print("2. Search for 'OpenAI' in the search box")
    print("3. Click on your Azure OpenAI resource")
    print("4. In the left menu, click 'Keys and Endpoint'")
    print("5. Copy the 'Endpoint' URL")
    print("6. Update your .env file:")
    print("   AZURE_OPENAI_ENDPOINT=https://YOUR-ACTUAL-RESOURCE-NAME.openai.azure.com/")
    print("\nExample endpoints:")
    print("   https://mycompany-openai.openai.azure.com/")
    print("   https://demo-gpt4.openai.azure.com/")
    print("   https://ai-service-prod.openai.azure.com/")

if __name__ == "__main__":
    is_configured = check_azure_openai_config()
    if not is_configured:
        get_endpoint_instructions()
    else:
        print("\n✅ Configuration looks good! Try testing the connection.")