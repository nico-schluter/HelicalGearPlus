# InferredJointInput
Namespace: adsk.fusion
Inherits: Base
Since: July 2025

Defines all of the information required to create a new inferred joint. This object provides equivalent functionality to the Joint command dialog, gathering the required information to create an inferred joint.

**Accessed from:** Joints.createInferredJointInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### geometricRelationships : GeometricRelationships [read-only]
Returns the collection object used to define the geometric relationships from which the joint will be inferred. A geometric relationship defines several things: the pair of entities, if the relationship is flipped, if it defines a mating alignment or an angle, and the value of the offset or angle.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
