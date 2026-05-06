# NurbsCurve2D
Namespace: adsk.core
Inherits: Curve2D
Since: August 2014

Transient 2D NURBS curve. A transient NURBS curve is not displayed or saved in a document. Transient 2D NURBS curves are used as a wrapper to work with raw 2D NURBS curve information. They are created statically using one of the create methods of the NurbsCurve2D class.

**Accessed from:** Arc2D.asNurbsCurve, Circle2D.asNurbsCurve, Ellipse2D.asNurbsCurve, EllipticalArc2D.asNurbsCurve, Line2D.asNurbsCurve, NurbsCurve2D.copy, NurbsCurve2D.createNonRational, NurbsCurve2D.createRational, NurbsCurve2D.extract, NurbsCurve2D.merge, Polyline2D.asNurbsCurve

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> NurbsCurve2D
Creates and returns an independent copy of this NurbsCurve2D object.
- **Returns** (NurbsCurve2D): Returns an independent copy of this NurbsCurve2D.

### createNonRational(controlPoints: Point2D[], degree: integer, knots: double[], isPeriodic: boolean) -> NurbsCurve2D
Creates a transient 2D NURBS non-rational b-spline object.
- **controlPoints** (Point2D[]): An array of control point that define the path of the spline
- **degree** (integer): The degree of curvature of the spline
- **knots** (double[]): An array of numbers that define the knot vector of the spline. The knots is an array of (>=degree + N + 1) numbers, where N is the number of control points.
- **isPeriodic** (boolean): A bool specifying if the spline is to be Periodic. A periodic spline has a start point and end point that meet forming a closed loop.
- **Returns** (NurbsCurve2D): Returns the new NurbsCurve2D object or null if the creation failed.

### createRational(controlPoints: Point2D[], degree: integer, knots: double[], weights: double[], isPeriodic: boolean) -> NurbsCurve2D
Creates a transient 2D NURBS rational b-spline object.
- **controlPoints** (Point2D[]): An array of control point that define the path of the spline
- **degree** (integer): The degree of curvature of the spline
- **knots** (double[]): An array of numbers that define the knot vector of the spline. The knots is an array of (>=degree + N + 1) numbers, where N is the number of control points.
- **weights** (double[]): An array of numbers that define the weights for the spline.
- **isPeriodic** (boolean): A bool specifying if the spline is to be Periodic. A periodic curve has a start point and end point that meet (with curvature continuity) forming a closed loop.
- **Returns** (NurbsCurve2D): Returns the new NurbsCurve2D object or null if the creation failed.

### extract(startParam: double, endParam: double) -> NurbsCurve2D
Defines a new NURBS curve that is the subset of this NURBS curve in the parameter range of [startParam, endParam]
- **startParam** (double): The parameter position of the start of the subset.
- **endParam** (double): The parameter position of the end of the subset.
- **Returns** (NurbsCurve2D): Returns a new NurbsCurve2D object.

### getData(controlPoints: Point2D[], degree: integer, knots: double[], isRational: boolean, weights: double[], isPeriodic: boolean) -> boolean
Gets the data that defines a transient 2D NURBS rational b-spline object.
- **controlPoints** (Point2D[]): The output array of control point that define the path of the spline.
- **degree** (integer): The output degree of curvature of the spline.
- **knots** (double[]): The output array of numbers that define the knots of the spline.
- **isRational** (boolean): The output value indicating if the spline is rational. A rational spline will have a weight value for each control point.
- **weights** (double[]): The output array of numbers that define the weights for the spline.
- **isPeriodic** (boolean): The output value indicating if the spline is Periodic. A periodic curve has a start point and end point that meet (with curvature continuity) forming a closed loop.
- **Returns** (boolean): Returns true if successful.

### merge(nurbsCurve: NurbsCurve2D) -> NurbsCurve2D
Define a new NURBS curve that is the result of combining this NURBS curve with another NURBS curve. The curves are merged with the end point of the current curve merging with the start point of the other curve. The curves are forced to join even if they are not physically touching so you will typically want to make sure the end and start points of the curves are where you expect them to be.
- **nurbsCurve** (NurbsCurve2D): The NURBS curve to combine with
- **Returns** (NurbsCurve2D): Returns a new NurbsCurve2D object.

### reverse()
Reverses the orientation of the curve so the start and end points are swapped. The shape of the curve remains unchanged. This is especially useful to prepare the curves to use with the merge method.

### set(controlPoints: Point2D[], degree: integer, knots: double[], isRational: boolean, weights: double[], isPeriodic: boolean) -> boolean
Sets the data that defines a transient 2D NURBS rational b-spline object.
- **controlPoints** (Point2D[]): The array of control point that define the path of the spline
- **degree** (integer): The degree of curvature of the spline
- **knots** (double[]): An array of numbers that define the knots of the spline.
- **isRational** (boolean): A bool indicating if the spline is rational. A rational spline must have a weight value for each control point.
- **weights** (double[]): An array of numbers that define the weights for the spline.
- **isPeriodic** (boolean): A bool specifying if the spline is to be Periodic. A periodic curve has a start point and end point that meet (with curvature continuity) forming a closed loop.
- **Returns** (boolean): Returns true if successful

### transformBy(matrix: Matrix2D) -> boolean
Transforms this curve in 2D space.
- **matrix** (Matrix2D): A 2D matrix that defines the transform to apply to the curve.
- **Returns** (boolean): Return true if the transform was successful.

## Properties

### controlPointCount : integer [read-only]
Gets the number of control points that define the curve

### controlPoints : array [read-only]
Returns an array of Point2D objects that define the control points of the curve.

### curveType : Curve2DTypes [read-only]
Returns the type of geometry this curve represents.

### degree : integer [read-only]
Returns the degree of the curve

### evaluator : CurveEvaluator2D [read-only]
Returns an evaluator object that lets you perform additional evaluations on the curve.

### isClosed : boolean [read-only]
Returns if the curve is closed

### isPeriodic : boolean [read-only]
Returns if the curve is periodic.

### isRational : boolean [read-only]
Returns if the curve is rational or non-rational type

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### knotCount : integer [read-only]
Returns the knot count of the curve

### knots : array [read-only]
Returns an array of numbers that define the Knots of the curve.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
