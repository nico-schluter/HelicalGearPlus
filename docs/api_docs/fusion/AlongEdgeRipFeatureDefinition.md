# AlongEdgeRipFeatureDefinition
Namespace: adsk.fusion
Inherits: RipFeatureDefinition
Since: September 2023

The definition for an along edge rip.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### gapDistance : ModelParameter [read-only]
Gets the ModelParameter that defines the gap distance of the rip. The value can be edited by using the properties of the returned ModelParameter object.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### ripEdge : BRepEdge [read-write]
Gets and sets the input edge for an along edge rip.
