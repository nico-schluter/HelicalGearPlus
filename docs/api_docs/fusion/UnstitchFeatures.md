# UnstitchFeatures
Namespace: adsk.fusion
Inherits: Base
Since: July 2015

Collection that provides access to all of the existing Unstitch features in a component and supports the ability to create new Unstitch features.

**Accessed from:** Features.unstitchFeatures

## Methods

### add(faces: ObjectCollection, isChainSelection: boolean) -> UnstitchFeature
Creates a new Unstitch feature.
- **faces** (ObjectCollection): The faces and/or bodies to Unstitch. Individual faces can be unstitched from solid and/or patch bodies. The faces being unstitched need not all come from the same body.
- **isChainSelection** (boolean): A boolean value for setting whether or not faces that are connected and adjacent to the input faces will be included in the selection. The default value is true.

This is an optional argument whose default value is True.
- **Returns** (UnstitchFeature): Returns the newly created UnstitchFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> UnstitchFeature
Function that returns the specified Unstitch feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (UnstitchFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> UnstitchFeature
Function that returns the specified unstitch feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (UnstitchFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of Unstitch features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Unstitch Feature API Sample**: Demonstrates creating a new unstitch feature
