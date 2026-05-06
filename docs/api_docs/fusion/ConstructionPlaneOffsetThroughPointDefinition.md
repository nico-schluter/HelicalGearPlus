# ConstructionPlaneOffsetThroughPointDefinition
Namespace: adsk.fusion
Inherits: ConstructionPlaneDefinition
Since: January 2025

Defines a construction plane that is offset from a planar face or construction plane and whose offset distance is defined by a vertex, sketch point, or construction point where the plane passes through the point.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### redefine(planarEntity: Base, point: Base) -> boolean
Redefines the input geometry of the construction plane.
- **planarEntity** (Base): A planar BRepFace or ConstructionPlane that the new construction plane will be offset from.
- **point** (Base): A BRepVertex, SketchPoint, or ConstructionPoint that defines the offset distance.
- **Returns** (boolean): Returns true is the operation is successful

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentConstructionPlane : ConstructionPlane [read-only]
Returns the ConstructionPlane object

### planarEntity : Base [read-only]
Returns the planar face or construction plane this construction plane is parametrically dependent on.

### point : Base [read-only]
Returns the point that controls the offset.
