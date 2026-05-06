# Polyline3D
Namespace: adsk.core
Inherits: Curve3D
Since: September 2024

Represents a single piecewise linear curve. This is a single curve that consists of a series of connected lines in 3D space.

**Accessed from:** Polyline3D.create, Polyline3D.createByArray

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(points: Point3D[]) -> Polyline3D
Creates a transient 3D polyline using an array of Point3D objects that defines the position of the polyline vertices.
- **points** (Point3D[]): An array of Point3D objects that define the coordinates of the curve.
- **Returns** (Polyline3D): Returns the created Polyline3D object or null if the creation failed.

### createByArray(pointCoordinates: double[]) -> Polyline3D
Creates a transient 3D polyline using an array of floating point values that specify the X, Y, Z coordinates for each point.
- **pointCoordinates** (double[]): An array of floating point values that define the X, Y, Z coordinates of each point in the polyline.
- **Returns** (Polyline3D): Returns the created Polyline3D object or null if the creation failed

### transformBy(matrix: Matrix3D) -> boolean
Transforms this curve in 3D space.
- **matrix** (Matrix3D): A 3D matrix that defines the transform to apply to the curve.
- **Returns** (boolean): Return true if the transform was successful.

## Properties

### asNurbsCurve : NurbsCurve3D [read-only]
Returns a NURBS curve that is geometrically identical to the polyline.

### curveType : Curve3DTypes [read-only]
Returns the type of geometry this curve represents.

### evaluator : CurveEvaluator3D [read-only]
Returns an evaluator object that lets you perform additional evaluations on the curve.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### pointCount : integer [read-only]
Returns the number of points defining the polyline.

### points : array [read-write]
Gets and sets the points that define the coordinates of the polyline.
