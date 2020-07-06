# coding: utf-8

"""
    Mozart API

    API for HySDS job submission and query.  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import hysds.mozart.client
from hysds.mozart.client.api.job_spec_api import JobSpecApi  # noqa: E501
from hysds.mozart.client.rest import ApiException


class TestJobSpecApi(unittest.TestCase):
    """JobSpecApi unit test stubs"""

    def setUp(self):
        self.api = hysds.mozart.client.api.job_spec_api.JobSpecApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_get_job_spec_type(self):
        """Test case for get_get_job_spec_type

        Gets a Job Type specification object for the given ID  # noqa: E501
        """
        pass

    def test_get_get_job_types(self):
        """Test case for get_get_job_types

        Gets a list of Job Type specifications  # noqa: E501
        """
        pass

    def test_get_remove_job_spec_type(self):
        """Test case for get_remove_job_spec_type

        Remove Job Type specification for the given ID  # noqa: E501
        """
        pass

    def test_post_add_job_spec_type(self):
        """Test case for post_add_job_spec_type

        Add a Job Type specification JSON object  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
