# coding: utf-8

"""
    Mozart API

    API for HySDS job submission and query.  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import hysds.mozart.client
from hysds.mozart.client.models.job_status_response_json import JobStatusResponseJSON  # noqa: E501
from hysds.mozart.client.rest import ApiException

class TestJobStatusResponseJSON(unittest.TestCase):
    """JobStatusResponseJSON unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobStatusResponseJSON
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = hysds.mozart.client.models.job_status_response_json.JobStatusResponseJSON()  # noqa: E501
        if include_optional :
            return JobStatusResponseJSON(
                success = True, 
                status = 'job-queued', 
                message = '0'
            )
        else :
            return JobStatusResponseJSON(
                success = True,
                status = 'job-queued',
                message = '0',
        )

    def testJobStatusResponseJSON(self):
        """Test JobStatusResponseJSON"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
