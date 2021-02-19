def GenerateConfig(context):
  """Generate YAML resource configuration."""

  endpoints = {
      '-v1': 'api/v1',
      '-v1beta1-apps': 'apis/apps/v1beta1',
      '-v1beta1-extensions': 'apis/extensions/v1beta1'
  }

  resources = []


  outputs = {
    'name': 'kubernetes-v1',
    'type': 'deploymentmanager.v2beta.typeProvider',
    'properties' : {
        'options': {
            'validationOptions': {
                'schemaValidation': 'IGNORE_WITH_WARNINGS'
            },
            'inputMappings': [
                {
                    'fieldName': 'namespace',
                    'location': 'PATH',
                    'value': '$.ifNull($.resource.properties.metadata.namespace, "default")'
                },
                {
                    'fieldName': 'name',
                    'location': 'PATH',
                    'methodMatch': '^(GET|DELETE|PUT|PATCH|get|delete|put|patch)$',
                    'value': '$.ifNull($.resource.properties.metadata.name, $.resource.name)'
                },
                {
                    'fieldName': 'metadata.name',
                    'location': 'BODY',
                    'methodMatch': '^(PUT|PATCH|POST|put|patch|post)$',
                    'value': '$.ifNull($.resource.properties.metadata.name, $.resource.name)'
                },
                {
                    'fieldName': 'metadata.resourceVersion',
                    'location': 'BODY',
                    'methodMatch': '^(PUT|PATCH|put|patch)$',
                    'value': '$.resource.self.metadata.resourceVersion'
                },
                {
                    'fieldName': 'Authorization',
                    'location': 'HEADER',
                    'value': '$.concat("Bearer ", $.googleOauth2AccessToken())'
                }]
            },
            'descriptorUrl': 'https://' + context.properties['endpoint'] + '/openapi/v2/kubernetes-v1'
        }
  }
    
  return {'resources': resources}
