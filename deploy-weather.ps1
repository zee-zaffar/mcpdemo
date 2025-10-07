# Weather MCP Server Deployment Script
param(
    [Parameter(Mandatory=$false)]
    [string]$EnvironmentName = "weather-mcp-dev",
    
    [Parameter(Mandatory=$false)]
    [string]$Location = "eastus",
    
    [Parameter(Mandatory=$false)]
    [string]$ResourceGroup = "rg-$EnvironmentName"
)

Write-Host "🚀 Starting Weather MCP Server deployment..." -ForegroundColor Green

# Step 1: Create Resource Group
Write-Host "📁 Creating resource group: $ResourceGroup" -ForegroundColor Yellow
az group create --name $ResourceGroup --location $Location

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to create resource group" -ForegroundColor Red
    exit 1
}

# Step 2: Deploy Infrastructure
Write-Host "🏗️ Deploying Azure App Service infrastructure..." -ForegroundColor Yellow
$deploymentResult = az deployment group create `
    --resource-group $ResourceGroup `
    --template-file "infra/weather-appservice.bicep" `
    --parameters environmentName=$EnvironmentName location=$Location `
    --query "properties.outputs" `
    --output json | ConvertFrom-Json

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to deploy infrastructure" -ForegroundColor Red
    exit 1
}

$weatherUrl = $deploymentResult.WEATHER_SERVER_URL.value
$appName = $weatherUrl -replace "https://", "" -replace "\.azurewebsites\.net", ""

Write-Host "✅ Infrastructure deployed successfully!" -ForegroundColor Green
Write-Host "📝 App Service Name: $appName" -ForegroundColor Cyan
Write-Host "🌐 App Service URL: $weatherUrl" -ForegroundColor Cyan

# Step 3: Create deployment package
Write-Host "📦 Creating deployment package..." -ForegroundColor Yellow
if (Test-Path "weather-app.zip") {
    Remove-Item "weather-app.zip" -Force
}

# Create ZIP with required files
$filesToZip = @(
    "src/",
    "requirements.txt", 
    "startup.py"
)

# Check if Procfile exists and add it
if (Test-Path "Procfile") {
    $filesToZip += "Procfile"
}

Compress-Archive -Path $filesToZip -DestinationPath "weather-app.zip" -Force

# Step 4: Deploy application
Write-Host "🚀 Deploying application code..." -ForegroundColor Yellow
az webapp deployment source config-zip `
    --resource-group $ResourceGroup `
    --name $appName `
    --src "weather-app.zip"

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to deploy application" -ForegroundColor Red
    exit 1
}

# Step 5: Test deployment
Write-Host "🧪 Testing deployment..." -ForegroundColor Yellow
Start-Sleep -Seconds 30  # Give the app time to start

try {
    $response = Invoke-WebRequest -Uri "$weatherUrl/health" -TimeoutSec 30 -ErrorAction SilentlyContinue
    if ($response.StatusCode -eq 200) {
        Write-Host "✅ Health check passed!" -ForegroundColor Green
    } else {
        Write-Host "⚠️ Health check returned status: $($response.StatusCode)" -ForegroundColor Yellow
    }
} catch {
    Write-Host "⚠️ Health check failed - app may still be starting up" -ForegroundColor Yellow
}

# Cleanup
Remove-Item "weather-app.zip" -Force -ErrorAction SilentlyContinue

Write-Host "🎉 Weather MCP Server deployment completed!" -ForegroundColor Green
Write-Host "🌐 Your server is available at: $weatherUrl" -ForegroundColor Cyan
Write-Host "📊 View logs at: https://portal.azure.com" -ForegroundColor Cyan