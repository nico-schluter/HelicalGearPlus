# AssemblyConstraintInput
Namespace: adsk.fusion
Inherits: Base
Since: July 2025

Defines all of the information required to create a new assembly constraint. This object provides equivalent functionality to the Assembly Relationships command dialog in that it gathers the required information to create an assembly constraint.

**Accessed from:** AssemblyConstraints.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### geometricRelationships : GeometricRelationships [read-only]
Returns the collection object used to define the geometric relationships that the constraints will be inferred from. A geometric relationship defines a pair of entities, if the relationships is flipped, and the offset or angle value.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
