# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class Parameter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, value=None):  # noqa: E501
        """Parameter - a model defined in OpenAPI

        :param name: The name of this Parameter.  # noqa: E501
        :type name: str
        :param value: The value of this Parameter.  # noqa: E501
        :type value: object
        """
        self.openapi_types = {
            'name': str,
            'value': object
        }

        self.attribute_map = {
            'name': 'name',
            'value': 'value'
        }

        self._name = name
        self._value = value

    @classmethod
    def from_dict(cls, dikt) -> 'Parameter':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Parameter of this Parameter.  # noqa: E501
        :rtype: Parameter
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this Parameter.

        Name of the feature  # noqa: E501

        :return: The name of this Parameter.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Parameter.

        Name of the feature  # noqa: E501

        :param name: The name of this Parameter.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def value(self):
        """Gets the value of this Parameter.

        Value of the feature  # noqa: E501

        :return: The value of this Parameter.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Parameter.

        Value of the feature  # noqa: E501

        :param value: The value of this Parameter.
        :type value: object
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value
