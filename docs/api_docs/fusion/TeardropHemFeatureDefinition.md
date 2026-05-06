# TeardropHemFeatureDefinition
Namespace: adsk.fusion
Inherits: HemFeatureDefinition
Since: September 2025

The definition for a teardrop hem.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### bendPositionType : BendPositionTypes [read-write]
Gets the bend position type for a hem.

### gap : ModelParameter [read-only]
Gets the gap for a teardrop hem.

### hemEdge : BRepEdge [read-write]
Gets and sets the input edge for a hem

### isFlipped : boolean [read-write]
Gets the flip direction for an open hem.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### length : ModelParameter [read-only]
Gets the length for a teardrop hem.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### radius : ModelParameter [read-only]
Gets the radius for a teardrop hem.
