# Point3D
Namespace: adsk.core
Inherits: Base
Since: August 2014

Transient 3D point. A transient point is not displayed or saved in a document. Transient 3D points are used as a wrapper to work with raw 3D point information. They are created statically using the create method of the Point3D class.

**Accessed from:** AdditiveFFFLimitsMachineElement.homePosition, AdditiveFFFLimitsMachineElement.parkPosition, AdditivePlatformMachineElement.origin, AdditivePlatformMachineElement.size, AngleValueCommandInput.manipulatorOrigin, Arc3D.center, Arc3D.endPoint, Arc3D.getData, Arc3D.startPoint, AreaProperties.centroid, BeamNetwork.vertices, BoundingBox3D.maxPoint, BoundingBox3D.minPoint, BRepEdge.pointOnEdge, BRepFace.centroid, BRepFace.pointOnFace, BRepVertex.geometry, BRepVertexDefinition.position, Camera.eye, Camera.target, Circle3D.center, Circle3D.getData, Cone.getData, Cone.origin, ConstructionPoint.geometry, CurveEvaluator3D.getEndPoints, CurveEvaluator3D.getPointAtParameter, CustomGraphicsBillBoard.anchorPoint, CustomGraphicsCoordinates.getCoordinate, CustomGraphicsViewPlacement.anchorPoint, CustomGraphicsViewScale.anchorPoint, Cylinder.getData, Cylinder.origin, DirectionCommandInput.manipulatorOrigin, DistanceValueCommandInput.manipulatorOrigin, Ellipse3D.center, Ellipse3D.getData, EllipticalArc3D.center, EllipticalArc3D.getData, EllipticalCone.getData, EllipticalCone.origin, EllipticalCylinder.getData, EllipticalCylinder.origin, FaceGroup.centroid, HoleFeature.position, InfiniteLine3D.getData, InfiniteLine3D.origin, JointGeometry.origin, Line3D.endPoint, Line3D.getData, Line3D.startPoint, Matrix3D.getAsCoordinateSystem, MeasureResults.positionOne, MeasureResults.positionThree, MeasureResults.positionTwo, NurbsCurve3D.controlPoints, NurbsSurface.controlPoints, OffsetConstraintInput.dimensionPoint, OrientedBoundingBox3D.centerPoint, PhysicalProperties.centerOfMass, Plane.intersectWithLine, Plane.origin, Point3D.copy, Point3D.create, PolygonMesh.nodeCoordinates, Polyline3D.points, RecognizedHole.bottom, RecognizedHole.top, SceneSettings.centerOfFocus, SceneSettings.groundPosition, Selection.point, Sketch.modelToSketchSpace, Sketch.origin, Sketch.sketchToModelSpace, SketchAngularDimension.textPosition, SketchConcentricCircleDimension.textPosition, SketchDiameterDimension.textPosition, SketchDimension.textPosition, SketchDistanceBetweenLineAndPlanarSurfaceDimension.textPosition, SketchDistanceBetweenPointAndSurfaceDimension.textPosition, SketchEllipseMajorRadiusDimension.textPosition, SketchEllipseMinorRadiusDimension.textPosition, SketchLinearDiameterDimension.textPosition, SketchLinearDimension.textPosition, SketchOffsetCurvesDimension.textPosition, SketchOffsetDimension.textPosition, SketchPoint.geometry, SketchPoint.worldGeometry, SketchRadialDimension.textPosition, SketchTangentDistanceDimension.textPosition, SketchText.position, SketchTextInput.position, Sphere.getData, Sphere.origin, SurfaceEvaluator.getPointAtParameter, Torus.getData, Torus.origin, TriangleMesh.nodeCoordinates, Vector3D.asPoint, Viewport.viewToModelSpace, VolumetricColorSample.point, VolumetricSample.point, VolumetricScalarSample.point, VolumetricVectorSample.point

## Methods

### asArray() -> double[]
Get coordinate data of the point.
- **Returns** (double[]): Returns the coordinate data of the point as an array [x, y, z].

### asVector() -> Vector3D
Defines a vector using the coordinates of the point.
- **Returns** (Vector3D): Returns a Vector2D object.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Point3D
Creates and returns a copy of this point object.
- **Returns** (Point3D): Returns an independent copy of this point object.

### create(x: double, y: double, z: double) -> Point3D
Creates a transient 3D point object.
- **x** (double): The x coordinate of the point

This is an optional argument whose default value is 0.0.
- **y** (double): The y coordinate of the point

This is an optional argument whose default value is 0.0.
- **z** (double): The z coordinate of the point

This is an optional argument whose default value is 0.0.
- **Returns** (Point3D): Returns the new Point3D object or null if the creation failed.

### distanceTo(point: Point3D) -> double
Returns the distance from this point to another point.
- **point** (Point3D): The point to measure the distance to.
- **Returns** (double): Returns the distance to the point.

### getData(x: double, y: double, z: double) -> boolean
Gets the data defining the point.
- **x** (double): The output x coordinate of the point.
- **y** (double): The output y coordinate of the point.
- **z** (double): The output z coordinate of the point.
- **Returns** (boolean): Returns true if successful.

### isEqualTo(point: Point3D) -> boolean
Checks to see if this point and another point are equal (have identical coordinates). The comparison is done within the modeling tolerance which can be found with the Application.pointTolerance property. If you want to compare two points with any other tolerance you can use the isEqualToByTolerance method.
- **point** (Point3D): The point to compare for equality.
- **Returns** (boolean): Returns true if the points are equal (have identical coordinates).

### isEqualToByTolerance(point: Point3D, tolerance: double) -> boolean
Checks to see if this point and another point are equal within the specified tolerance.
- **point** (Point3D): The point to compare for equality.
- **tolerance** (double): The tolerance, in centimeters, to use when comparing the two points.
- **Returns** (boolean): Returns true if the points are equal (have identical coordinates).

### set(x: double, y: double, z: double) -> boolean
Sets the data defining the point.
- **x** (double): The x coordinate of the point.
- **y** (double): The y coordinate of the point.
- **z** (double): The z coordinate of the point.
- **Returns** (boolean): Returns true if successful.

### setWithArray(coordinates: double[]) -> boolean
Sets the coordinates of the point using an array as input.
- **coordinates** (double[]): An array that defines the coordinates of the point [x, y, z].
- **Returns** (boolean): Returns true if successful.

### transformBy(matrix: Matrix3D) -> boolean
Transforms the point using the provided matrix.
- **matrix** (Matrix3D): The Matrix3D object that defines the transformation.
- **Returns** (boolean): Returns true if successful.

### translateBy(vector: Vector3D) -> boolean
Translates the point using the provided vector.
- **vector** (Vector3D): The vector to use to translate the point.
- **Returns** (boolean): Returns true if successful.

### vectorTo(point: Point3D) -> Vector3D
Returns a vector from this point to another point.
- **point** (Point3D): The other point to use to create the vector.
- **Returns** (Vector3D): Returns a Vector3D object.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### x : double [read-write]
Gets and sets the X coordinate of the point.

### y : double [read-write]
Gets and sets the Y coordinate of the point.

### z : double [read-write]
Gets and sets the Z coordinate of the point.

## Samples
- **SketchArcs.addByCenterStartSweep**: Demonstrates the SketchArcs.addByCenterStartSweep method.
- **SketchArcs.addByThreePoints**: Demonstrates the SketchArcs.addByThreePoints method.
- **SketchArcs.addFillet**: Demonstrates the SketchArcs.addFillet method.
