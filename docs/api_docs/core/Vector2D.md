# Vector2D
Namespace: adsk.core
Inherits: Base
Since: August 2014

Transient 2D vector. This object is a wrapper for 2D vector data and is used to pass vector data in and out of the API. They are created statically using the create method of the Vector2D class.

**Accessed from:** CurveEvaluator2D.getCurvature, CurveEvaluator2D.getFirstDerivative, CurveEvaluator2D.getSecondDerivative, CurveEvaluator2D.getTangent, CurveEvaluator2D.getThirdDerivative, Ellipse2D.getData, Ellipse2D.majorAxis, EllipticalArc2D.getData, EllipticalArc2D.majorAxis, Matrix2D.getAsCoordinateSystem, Point2D.asVector, Point2D.vectorTo, Vector2D.copy, Vector2D.create

## Methods

### add(vector: Vector2D) -> boolean
Add a vector to this vector.
- **vector** (Vector2D): The vector to add to this vector.
- **Returns** (boolean): Returns true if successful.

### angleTo(vector: Vector2D) -> double
Gets the angle between this vector and another vector.
- **vector** (Vector2D): The vector to measure the angle to.
- **Returns** (double): Returns the angle in radians.

### asArray() -> double[]
Returns the vector values as an array [x, y].
- **Returns** (double[]): Returns an array of the vector's values [x, y].

### asPoint() -> Point2D
Return a point with the same x and y values as this vector.
- **Returns** (Point2D): Returns the new point.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Vector2D
Creates and returns an independent copy of this Vector2D object.
- **Returns** (Vector2D): Returns a new Vector2D object that is a copy of this Vector2D object.

### create(x: double, y: double) -> Vector2D
Creates a 2D vector object.
- **x** (double): The x coordinate of the vector.

This is an optional argument whose default value is 0.0.
- **y** (double): The y coordinate of the vector.

This is an optional argument whose default value is 0.0.
- **Returns** (Vector2D): Returns the new Vector2D object or null if the creation failed.

### dotProduct(vector: Vector2D) -> double
Calculates the Dot Product of this vector and an input vector.
- **vector** (Vector2D): The vector to use in the dot product calculation.
- **Returns** (double): Returns the dot product of the two vectors.

### isEqualTo(vector: Vector2D) -> boolean
Compare this vector with another to check for equality.
- **vector** (Vector2D): The vector to compare with for equality.
- **Returns** (boolean): Returns true if the vectors are equal.

### isParallelTo(vector: Vector2D) -> boolean
Compare this vector with another to check for parallelism.
- **vector** (Vector2D): The vector to compare with for parallelism.
- **Returns** (boolean): Returns true if the vectors are parallel.

### isPerpendicularTo(vector: Vector2D) -> boolean
Compare this vector with another to check for perpendicularity.
- **vector** (Vector2D): The vector to compare with for perpendicularity.
- **Returns** (boolean): Returns true if the vectors are perpendicular.

### normalize() -> boolean
Normalizes the vector. Normalization makes the vector length equal to one. The vector should not be zero length.
- **Returns** (boolean): Returns true if successful.

### scaleBy(scale: double) -> boolean
Scales the vector by specifying a scaling factor.
- **scale** (double): The scale factor to multiple the vector by (i.e. 1.5).
- **Returns** (boolean): Returns true if successful.

### setWithArray(coordinates: double[]) -> boolean
Sets the definition of the vector by specifying an array containing the x and y coordinates.
- **coordinates** (double[]): An array that specifies the values for the x and y coordinates of the vector.
- **Returns** (boolean): Returns true if successful

### subtract(vector: Vector2D) -> boolean
Subtract a vector from this vector.
- **vector** (Vector2D): The vector to subtract from this vector.
- **Returns** (boolean): Returns true if successful.

### transformBy(matrix: Matrix2D) -> boolean
Transforms the vector by specifying a 2D transformation matrix.
- **matrix** (Matrix2D): The Matrix2D object that defines the transformation.
- **Returns** (boolean): Returns true if successful.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### length : double [read-only]
Gets the length of the vector.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### x : double [read-write]
Gets and sets the X coordinate of the vector.

### y : double [read-write]
Gets and sets the Y coordinate of the vector.
