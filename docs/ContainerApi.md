# hysds.mozart.client.ContainerApi

All URIs are relative to *http://localhost/mozart/api/v0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_container_info**](ContainerApi.md#get_get_container_info) | **GET** /container/info | Get information on container by ID
[**get_get_container_remove**](ContainerApi.md#get_get_container_remove) | **GET** /container/remove | Remove container based on ID
[**get_get_container_types**](ContainerApi.md#get_get_container_types) | **GET** /container/list | Get a list of containers managed by Mozart
[**post_get_container_add**](ContainerApi.md#post_get_container_add) | **POST** /container/add | Add a container specification to Mozart


# **get_get_container_info**
> ContainerInfoResponseJSON get_get_container_info(id, x_fields=x_fields)

Get information on container by ID

Get info on a container.

### Example

```python
from __future__ import print_function
import time
import hysds.mozart.client
from hysds.mozart.client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/mozart/api/v0.1
# See configuration.py for a list of all supported configuration parameters.
configuration = hysds.mozart.client.Configuration(
    host = "http://localhost/mozart/api/v0.1"
)


# Enter a context with an instance of the API client
with hysds.mozart.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = hysds.mozart.client.ContainerApi(api_client)
    id = 'id_example' # str | Container ID
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Get information on container by ID
        api_response = api_instance.get_get_container_info(id, x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerApi->get_get_container_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Container ID | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ContainerInfoResponseJSON**](ContainerInfoResponseJSON.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Query execution failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_container_remove**
> ContainerRemovalResponseJSON get_get_container_remove(id, x_fields=x_fields)

Remove container based on ID

Remove a container.

### Example

```python
from __future__ import print_function
import time
import hysds.mozart.client
from hysds.mozart.client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/mozart/api/v0.1
# See configuration.py for a list of all supported configuration parameters.
configuration = hysds.mozart.client.Configuration(
    host = "http://localhost/mozart/api/v0.1"
)


# Enter a context with an instance of the API client
with hysds.mozart.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = hysds.mozart.client.ContainerApi(api_client)
    id = 'id_example' # str | Container ID
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Remove container based on ID
        api_response = api_instance.get_get_container_remove(id, x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerApi->get_get_container_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Container ID | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ContainerRemovalResponseJSON**](ContainerRemovalResponseJSON.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Query execution failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_container_types**
> ContainerListResponseJSON get_get_container_types(x_fields=x_fields)

Get a list of containers managed by Mozart

Get list of registered containers and return as JSON.

### Example

```python
from __future__ import print_function
import time
import hysds.mozart.client
from hysds.mozart.client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/mozart/api/v0.1
# See configuration.py for a list of all supported configuration parameters.
configuration = hysds.mozart.client.Configuration(
    host = "http://localhost/mozart/api/v0.1"
)


# Enter a context with an instance of the API client
with hysds.mozart.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = hysds.mozart.client.ContainerApi(api_client)
    x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Get a list of containers managed by Mozart
        api_response = api_instance.get_get_container_types(x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerApi->get_get_container_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ContainerListResponseJSON**](ContainerListResponseJSON.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Query execution failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_get_container_add**
> ContainerAddResponseJSON post_get_container_add(name, url, version, digest, x_fields=x_fields)

Add a container specification to Mozart

Add a new container.

### Example

```python
from __future__ import print_function
import time
import hysds.mozart.client
from hysds.mozart.client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/mozart/api/v0.1
# See configuration.py for a list of all supported configuration parameters.
configuration = hysds.mozart.client.Configuration(
    host = "http://localhost/mozart/api/v0.1"
)


# Enter a context with an instance of the API client
with hysds.mozart.client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = hysds.mozart.client.ContainerApi(api_client)
    name = 'name_example' # str | Container Name
url = 'url_example' # str | Container URL
version = 'version_example' # str | Container Version
digest = 'digest_example' # str | Container Digest
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Add a container specification to Mozart
        api_response = api_instance.post_get_container_add(name, url, version, digest, x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ContainerApi->post_get_container_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Container Name | 
 **url** | **str**| Container URL | 
 **version** | **str**| Container Version | 
 **digest** | **str**| Container Digest | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**ContainerAddResponseJSON**](ContainerAddResponseJSON.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Query execution failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

