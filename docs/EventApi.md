# hysds.mozart.client.EventApi

All URIs are relative to *http://localhost/mozart/api/v0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**post_add_log_event**](EventApi.md#post_add_log_event) | **POST** /event/add | Log HySDS custom event


# **post_add_log_event**
> HySDS20Event20Log20Response28JSON29 post_add_log_event(type, status, event, tags=tags, hostname=hostname, x_fields=x_fields)

Log HySDS custom event

Logs a HySDS custom event

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
    api_instance = hysds.mozart.client.EventApi(api_client)
    type = 'type_example' # str | Event type, e.g. aws_autoscaling, verdi_anomalies
status = 'status_example' # str | Event status, e.g. spot_termination, docker_daemon_failed
event = 'event_example' # str | Arbitrary JSON event payload, e.g. {} or {         \"ec2_instance_id\": \"i-07b8989f41ce23880\",         \"private_ip\": \"100.64.134.145\",         \"az\": \"us-west-2a\",         \"reservation\": \"r-02fd006170749a0a8\",         \"termination_date\": \"2015-01-02T15:49:05.571384\"     }
tags = 'tags_example' # str | JSON list of tags, e.g. [\"dumby\", \"test_job\"] (optional)
hostname = 'hostname_example' # str | Event-related hostname, e.g. \"job.hysds.net\", \"192.168.0.1\" (optional)
x_fields = 'x_fields_example' # str | An optional fields mask (optional)

    try:
        # Log HySDS custom event
        api_response = api_instance.post_add_log_event(type, status, event, tags=tags, hostname=hostname, x_fields=x_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling EventApi->post_add_log_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Event type, e.g. aws_autoscaling, verdi_anomalies | 
 **status** | **str**| Event status, e.g. spot_termination, docker_daemon_failed | 
 **event** | **str**| Arbitrary JSON event payload, e.g. {} or {         \&quot;ec2_instance_id\&quot;: \&quot;i-07b8989f41ce23880\&quot;,         \&quot;private_ip\&quot;: \&quot;100.64.134.145\&quot;,         \&quot;az\&quot;: \&quot;us-west-2a\&quot;,         \&quot;reservation\&quot;: \&quot;r-02fd006170749a0a8\&quot;,         \&quot;termination_date\&quot;: \&quot;2015-01-02T15:49:05.571384\&quot;     } | 
 **tags** | **str**| JSON list of tags, e.g. [\&quot;dumby\&quot;, \&quot;test_job\&quot;] | [optional] 
 **hostname** | **str**| Event-related hostname, e.g. \&quot;job.hysds.net\&quot;, \&quot;192.168.0.1\&quot; | [optional] 
 **x_fields** | **str**| An optional fields mask | [optional] 

### Return type

[**HySDS20Event20Log20Response28JSON29**](HySDS20Event20Log20Response28JSON29.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**500** | Event log failed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

