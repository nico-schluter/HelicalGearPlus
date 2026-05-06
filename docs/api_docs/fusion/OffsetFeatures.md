# OffsetFeatures
Namespace: adsk.fusion
Inherits: Base
Since: June 2015

Collection that provides access to all of the existing Offset features in a component and supports the ability to create new Offset features.

**Accessed from:** Features.offsetFeatures

## Methods

### add(input: OffsetFeatureInput) -> OffsetFeature
Creates a new offset feature.
- **input** (OffsetFeatureInput): A FeatureInput object that defines the desired offset feature. Use the createInput method to create a new OffsetFeatureInput object and then use methods on it (the OffsetFeatureInput object) to define the offset feature.
- **Returns** (OffsetFeature): Returns the newly created OffsetFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(entities: ObjectCollection, distance: ValueInput, operation: FeatureOperations, isChainSelection: boolean) -> OffsetFeatureInput
Creates an OffsetFeatureInput object. Use properties and methods on this object to define the offset feature you want to create and then use the Add method, passing in the OffsetFeatureInput object to create the feature.
- **entities** (ObjectCollection): An ObjectCollection containing the BRepFace objects to offset. Additional faces may be automatically used depending on the value of the isChainSelection argument. Input faces need not be from the same body.
- **distance** (ValueInput): ValueInput object that defines the offset distance. A positive value is in the positive normal direction of the face being offset.
- **operation** (FeatureOperations): The feature operation to perform. 'NewBodyFeatureOperation' and 'NewComponentFeatureOperation' are the options supported.
- **isChainSelection** (boolean): A boolean value for setting whether or not faces that are tangentially connected to the input faces (if any) will be included in the offset. The default value is true.

This is an optional argument whose default value is True.
- **Returns** (OffsetFeatureInput): Returns the newly created OffsetFeatureInput object or null if the creation failed.

### item(index: uinteger) -> OffsetFeature
Function that returns the specified offset feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (OffsetFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> OffsetFeature
Function that returns the specified offset feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (OffsetFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of Offset features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Offset Feature API Sample**: Demonstrates creating a new offset feature
