# Ellipse2D
Namespace: adsk.core
Inherits: Curve2D
Since: August 2014

Transient 2D ellipse. A transient ellipse is not displayed or saved in a document. Transient 2D ellipses are used as a wrapper to work with raw 2D ellipse information. They are created statically using the create method of the Ellipse2D class.

**Accessed from:** Ellipse2D.copy, Ellipse2D.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Ellipse2D
Creates and returns a copy of this Ellipse2D object.
- **Returns** (Ellipse2D): Returns a new Ellipse2D object that is a copy of this Ellipse2D object.

### create(center: Point2D, majorAxis: Vector2D, majorRadius: double, minorRadius: double) -> Ellipse2D
Creates a transient 2D ellipse by specifying a center position, major and minor axes, and major and minor radii.
- **center** (Point2D): A Point2D object that defines the center of the ellipse.
- **majorAxis** (Vector2D): The major axis of the ellipse
- **majorRadius** (double): The major radius of the of the ellipse.
- **minorRadius** (double): The minor radius of the of the ellipse.
- **Returns** (Ellipse2D): Returns the new Ellipse 2D object or null if the creation failed.

### getData(center: Point2D, majorAxis: Vector2D, majorRadius: double, minorRadius: double) -> boolean
Gets all of the data defining the ellipse.
- **center** (Point2D): The output center point of the ellipse.
- **majorAxis** (Vector2D): The output major axis of the ellipse.
- **majorRadius** (double): The output major radius of the of the ellipse.
- **minorRadius** (double): The output minor radius of the of the ellipse.
- **Returns** (boolean): Returns true if successful.

### set(center: Point2D, majorAxis: Vector2D, majorRadius: double, minorRadius: double) -> boolean
Sets all of the data defining the ellipse.
- **center** (Point2D): A Point2D object that defines the center of the ellipse.
- **majorAxis** (Vector2D): The major axis of the ellipse.
- **majorRadius** (double): The major radius of the of the ellipse.
- **minorRadius** (double): The minor radius of the of the ellipse.
- **Returns** (boolean): Returns true if redefining the ellipse is successful.

### transformBy(matrix: Matrix2D) -> boolean
Transforms this curve in 2D space.
- **matrix** (Matrix2D): A 2D matrix that defines the transform to apply to the curve.
- **Returns** (boolean): Return true if the transform was successful.

## Properties

### asNurbsCurve : NurbsCurve2D [read-only]
Returns a NURBS curve that is geometrically identical to the ellipse.

### center : Point2D [read-write]
Gets and sets the center position of the ellipse.

### curveType : Curve2DTypes [read-only]
Returns the type of geometry this curve represents.

### evaluator : CurveEvaluator2D [read-only]
Returns an evaluator object that lets you perform additional evaluations on the curve.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### majorAxis : Vector2D [read-write]
Gets and sets the major axis of the ellipse.

### majorRadius : double [read-write]
Gets and sets the major radius of the ellipse.

### minorRadius : double [read-write]
Gets and sets the minor radius of the ellipse.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
