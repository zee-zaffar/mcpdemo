# Weather MCP Server - Azure App Service Deployment Guide

## Prerequisites
```powershell
# Check required tools
azd version
az --version
```

## Deployment Steps

### 1. Login to Azure
```powershell
# Login to Azure
az login
azd auth login
```

### 2. Initialize Environment
```powershell
# Set environment name
$env:AZURE_ENV_NAME = "weather-mcp-dev"

# Set location
$env:AZURE_LOCATION = "eastus"
```

### 3. Deploy Infrastructure
```powershell
# Create resource group
az group create --name "rg-weather-mcp-dev" --location eastus

# Deploy Bicep template
az deployment group create `
  --resource-group "rg-weather-mcp-dev" `
  --template-file "infra/weather-appservice.bicep" `
  --parameters environmentName="weather-mcp-dev"
```

### 4. Deploy Application Code
```powershell
# Get the App Service name from deployment output
$appName = az deployment group show `
  --resource-group "rg-weather-mcp-dev" `
  --name "weather-appservice" `
  --query "properties.outputs.weatherServerUrl.value" `
  --output tsv

# Create ZIP deployment package
Compress-Archive -Path "src", "requirements.txt", "startup.py", "Procfile" -DestinationPath "weather-app.zip" -Force

# Deploy using ZIP deployment
az webapp deployment source config-zip `
  --resource-group "rg-weather-mcp-dev" `
  --name $appName `
  --src "weather-app.zip"
```

### 5. Test Deployment
```powershell
# Get the App Service URL
$appUrl = az webapp show `
  --resource-group "rg-weather-mcp-dev" `
  --name $appName `
  --query "defaultHostName" `
  --output tsv

# Test the endpoint
curl "https://$appUrl"
```

## Manual Deployment Option

Alternatively, you can deploy manually through Azure Portal:

1. Create App Service with Python 3.11
2. Configure application settings:
   - `TRANSPORT=http`
   - `PORT=8000` 
   - `SERVER_TYPE=weather`
3. Deploy code via VS Code Azure extension or ZIP upload