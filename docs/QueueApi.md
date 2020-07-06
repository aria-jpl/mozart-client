# hysds.mozart.client.QueueApi

All URIs are relative to *http://localhost/mozart/api/v0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_queue_names**](QueueApi.md#get_get_queue_names) | **GET** /queue/list | Gets a listing of non-celery queues handling jobs


# **get_get_queue_names**
> Queue20Listing20Response28JSON29 get_get_queue_names(id=id, x_fields=x_fields)

Gets a listing of non-celery queues handling jobs

Get list of available job queues and return as JSON.

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
    api_instance = hysds.mozart.client.QueueApi(api_client)
    id = 'id_example' # str | Job Type Specification ID (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Gets a listing of non-celery queues handling jobs
        api_response = api_instance.get_get_queue_names(id=id, x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling QueueApi->get_get_queue_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job Type Specification ID | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Queue20Listing20Response28JSON29**](Queue20Listing20Response28JSON29.md)

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

