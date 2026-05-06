# CustomFeatures
Namespace: adsk.fusion
Inherits: Base
Since: January 2021

Collection that provides access to all of the existing custom features in a component and supports the ability to create new custom features.

**Accessed from:** Features.customFeatures

## Methods

### add(input: CustomFeatureInput) -> CustomFeature
Creates a new custom feature.
- **input** (CustomFeatureInput): The CustomFeatureInput object that defines the information needed to create a custom feature.
- **Returns** (CustomFeature): Returns the newly created CustomFeature.

> **Known issue — `RuntimeError: 3 : make params invalid`:** This error is thrown if the
> add-in's `.manifest` file does not have an `id` field set. The Fusion documentation
> states the `id` field is not needed and the default add-in template does not include it,
> but `CustomFeatures.add()` silently requires it. Add a UUID to the manifest and
> **restart Fusion** (reload add-in alone is not sufficient). Example:
> `"id": "8ddf023b-89bd-4313-84ea-1d94c4dba3bd"`

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(definition: CustomFeatureDefinition) -> CustomFeatureInput
Creates a new input object that you use to define a custom feature. Creating an input object doesn't create the feature but provides a way to gather all of the input needed to create a custom feature. To create the custom feature, the fully defined input object is passed to the add method.
- **definition** (CustomFeatureDefinition): The CustomFeatureDefinition for the type of custom feature being created.
- **Returns** (CustomFeatureInput): Returns the newly created CustomFeatureInput object or null in the case of invalid input.

### item(index: uinteger) -> CustomFeature
Function that returns the specified ruled surface feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (CustomFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> CustomFeature
Function that returns the specified CustomFeature feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (CustomFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of CustomFeature objects in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
