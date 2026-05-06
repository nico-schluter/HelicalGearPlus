# Profiles
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

A collection of all of the closed profiles currently calculated for this sketch. Closed profiles are automatically computed by Fusion and represent closed areas within the sketch.

This class also provides some additional utility functions to create open profiles and text based profiles that can be used as input for various features.

**Accessed from:** Sketch.profiles

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Profile
Function that returns the specified closed profile using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Profile): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of closed profiles in the sketch. Open and text based profiles are not included.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Loft Feature API Sample**: Demonstrates creating a new loft feature.
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
- **Simple Extrusion Sample**: Creates a new extrusion feature, resulting in a new component.
- **Simple Revolve Feature Sample**: Creates a new revolve feature, resulting in a new component.
