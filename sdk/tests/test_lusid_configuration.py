import unittest
import json
import logging
import os

import lusid_configuration
from lusid_configuration import ConfigurationSetsApi
from fbnsdkutilities import ApiClientFactory

class LusidConfigurationTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:

        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.INFO)

        if os.getenv("FBN_ACCESS_TOKEN", None) is not None:
            cls.api_factory = ApiClientFactory(lusid_configuration, token=os.environ.get("FBN_ACCESS_TOKEN"))
        else:
            cls.api_factory = ApiClientFactory(lusid_configuration, api_secrets_filename="secrets.json")

        cls.api = cls.api_factory.build(lusid_configuration.api.ConfigurationSetsApi)

    def test_get_types(self):

        response = self.api.list_configuration_sets().values
        self.assertGreaterEqual(len(response), 0, response)


if __name__ == '__main__':
    unittest.main()
