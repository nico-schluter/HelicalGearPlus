# TrimFeatures
Namespace: adsk.fusion
Inherits: Base
Since: July 2015

Collection that provides access to all of the existing trim features in a component and supports the ability to create new trim features.

**Accessed from:** Features.trimFeatures

## Methods

### add(input: TrimFeatureInput) -> TrimFeature
Creates a new trim feature.
- **input** (TrimFeatureInput): A TrimFeatureInput object that defines the desired trim feature. Use the createInput method to create a new TrimFeatureInput object and then use methods on it (the TrimFeatureInput object) to define the trim feature.
- **Returns** (TrimFeature): Returns the newly created TrimFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(trimTool: Base) -> TrimFeatureInput
Creates a TrimFeatureInput object. Use properties and methods on this object to define the trim feature you want to create and then use the Add method, passing in the TrimFeatureInput object.

To determine the possible boundaries and allow you to choose which cells to keep, the trim feature does a partial compute when the input object is created. To do this it starts a trim feature transaction and completes the transaction when you call the add method. If you don't call the add method to finish the transaction it leaves Fusion in a bad state and there will be undo problems and possibly a crash. If you have created a TrimFeatureInput object and don't want to finish the feature creation, you need to call the cancel method on the TrimFeatureInput object to safely abort the current boundary fill transaction.
- **trimTool** (Base): A patch body, B-Rep face, construction plane or sketch curve that intersects the surface or surfaces to be trimmed
- **Returns** (TrimFeatureInput): Returns the newly created TrimFeatureInput object or null if the creation failed.

### item(index: uinteger) -> TrimFeature
Function that returns the specified trim feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (TrimFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> TrimFeature
Function that returns the specified trim feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (TrimFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of trim features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Trim Feature API Sample**: Demonstrates creating a new trim feature.
