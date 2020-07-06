# coding: utf-8

"""
    Mozart API

    API for HySDS job submission and query.  # noqa: E501

    The version of the OpenAPI document: 0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hysds.mozart.client.configuration import Configuration


class HySDSEventLogResponseJSON(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'success': 'bool',
        'message': 'str',
        'result': 'str'
    }

    attribute_map = {
        'success': 'success',
        'message': 'message',
        'result': 'result'
    }

    def __init__(self, success=None, message=None, result=None, local_vars_configuration=None):  # noqa: E501
        """HySDSEventLogResponseJSON - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._success = None
        self._message = None
        self._result = None
        self.discriminator = None

        self.success = success
        self.message = message
        self.result = result

    @property
    def success(self):
        """Gets the success of this HySDSEventLogResponseJSON.  # noqa: E501

        if 'false', encountered exception; otherwise no errors occurred  # noqa: E501

        :return: The success of this HySDSEventLogResponseJSON.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this HySDSEventLogResponseJSON.

        if 'false', encountered exception; otherwise no errors occurred  # noqa: E501

        :param success: The success of this HySDSEventLogResponseJSON.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and success is None:  # noqa: E501
            raise ValueError("Invalid value for `success`, must not be `None`")  # noqa: E501

        self._success = success

    @property
    def message(self):
        """Gets the message of this HySDSEventLogResponseJSON.  # noqa: E501

        message describing success or failure  # noqa: E501

        :return: The message of this HySDSEventLogResponseJSON.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this HySDSEventLogResponseJSON.

        message describing success or failure  # noqa: E501

        :param message: The message of this HySDSEventLogResponseJSON.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message is None:  # noqa: E501
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def result(self):
        """Gets the result of this HySDSEventLogResponseJSON.  # noqa: E501

        HySDS custom event log ID  # noqa: E501

        :return: The result of this HySDSEventLogResponseJSON.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this HySDSEventLogResponseJSON.

        HySDS custom event log ID  # noqa: E501

        :param result: The result of this HySDSEventLogResponseJSON.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and result is None:  # noqa: E501
            raise ValueError("Invalid value for `result`, must not be `None`")  # noqa: E501

        self._result = result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, HySDSEventLogResponseJSON):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HySDSEventLogResponseJSON):
            return True

        return self.to_dict() != other.to_dict()
