# hysds.mozart.client
API for HySDS job submission and query.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import hysds.mozart.client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import hysds.mozart.client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
with hysds.mozart.client.ApiClient(configuration) as api_client:
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

## Documentation for API Endpoints

All URIs are relative to *http://localhost/mozart/api/v0.1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ContainerApi* | [**get_get_container_info**](docs/ContainerApi.md#get_get_container_info) | **GET** /container/info | Get information on container by ID
*ContainerApi* | [**get_get_container_remove**](docs/ContainerApi.md#get_get_container_remove) | **GET** /container/remove | Remove container based on ID
*ContainerApi* | [**get_get_container_types**](docs/ContainerApi.md#get_get_container_types) | **GET** /container/list | Get a list of containers managed by Mozart
*ContainerApi* | [**post_get_container_add**](docs/ContainerApi.md#post_get_container_add) | **POST** /container/add | Add a container specification to Mozart
*EventApi* | [**post_add_log_event**](docs/EventApi.md#post_add_log_event) | **POST** /event/add | Log HySDS custom event
*HysdsIoApi* | [**get_get_hy_sdsio_type**](docs/HysdsIoApi.md#get_get_hy_sdsio_type) | **GET** /hysds_io/type | Gets a HySDS-IO specification by ID
*HysdsIoApi* | [**get_get_hy_sdsio_types**](docs/HysdsIoApi.md#get_get_hy_sdsio_types) | **GET** /hysds_io/list | List HySDS IO specifications
*HysdsIoApi* | [**get_remove_hy_sdsio_type**](docs/HysdsIoApi.md#get_remove_hy_sdsio_type) | **GET** /hysds_io/remove | Remove HySDS IO for the given ID
*HysdsIoApi* | [**post_add_hy_sdsio_type**](docs/HysdsIoApi.md#post_add_hy_sdsio_type) | **POST** /hysds_io/add | Add a HySDS IO specification
*JobApi* | [**get_get_job_info**](docs/JobApi.md#get_get_job_info) | **GET** /job/info | Get complete infor on submitted job based on id
*JobApi* | [**get_get_job_status**](docs/JobApi.md#get_get_job_status) | **GET** /job/status | Gets the status of a submitted job based on job id
*JobApi* | [**get_get_jobs**](docs/JobApi.md#get_get_jobs) | **GET** /job/list | Paginated list submitted jobs
*JobApi* | [**post_submit_job**](docs/JobApi.md#post_submit_job) | **POST** /job/submit | Submits a job to run inside HySDS
*JobSpecApi* | [**get_get_job_spec_type**](docs/JobSpecApi.md#get_get_job_spec_type) | **GET** /job_spec/type | Gets a Job Type specification object for the given ID
*JobSpecApi* | [**get_get_job_types**](docs/JobSpecApi.md#get_get_job_types) | **GET** /job_spec/list | Gets a list of Job Type specifications
*JobSpecApi* | [**get_remove_job_spec_type**](docs/JobSpecApi.md#get_remove_job_spec_type) | **GET** /job_spec/remove | Remove Job Type specification for the given ID
*JobSpecApi* | [**post_add_job_spec_type**](docs/JobSpecApi.md#post_add_job_spec_type) | **POST** /job_spec/add | Add a Job Type specification JSON object
*QueueApi* | [**get_get_queue_names**](docs/QueueApi.md#get_get_queue_names) | **GET** /queue/list | Gets a listing of non-celery queues handling jobs


## Documentation For Models

 - [ContainerAddResponseJSON](docs/ContainerAddResponseJSON.md)
 - [ContainerInfoResponseJSON](docs/ContainerInfoResponseJSON.md)
 - [ContainerListResponseJSON](docs/ContainerListResponseJSON.md)
 - [ContainerRemovalResponseJSON](docs/ContainerRemovalResponseJSON.md)
 - [HySDSEventLogResponseJSON](docs/HySDSEventLogResponseJSON.md)
 - [HySDSIOAdditionResponseJSON](docs/HySDSIOAdditionResponseJSON.md)
 - [HySDSIOListResponseJSON](docs/HySDSIOListResponseJSON.md)
 - [HySDSIORemovalResponseJSON](docs/HySDSIORemovalResponseJSON.md)
 - [HySDSIOResponseJSON](docs/HySDSIOResponseJSON.md)
 - [JobInfoResponseJSON](docs/JobInfoResponseJSON.md)
 - [JobStatusResponseJSON](docs/JobStatusResponseJSON.md)
 - [JobTypeListResponseJSON](docs/JobTypeListResponseJSON.md)
 - [JobTypeSpecificationAdditionResponseJSON](docs/JobTypeSpecificationAdditionResponseJSON.md)
 - [JobTypeSpecificationRemovalResponseJSON](docs/JobTypeSpecificationRemovalResponseJSON.md)
 - [JobTypeSpecificationResponseJSON](docs/JobTypeSpecificationResponseJSON.md)
 - [JobsListingResponseJSON](docs/JobsListingResponseJSON.md)
 - [QueueListingResponseJSON](docs/QueueListingResponseJSON.md)
 - [SubmitJobResponse](docs/SubmitJobResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author




