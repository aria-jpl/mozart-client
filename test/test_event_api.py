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
from hysds.mozart.client.api.event_api import EventApi  # noqa: E501
from hysds.mozart.client.rest import ApiException


class TestEventApi(unittest.TestCase):
    """EventApi unit test stubs"""

    def setUp(self):
        self.api = hysds.mozart.client.api.event_api.EventApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_post_add_log_event(self):
        """Test case for post_add_log_event

        Log HySDS custom event  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
