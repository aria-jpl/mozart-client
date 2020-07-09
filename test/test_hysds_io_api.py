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
from hysds.mozart.client.api.hysds_io_api import HysdsIoApi  # noqa: E501
from hysds.mozart.client.rest import ApiException


class TestHysdsIoApi(unittest.TestCase):
    """HysdsIoApi unit test stubs"""

    def setUp(self):
        self.api = hysds.mozart.client.api.hysds_io_api.HysdsIoApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_get_hy_sdsio_type(self):
        """Test case for get_get_hy_sdsio_type

        Gets a HySDS-IO specification by ID  # noqa: E501
        """
        pass

    def test_get_get_hy_sdsio_types(self):
        """Test case for get_get_hy_sdsio_types

        List HySDS IO specifications  # noqa: E501
        """
        pass

    def test_get_remove_hy_sdsio_type(self):
        """Test case for get_remove_hy_sdsio_type

        Remove HySDS IO for the given ID  # noqa: E501
        """
        pass

    def test_post_add_hy_sdsio_type(self):
        """Test case for post_add_hy_sdsio_type

        Add a HySDS IO specification  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()