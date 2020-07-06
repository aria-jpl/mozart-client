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
from hysds.mozart.client.models.submit_job_response import SubmitJobResponse  # noqa: E501
from hysds.mozart.client.rest import ApiException

class TestSubmitJobResponse(unittest.TestCase):
    """SubmitJobResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubmitJobResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = hysds.mozart.client.models.submit_job_response.SubmitJobResponse()  # noqa: E501
        if include_optional :
            return SubmitJobResponse(
                success = True, 
                message = '0', 
                result = '0'
            )
        else :
            return SubmitJobResponse(
                success = True,
                message = '0',
                result = '0',
        )

    def testSubmitJobResponse(self):
        """Test SubmitJobResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
