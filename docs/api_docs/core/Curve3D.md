# Curve3D
Namespace: adsk.core
Inherits: Base
Since: August 2014

The base class for all 3D transient geometry classes.

**Accessed from:** BRepEdge.geometry, BRepEdgeDefinition.modelSpaceCurve, BRepWireEdgeDefinition.modelSpaceCurve, Curve3DPath.item, CustomGraphicsCurve.curve, PathEntity.curve, ProfileCurve.geometry, SketchText.asCurves

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### transformBy(matrix: Matrix3D) -> boolean
Transforms this curve in 3D space.
- **matrix** (Matrix3D): A 3D matrix that defines the transform to apply to the curve.
- **Returns** (boolean): Return true if the transform was successful.

## Properties

### curveType : Curve3DTypes [read-only]
Returns the type of geometry this curve represents.

### evaluator : CurveEvaluator3D [read-only]
Returns an evaluator object that lets you perform additional evaluations on the curve.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
