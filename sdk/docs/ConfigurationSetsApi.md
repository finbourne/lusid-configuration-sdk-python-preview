# lusid_configuration.ConfigurationSetsApi

All URIs are relative to *https://fbn-ci.lusid.com/configuration*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_configuration_to_set**](ConfigurationSetsApi.md#add_configuration_to_set) | **POST** /api/sets/{type}/{scope}/{code}/items | [EARLY ACCESS] AddConfigurationToSet: Add a configuration item to an existing set
[**check_access_token_exists**](ConfigurationSetsApi.md#check_access_token_exists) | **HEAD** /api/sets/personal/me | [BETA] CheckAccessTokenExists: Check the Personal Access Token exists for the current user
[**create_configuration_set**](ConfigurationSetsApi.md#create_configuration_set) | **POST** /api/sets | [EARLY ACCESS] CreateConfigurationSet: Create a configuration set
[**delete_access_token**](ConfigurationSetsApi.md#delete_access_token) | **DELETE** /api/sets/personal/me | [EARLY ACCESS] DeleteAccessToken: Delete any stored Personal Access Token for the current user
[**delete_configuration_item**](ConfigurationSetsApi.md#delete_configuration_item) | **DELETE** /api/sets/{type}/{scope}/{code}/items/{key} | [EARLY ACCESS] DeleteConfigurationItem: Remove the specified configuration item from the specified configuration set
[**delete_configuration_set**](ConfigurationSetsApi.md#delete_configuration_set) | **DELETE** /api/sets/{type}/{scope}/{code} | [EARLY ACCESS] DeleteConfigurationSet: Deletes a configuration set along with all their configuration items
[**generate_access_token**](ConfigurationSetsApi.md#generate_access_token) | **PUT** /api/sets/personal/me | [EARLY ACCESS] GenerateAccessToken: Generate a Personal Access Token for the current user and stores it in the me token
[**get_configuration_item**](ConfigurationSetsApi.md#get_configuration_item) | **GET** /api/sets/{type}/{scope}/{code}/items/{key} | [EARLY ACCESS] GetConfigurationItem: Get the specific configuration item within an existing set
[**get_configuration_set**](ConfigurationSetsApi.md#get_configuration_set) | **GET** /api/sets/{type}/{scope}/{code} | [EARLY ACCESS] GetConfigurationSet: Get a configuration set, including all the associated metadata. By default secrets will not be revealed
[**get_system_configuration_items**](ConfigurationSetsApi.md#get_system_configuration_items) | **GET** /api/sets/system/{code}/items/{key} | [EARLY ACCESS] GetSystemConfigurationItems: Get the specific system configuration items within a system set  All users have access to this endpoint
[**get_system_configuration_sets**](ConfigurationSetsApi.md#get_system_configuration_sets) | **GET** /api/sets/system/{code} | [EARLY ACCESS] GetSystemConfigurationSets: Get the specified system configuration sets, including all their associated metadata. By default secrets will not be revealed  All users have access to this endpoint
[**list_configuration_sets**](ConfigurationSetsApi.md#list_configuration_sets) | **GET** /api/sets | [EARLY ACCESS] ListConfigurationSets: List all configuration sets summaries (I.e. list of scope/code combinations available)
[**update_configuration_item**](ConfigurationSetsApi.md#update_configuration_item) | **PUT** /api/sets/{type}/{scope}/{code}/items/{key} | [EARLY ACCESS] UpdateConfigurationItem: Update a configuration item&#39;s value and/or description
[**update_configuration_set**](ConfigurationSetsApi.md#update_configuration_set) | **PUT** /api/sets/{type}/{scope}/{code} | [EARLY ACCESS] UpdateConfigurationSet: Update the description of a configuration set


# **add_configuration_to_set**
> ConfigurationSet add_configuration_to_set(type, scope, code, create_configuration_item, user_id=user_id)

[EARLY ACCESS] AddConfigurationToSet: Add a configuration item to an existing set

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_configuration
from lusid_configuration.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/configuration
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_configuration.ConfigurationSetsApi(api_client)
    type = 'type_example' # str | Whether the configuration set is Personal or Shared
scope = 'scope_example' # str | The scope that identifies a configuration set
code = 'code_example' # str | The code that identifies a configuration set
create_configuration_item = {"key":"password","value":"a super secret password","valueType":"text","isSecret":false,"description":"Password for System A"} # CreateConfigurationItem | The data to create a configuration item
user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

    try:
        # [EARLY ACCESS] AddConfigurationToSet: Add a configuration item to an existing set
        api_response = api_instance.add_configuration_to_set(type, scope, code, create_configuration_item, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationSetsApi->add_configuration_to_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | 
 **scope** | **str**| The scope that identifies a configuration set | 
 **code** | **str**| The code that identifies a configuration set | 
 **create_configuration_item** | [**CreateConfigurationItem**](CreateConfigurationItem.md)| The data to create a configuration item | 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_access_token_exists**
> check_access_token_exists()

[BETA] CheckAccessTokenExists: Check the Personal Access Token exists for the current user

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_configuration
from lusid_configuration.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/configuration
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_configuration.ConfigurationSetsApi(api_client)
    
    try:
        # [BETA] CheckAccessTokenExists: Check the Personal Access Token exists for the current user
        api_instance.check_access_token_exists()
    except ApiException as e:
        print("Exception when calling ConfigurationSetsApi->check_access_token_exists: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Personal Access Token exists |  -  |
**404** | The Personal Access Token does not exist |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_configuration_set**
> ConfigurationSet create_configuration_set(create_configuration_set, user_id=user_id)

[EARLY ACCESS] CreateConfigurationSet: Create a configuration set

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_configuration
from lusid_configuration.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/configuration
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_configuration.ConfigurationSetsApi(api_client)
    create_configuration_set = {"id":{"scope":"official","code":"system-a-config"},"type":"shared","description":"All the config related to System A"} # CreateConfigurationSet | The data to create a configuration set
user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

    try:
        # [EARLY ACCESS] CreateConfigurationSet: Create a configuration set
        api_response = api_instance.create_configuration_set(create_configuration_set, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationSetsApi->create_configuration_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_configuration_set** | [**CreateConfigurationSet**](CreateConfigurationSet.md)| The data to create a configuration set | 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_token**
> delete_access_token()

[EARLY ACCESS] DeleteAccessToken: Delete any stored Personal Access Token for the current user

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_configuration
from lusid_configuration.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/configuration
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_configuration.ConfigurationSetsApi(api_client)
    
    try:
        # [EARLY ACCESS] DeleteAccessToken: Delete any stored Personal Access Token for the current user
        api_instance.delete_access_token()
    except ApiException as e:
        print("Exception when calling ConfigurationSetsApi->delete_access_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_configuration_item**
> delete_configuration_item(type, scope, code, key, user_id=user_id)

[EARLY ACCESS] DeleteConfigurationItem: Remove the specified configuration item from the specified configuration set

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_configuration
from lusid_configuration.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/configuration
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_configuration.ConfigurationSetsApi(api_client)
    type = 'type_example' # str | Whether the configuration set is Personal or Shared
scope = 'scope_example' # str | The scope that identifies a configuration set
code = 'code_example' # str | The code that identifies a configuration set
key = 'key_example' # str | The key that identifies a configuration item
user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

    try:
        # [EARLY ACCESS] DeleteConfigurationItem: Remove the specified configuration item from the specified configuration set
        api_instance.delete_configuration_item(type, scope, code, key, user_id=user_id)
    except ApiException as e:
        print("Exception when calling ConfigurationSetsApi->delete_configuration_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | 
 **scope** | **str**| The scope that identifies a configuration set | 
 **code** | **str**| The code that identifies a configuration set | 
 **key** | **str**| The key that identifies a configuration item | 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration item exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_configuration_set**
> delete_configuration_set(type, scope, code, user_id=user_id)

[EARLY ACCESS] DeleteConfigurationSet: Deletes a configuration set along with all their configuration items

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_configuration
from lusid_configuration.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/configuration
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_configuration.ConfigurationSetsApi(api_client)
    type = 'type_example' # str | Whether the configuration set is Personal or Shared
scope = 'scope_example' # str | The scope that identifies a configuration set
code = 'code_example' # str | The code that identifies a configuration set
user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

    try:
        # [EARLY ACCESS] DeleteConfigurationSet: Deletes a configuration set along with all their configuration items
        api_instance.delete_configuration_set(type, scope, code, user_id=user_id)
    except ApiException as e:
        print("Exception when calling ConfigurationSetsApi->delete_configuration_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | 
 **scope** | **str**| The scope that identifies a configuration set | 
 **code** | **str**| The code that identifies a configuration set | 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

void (empty response body)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_access_token**
> PersonalAccessToken generate_access_token(action=action)

[EARLY ACCESS] GenerateAccessToken: Generate a Personal Access Token for the current user and stores it in the me token

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_configuration
from lusid_configuration.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/configuration
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_configuration.ConfigurationSetsApi(api_client)
    action = 'action_example' # str | action=regenerate = Even if an existing parameter exists, forcibly regenerate a new one (deleting the old)  action=ensure = If no parameter exists, create one. If one does already exist, verify that it is still valid (call a service?), and if so, return it. If it is not still valid, then regenerate a new one.  action=default = If a parameter exists, return it. If not then create one. If this parameter is not provided, this is the default behaviour. (optional)

    try:
        # [EARLY ACCESS] GenerateAccessToken: Generate a Personal Access Token for the current user and stores it in the me token
        api_response = api_instance.generate_access_token(action=action)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationSetsApi->generate_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| action&#x3D;regenerate &#x3D; Even if an existing parameter exists, forcibly regenerate a new one (deleting the old)  action&#x3D;ensure &#x3D; If no parameter exists, create one. If one does already exist, verify that it is still valid (call a service?), and if so, return it. If it is not still valid, then regenerate a new one.  action&#x3D;default &#x3D; If a parameter exists, return it. If not then create one. If this parameter is not provided, this is the default behaviour. | [optional] 

### Return type

[**PersonalAccessToken**](PersonalAccessToken.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_item**
> ConfigurationItem get_configuration_item(type, scope, code, key, reveal=reveal, user_id=user_id)

[EARLY ACCESS] GetConfigurationItem: Get the specific configuration item within an existing set

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_configuration
from lusid_configuration.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/configuration
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_configuration.ConfigurationSetsApi(api_client)
    type = 'type_example' # str | Whether the configuration set is Personal or Shared
scope = 'scope_example' # str | The scope that identifies a configuration set
code = 'code_example' # str | The code that identifies a configuration set
key = 'key_example' # str | The key that identifies a configuration item
reveal = True # bool | Whether to reveal the secrets. This is only available when the userId query setting has not been specified. (optional)
user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

    try:
        # [EARLY ACCESS] GetConfigurationItem: Get the specific configuration item within an existing set
        api_response = api_instance.get_configuration_item(type, scope, code, key, reveal=reveal, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationSetsApi->get_configuration_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | 
 **scope** | **str**| The scope that identifies a configuration set | 
 **code** | **str**| The code that identifies a configuration set | 
 **key** | **str**| The key that identifies a configuration item | 
 **reveal** | **bool**| Whether to reveal the secrets. This is only available when the userId query setting has not been specified. | [optional] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationItem**](ConfigurationItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration item exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_configuration_set**
> ConfigurationSet get_configuration_set(type, scope, code, reveal=reveal, user_id=user_id)

[EARLY ACCESS] GetConfigurationSet: Get a configuration set, including all the associated metadata. By default secrets will not be revealed

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_configuration
from lusid_configuration.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/configuration
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_configuration.ConfigurationSetsApi(api_client)
    type = 'type_example' # str | Whether the configuration set is Personal or Shared
scope = 'scope_example' # str | The scope that identifies a configuration set
code = 'code_example' # str | The code that identifies a configuration set
reveal = True # bool | Whether to reveal the secrets. This is only available when the userId query setting has not been specified. (optional)
user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

    try:
        # [EARLY ACCESS] GetConfigurationSet: Get a configuration set, including all the associated metadata. By default secrets will not be revealed
        api_response = api_instance.get_configuration_set(type, scope, code, reveal=reveal, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationSetsApi->get_configuration_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | 
 **scope** | **str**| The scope that identifies a configuration set | 
 **code** | **str**| The code that identifies a configuration set | 
 **reveal** | **bool**| Whether to reveal the secrets. This is only available when the userId query setting has not been specified. | [optional] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_configuration_items**
> ResourceListOfConfigurationItem get_system_configuration_items(code, key, reveal=reveal)

[EARLY ACCESS] GetSystemConfigurationItems: Get the specific system configuration items within a system set  All users have access to this endpoint

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_configuration
from lusid_configuration.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/configuration
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_configuration.ConfigurationSetsApi(api_client)
    code = 'code_example' # str | The code that identifies a system configuration set
key = 'key_example' # str | The key that identifies a system configuration item
reveal = True # bool | Whether to reveal the secrets (optional)

    try:
        # [EARLY ACCESS] GetSystemConfigurationItems: Get the specific system configuration items within a system set  All users have access to this endpoint
        api_response = api_instance.get_system_configuration_items(code, key, reveal=reveal)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationSetsApi->get_system_configuration_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code that identifies a system configuration set | 
 **key** | **str**| The key that identifies a system configuration item | 
 **reveal** | **bool**| Whether to reveal the secrets | [optional] 

### Return type

[**ResourceListOfConfigurationItem**](ResourceListOfConfigurationItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No system configuration item exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_configuration_sets**
> ResourceListOfConfigurationSet get_system_configuration_sets(code, reveal=reveal)

[EARLY ACCESS] GetSystemConfigurationSets: Get the specified system configuration sets, including all their associated metadata. By default secrets will not be revealed  All users have access to this endpoint

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_configuration
from lusid_configuration.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/configuration
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_configuration.ConfigurationSetsApi(api_client)
    code = 'code_example' # str | The code that identifies a system configuration set
reveal = True # bool | Whether to reveal the secrets (optional)

    try:
        # [EARLY ACCESS] GetSystemConfigurationSets: Get the specified system configuration sets, including all their associated metadata. By default secrets will not be revealed  All users have access to this endpoint
        api_response = api_instance.get_system_configuration_sets(code, reveal=reveal)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationSetsApi->get_system_configuration_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| The code that identifies a system configuration set | 
 **reveal** | **bool**| Whether to reveal the secrets | [optional] 

### Return type

[**ResourceListOfConfigurationSet**](ResourceListOfConfigurationSet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No system configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_configuration_sets**
> ResourceListOfConfigurationSetSummary list_configuration_sets(type=type, user_id=user_id)

[EARLY ACCESS] ListConfigurationSets: List all configuration sets summaries (I.e. list of scope/code combinations available)

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_configuration
from lusid_configuration.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/configuration
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_configuration.ConfigurationSetsApi(api_client)
    type = 'type_example' # str | Whether the configuration set is Personal or Shared (optional)
user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

    try:
        # [EARLY ACCESS] ListConfigurationSets: List all configuration sets summaries (I.e. list of scope/code combinations available)
        api_response = api_instance.list_configuration_sets(type=type, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationSetsApi->list_configuration_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | [optional] 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ResourceListOfConfigurationSetSummary**](ResourceListOfConfigurationSetSummary.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration_item**
> ConfigurationItem update_configuration_item(type, scope, code, key, update_configuration_item, user_id=user_id)

[EARLY ACCESS] UpdateConfigurationItem: Update a configuration item's value and/or description

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_configuration
from lusid_configuration.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/configuration
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_configuration.ConfigurationSetsApi(api_client)
    type = 'type_example' # str | Whether the configuration set is Personal or Shared
scope = 'scope_example' # str | The scope that identifies a configuration set
code = 'code_example' # str | The code that identifies a configuration set
key = 'key_example' # str | The key that identifies a configuration item
update_configuration_item = {"value":"updated password","description":"Password for system A and B"} # UpdateConfigurationItem | The data to update a configuration item
user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

    try:
        # [EARLY ACCESS] UpdateConfigurationItem: Update a configuration item's value and/or description
        api_response = api_instance.update_configuration_item(type, scope, code, key, update_configuration_item, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationSetsApi->update_configuration_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | 
 **scope** | **str**| The scope that identifies a configuration set | 
 **code** | **str**| The code that identifies a configuration set | 
 **key** | **str**| The key that identifies a configuration item | 
 **update_configuration_item** | [**UpdateConfigurationItem**](UpdateConfigurationItem.md)| The data to update a configuration item | 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationItem**](ConfigurationItem.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration item exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_configuration_set**
> ConfigurationSet update_configuration_set(type, scope, code, update_configuration_set, user_id=user_id)

[EARLY ACCESS] UpdateConfigurationSet: Update the description of a configuration set

### Example

* OAuth Authentication (oauth2):
```python
from __future__ import print_function
import time
import lusid_configuration
from lusid_configuration.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://fbn-ci.lusid.com/configuration
# See configuration.py for a list of all supported configuration parameters.
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oauth2
configuration = lusid_configuration.Configuration(
    host = "https://fbn-ci.lusid.com/configuration"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with lusid_configuration.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = lusid_configuration.ConfigurationSetsApi(api_client)
    type = 'type_example' # str | Whether the configuration set is Personal or Shared
scope = 'scope_example' # str | The scope that identifies a configuration set
code = 'code_example' # str | The code that identifies a configuration set
update_configuration_set = {"description":"The group of configurations related to System A and B"} # UpdateConfigurationSet | The data to update a configuration set
user_id = 'user_id_example' # str | Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. (optional)

    try:
        # [EARLY ACCESS] UpdateConfigurationSet: Update the description of a configuration set
        api_response = api_instance.update_configuration_set(type, scope, code, update_configuration_set, user_id=user_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ConfigurationSetsApi->update_configuration_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Whether the configuration set is Personal or Shared | 
 **scope** | **str**| The scope that identifies a configuration set | 
 **code** | **str**| The code that identifies a configuration set | 
 **update_configuration_set** | [**UpdateConfigurationSet**](UpdateConfigurationSet.md)| The data to update a configuration set | 
 **user_id** | **str**| Feature that allows Administrators to administer personal settings  (but never reveal the value of secrets) of a specific user. | [optional] 

### Return type

[**ConfigurationSet**](ConfigurationSet.md)

### Authorization

[oauth2](../README.md#oauth2)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | The details of the input related failure |  -  |
**404** | No configuration set exists with the provided identifiers |  -  |
**0** | Error response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

