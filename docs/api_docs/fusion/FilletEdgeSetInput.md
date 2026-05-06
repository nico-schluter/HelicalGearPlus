# FilletEdgeSetInput
Namespace: adsk.fusion
Inherits: Base
Since: November 2022

Represents the input to define a fillet edge set.

**Accessed from:** FilletEdgeSetInputs.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### continuity : SurfaceContinuityTypes [read-write]
Gets and sets the continuity of the fillet edge set. Valid values are TangentSurfaceContinuityType and CurvatureSurfaceContinuityType. The default is TangentSurfaceContinuityType.

For an asymmetric fillet edge set, this must always be tangent continuity (G1) and setting it to another value will fail.

### entities : ObjectCollection [read-write]
Gets and sets the entities associated with this fillet edge set. For constant radius and chord length edge sets, this can be edges, faces, and features. For variable radius edges sets, this must be edges.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### tangencyWeight : ValueInput [read-write]
Gets and sets the tangency weight for the given edge set. The tangency weight controls the influence of the continuity (G1 or G2) on the fillet. The ValueInput must be a real value between 0.1 and 2.0 inclusive, with no units. The default value is 1.0.
