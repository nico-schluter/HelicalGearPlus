# ConstructionPointEdgePlaneDefinition
Namespace: adsk.fusion
Inherits: ConstructionPointDefinition
Since: August 2014

The definition for a parametric construction point created using the SetbyEdgePlane method

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### redefine(edge: Base, plane: Base) -> boolean
Redefines the input geometry of the construction point.
- **edge** (Base): A linear B-Rep edge, construction axis or sketch line.
- **plane** (Base): A plane, planar B-Rep face or construction plane.
- **Returns** (boolean): Returns true if the redefinition of the Construction Point is successful.

## Properties

### edge : Base [read-only]
A linear B-Rep edge, construction axis or sketch line.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentConstructionPoint : ConstructionPoint [read-only]
Returns the ConstructionPoint object

### plane : Base [read-only]
A plane, planar B-Rep face or construction plane.
