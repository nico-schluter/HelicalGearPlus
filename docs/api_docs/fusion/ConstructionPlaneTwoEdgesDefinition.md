# ConstructionPlaneTwoEdgesDefinition
Namespace: adsk.fusion
Inherits: ConstructionPlaneDefinition
Since: August 2014

ConstructionPlaneTwoEdgesDefinition defines a ConstructionPlane by two co-planar linear entities like edges, sketch lines or construction axis.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### redefine(linearEntityOne: Base, linearEntityTwo: Base) -> boolean
Redefines the input geometry of the construction plane.
- **linearEntityOne** (Base): The first linear edge, construction line, or sketch line that defines the construction plane.
- **linearEntityTwo** (Base): The second linear edge, construction line, or sketch line that defines the construction plane.
- **Returns** (boolean): Returns true if successful.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### linearEntityOne : Base [read-only]
Gets the first linear edge, construction line, or sketch line that defines the construction plane.

### linearEntityTwo : Base [read-only]
Gets the second linear edge, construction line, or sketch line that defines the construction plane.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentConstructionPlane : ConstructionPlane [read-only]
Returns the ConstructionPlane object
