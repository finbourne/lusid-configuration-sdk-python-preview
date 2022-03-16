# ConfigurationItemSummary

A single configuration object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key which identifies the configuration item | 
**value** | **str** | The value of the configuration item | 
**type** | **str** | Defines how the value is presented.  If it is secret, the value will be hidden.  If it is text, the value will be in plain-text. | [optional] [readonly] 
**value_type** | **str** | The type of the configuration item&#39;s value | 
**is_secret** | **bool** | Defines whether or not the value is a secret.  This field will eventually replace the Type field of this class. | 
**ref** | **str** | The reference to the configuration item | [readonly] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


