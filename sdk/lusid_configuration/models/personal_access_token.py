# coding: utf-8

"""
    FINBOURNE ConfigurationService API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 0.1.429
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


class PersonalAccessToken(object):
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
        'value': 'str',
        'type': 'str',
        'description': 'str',
        'ref': 'str',
        'links': 'list[Link]'
    }

    attribute_map = {
        'value': 'value',
        'type': 'type',
        'description': 'description',
        'ref': 'ref',
        'links': 'links'
    }

    required_map = {
        'value': 'required',
        'type': 'required',
        'description': 'required',
        'ref': 'required',
        'links': 'optional'
    }

    def __init__(self, value=None, type=None, description=None, ref=None, links=None, local_vars_configuration=None):  # noqa: E501
        """PersonalAccessToken - a model defined in OpenAPI"
        
        :param value:  Value of the Personal Access Token. (required)
        :type value: str
        :param type:  The type of the Personal Access Token. (required)
        :type type: str
        :param description:  The description of the Personal Access Token. (required)
        :type description: str
        :param ref:  The reference to the Personal Access Token (required)
        :type ref: str
        :param links: 
        :type links: list[lusid_configuration.Link]

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._value = None
        self._type = None
        self._description = None
        self._ref = None
        self._links = None
        self.discriminator = None

        self.value = value
        self.type = type
        self.description = description
        self.ref = ref
        self.links = links

    @property
    def value(self):
        """Gets the value of this PersonalAccessToken.  # noqa: E501

        Value of the Personal Access Token.  # noqa: E501

        :return: The value of this PersonalAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PersonalAccessToken.

        Value of the Personal Access Token.  # noqa: E501

        :param value: The value of this PersonalAccessToken.  # noqa: E501
        :type value: str
        """
        if self.local_vars_configuration.client_side_validation and value is None:  # noqa: E501
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                value is not None and len(value) < 1):
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

        self._value = value

    @property
    def type(self):
        """Gets the type of this PersonalAccessToken.  # noqa: E501

        The type of the Personal Access Token.  # noqa: E501

        :return: The type of this PersonalAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PersonalAccessToken.

        The type of the Personal Access Token.  # noqa: E501

        :param type: The type of this PersonalAccessToken.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                type is not None and len(type) < 1):
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def description(self):
        """Gets the description of this PersonalAccessToken.  # noqa: E501

        The description of the Personal Access Token.  # noqa: E501

        :return: The description of this PersonalAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PersonalAccessToken.

        The description of the Personal Access Token.  # noqa: E501

        :param description: The description of this PersonalAccessToken.  # noqa: E501
        :type description: str
        """
        if self.local_vars_configuration.client_side_validation and description is None:  # noqa: E501
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def ref(self):
        """Gets the ref of this PersonalAccessToken.  # noqa: E501

        The reference to the Personal Access Token  # noqa: E501

        :return: The ref of this PersonalAccessToken.  # noqa: E501
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """Sets the ref of this PersonalAccessToken.

        The reference to the Personal Access Token  # noqa: E501

        :param ref: The ref of this PersonalAccessToken.  # noqa: E501
        :type ref: str
        """
        if self.local_vars_configuration.client_side_validation and ref is None:  # noqa: E501
            raise ValueError("Invalid value for `ref`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                ref is not None and len(ref) < 1):
            raise ValueError("Invalid value for `ref`, length must be greater than or equal to `1`")  # noqa: E501

        self._ref = ref

    @property
    def links(self):
        """Gets the links of this PersonalAccessToken.  # noqa: E501


        :return: The links of this PersonalAccessToken.  # noqa: E501
        :rtype: list[lusid_configuration.Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PersonalAccessToken.


        :param links: The links of this PersonalAccessToken.  # noqa: E501
        :type links: list[lusid_configuration.Link]
        """

        self._links = links

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
        if not isinstance(other, PersonalAccessToken):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PersonalAccessToken):
            return True

        return self.to_dict() != other.to_dict()
