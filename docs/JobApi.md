# hysds.mozart.client.JobApi

All URIs are relative to *http://localhost/mozart/api/v0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_get_job_info**](JobApi.md#get_get_job_info) | **GET** /job/info | Get complete infor on submitted job based on id
[**get_get_job_status**](JobApi.md#get_get_job_status) | **GET** /job/status | Gets the status of a submitted job based on job id
[**get_get_jobs**](JobApi.md#get_get_jobs) | **GET** /job/list | Paginated list submitted jobs
[**post_submit_job**](JobApi.md#post_submit_job) | **POST** /job/submit | Submits a job to run inside HySDS


# **get_get_job_info**
> Job20Info20Response28JSON29 get_get_job_info(id, x_fields=x_fields)

Get complete infor on submitted job based on id

Gets the complete info for a job.

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
    api_instance = hysds.mozart.client.JobApi(api_client)
    id = 'id_example' # str | Job ID
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Get complete infor on submitted job based on id
        api_response = api_instance.get_get_job_info(id, x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->get_get_job_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job ID | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Job20Info20Response28JSON29**](Job20Info20Response28JSON29.md)

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

# **get_get_job_status**
> Job20Status20Response28JSON29 get_get_job_status(id, x_fields=x_fields)

Gets the status of a submitted job based on job id

Get status of job by ID.

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
    api_instance = hysds.mozart.client.JobApi(api_client)
    id = 'id_example' # str | Job ID
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Gets the status of a submitted job based on job id
        api_response = api_instance.get_get_job_status(id, x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->get_get_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Job ID | 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Job20Status20Response28JSON29**](Job20Status20Response28JSON29.md)

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

# **get_get_jobs**
> Jobs20Listing20Response28JSON29 get_get_jobs(x_fields=x_fields)

Paginated list submitted jobs

Get list of submitted job IDs.

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
    api_instance = hysds.mozart.client.JobApi(api_client)
    x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Paginated list submitted jobs
        api_response = api_instance.get_get_jobs(x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->get_get_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**Jobs20Listing20Response28JSON29**](Jobs20Listing20Response28JSON29.md)

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

# **post_submit_job**
> SubmitJobResponse post_submit_job(type, queue, priority=priority, tags=tags, name=name, payload_hash=payload_hash, enable_dedup=enable_dedup, params=params, x_fields=x_fields)

Submits a job to run inside HySDS

Submit job for execution in HySDS.

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
    api_instance = hysds.mozart.client.JobApi(api_client)
    type = 'type_example' # str | a job type from jobspec/list
queue = 'queue_example' # str | Job queue from /queue/list e.g. grfn-job_worker-small
priority = 56 # int | Job priority in the range of 0 to 9 (optional)
tags = 'tags_example' # str | JSON list of tags, e.g. [\"dumby\", \"test_job\"] (optional)
name = 'name_example' # str | base job name override; defaults to job type (optional)
payload_hash = 'payload_hash_example' # str | user-generated payload hash (optional)
enable_dedup = True # bool | flag to enable/disable job dedup (optional)
params = 'params_example' # str | JSON job context, e.g. {         \"entity_id\": \"LC80101172015002LGN00\",         \"min_lat\": -79.09923,         \"max_lon\": -125.09297,         \"id\": \"dumby-product-20161114180506209624\",         \"acq_time\": \"2015-01-02T15:49:05.571384\",         \"min_sleep\": 1,         \"max_lat\": -77.7544,         \"min_lon\": -139.66082,         \"max_sleep\": 10     } (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Submits a job to run inside HySDS
        api_response = api_instance.post_submit_job(type, queue, priority=priority, tags=tags, name=name, payload_hash=payload_hash, enable_dedup=enable_dedup, params=params, x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling JobApi->post_submit_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| a job type from jobspec/list | 
 **queue** | **str**| Job queue from /queue/list e.g. grfn-job_worker-small | 
 **priority** | **int**| Job priority in the range of 0 to 9 | [optional] 
 **tags** | **str**| JSON list of tags, e.g. [\&quot;dumby\&quot;, \&quot;test_job\&quot;] | [optional] 
 **name** | **str**| base job name override; defaults to job type | [optional] 
 **payload_hash** | **str**| user-generated payload hash | [optional] 
 **enable_dedup** | **bool**| flag to enable/disable job dedup | [optional] 
 **params** | **str**| JSON job context, e.g. {         \&quot;entity_id\&quot;: \&quot;LC80101172015002LGN00\&quot;,         \&quot;min_lat\&quot;: -79.09923,         \&quot;max_lon\&quot;: -125.09297,         \&quot;id\&quot;: \&quot;dumby-product-20161114180506209624\&quot;,         \&quot;acq_time\&quot;: \&quot;2015-01-02T15:49:05.571384\&quot;,         \&quot;min_sleep\&quot;: 1,         \&quot;max_lat\&quot;: -77.7544,         \&quot;min_lon\&quot;: -139.66082,         \&quot;max_sleep\&quot;: 10     } | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**SubmitJobResponse**](SubmitJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid parameters |  -  |
**500** | Job submission failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

