# SurfaceEvaluator
Namespace: adsk.core
Inherits: Base
Since: August 2014

Surface evaluator that is obtained from a transient surface and allows you to perform various evaluations on the surface.

**Accessed from:** BRepFace.evaluator, Cone.evaluator, Cylinder.evaluator, EllipticalCone.evaluator, EllipticalCylinder.evaluator, NurbsSurface.evaluator, Plane.evaluator, Sphere.evaluator, Surface.evaluator, Torus.evaluator

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getCurvature(parameter: Point2D, maxTangent: Vector3D, maxCurvature: double, minCurvature: double) -> boolean
Get the curvature values at a parameter positions on the surface.
- **parameter** (Point2D): The parameter positions to return curvature information at.
- **maxTangent** (Vector3D): The output directions of maximum curvature at the position on the surface.
- **maxCurvature** (double): The output magnitude of the maximum curvature at the position on the surface.
- **minCurvature** (double): The output magnitude of the minimum curvature at the position on the surface. The minimum curvature direction is perpendicular to the maximum curvature tangent directions.
- **Returns** (boolean): Returns true if the curvature was successfully returned.

### getCurvatures(parameters: Point2D[], maxTangents: Vector3D[], maxCurvatures: double[], minCurvatures: double[]) -> boolean
Get the curvature values at a number of parameter positions on the surface.
- **parameters** (Point2D[]): The array of parameter positions to return curvature information at. Each parameter position must be with the range of the parameter extents as verified by isParameterOnFace.
- **maxTangents** (Vector3D[]): The output array of directions of maximum curvature at each position on the surface. The length of this array will be the same as the length of the parameters array provided.
- **maxCurvatures** (double[]): The output array of the magnitude of the maximum curvature at each position on the surface. The length of this array will be the same as the length of the parameters array provided.
- **minCurvatures** (double[]): The output array of the magnitude of the minimum curvature at each position on the surface. The minimum curvature direction is perpendicular to the maximum curvature tangent directions. The length of this array will be the same as the length of the parameters array provided.
- **Returns** (boolean): Returns true if the curvatures were successfully returned.

### getFirstDerivative(parameter: Point2D, partialU: Vector3D, partialV: Vector3D) -> boolean
Get the first derivative of the surface at the specified parameter position.
- **parameter** (Point2D): The parameter positions to get the surface first derivative at. The parameter position must be within the range of the parameter extents as verified by isParameterOnFace.
- **partialU** (Vector3D): The output first derivative U partial vector at the parameter position specified.
- **partialV** (Vector3D): The output first derivative V partial vector at the parameter position specified.
- **Returns** (boolean): Returns true if the first derivative was successfully returned.

### getFirstDerivatives(parameters: Point2D[], partialsU: Vector3D[], partialsV: Vector3D[]) -> boolean
Get the first derivatives of the surface at the specified parameter positions.
- **parameters** (Point2D[]): The array of parameter positions to get the surface first derivative at. Each parameter position must be within the range of the parameter extents as verified by isParameterOnFace.
- **partialsU** (Vector3D[]): The output array of first derivative U partial vectors at each parameter position specified. The length of this array is equal to the length of the parameters array specified.
- **partialsV** (Vector3D[]): The output array of first derivative V partial vectors at each parameter position specified. The length of this array is equal to the length of the parameters array specified.
- **Returns** (boolean): Returns true if the first derivatives were successfully returned.

### getIsoCurve(parameter: double, isUDirection: boolean) -> ObjectCollection
Gets (by extraction) a curve that follows a constant u or v parameter along the surface. The curve will have the same properties as the surface in the direction of the extraction. For example, when a curve is extracted from the periodic direction of a surface, the extracted curve will also be periodic. The type of curve returned is dependent on the shape the surface.

Getting an iso curve is limited to a SurfaceEvaluator that is obtained from a BRepFace. It will fail when the SurfaceEvaluator is obtained from a geometry object (Plane, Sphere, Torus, Cylinder, Cone, EllipticalCone, EllipticalCylinder, or NurbsSurface).
- **parameter** (double): The parameter at which to extract the curve
- **isUDirection** (boolean): A bool that indicates whether to extract the curve from the U or V direction
- **Returns** (ObjectCollection): Returns an ObjectCollection that contains one or more curves. Multiple curves are returned when the SurfaceEvaluator is obtained from a Face and the curve cuts across internal boundaries. The resulting curves are trimmed to the boundaries of the Face. When the SurfaceEvaluator is obtained from a geometry object, a single curve is returned because there are no boundaries to trim the curve. The type of curve(s) returned is dependent on the shape of the surface.

### getModelCurveFromParametricCurve(parametricCurve: Curve2D) -> ObjectCollection
Creates the 3D equivalent curve in model space, of a 2D curve defined in the parametric space of the surface.
- **parametricCurve** (Curve2D): The parameter space curve to map into this surface's parameter space.
- **Returns** (ObjectCollection): Returns an ObjectCollection containing one or more curves. When the SufaceEvaluatior is obtained from a face, and the curve cuts across internal boundaries of the face, multiple curves are returned. The returned curves are trimmed to the boundaries of the face. If the SurfaceEvaluator is obtained from a geometry object, a single curve returned because there are no boundaries with which to trim the curve. The type of curve(s) returned depends on the shape of the input curve and surface.

### getNormalAtParameter(parameter: Point2D, normal: Vector3D) -> boolean
Gets the surface normal at a parameter position on the surface.
- **parameter** (Point2D): The parameter position to return the normal at. The parameter position must be with the range of the parameter extents as verified by isParameterOnFace.
- **normal** (Vector3D): The output normal for the parameter position on the surface.
- **Returns** (boolean): Returns true if the normal was successfully returned.

### getNormalAtPoint(point: Point3D, normal: Vector3D) -> boolean
Gets the surface normal at a point on the surface.
- **point** (Point3D): The point to return the normal at. For reliable results the point should lie on the surface.
- **normal** (Vector3D): The output normal for the point on the surface.
- **Returns** (boolean): Returns true if the normal was successfully returned.

### getNormalsAtParameters(parameters: Point2D[], normals: Vector3D[]) -> boolean
Gets the surface normal at a number of parameter positions on the surface.
- **parameters** (Point2D[]): The array of parameter positions to return the normal at. Each parameter position must be with the range of the parameter extents as verified by isParameterOnFace.
- **normals** (Vector3D[]): The output array of normals for each parameter position on the surface. The length of this array will be the same as the length of the parameters array provided.
- **Returns** (boolean): Returns true if the normals were successfully returned.

### getNormalsAtPoints(points: Point3D[], normals: Vector3D[]) -> boolean
Gets the surface normal at a number of positions on the surface.
- **points** (Point3D[]): The array of points to return the normal at. For reliable results each point should lie on the surface.
- **normals** (Vector3D[]): The output array of normals for each point on the surface. The length of this array will be the same as the length of the points array provided.
- **Returns** (boolean): Returns true if the normals were successfully returned.

### getParamAnomaly(periodicityU: double[], periodicityV: double[], singularitiesU: double[], singularitiesV: double[], unboundedParameters: boolean[]) -> boolean
Gets details about anomalies in parameter space of the surface. This includes information about periodic intervals, singularities, or unbounded parameter ranges.
- **periodicityU** (double[]): The output array with information about the period of the surface in U. periodicityU[0] will contain the period of the surface in U. If periodicityU[0] is 0, the surface is not periodic in U. If the surface is periodic in U, peridocityU[1] will contain the parameter value at the start of the principle period.
- **periodicityV** (double[]): The output array with information about the period of the surface in V. periodicityV[0] will contain the period of the surface in V. If periodicityV[0] is 0, the surface is not periodic in V. If the surface is periodic in V, peridocityV[1] will contain the parameter value at the start of the principle period.
- **singularitiesU** (double[]): The output array parameter values of singularities in U. If this array is empty, there are no singularities in U.
- **singularitiesV** (double[]): The output array parameter values of singularities in V. If this array is empty, there are no singularities in V.
- **unboundedParameters** (boolean[]): The output array that indicates if the parameter range is unbounded in U or V. unboundedParameters[0] will be true if U is unbounded. unboundedParameters[1] will be true if V is unbounded.
- **Returns** (boolean): Returns true if the parameter anomalies were successfully returned.

### getParameterAtPoint(point: Point3D, parameter: Point2D) -> boolean
Get the parameter position that correspond to a point on the surface. For reliable results, the point should lie on the surface within model tolerance. If the point does not lie on the surface, the parameter of the nearest point on the surface will generally be returned.
- **point** (Point3D): The point to get the curve parameter value at.
- **parameter** (Point2D): The output parameter position corresponding to the point.
- **Returns** (boolean): Returns true of the parameter was successfully returned.

### getParametersAtPoints(points: Point3D[], parameters: Point2D[]) -> boolean
Get the parameter positions that correspond to a set of points on the surface. For reliable results, the points should lie on the surface within model tolerance. If the points do not lie on the surface, the parameter of the nearest point on the surface will generally be returned.
- **points** (Point3D[]): An array of points to get the surface parameter values at.
- **parameters** (Point2D[]): The output array of parameter positions corresponding to the set of points. The length of this array will be equal to the length of the points array specified.
- **Returns** (boolean): Returns true if the parameters were successfully returned.

### getPointAtParameter(parameter: Point2D, point: Point3D) -> boolean
Get the point on the surface that correspond to evaluating a parameter position on the surface.
- **parameter** (Point2D): The parameter positions to evaluate the surface position at. The parameter position must be within the range of the parameter extents as verified by isParameterOnFace.
- **point** (Point3D): The output point corresponding to evaluating the curve at that parameter position.
- **Returns** (boolean): Returns true if the point was successfully returned.

### getPointsAtParameters(parameters: Point2D[], points: Point3D[]) -> boolean
Get the points on the surface that correspond to evaluating a set of parameter positions on the surface.
- **parameters** (Point2D[]): The array of parameter positions to evaluate the surface position at. Each parameter position must be within the range of the parameter extents as verified by isParameterOnFace.
- **points** (Point3D[]): The output array of points corresponding to evaluating the curve at that parameter position. The length of this array will be equal to the length of the parameters array specified.
- **Returns** (boolean): Returns true if the points were successfully returned.

### getSecondDerivative(parameter: Point2D, partialUU: Vector3D, partialUV: Vector3D, partialVV: Vector3D) -> boolean
Get the second derivative of the surface at the specified parameter position.
- **parameter** (Point2D): The parameter position to get the surface second derivative at. The parameter position must be within the range of the parameter extents as verified by isParameterOnFace.
- **partialUU** (Vector3D): The output second derivative UU partial vector at each parameter position specified.
- **partialUV** (Vector3D): The output second derivative UV mixed partial vector at each parameter position specified.
- **partialVV** (Vector3D): The output second derivative VV partial vector at each parameter position specified.
- **Returns** (boolean): Returns true if the second derivative was successfully returned.

### getSecondDerivatives(parameters: Point2D[], partialsUU: Vector3D[], partialsUV: Vector3D[], partialsVV: Vector3D[]) -> boolean
Get the second derivatives of the surface at the specified parameter positions.
- **parameters** (Point2D[]): The array of parameter positions to get the surface second derivative at. Each parameter position must be within the range of the parameter extents as verified by isParameterOnFace.
- **partialsUU** (Vector3D[]): The output array of second derivative UU partial vectors at each parameter position specified. The length of this array is equal to the length of the parameters array specified.
- **partialsUV** (Vector3D[]): The output array of second derivative UV mixed partial vectors at each parameter position specified. The length of this array is equal to the length of the parameters array specified.
- **partialsVV** (Vector3D[]): The output array of second derivative VV partial vectors at each parameter position specified. The length of this array is equal to the length of the parameters array specified.
- **Returns** (boolean): Returns true if the second derivatives were successfully returned.

### getThirdDerivative(parameter: Point2D, partialUUU: Vector3D, partialVVV: Vector3D) -> boolean
Get the third derivative of the surface at the specified parameter position.
- **parameter** (Point2D): The parameter position to get the surface third derivative at. The parameter position must be within the range of the parameter extents as verified by isParameterOnFace.
- **partialUUU** (Vector3D): The output third derivative UUU partial vector at each parameter position specified.
- **partialVVV** (Vector3D): The output third derivative VVV partial vector at each parameter position specified.
- **Returns** (boolean): Returns true if the third derivative was successfully returned.

### getThirdDerivatives(parameters: Point2D[], partialsUUU: Vector3D[], partialsVVV: Vector3D[]) -> boolean
Get the third derivatives of the surface at the specified parameter positions.
- **parameters** (Point2D[]): The array of parameter positions to get the surface third derivative at. Each parameter position must be within the range of the parameter extents as verified by isParameterOnFace.
- **partialsUUU** (Vector3D[]): The output array of third derivative UUU partial vectors at each parameter position specified. The length of this array is equal to the length of the parameters array specified.
- **partialsVVV** (Vector3D[]): The output array of third derivative VVV partial vectors at each parameter position specified. The length of this array is equal to the length of the parameters array specified.
- **Returns** (boolean): Returns true if the third derivatives were successfully returned.

### isParameterOnFace(parameter: Point2D) -> boolean
Determines if the specified parameter position lies within the surface. When the SurfaceEvaluator is obtained from a BRepFace object, this will respect the boundaries of the face and return true when point is on the visible portion of the surface. When obtained from surface geometry it returns true if the point is within the parametric range of surface.
- **parameter** (Point2D): The parameter position to test.
- **Returns** (boolean): Returns true if the parameter position lies within the surface.

### parametricRange() -> BoundingBox2D
Returns the parametric range of the surface. If the surface is periodic in a direction, the range is set to the principle period's range. If the surface is only upper bounded in a direction, the lower bound is set to -double-max. If the surface is only lower bounded in a direction, the upper bound is set to double-max. If the surface is unbounded in a direction, the lower bound and upper bound of the range will both be zero.
- **Returns** (BoundingBox2D): Returns the bounding box with the parameter extents, with the X value being the U range, and the Y value being the V range.

## Properties

### area : double [read-only]
Returns the area of the surface. This is typically used when the SurfaceEvaluator is associated with a BRepFace object where it is always valid. This can fail in the case where the SurfaceEvaluator is associated with one of the geometry classes, (Plane, Cylinder, Cone, EllipticalCone, or EllipticalCylinder object), because these surfaces are unbounded. A BRepFace, even one of these shapes, is bounded by its edges and has a well-defined area.

### isClosedInU : boolean [read-only]
Returns if the surface is closed (forms a loop) in the U direction

### isClosedInV : boolean [read-only]
Returns if the surface is closed (forms a loop) in the V direction

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
