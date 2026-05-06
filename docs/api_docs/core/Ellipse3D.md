# Ellipse3D
Namespace: adsk.core
Inherits: Curve3D
Since: August 2014

Transient 3D ellipse. A transient ellipse is n0t displayed or saved in a document. Transient 3D ellipses are used as a wrapper to work with raw 3D ellipse information. They are created statically using the create method of the Ellipse3D class.

**Accessed from:** Ellipse3D.copy, Ellipse3D.create, SketchEllipse.geometry, SketchEllipse.worldGeometry

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Ellipse3D
Creates a copy of this Ellipse3D object.
- **Returns** (Ellipse3D): Returns the independent copy of the ellipse.

### create(center: Point3D, normal: Vector3D, majorAxis: Vector3D, majorRadius: double, minorRadius: double) -> Ellipse3D
Creates a transient 3D ellipse object.
- **center** (Point3D): The center point of the ellipse.
- **normal** (Vector3D): The normal vector of the ellipse. The plane through the center point and perpendicular to the normal vector defines the plane of the ellipse.
- **majorAxis** (Vector3D): The major axis of the ellipse
- **majorRadius** (double): The major radius of the of the ellipse.
- **minorRadius** (double): The minor radius of the of the ellipse.
- **Returns** (Ellipse3D): Returns the new Ellipse 3D object or null if the creation failed.

### getData(center: Point3D, normal: Vector3D, majorAxis: Vector3D, majorRadius: double, minorRadius: double) -> boolean
Gets all of the data defining the ellipse.
- **center** (Point3D): The output center point of the ellipse.
- **normal** (Vector3D): The output normal vector of the ellipse.
- **majorAxis** (Vector3D): The output major axis of the ellipse
- **majorRadius** (double): The output major radius of the of the ellipse.
- **minorRadius** (double): The output minor radius of the of the ellipse.
- **Returns** (boolean): Returns true if successful.

### set(center: Point3D, normal: Vector3D, majorAxis: Vector3D, majorRadius: double, minorRadius: double) -> boolean
Sets all of the data defining the ellipse.
- **center** (Point3D): The center point of the ellipse.
- **normal** (Vector3D): The normal vector of the ellipse. The plane through the center point and perpendicular to the normal vector defines the plane of the ellipse.
- **majorAxis** (Vector3D): The major axis of the ellipse.
- **majorRadius** (double): The major radius of the of the ellipse.
- **minorRadius** (double): The minor radius of the of the ellipse.
- **Returns** (boolean): Returns true if successful.

### transformBy(matrix: Matrix3D) -> boolean
Transforms this curve in 3D space.
- **matrix** (Matrix3D): A 3D matrix that defines the transform to apply to the curve.
- **Returns** (boolean): Return true if the transform was successful.

## Properties

### asNurbsCurve : NurbsCurve3D [read-only]
Returns a NURBS curve that is geometrically identical to the ellipse.

### center : Point3D [read-write]
Gets and sets the center position of the ellipse.

### curveType : Curve3DTypes [read-only]
Returns the type of geometry this curve represents.

### evaluator : CurveEvaluator3D [read-only]
Returns an evaluator object that lets you perform additional evaluations on the curve.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### majorAxis : Vector3D [read-write]
Gets and sets the major axis of the ellipse.

### majorRadius : double [read-write]
Gets and sets the major radius of the ellipse.

### minorRadius : double [read-write]
Gets and sets the minor radius of the ellipse.

### normal : Vector3D [read-only]
Gets the normal of the ellipse.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
