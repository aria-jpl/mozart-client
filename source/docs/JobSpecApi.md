# hysds.mozart.client.JobSpecApi

All URIs are relative to *http://localhost/mozart/api/v0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_job_spec_type**](JobSpecApi.md#get_get_job_spec_type) | **GET** /job_spec/type | Gets a Job Type specification object for the given ID
[**get_get_job_types**](JobSpecApi.md#get_get_job_types) | **GET** /job_spec/list | Gets a list of Job Type specifications
[**get_remove_job_spec_type**](JobSpecApi.md#get_remove_job_spec_type) | **GET** /job_spec/remove | Remove Job Type specification for the given ID
[**post_add_job_spec_type**](JobSpecApi.md#post_add_job_spec_type) | **POST** /job_spec/add | Add a Job Type specification JSON object


# **get_get_job_spec_type**
> JobTypeSpecificationResponseJSON get_get_job_spec_type(id, x_fields=x_fields)

Gets a Job Type specification object for the given ID

Get a full JSON specification of job type from id.

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
    api_instance = hysds.mozart.client.JobSpecApi(api_client)
    id = 'id_example' # str | Job Type ID
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Gets a Job Type specification object for the given ID
        api_response = api_instance.get_get_job_spec_type(id, x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobSpecApi->get_get_job_spec_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job Type ID | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**JobTypeSpecificationResponseJSON**](JobTypeSpecificationResponseJSON.md)

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

# **get_get_job_types**
> JobTypeListResponseJSON get_get_job_types(x_fields=x_fields)

Gets a list of Job Type specifications

Get list of registered job types and return as JSON.

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
    api_instance = hysds.mozart.client.JobSpecApi(api_client)
    x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Gets a list of Job Type specifications
        api_response = api_instance.get_get_job_types(x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobSpecApi->get_get_job_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**JobTypeListResponseJSON**](JobTypeListResponseJSON.md)

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

# **get_remove_job_spec_type**
> JobTypeSpecificationRemovalResponseJSON get_remove_job_spec_type(id, x_fields=x_fields)

Remove Job Type specification for the given ID

Removes a job type specification.

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
    api_instance = hysds.mozart.client.JobSpecApi(api_client)
    id = 'id_example' # str | Job Type Specification ID
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Remove Job Type specification for the given ID
        api_response = api_instance.get_remove_job_spec_type(id, x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobSpecApi->get_remove_job_spec_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job Type Specification ID | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**JobTypeSpecificationRemovalResponseJSON**](JobTypeSpecificationRemovalResponseJSON.md)

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

# **post_add_job_spec_type**
> JobTypeSpecificationAdditionResponseJSON post_add_job_spec_type(spec, x_fields=x_fields)

Add a Job Type specification JSON object

Adds a job type specification from JSON.

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
    api_instance = hysds.mozart.client.JobSpecApi(api_client)
    spec = 'spec_example' # str | Job Type Specification JSON Object
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Add a Job Type specification JSON object
        api_response = api_instance.post_add_job_spec_type(spec, x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobSpecApi->post_add_job_spec_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spec** | **str**| Job Type Specification JSON Object | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**JobTypeSpecificationAdditionResponseJSON**](JobTypeSpecificationAdditionResponseJSON.md)

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

