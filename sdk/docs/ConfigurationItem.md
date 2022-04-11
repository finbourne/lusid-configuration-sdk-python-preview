# ConfigurationItem

The full version of the configuration item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The date referring to the creation date of the configuration item | 
**created_by** | **str** | Who created the configuration item | 
**last_modified_at** | **datetime** | The date referring to the date when the configuration item was last modified | 
**last_modified_by** | **str** | Who modified the configuration item most recently | 
**description** | **str** | Describes the configuration item | [optional] 
**key** | **str** | The key which identifies the configuration item | 
**value** | **str** | The value of the configuration item | 
**value_type** | **str** | The type of the configuration item&#39;s value | 
**is_secret** | **bool** | Defines whether or not the value is a secret. | 
**ref** | **str** | The reference to the configuration item | [readonly] 
**links** | [**list[Link]**](Link.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


