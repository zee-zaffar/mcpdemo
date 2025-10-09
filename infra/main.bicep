@description('Environment name')
param environmentName string

@description('Primary location for all resources')
param location string = resourceGroup().location

@description('Resource group name')
param resourceGroupName string = 'rg-${environmentName}'

// Generate unique token for resource naming
var resourceToken = uniqueString(subscription().id, resourceGroup().id, location, environmentName)

// Resource names following AZD patterns
var containerRegistryName = 'acr${resourceToken}'
var logAnalyticsName = 'log${resourceToken}'
var appInsightsName = 'appi${resourceToken}'
var managedIdentityName = 'id${resourceToken}'
var containerAppEnvName = 'cae${resourceToken}'

// Container app names
var mathAppName = 'ca-math-${resourceToken}'
var weatherAppName = 'ca-weather-${resourceToken}'
var directoryAppName = 'ca-directory-${resourceToken}'

// Create User-Assigned Managed Identity (required by AZD rules)
resource managedIdentity 'Microsoft.ManagedIdentity/userAssignedIdentities@2023-01-31' = {
  name: managedIdentityName
  location: location
}

// Create Container Registry
resource containerRegistry 'Microsoft.ContainerRegistry/registries@2023-07-01' = {
  name: containerRegistryName
  location: location
  sku: {
    name: 'Basic'
  }
  properties: {
    adminUserEnabled: false
  }
}

// Create Log Analytics Workspace
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

// Create Application Insights
resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: appInsightsName
  location: location
  kind: 'web'
  properties: {
    Application_Type: 'web'
    WorkspaceResourceId: logAnalytics.id
  }
}

// MANDATORY: Assign AcrPull role to managed identity (required before container apps)
resource acrPullRoleAssignment 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  scope: containerRegistry
  name: guid(containerRegistry.id, managedIdentity.id, '7f951dda-4ed3-4680-a7ca-43fe172d538d')
  properties: {
    roleDefinitionId: subscriptionResourceId('Microsoft.Authorization/roleDefinitions', '7f951dda-4ed3-4680-a7ca-43fe172d538d') // AcrPull role
    principalId: managedIdentity.properties.principalId
    principalType: 'ServicePrincipal'
  }
}

// Create Container Apps Environment
resource containerAppEnvironment 'Microsoft.App/managedEnvironments@2024-03-01' = {
  name: containerAppEnvName
  location: location
  properties: {
    appLogsConfiguration: {
      destination: 'log-analytics'
      logAnalyticsConfiguration: {
        customerId: logAnalytics.properties.customerId
        sharedKey: logAnalytics.listKeys().primarySharedKey
      }
    }
  }
}

// Math MCP Server Container App
resource mathContainerApp 'Microsoft.App/containerApps@2024-03-01' = {
  name: mathAppName
  location: location
  tags: {
    'azd-service-name': 'math-server'
  }
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '${managedIdentity.id}': {}
    }
  }
  properties: {
    managedEnvironmentId: containerAppEnvironment.id
    configuration: {
      ingress: {
        external: true
        targetPort: 8000
        allowInsecure: false
        corsPolicy: {
          allowedOrigins: ['*']
          allowedMethods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
          allowedHeaders: ['*']
          allowCredentials: false
        }
      }
      registries: [
        {
          server: containerRegistry.properties.loginServer
          identity: managedIdentity.id
        }
      ]
    }
    template: {
      containers: [
        {
          name: 'math-server'
          image: 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest' // Required base image by AZD rules
          env: [
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
              value: 'math'
            }
            {
              name: 'APPLICATIONINSIGHTS_CONNECTION_STRING'
              value: appInsights.properties.ConnectionString
            }
          ]
          resources: {
            cpu: json('0.5')
            memory: '1Gi'
          }
        }
      ]
      scale: {
        minReplicas: 0
        maxReplicas: 10
      }
    }
  }
  dependsOn: [
    acrPullRoleAssignment
  ]
}

// Weather MCP Server Container App
resource weatherContainerApp 'Microsoft.App/containerApps@2024-03-01' = {
  name: weatherAppName
  location: location
  tags: {
    'azd-service-name': 'weather-server'
  }
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '${managedIdentity.id}': {}
    }
  }
  properties: {
    managedEnvironmentId: containerAppEnvironment.id
    configuration: {
      ingress: {
        external: true
        targetPort: 8001
        allowInsecure: false
        corsPolicy: {
          allowedOrigins: ['*']
          allowedMethods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
          allowedHeaders: ['*']
          allowCredentials: false
        }
      }
      registries: [
        {
          server: containerRegistry.properties.loginServer
          identity: managedIdentity.id
        }
      ]
    }
    template: {
      containers: [
        {
          name: 'weather-server'
          image: 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest' // Required base image by AZD rules
          env: [
            {
              name: 'TRANSPORT'
              value: 'http'
            }
            {
              name: 'PORT'
              value: '8001'
            }
            {
              name: 'SERVER_TYPE'
              value: 'weather'
            }
            {
              name: 'APPLICATIONINSIGHTS_CONNECTION_STRING'
              value: appInsights.properties.ConnectionString
            }
          ]
          resources: {
            cpu: json('0.5')
            memory: '1Gi'
          }
        }
      ]
      scale: {
        minReplicas: 0
        maxReplicas: 10
      }
    }
  }
  dependsOn: [
    acrPullRoleAssignment
  ]
}

// Directory MCP Server Container App
resource directoryContainerApp 'Microsoft.App/containerApps@2024-03-01' = {
  name: directoryAppName
  location: location
  tags: {
    'azd-service-name': 'directory-server'
  }
  identity: {
    type: 'UserAssigned'
    userAssignedIdentities: {
      '${managedIdentity.id}': {}
    }
  }
  properties: {
    managedEnvironmentId: containerAppEnvironment.id
    configuration: {
      ingress: {
        external: true
        targetPort: 8002
        allowInsecure: false
        corsPolicy: {
          allowedOrigins: ['*']
          allowedMethods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
          allowedHeaders: ['*']
          allowCredentials: false
        }
      }
      registries: [
        {
          server: containerRegistry.properties.loginServer
          identity: managedIdentity.id
        }
      ]
    }
    template: {
      containers: [
        {
          name: 'directory-server'
          image: 'mcr.microsoft.com/azuredocs/containerapps-helloworld:latest' // Required base image by AZD rules
          env: [
            {
              name: 'TRANSPORT'
              value: 'http'
            }
            {
              name: 'PORT'
              value: '8002'
            }
            {
              name: 'SERVER_TYPE'
              value: 'directory'
            }
            {
              name: 'APPLICATIONINSIGHTS_CONNECTION_STRING'
              value: appInsights.properties.ConnectionString
            }
          ]
          resources: {
            cpu: json('0.5')
            memory: '1Gi'
          }
        }
      ]
      scale: {
        minReplicas: 0
        maxReplicas: 10
      }
    }
  }
  dependsOn: [
    acrPullRoleAssignment
  ]
}

// Required outputs by AZD rules
output RESOURCE_GROUP_ID string = resourceGroup().id
output AZURE_CONTAINER_REGISTRY_ENDPOINT string = containerRegistry.properties.loginServer

// Additional useful outputs
output MATH_SERVER_URL string = 'https://${mathContainerApp.properties.configuration.ingress.fqdn}'
output WEATHER_SERVER_URL string = 'https://${weatherContainerApp.properties.configuration.ingress.fqdn}'
output DIRECTORY_SERVER_URL string = 'https://${directoryContainerApp.properties.configuration.ingress.fqdn}'
output APPLICATION_INSIGHTS_CONNECTION_STRING string = appInsights.properties.ConnectionString