# hysds.mozart.client.HysdsIoApi

All URIs are relative to *http://localhost/mozart/api/v0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_hy_sdsio_type**](HysdsIoApi.md#get_get_hy_sdsio_type) | **GET** /hysds_io/type | Gets a HySDS-IO specification by ID
[**get_get_hy_sdsio_types**](HysdsIoApi.md#get_get_hy_sdsio_types) | **GET** /hysds_io/list | List HySDS IO specifications
[**get_remove_hy_sdsio_type**](HysdsIoApi.md#get_remove_hy_sdsio_type) | **GET** /hysds_io/remove | Remove HySDS IO for the given ID
[**post_add_hy_sdsio_type**](HysdsIoApi.md#post_add_hy_sdsio_type) | **POST** /hysds_io/add | Add a HySDS IO specification


# **get_get_hy_sdsio_type**
> HySDSIOResponseJSON get_get_hy_sdsio_type(id, x_fields=x_fields)

Gets a HySDS-IO specification by ID

Gets info on a hysds-io specification.

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
    api_instance = hysds.mozart.client.HysdsIoApi(api_client)
    id = 'id_example' # str | HySDS IO Type ID
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Gets a HySDS-IO specification by ID
        api_response = api_instance.get_get_hy_sdsio_type(id, x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HysdsIoApi->get_get_hy_sdsio_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| HySDS IO Type ID | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**HySDSIOResponseJSON**](HySDSIOResponseJSON.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Queue listing failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_get_hy_sdsio_types**
> HySDSIOListResponseJSON get_get_hy_sdsio_types(x_fields=x_fields)

List HySDS IO specifications

Gets list of registered hysds-io specifications and return as JSON.

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
    api_instance = hysds.mozart.client.HysdsIoApi(api_client)
    x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # List HySDS IO specifications
        api_response = api_instance.get_get_hy_sdsio_types(x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HysdsIoApi->get_get_hy_sdsio_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**HySDSIOListResponseJSON**](HySDSIOListResponseJSON.md)

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

# **get_remove_hy_sdsio_type**
> HySDSIORemovalResponseJSON get_remove_hy_sdsio_type(id, x_fields=x_fields)

Remove HySDS IO for the given ID

Removes a hysds-io specification.

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
    api_instance = hysds.mozart.client.HysdsIoApi(api_client)
    id = 'id_example' # str | HySDS IO ID
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Remove HySDS IO for the given ID
        api_response = api_instance.get_remove_hy_sdsio_type(id, x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HysdsIoApi->get_remove_hy_sdsio_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| HySDS IO ID | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**HySDSIORemovalResponseJSON**](HySDSIORemovalResponseJSON.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Remove JSON failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_add_hy_sdsio_type**
> HySDSIOAdditionResponseJSON post_add_hy_sdsio_type(spec, x_fields=x_fields)

Add a HySDS IO specification

Adds a hysds-io specification

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
    api_instance = hysds.mozart.client.HysdsIoApi(api_client)
    spec = 'spec_example' # str | HySDS IO JSON Object
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Add a HySDS IO specification
        api_response = api_instance.post_add_hy_sdsio_type(spec, x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling HysdsIoApi->post_add_hy_sdsio_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec** | **str**| HySDS IO JSON Object | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**HySDSIOAdditionResponseJSON**](HySDSIOAdditionResponseJSON.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Adding JSON failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

