# ConstructionPlaneMidplaneDefinition
Namespace: adsk.fusion
Inherits: ConstructionPlaneDefinition
Since: August 2014

ConstructionPlaneMidplaneDefinition defines a ConstructionPlane by...

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### redefine(planarEntityOne: Base, planarEntityTwo: Base) -> boolean
Redefines the input geometry of the construction plane.
- **planarEntityOne** (Base): The first planar face or construction plane that defines this ConstructionPlane.
- **planarEntityTwo** (Base): The second planar face or construction plane that defines this ConstructionPlane.
- **Returns** (boolean): Returns true if the redefinition of the plane is successful.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentConstructionPlane : ConstructionPlane [read-only]
Returns the ConstructionPlane object

### planarEntityOne : Base [read-only]
Gets the first planar face or construction plane that defines this ConstructionPlane.

### planarEntityTwo : Base [read-only]
Gets the second planar face or construction plane that defines this ConstructionPlane.
