# CreateConfigurationItem

The information required to create a configuration item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the new configuration item | 
**value** | **str** | The value of the new configuration item                The maximum size for secrets is 4KB and for text values is 2MB | 
**type** | **str** | The type (text or secret) of the new configuration item | [optional] 
**is_secret** | **bool** | Defines whether or not the value is a secret.  This field will eventually replace the Type field of this class. | [optional] 
**description** | **str** | The description of the new configuration item | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


