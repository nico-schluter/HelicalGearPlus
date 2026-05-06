# CombineFeatures
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

Collection that provides access to all of the existing Combine features in a component and supports the ability to create new Combine features.

**Accessed from:** Features.combineFeatures

## Methods

### add(input: CombineFeatureInput) -> CombineFeature
Creates a new combine feature.
- **input** (CombineFeatureInput): A CombineFeatureInput object that defines the desired combine. Use the createInput method to create a new CombineFeatureInput object and then use methods on it (the CombineFeatureInput object) to define the combine.
- **Returns** (CombineFeature): Returns the newly created CombineFeature object or null if the creation failed. This function returns nothing in the case where the feature is non-parametric.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(targetBody: BRepBody, toolBodies: ObjectCollection) -> CombineFeatureInput
Creates a CombineFeatureInput object. Use properties and methods on this object to define the combine you want to create and then use the Add method, passing in the CombineFeatureInput object.
- **targetBody** (BRepBody): A BRep body that represents the blank body.
- **toolBodies** (ObjectCollection): An ObjectCollection containing one or more BRep bodies that represent tool bodies.
- **Returns** (CombineFeatureInput): Returns the newly created CombineFeatureInput object or null if the creation failed.

### item(index: uinteger) -> CombineFeature
Function that returns the specified combine feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (CombineFeature): Returns the specified item or null if an invalid index was specified. This property returns nothing in the case where the feature is non-parametric.

### itemByName(name: string) -> CombineFeature
Function that returns the specified combine feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (CombineFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of combine features in the collection. This property returns nothing in the case where the feature is non-parametric.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
