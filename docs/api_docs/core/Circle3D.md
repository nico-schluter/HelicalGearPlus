# Circle3D
Namespace: adsk.core
Inherits: Curve3D
Since: August 2014

Transient 3D circle. A transient circle is not displayed or saved in a document. Transient 3D circles are used as a wrapper to work with raw 3D circle information. They are created statically using one of the create methods of the Circle3D class.

**Accessed from:** Circle3D.copy, Circle3D.createByCenter, Circle3D.createByThreePoints, SketchCircle.geometry, SketchCircle.worldGeometry

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Circle3D
Creates and returns an independent copy of this Circle3D object.
- **Returns** (Circle3D): Returns an independent copy of this Circle3D object.

### createByCenter(center: Point3D, normal: Vector3D, radius: double) -> Circle3D
Creates a transient 3D circle object by specifying a center and radius.
- **center** (Point3D): The center point of the circle.
- **normal** (Vector3D): The normal vector of the circle. The plane through the center point and perpendicular to the normal vector defines the plane of the circle.
- **radius** (double): The radius of the circle.
- **Returns** (Circle3D): Returns the new Circle3D object or null if the creation failed.

### createByThreePoints(pointOne: Point3D, pointTwo: Point3D, pointThree: Point3D) -> Circle3D
Creates a transient 3D circle through three points.
- **pointOne** (Point3D): The first point on the circle.
- **pointTwo** (Point3D): The second point on the circle. This point cannot be coincident with pointOne or pointThree. This point cannot lie on the line defined by pointOne and pointThree.
- **pointThree** (Point3D): The third point on the circle. This point cannot be coincident with pointOne or pointThree.
- **Returns** (Circle3D): Returns the new Circle3D object or null if the creation failed.

### getData(center: Point3D, normal: Vector3D, radius: double) -> boolean
Gets all of the data defining the circle.
- **center** (Point3D): The output center point of the circle.
- **normal** (Vector3D): The output normal vector.
- **radius** (double): The output radius of the circle.
- **Returns** (boolean): Returns true if successful

### set(center: Point3D, normal: Vector3D, radius: double) -> boolean
Sets all of the data defining the circle.
- **center** (Point3D): The center point of the circle.
- **normal** (Vector3D): The normal vector of the circle. The plane through the center point and perpendicular to the normal vector defines the plane of the circle.
- **radius** (double): The radius of the circle.
- **Returns** (boolean): Returns true if successful

### transformBy(matrix: Matrix3D) -> boolean
Transforms this curve in 3D space.
- **matrix** (Matrix3D): A 3D matrix that defines the transform to apply to the curve.
- **Returns** (boolean): Return true if the transform was successful.

## Properties

### asNurbsCurve : NurbsCurve3D [read-only]
Returns a NURBS curve that is geometrically identical to the circle.

### center : Point3D [read-write]
Gets and sets the center position of the circle.

### curveType : Curve3DTypes [read-only]
Returns the type of geometry this curve represents.

### evaluator : CurveEvaluator3D [read-only]
Returns an evaluator object that lets you perform additional evaluations on the curve.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### normal : Vector3D [read-write]
Gets and sets the normal of the circle.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### radius : double [read-write]
Gets and sets the radius of the circle.

## Samples
- **Get Circle and Arc Data from Edge API Sample**: Display the arc and circle geometric information from a selected circular edge.
