# coding: utf-8

"""
    FINBOURNE ConfigurationService API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.379
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


class CreateConfigurationItem(object):
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
        'key': 'str',
        'value': 'str',
        'value_type': 'str',
        'is_secret': 'bool',
        'description': 'str'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'value_type': 'valueType',
        'is_secret': 'isSecret',
        'description': 'description'
    }

    required_map = {
        'key': 'required',
        'value': 'required',
        'value_type': 'optional',
        'is_secret': 'required',
        'description': 'optional'
    }

    def __init__(self, key=None, value=None, value_type=None, is_secret=None, description=None, local_vars_configuration=None):  # noqa: E501
        """CreateConfigurationItem - a model defined in OpenAPI"
        
        :param key:  The key of the new configuration item (required)
        :type key: str
        :param value:  The value of the new configuration item                The maximum size for secrets is 4KB and for text values is 2MB (required)
        :type value: str
        :param value_type:  The type (text, number, boolean, textCollection, numberCollection) of the new configuration item's value.  The validation for each type is as follows:  - text: any value  - number: double (e.g. \"5.5\")  - boolean: true/false  - textCollection: comma separated list (e.g. \"a,b,c\")  - numberCollection: comma separated list of doubles (e.g. \"1,2,3\")
        :type value_type: str
        :param is_secret:  Defines whether or not the value is a secret (required)
        :type is_secret: bool
        :param description:  The description of the new configuration item
        :type description: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._key = None
        self._value = None
        self._value_type = None
        self._is_secret = None
        self._description = None
        self.discriminator = None

        self.key = key
        self.value = value
        self.value_type = value_type
        self.is_secret = is_secret
        self.description = description

    @property
    def key(self):
        """Gets the key of this CreateConfigurationItem.  # noqa: E501

        The key of the new configuration item  # noqa: E501

        :return: The key of this CreateConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateConfigurationItem.

        The key of the new configuration item  # noqa: E501

        :param key: The key of this CreateConfigurationItem.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key is not None and len(key) > 256):
            raise ValueError("Invalid value for `key`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key is not None and len(key) < 1):
            raise ValueError("Invalid value for `key`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                key is not None and not re.search(r'^[^_][a-zA-Z0-9\-_]*$', key)):  # noqa: E501
            raise ValueError(r"Invalid value for `key`, must be a follow pattern or equal to `/^[^_][a-zA-Z0-9\-_]*$/`")  # noqa: E501

        self._key = key

    @property
    def value(self):
        """Gets the value of this CreateConfigurationItem.  # noqa: E501

        The value of the new configuration item                The maximum size for secrets is 4KB and for text values is 2MB  # noqa: E501

        :return: The value of this CreateConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateConfigurationItem.

        The value of the new configuration item                The maximum size for secrets is 4KB and for text values is 2MB  # noqa: E501

        :param value: The value of this CreateConfigurationItem.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value is not None and len(value) > 2000000):
            raise ValueError("Invalid value for `value`, length must be less than or equal to `2000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value is not None and len(value) < 1):
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value is not None and not re.search(r'(?s).*', value)):  # noqa: E501
            raise ValueError(r"Invalid value for `value`, must be a follow pattern or equal to `/(?s).*/`")  # noqa: E501

        self._value = value

    @property
    def value_type(self):
        """Gets the value_type of this CreateConfigurationItem.  # noqa: E501

        The type (text, number, boolean, textCollection, numberCollection) of the new configuration item's value.  The validation for each type is as follows:  - text: any value  - number: double (e.g. \"5.5\")  - boolean: true/false  - textCollection: comma separated list (e.g. \"a,b,c\")  - numberCollection: comma separated list of doubles (e.g. \"1,2,3\")  # noqa: E501

        :return: The value_type of this CreateConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this CreateConfigurationItem.

        The type (text, number, boolean, textCollection, numberCollection) of the new configuration item's value.  The validation for each type is as follows:  - text: any value  - number: double (e.g. \"5.5\")  - boolean: true/false  - textCollection: comma separated list (e.g. \"a,b,c\")  - numberCollection: comma separated list of doubles (e.g. \"1,2,3\")  # noqa: E501

        :param value_type: The value_type of this CreateConfigurationItem.  # noqa: E501
        :type value_type: str
        """

        self._value_type = value_type

    @property
    def is_secret(self):
        """Gets the is_secret of this CreateConfigurationItem.  # noqa: E501

        Defines whether or not the value is a secret  # noqa: E501

        :return: The is_secret of this CreateConfigurationItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_secret

    @is_secret.setter
    def is_secret(self, is_secret):
        """Sets the is_secret of this CreateConfigurationItem.

        Defines whether or not the value is a secret  # noqa: E501

        :param is_secret: The is_secret of this CreateConfigurationItem.  # noqa: E501
        :type is_secret: bool
        """
        if self.local_vars_configuration.client_side_validation and is_secret is None:  # noqa: E501
            raise ValueError("Invalid value for `is_secret`, must not be `None`")  # noqa: E501

        self._is_secret = is_secret

    @property
    def description(self):
        """Gets the description of this CreateConfigurationItem.  # noqa: E501

        The description of the new configuration item  # noqa: E501

        :return: The description of this CreateConfigurationItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateConfigurationItem.

        The description of the new configuration item  # noqa: E501

        :param description: The description of this CreateConfigurationItem.  # noqa: E501
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
        if not isinstance(other, CreateConfigurationItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateConfigurationItem):
            return True

        return self.to_dict() != other.to_dict()
