# LUSID<sup>®</sup> Configuration Python Preview SDK
This is the Python Preview SDK for the Configuration API for [LUSID by FINBOURNE](https://www.finbourne.com/lusid-technology), a bi-temporal investment management data platform with portfolio accounting capabilities. To use it you'll need a LUSID account. [Sign up for free at lusid.com](https://www.lusid.com/app/signup)

<a href="https://www.lusid.com/app/signup"><img src="https://content.finbourne.com/LUSID_repo.png" alt="LUSID_by_Finbourne"></a>

| branch | status |
| --- | --- |
| `master` |  ![PyPI](https://img.shields.io/pypi/v/lusid-configuration-sdk-preview?color=blue)

## Installation

The PyPi package for the LUSID Configuration Preview SDK can installed using the following:

```
pip install lusid-configuration-sdk-preview finbourne-sdk-utilities
```

## Usage

```
import lusid_configuration
from fbnsdkutilities import ApiClientFactory

scheduler_factory = ApiClientFactory(lusid_configuration, api_secrets_filename="/path/to/secrets.json")
sets_api = scheduler_factory.build(lusid_configuration.api.ConfigurationSetsApi)

sets_api.list_configuration_sets()
```
