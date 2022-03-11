# coding: utf-8

"""
    FINBOURNE ConfigurationService API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.210
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid_configuration.configuration import Configuration


class CreateConfigurationSet(object):
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
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'id': 'ResourceId',
        'type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'type': 'type',
        'description': 'description'
    }

    required_map = {
        'id': 'required',
        'type': 'required',
        'description': 'optional'
    }

    def __init__(self, id=None, type=None, description=None, local_vars_configuration=None):  # noqa: E501
        """CreateConfigurationSet - a model defined in OpenAPI"
        
        :param id:  (required)
        :type id: lusid_configuration.ResourceId
        :param type:  The type (personal or shared) of the new configuration set (required)
        :type type: str
        :param description:  The description of the new configuration set
        :type description: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._type = None
        self._description = None
        self.discriminator = None

        self.id = id
        self.type = type
        self.description = description

    @property
    def id(self):
        """Gets the id of this CreateConfigurationSet.  # noqa: E501


        :return: The id of this CreateConfigurationSet.  # noqa: E501
        :rtype: lusid_configuration.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateConfigurationSet.


        :param id: The id of this CreateConfigurationSet.  # noqa: E501
        :type id: lusid_configuration.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def type(self):
        """Gets the type of this CreateConfigurationSet.  # noqa: E501

        The type (personal or shared) of the new configuration set  # noqa: E501

        :return: The type of this CreateConfigurationSet.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CreateConfigurationSet.

        The type (personal or shared) of the new configuration set  # noqa: E501

        :param type: The type of this CreateConfigurationSet.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def description(self):
        """Gets the description of this CreateConfigurationSet.  # noqa: E501

        The description of the new configuration set  # noqa: E501

        :return: The description of this CreateConfigurationSet.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateConfigurationSet.

        The description of the new configuration set  # noqa: E501

        :param description: The description of this CreateConfigurationSet.  # noqa: E501
        :type description: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 255):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 0):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `0`")  # noqa: E501

        self._description = description

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateConfigurationSet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateConfigurationSet):
            return True

        return self.to_dict() != other.to_dict()
