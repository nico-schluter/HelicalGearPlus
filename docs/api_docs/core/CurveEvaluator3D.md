# CurveEvaluator3D
Namespace: adsk.core
Inherits: Base
Since: August 2014

3D curve evaluator that is obtained from a transient curve and allows you to perform various evaluations on the curve.

**Accessed from:** Arc3D.evaluator, BRepEdge.evaluator, Circle3D.evaluator, Curve3D.evaluator, Ellipse3D.evaluator, EllipticalArc3D.evaluator, InfiniteLine3D.evaluator, Line3D.evaluator, NurbsCurve3D.evaluator, Polyline3D.evaluator, SketchConicCurve.evaluator, SketchControlPointSpline.evaluator, SketchFixedSpline.evaluator

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getCurvature(parameter: double, direction: Vector3D, curvature: double) -> boolean
Get the curvature value at a parameter position on the curve.
- **parameter** (double): The parameter position to return the curvature information at. This value must be within the range of the parameter extents as provided by getParameterExtents.
- **direction** (Vector3D): The output direction of the curvature at the position on the curve.
- **curvature** (double): The output magnitude of the curvature at the position on the curve.
- **Returns** (boolean): Returns true if the curvature was successfully returned.

### getCurvatures(parameters: double[], directions: Vector3D[], curvatures: double[]) -> boolean
Get the curvature values at a number of parameter positions on the curve.
- **parameters** (double[]): The array of parameter positions to return curvature information at. Each parameter value must be within the range of the parameter extents as provided by getParameterExtents.
- **directions** (Vector3D[]): The output array of the direction of the curvature at each position on the curve. The length of this array will be the same as the length of the parameters array provided.
- **curvatures** (double[]): The output array of the magnitude of the curvature at the position on the curve. The length of this array will be the same as the length of the parameters array provided.
- **Returns** (boolean): Returns true if the curvatures were successfully returned.

### getEndPoints(startPoint: Point3D, endPoint: Point3D) -> boolean
Get the end points of the curve.
- **startPoint** (Point3D): The output start point of the curve. If the curve is unbounded at the start, this value will be null.
- **endPoint** (Point3D): The output end point of the curve. If the curve is unbounded at the end, this value will be null.
- **Returns** (boolean): Returns true if the end points were successfully returned.

### getFirstDerivative(parameter: double, firstDerivative: Vector3D) -> boolean
Get the first derivative of the curve at the specified parameter position.
- **parameter** (double): The parameter position to get the curve first derivative at. The parameter value must be within the range of the parameter extents as provided by getParameterExtents.
- **firstDerivative** (Vector3D): The output first derivative vector at the parameter position specified.
- **Returns** (boolean): Returns true if the first derivative was successfully returned.

### getFirstDerivatives(parameters: double[], firstDerivatives: Vector3D[]) -> boolean
Get the first derivatives of the curve at the specified parameter positions.
- **parameters** (double[]): The array of parameter positions to get the curve first derivative at. Each parameter value must be within the range of the parameter extents as provided by getParameterExtents.
- **firstDerivatives** (Vector3D[]): The output array of first derivative vectors at each parameter position specified. The length of this array is equal to the length of the parameters array specified.
- **Returns** (boolean): Returns true if the first derivatives were successfully returned.

### getLengthAtParameter(fromParameter: double, toParameter: double, length: double) -> boolean
Get the length of the curve between two parameter positions on the curve.
- **fromParameter** (double): The parameter position to measure the curve length from. This value must be within the range of the parameter extents as provided by getParameterExtents.
- **toParameter** (double): The parameter position to measure the curve length to. This value must be within the range of the parameter extents as provided by getParameterExtents.
- **length** (double): The output curve length between the from and to parameter positions on the curve.
- **Returns** (boolean): Returns true if the length was successfully returned.

### getParameterAtLength(fromParameter: double, length: double, parameter: double) -> boolean
Get the parameter position on the curve that is the specified curve length from the specified starting parameter position.
- **fromParameter** (double): The parameter position to start measuring the curve length from. This value must be within the range of the parameter extents as provided by getParameterExtents.
- **length** (double): The curve length to offset the from parameter by. A negative length value will offset in the negative parameter direction.
- **parameter** (double): The output parameter value that is the specified curve length from the starting parameter position.
- **Returns** (boolean): Returns true if the parameter was successfully returned.

### getParameterAtPoint(point: Point3D, parameter: double) -> boolean
Get the parameter position that correspond to a point on the curve. For reliable results, the point should lie on the curve within model tolerance. If the point does not lie on the curve, the parameter of the nearest point on the curve will generally be returned.
- **point** (Point3D): The point to get the curve parameter value at.
- **parameter** (double): The output parameter position corresponding to the point.
- **Returns** (boolean): Returns true of the parameter was successfully returned.

### getParameterExtents(startParameter: double, endParameter: double) -> boolean
Get the parametric range of the curve.
- **startParameter** (double): The output lower bound of the parameter range.
- **endParameter** (double): The output upper bound of the parameter range.
- **Returns** (boolean): Returns true if the curve is bounded and the parameter extents were successfully returned.

### getParametersAtPoints(points: Point3D[], parameters: double[]) -> boolean
Get the parameter positions that correspond to a set of points on the curve. For reliable results, the points should lie on the curve within model tolerance. If the points do not lie on the curve, the parameter of the nearest point on the curve will generally be returned.
- **points** (Point3D[]): An array of points to get the curve parameter values at.
- **parameters** (double[]): The output array of parameter positions corresponding to the set of points. The length of this array will be equal to the length of the points array specified.
- **Returns** (boolean): Returns true if the parameters were successfully returned.

### getPointAtParameter(parameter: double, point: Point3D) -> boolean
Get the point on the curve that corresponds to evaluating a parameter position on the curve.
- **parameter** (double): The parameter position to evaluate the curve position at. The parameter value must be within the range of the parameter extents as provided by getParameterExtents.
- **point** (Point3D): The output curve position corresponding to evaluating the curve at that parameter position.
- **Returns** (boolean): Returns true if the point was successfully returned.

### getPointsAtParameters(parameters: double[], points: Point3D[]) -> boolean
Get the points on the curve that correspond to evaluating a set of parameter positions on the curve.
- **parameters** (double[]): The array of parameter positions to evaluate the curve position at. Each parameter value must be within the range of the parameter extents as provided by getParameterExtents.
- **points** (Point3D[]): The output array of curve positions corresponding to evaluating the curve at that parameter position. The length of this array will be equal to the length of the parameters array specified.
- **Returns** (boolean): Returns true if the points were successfully returned.

### getSecondDerivative(parameter: double, secondDerivative: Vector3D) -> boolean
Get the second derivative of the curve at the specified parameter position.
- **parameter** (double): The parameter position to get the curve second derivative at. The parameter value must be within the range of the parameter extents as provided by getParameterExtents.
- **secondDerivative** (Vector3D): The output second derivative vector at the parameter position specified.
- **Returns** (boolean): Returns true if the second derivative was successfully returned.

### getSecondDerivatives(parameters: double[], secondDerivatives: Vector3D[]) -> boolean
Get the second derivatives of the curve at the specified parameter positions.
- **parameters** (double[]): The array of parameter positions to get the curve second derivative at. Each parameter value must be within the range of the parameter extents as provided by getParameterExtents.
- **secondDerivatives** (Vector3D[]): The output array of second derivative vectors at each parameter position specified. The length of this array is equal to the length of the parameters array specified.
- **Returns** (boolean): Returns true if the second derivatives were successfully returned.

### getStrokes(fromParameter: double, toParameter: double, tolerance: double, vertexCoordinates: Point3D[]) -> boolean
Get a sequence of points between two curve parameter positions. The points will be a linear interpolation along the curve between these two parameter positions where the maximum deviation between the curve and each line segment will not exceed the specified tolerance value.
- **fromParameter** (double): The starting parameter position to interpolate points from. The parameter value must be within the range of the parameter extents as provided by getParameterExtents.
- **toParameter** (double): The ending parameter position to interpolate points to. The parameter value must be within the range of the parameter extents as provided by getParameterExtents.
- **tolerance** (double): The maximum distance tolerance between the curve and the linear interpolation.
- **vertexCoordinates** (Point3D[]): The output array of linear interpolation points.
- **Returns** (boolean): Returns true if the interpolation points were successfully returned.

### getTangent(parameter: double, tangent: Vector3D) -> boolean
Get the tangent to the curve at a parameter position on the curve.
- **parameter** (double): The parameter position to return the tangent at. This value must be within the range of the parameter extents as provided by getParameterExtents.
- **tangent** (Vector3D): The output tangent vector at the curve position.
- **Returns** (boolean): Returns true if the tangent was successfully returned.

### getTangents(parameters: double[], tangents: Vector3D[]) -> boolean
Get the tangent to the curve at a number of parameter positions on the curve.
- **parameters** (double[]): The array of parameter positions to return the tangent at. Each parameter value must be within the range of the parameter extents as provided by getParameterExtents.
- **tangents** (Vector3D[]): The output array of tangent vectors for each position on the curve. The length of this array will be the same as the length of the parameters array provided.
- **Returns** (boolean): Returns true if the tangents were successfully returned.

### getThirdDerivative(parameter: double, thirdDerivative: Vector3D) -> boolean
Get the third derivative of the curve at the specified parameter position.
- **parameter** (double): The parameter position to get the curve third derivative at. The parameter value must be within the range of the parameter extents as provided by getParameterExtents.
- **thirdDerivative** (Vector3D): The output third derivative vector at the parameter position specified.
- **Returns** (boolean): Returns true if the third derivative was successfully returned.

### getThirdDerivatives(parameters: double[], thirdDerivatives: Vector3D[]) -> boolean
Get the third derivatives of the curve at the specified parameter positions.
- **parameters** (double[]): The array of parameter positions to get the curve third derivative at. Each parameter value must be within the range of the parameter extents as provided by getParameterExtents.
- **thirdDerivatives** (Vector3D[]): The output array of third derivative vectors at each parameter position specified. The length of this array is equal to the length of the parameters array specified.
- **Returns** (boolean): Returns true if the third derivatives were successfully returned.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **SketchArcs.split**: Demonstrates the SketchArc.split method.
