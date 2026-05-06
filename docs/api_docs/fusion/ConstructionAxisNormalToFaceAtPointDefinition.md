# ConstructionAxisNormalToFaceAtPointDefinition
Namespace: adsk.fusion
Inherits: ConstructionAxisDefinition
Since: August 2014

The definition for a parametric construction axis created using the SetByNormalToFaceAtPoint method

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### redefine(face: Base, pointEntity: Base) -> boolean
Redefines the input geometry of the construction axis.
- **face** (Base): The face the axis is normal to
- **pointEntity** (Base): The point that positions the axis
- **Returns** (boolean): Returns true if the redefinition of the construction axis is successful.

## Properties

### face : Base [read-only]
Gets the face the axis is normal to

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentConstructionAxis : ConstructionAxis [read-only]
Returns the ConstructionAxis object

### pointEntity : Base [read-only]
Gets the point that positions the axis
