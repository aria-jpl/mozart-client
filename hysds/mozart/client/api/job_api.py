# coding: utf-8

"""
    Mozart API

    API for HySDS job submission and query.  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hysds.mozart.client.api_client import ApiClient
from hysds.mozart.client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class JobApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_get_job_info(self, id, **kwargs):  # noqa: E501
        """Get complete infor on submitted job based on id  # noqa: E501

        Gets the complete info for a job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_job_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Job ID (required)
        :param str x_fields: An optional fields mask
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Job20Info20Response28JSON29
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_get_job_info_with_http_info(id, **kwargs)  # noqa: E501

    def get_get_job_info_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get complete infor on submitted job based on id  # noqa: E501

        Gets the complete info for a job.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_job_info_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Job ID (required)
        :param str x_fields: An optional fields mask
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Job20Info20Response28JSON29, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'x_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_get_job_info" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_get_job_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params and local_var_params['id'] is not None:  # noqa: E501
            query_params.append(('id', local_var_params['id']))  # noqa: E501

        header_params = {}
        if 'x_fields' in local_var_params:
            header_params['X-Fields'] = local_var_params['x_fields']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/job/info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Job20Info20Response28JSON29',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_get_job_status(self, id, **kwargs):  # noqa: E501
        """Gets the status of a submitted job based on job id  # noqa: E501

        Get status of job by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_job_status(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Job ID (required)
        :param str x_fields: An optional fields mask
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Job20Status20Response28JSON29
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_get_job_status_with_http_info(id, **kwargs)  # noqa: E501

    def get_get_job_status_with_http_info(self, id, **kwargs):  # noqa: E501
        """Gets the status of a submitted job based on job id  # noqa: E501

        Get status of job by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_job_status_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str id: Job ID (required)
        :param str x_fields: An optional fields mask
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Job20Status20Response28JSON29, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'id',
            'x_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_get_job_status" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in local_var_params or  # noqa: E501
                                                        local_var_params['id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `id` when calling `get_get_job_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in local_var_params and local_var_params['id'] is not None:  # noqa: E501
            query_params.append(('id', local_var_params['id']))  # noqa: E501

        header_params = {}
        if 'x_fields' in local_var_params:
            header_params['X-Fields'] = local_var_params['x_fields']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/job/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Job20Status20Response28JSON29',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_get_jobs(self, **kwargs):  # noqa: E501
        """Paginated list submitted jobs  # noqa: E501

        Get list of submitted job IDs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_jobs(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_fields: An optional fields mask
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Jobs20Listing20Response28JSON29
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_get_jobs_with_http_info(**kwargs)  # noqa: E501

    def get_get_jobs_with_http_info(self, **kwargs):  # noqa: E501
        """Paginated list submitted jobs  # noqa: E501

        Get list of submitted job IDs.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_get_jobs_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str x_fields: An optional fields mask
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Jobs20Listing20Response28JSON29, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'x_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_get_jobs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_fields' in local_var_params:
            header_params['X-Fields'] = local_var_params['x_fields']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/job/list', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Jobs20Listing20Response28JSON29',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_submit_job(self, type, queue, **kwargs):  # noqa: E501
        """Submits a job to run inside HySDS  # noqa: E501

        Submit job for execution in HySDS.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_submit_job(type, queue, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str type: a job type from jobspec/list (required)
        :param str queue: Job queue from /queue/list e.g. grfn-job_worker-small (required)
        :param int priority: Job priority in the range of 0 to 9
        :param str tags: JSON list of tags, e.g. [\"dumby\", \"test_job\"]
        :param str name: base job name override; defaults to job type
        :param str payload_hash: user-generated payload hash
        :param bool enable_dedup: flag to enable/disable job dedup
        :param str params: JSON job context, e.g. {         \"entity_id\": \"LC80101172015002LGN00\",         \"min_lat\": -79.09923,         \"max_lon\": -125.09297,         \"id\": \"dumby-product-20161114180506209624\",         \"acq_time\": \"2015-01-02T15:49:05.571384\",         \"min_sleep\": 1,         \"max_lat\": -77.7544,         \"min_lon\": -139.66082,         \"max_sleep\": 10     }
        :param str x_fields: An optional fields mask
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SubmitJobResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.post_submit_job_with_http_info(type, queue, **kwargs)  # noqa: E501

    def post_submit_job_with_http_info(self, type, queue, **kwargs):  # noqa: E501
        """Submits a job to run inside HySDS  # noqa: E501

        Submit job for execution in HySDS.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_submit_job_with_http_info(type, queue, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str type: a job type from jobspec/list (required)
        :param str queue: Job queue from /queue/list e.g. grfn-job_worker-small (required)
        :param int priority: Job priority in the range of 0 to 9
        :param str tags: JSON list of tags, e.g. [\"dumby\", \"test_job\"]
        :param str name: base job name override; defaults to job type
        :param str payload_hash: user-generated payload hash
        :param bool enable_dedup: flag to enable/disable job dedup
        :param str params: JSON job context, e.g. {         \"entity_id\": \"LC80101172015002LGN00\",         \"min_lat\": -79.09923,         \"max_lon\": -125.09297,         \"id\": \"dumby-product-20161114180506209624\",         \"acq_time\": \"2015-01-02T15:49:05.571384\",         \"min_sleep\": 1,         \"max_lat\": -77.7544,         \"min_lon\": -139.66082,         \"max_sleep\": 10     }
        :param str x_fields: An optional fields mask
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SubmitJobResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'type',
            'queue',
            'priority',
            'tags',
            'name',
            'payload_hash',
            'enable_dedup',
            'params',
            'x_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_submit_job" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'type' is set
        if self.api_client.client_side_validation and ('type' not in local_var_params or  # noqa: E501
                                                        local_var_params['type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `type` when calling `post_submit_job`")  # noqa: E501
        # verify the required parameter 'queue' is set
        if self.api_client.client_side_validation and ('queue' not in local_var_params or  # noqa: E501
                                                        local_var_params['queue'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `queue` when calling `post_submit_job`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'type' in local_var_params and local_var_params['type'] is not None:  # noqa: E501
            query_params.append(('type', local_var_params['type']))  # noqa: E501
        if 'queue' in local_var_params and local_var_params['queue'] is not None:  # noqa: E501
            query_params.append(('queue', local_var_params['queue']))  # noqa: E501
        if 'priority' in local_var_params and local_var_params['priority'] is not None:  # noqa: E501
            query_params.append(('priority', local_var_params['priority']))  # noqa: E501
        if 'tags' in local_var_params and local_var_params['tags'] is not None:  # noqa: E501
            query_params.append(('tags', local_var_params['tags']))  # noqa: E501
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'payload_hash' in local_var_params and local_var_params['payload_hash'] is not None:  # noqa: E501
            query_params.append(('payload_hash', local_var_params['payload_hash']))  # noqa: E501
        if 'enable_dedup' in local_var_params and local_var_params['enable_dedup'] is not None:  # noqa: E501
            query_params.append(('enable_dedup', local_var_params['enable_dedup']))  # noqa: E501
        if 'params' in local_var_params and local_var_params['params'] is not None:  # noqa: E501
            query_params.append(('params', local_var_params['params']))  # noqa: E501

        header_params = {}
        if 'x_fields' in local_var_params:
            header_params['X-Fields'] = local_var_params['x_fields']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/job/submit', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SubmitJobResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)