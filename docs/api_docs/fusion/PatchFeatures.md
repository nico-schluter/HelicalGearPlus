# PatchFeatures
Namespace: adsk.fusion
Inherits: Base
Since: September 2015

Collection that provides access to all of the existing Patch features in a component and supports the ability to create new Patch features.

**Accessed from:** Features.patchFeatures

## Methods

### add(input: PatchFeatureInput) -> PatchFeature
Creates a new patch feature.
- **input** (PatchFeatureInput): A PatchFeatureInput object that defines the desired patch feature. Use the createInput method to create a new PatchFeatureInput object and then use methods on it (the PatchFeatureInput object) to define the patch feature.
- **Returns** (PatchFeature): Returns the newly created PatchFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(boundaryCurve: Base, operation: FeatureOperations) -> PatchFeatureInput
Creates a PatchFeatureInput object. Use properties and methods on the returned PatchFeatureInput object to set other settings. The PatchFeatureInput object is used as input to the add method to create the patch feature.
- **boundaryCurve** (Base): Defines the input geometry that will be used to define the boundary. This can be a sketch profile, a single sketch curve, a single B-Rep edge, an ObjectCollection, or a Path object.

If a single sketch curve or B-Rep edge is an input that is not closed; Fusion will automatically find connected sketch curves or B-Rep edges to define a closed loop.

If an ObjectCollection is an input, it must be a set of curves that define a closed shape.

If a Path is an input, it must define a closed shape.
- **operation** (FeatureOperations): The feature operation to perform. Only 'NewBodyFeatureOperation' and 'NewComponentFeatureOperation' are valid operations for patch features.
- **Returns** (PatchFeatureInput): Returns the newly created PatchFeatureInput object or null if the creation fails.

### item(index: uinteger) -> PatchFeature
Function that returns the specified patch feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (PatchFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> PatchFeature
Function that returns the specified patch feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (PatchFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of Patch features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
