# ReverseNormalFeatures
Namespace: adsk.fusion
Inherits: Base
Since: September 2015

Collection that provides access to all of the existing Reverse Normal features in a component and supports the ability to create new Reverse Normal features.

**Accessed from:** Features.reverseNormalFeatures

## Methods

### add(surfaces: ObjectCollection) -> ReverseNormalFeature
Creates a new Reverse Normal feature.
- **surfaces** (ObjectCollection): One or more surface bodies (open BRepBodies) containing the faces whose normals are to be reversed. All faces of the input surface bodies get reversed.
- **Returns** (ReverseNormalFeature): Returns the newly created ReverseNormalFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ReverseNormalFeature
Function that returns the specified Reverse Normal feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ReverseNormalFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> ReverseNormalFeature
Function that returns the specified reverse normal feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (ReverseNormalFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of Reverse Normal features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Reverse Normal Feature**: Demonstrates creating a new reverse normal feature.
