# 🚀 FastMCP Servers Azure Deployment Guide

## **Overview**
This guide will help you deploy your three FastMCP servers (math, weather, directory) to Azure Container Apps using streamable-HTTP transport protocol for RESTful API access.

## **Prerequisites**
Ensure you have the following tools installed:

```powershell
# Check Azure Developer CLI
azd version

# Check Azure CLI
az --version

# Check Docker
docker --version
```

If any are missing, install them:
- **Azure Developer CLI**: [Install AZD](https://docs.microsoft.com/azure/developer/azure-developer-cli/install-azd)
- **Azure CLI**: [Install Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli)
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)

## **Deployment Steps**

### **1. Initialize Azure Developer Environment**

```powershell
# Navigate to your project directory
cd C:\Source\mcpdemo

# Initialize azd environment
azd init --environment mcpdemo-prod

# Login to Azure
azd auth login
az login
```

### **2. Configure Environment Variables**

```powershell
# Set your preferred Azure region
azd env set AZURE_LOCATION "eastus2"

# Optional: Set specific subscription
azd env set AZURE_SUBSCRIPTION_ID "your-subscription-id"
```

### **3. Preview the Deployment** 

```powershell
# Preview what will be deployed (recommended)
azd provision --preview
```

### **4. Deploy to Azure**

```powershell
# Deploy infrastructure and applications
azd up
```

This will:
- ✅ Create Azure Container Registry
- ✅ Build and push Docker images for all three servers
- ✅ Create Container Apps Environment with Log Analytics
- ✅ Deploy three Container Apps with HTTP endpoints
- ✅ Configure Application Insights monitoring
- ✅ Set up managed identity and permissions

### **5. Get Deployment Information**

```powershell
# Get service endpoints
azd env get-values

# Check application logs
azd logs
```

## **Server Endpoints**

After deployment, your servers will be available at:

- **Math Server**: `https://<math-app-url>/`
- **Weather Server**: `https://<weather-app-url>/`  
- **Directory Server**: `https://<directory-app-url>/`

## **Testing Your Deployed Servers**

### **Test HTTP Endpoints**

```powershell
# Test math server
curl https://<math-server-url>/mcp/tools

# Test weather server  
curl https://<weather-server-url>/mcp/tools

# Test directory server
curl https://<directory-server-url>/mcp/tools
```

### **Test MCP Tool Calls**

```bash
# Example: Call math server add function
curl -X POST https://<math-server-url>/mcp/call \
  -H "Content-Type: application/json" \
  -d '{
    "method": "tools/call",
    "params": {
      "name": "add_two_numbers",
      "arguments": {"a": 10, "b": 5}
    }
  }'
```

## **Monitoring and Management**

### **View Logs**
```powershell
# View all application logs
azd logs

# View specific service logs
azd logs --service math-server
```

### **Scale Applications**
```bash
# Scale math server replicas
az containerapp update \
  --name <math-app-name> \
  --resource-group <resource-group> \
  --min-replicas 1 \
  --max-replicas 20
```

### **View Metrics**
- Open Azure Portal
- Navigate to Application Insights
- View performance metrics and traces

## **Using with Claude Desktop**

Update your Claude Desktop configuration to use the deployed HTTP endpoints:

```json
{
  "mcpServers": {
    "math-server": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-everything"],
      "env": {
        "MCP_SERVER_URL": "https://<math-server-url>"
      }
    },
    "weather-server": {
      "command": "npx", 
      "args": ["@modelcontextprotocol/server-everything"],
      "env": {
        "MCP_SERVER_URL": "https://<weather-server-url>"
      }
    },
    "directory-server": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-everything"], 
      "env": {
        "MCP_SERVER_URL": "https://<directory-server-url>"
      }
    }
  }
}
```

## **Cleanup**

To remove all deployed resources:

```powershell
# Delete all Azure resources
azd down --purge
```

## **Troubleshooting**

### **Common Issues**

**Issue**: Container fails to start
**Solution**: Check logs with `azd logs --service <service-name>`

**Issue**: Build fails
**Solution**: Test Docker build locally:
```powershell
docker build -f math.Dockerfile -t math-server .
docker run -p 8000:8000 math-server
```

**Issue**: HTTP endpoint not accessible
**Solution**: Verify ingress configuration in Azure Portal

### **Support Resources**
- [Azure Container Apps Documentation](https://docs.microsoft.com/azure/container-apps/)
- [Azure Developer CLI Documentation](https://docs.microsoft.com/azure/developer/azure-developer-cli/)
- [FastMCP Documentation](https://fastmcp.com)

## **Next Steps**
- ✅ Set up CI/CD pipelines with GitHub Actions
- ✅ Configure custom domains and SSL certificates
- ✅ Implement authentication and authorization
- ✅ Add monitoring alerts and dashboards