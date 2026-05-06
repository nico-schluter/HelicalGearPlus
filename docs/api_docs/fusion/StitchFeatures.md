# StitchFeatures
Namespace: adsk.fusion
Inherits: Base
Since: June 2015

Collection that provides access to all of the existing Stitch features in a component and supports the ability to create new Stitch features.

**Accessed from:** Features.stitchFeatures

## Methods

### add(input: StitchFeatureInput) -> StitchFeature
Creates a new stitch feature.
- **input** (StitchFeatureInput): A StitchFeatureInput object that defines the desired stitch feature. Use the createInput method to create a new StitchFeatureInput object and then use methods on it (the StitchFeatureInput object) to define the stitch feature.
- **Returns** (StitchFeature): Returns the newly created StitchFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(stitchSurfaces: ObjectCollection, tolerance: ValueInput, operation: FeatureOperations) -> StitchFeatureInput
Creates a StitchFeatureInput object. Use properties and methods on this object to define the stitch feature you want to create and then use the Add method, passing in the StitchFeatureInput object.
- **stitchSurfaces** (ObjectCollection): The surfaces (open BRepBodies) to stitch together. Stitching surfaces can form multiple closed volumes resulting in multiple solids. Stitch Surfaces can form multiple BRepShells (entirely connected set of entities) that would result in a single non-solid BRepBody.
- **tolerance** (ValueInput): ValueInput object that defines the stitching tolerance. It must define a distance value.
- **operation** (FeatureOperations): Specifies the operation type for the result when the final result is a closed solid. Otherwise this argument is ignored.

This is an optional argument whose default value is FeatureOperations.NewBodyFeatureOperation.
- **Returns** (StitchFeatureInput): Returns the newly created StitchFeatureInput object or null if the creation failed.

### item(index: uinteger) -> StitchFeature
Function that returns the specified stitch feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (StitchFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> StitchFeature
Function that returns the specified stitch feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (StitchFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of Stitch features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Stitch Feature API Sample**: Demonstrates creating a new stitch feature.
