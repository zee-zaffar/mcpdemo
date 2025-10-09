@description('Environment name')
param environmentName string

@description('Primary location for all resources')
param location string = resourceGroup().location

// Generate unique token for resource naming
var resourceToken = uniqueString(subscription().id, resourceGroup().id, location, environmentName)

// Resource names following Azure naming conventions
var appServicePlanName = 'asp-weather-${resourceToken}'
var appServiceName = 'app-weather-${resourceToken}'
var logAnalyticsName = 'log-weather-${resourceToken}'
var appInsightsName = 'appi-weather-${resourceToken}'

// Create Log Analytics Workspace for monitoring
resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: logAnalyticsName
  location: location
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
  }
}

// Create Application Insights for telemetry
resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: appInsightsName
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: logAnalytics.id
  }
}

// Create App Service Plan (Linux, Python)
resource appServicePlan 'Microsoft.Web/serverfarms@2023-12-01' = {
  name: appServicePlanName
  location: location
  sku: {
    name: 'B1' // Basic tier - good for development/testing
    tier: 'Basic'
    size: 'B1'
    family: 'B'
    capacity: 1
  }
  kind: 'linux'
  properties: {
    reserved: true // Required for Linux
  }
}

// Create App Service for Weather MCP Server
resource appService 'Microsoft.Web/sites@2023-12-01' = {
  name: appServiceName
  location: location
  tags: {
    'azd-service-name': 'weather-server'
  }
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      linuxFxVersion: 'PYTHON|3.11' // Python 3.11 runtime
      alwaysOn: true
      ftpsState: 'Disabled'
      minTlsVersion: '1.2'
      scmMinTlsVersion: '1.2'
      appSettings: [
        {
          name: 'TRANSPORT'
          value: 'http'
        }
        {
          name: 'PORT'
          value: '8000'
        }
        {
          name: 'SERVER_TYPE'
          value: 'weather'
        }
        {
          name: 'APPLICATIONINSIGHTS_CONNECTION_STRING'
          value: appInsights.properties.ConnectionString
        }
        {
          name: 'SCM_DO_BUILD_DURING_DEPLOYMENT'
          value: 'true'
        }
        {
          name: 'ENABLE_ORYX_BUILD'
          value: 'true'
        }
        {
          name: 'POST_BUILD_SCRIPT_PATH'
          value: 'deploy/post_build.sh'
        }
      ]
      cors: {
        allowedOrigins: ['*']
        supportCredentials: false
      }
    }
    httpsOnly: true
    clientAffinityEnabled: false
  }
  identity: {
    type: 'SystemAssigned'
  }
}

// Output the App Service URL and other important information
output WEATHER_SERVER_URL string = 'https://${appService.properties.defaultHostName}'
output APPLICATION_INSIGHTS_CONNECTION_STRING string = appInsights.properties.ConnectionString
output RESOURCE_GROUP_ID string = resourceGroup().id