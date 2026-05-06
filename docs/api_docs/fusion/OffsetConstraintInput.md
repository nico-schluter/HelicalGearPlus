# OffsetConstraintInput
Namespace: adsk.fusion
Inherits: Base
Since: September 2024

Used to define the inputs needed to create an offset constraint.

**Accessed from:** GeometricConstraints.createOffsetInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### curves : array [read-write]
Gets and sets an array of SketchCurve objects that defines the connected curves that will be offset. The Sketch.FindConnectedCurves method is a convenient way to get this set of curves.

### dimensionPoint : Point3D [read-write]
A location on one of the curves where the offset dimension will be created. A value of null can be used to indicate that a default location should be used.

When the OffsetContraintInput is created this property defaults to null.

### isTopologyMatched : boolean [read-write]
Specifies if the offset curves must match the topology of the original curves. For example, if you have a sketch containing two lines with a fillet (arc) connecting them and offset them inward more than the arc radius, the resulting offset will be two lines. This is a change in topology because the original curves were line-arc-line, and the offset is line-line. An offset of less than the radius still results in a line-arc-line result. If this property is true, indicating the topology must match, creating the offset with a value greater than the arc radius will fail because the result will not have a matching topology.

When the OffsetConstraintInput is created, this property default to true.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### offset : ValueInput [read-write]
Gets and sets the value that defines the offset. This is a ValueInput object so it can be a float value to define the offset in centimeters or it can be a string defining an expression that will be used by the parameter controlling the offset. A positive offset value creates the offset curve to the "right" and a negative offset value goes to the "left".

The flow direction of the provided curves implies the offset direction. For example, if two connected lines are offset, the flow direction is from line 1 to line 2. Left and right are evaluated relative to the input geometry. If you are standing on line 1 and looking towards line 2, the offset's left side is on your left, and the right side is to your right. Closed single curves like circles and ellipses always have a counterclockwise flow, so a positive offset is always to the outside. For closed splines, the positive direction is based on the spline's parameterization.
