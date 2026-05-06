# ConstructionPlaneOffsetDefinition
Namespace: adsk.fusion
Inherits: ConstructionPlaneDefinition
Since: August 2014

ConstructionPlaneOffsetDefinition defines a construction plane that is offset by a specified distance from a planar face or construction plane by a specified distance. A positive or negative value can control the direction of the offset.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### redefine(offset: ValueInput, planarEntity: Base) -> boolean
Redefines the input geometry of the construction plane.
- **offset** (ValueInput): ValueInput object that specifies the offset distance
- **planarEntity** (Base): A plane, planar face or construction plane from which to measure the offset from
- **Returns** (boolean): Returns true is the operation is successful

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### offset : Parameter [read-only]
Returns a Parameter object that controls the value of the offset. You can use properties of the returned Parameter object to modify the offset.

### parentConstructionPlane : ConstructionPlane [read-only]
Returns the ConstructionPlane object

### planarEntity : Base [read-only]
Gets the planar face or construction plane this construction plane is parametrically dependent on.
