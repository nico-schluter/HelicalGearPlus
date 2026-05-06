# Point2D
Namespace: adsk.core
Inherits: Base
Since: August 2014

Transient 2D point. A transient point is not displayed or saved in a document. Transient 2D points are used as a wrapper to work with raw 2D point information. They are created statically using the create methods of the Point2D class.

**Accessed from:** Arc2D.center, Arc2D.endPoint, Arc2D.getData, Arc2D.startPoint, BoundingBox2D.maxPoint, BoundingBox2D.minPoint, Circle2D.center, Circle2D.getData, CurveEvaluator2D.getEndPoints, CurveEvaluator2D.getPointAtParameter, CustomGraphicsViewPlacement.viewPoint, DXF2DImportOptions.position, Ellipse2D.center, Ellipse2D.getData, EllipticalArc2D.center, EllipticalArc2D.endPoint, EllipticalArc2D.getData, EllipticalArc2D.startPoint, Line2D.endPoint, Line2D.getData, Line2D.startPoint, Matrix2D.getAsCoordinateSystem, MouseEventArgs.position, MouseEventArgs.viewportPosition, NurbsCurve2D.controlPoints, Point2D.copy, Point2D.create, Polyline2D.points, SurfaceEvaluator.getParameterAtPoint, TriangleMesh.textureCoordinates, Vector2D.asPoint, Viewport.modelToViewSpace, Viewport.screenToView, Viewport.viewToScreen

## Methods

### asArray() -> double[]
Get coordinate data of the point
- **Returns** (double[]): Returns the coordinate data of the point as an array

### asVector() -> Vector2D
Defines a vector using the coordinates of the point.
- **Returns** (Vector2D): Returns a Vector2D object

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Point2D
Creates and returns a copy of this point object.
- **Returns** (Point2D): Returns an independent copy of this point object.

### create(x: double, y: double) -> Point2D
Creates a transient 2D point object.
- **x** (double): The x coordinate of the point

This is an optional argument whose default value is 0.0.
- **y** (double): The y coordinate of the point

This is an optional argument whose default value is 0.0.
- **Returns** (Point2D): Returns the new Point2D object or null if the creation failed.

### distanceTo(point: Point2D) -> double
Returns the distance from this point to another point.
- **point** (Point2D): The point to measure the distance to
- **Returns** (double): Returns the distance to the point.

### getData(x: double, y: double) -> boolean
Gets the data defining the point.
- **x** (double): The output x coordinate of the point.
- **y** (double): The output y coordinate of the point.
- **Returns** (boolean): Returns true if successful.

### isEqualTo(point: Point2D) -> boolean
Checks to see if this point and another point are equal (have identical coordinates). The comparison is done within the modeling tolerance which can be found with the Application.pointTolerance property. If you want to compare two points with any other tolerance you can use the isEqualToByTolerance method.
- **point** (Point2D): The point to compare for equality
- **Returns** (boolean): Returns true if the points are equal. (have identical coordinates)

### isEqualToByTolerance(point: Point2D, tolerance: double) -> boolean
Checks to see if this point and another point are equal within the specified tolerance.
- **point** (Point2D): The point to compare for equality.
- **tolerance** (double): The tolerance, in centimeters, to use when comparing the two points.
- **Returns** (boolean): Returns true if the points are equal (have identical coordinates).

### set(x: double, y: double) -> boolean
Sets the coordinates of the point by specifying the x, y coordinates.
- **x** (double): The x coordinate of the point.
- **y** (double): The y coordinate of the point.
- **Returns** (boolean): Returns true if successful

### setWithArray(coordinates: double[]) -> boolean
Sets the coordinates of the point using an array as input.
- **coordinates** (double[]): An array that defines the coordinates of the point
- **Returns** (boolean): Returns true if successful

### transformBy(matrix: Matrix2D) -> boolean
Transforms the point using the provided matrix.
- **matrix** (Matrix2D): The Matrix2D object that defines the transformation
- **Returns** (boolean): Returns true if successful

### translateBy(vector: Vector2D) -> boolean
Translates the point using the provided vector.
- **vector** (Vector2D): The vector to use to translate the point
- **Returns** (boolean): Returns true if successful

### vectorTo(point: Point2D) -> Vector2D
Returns a vector from this point to another point.
- **point** (Point2D): The other point to use to create the vector
- **Returns** (Vector2D): Returns a Vector2D object

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
