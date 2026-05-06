# Circle2D
Namespace: adsk.core
Inherits: Curve2D
Since: August 2014

Transient 2D circle. A transient circle is not displayed or saved in a document. Transient circles are used as a wrapper to work with raw 2D arc information. They are created statically using one of the create methods of the Circle2D class.

**Accessed from:** Circle2D.copy, Circle2D.createByCenter, Circle2D.createByThreePoints

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Circle2D
Creates and returns an independent copy of this Circle2D object.
- **Returns** (Circle2D): Returns an independent copy of this Circle2D object.

### createByCenter(center: Point2D, radius: double) -> Circle2D
Creates a transient 2D circle object by specifying a center and radius.
- **center** (Point2D): A Point2D object that defines the center of the circle.
- **radius** (double): The radius of the circle.
- **Returns** (Circle2D): Returns the new Circle2D object or null if the creation failed.

### createByThreePoints(pointOne: Point2D, pointTwo: Point2D, pointThree: Point2D) -> Circle2D
Creates a transient 2D circle through three points.
- **pointOne** (Point2D): The first point on the circle.
- **pointTwo** (Point2D): The second point on the circle.
- **pointThree** (Point2D): The third point on the circle.
- **Returns** (Circle2D): Returns the new Circle2D object or null if the creation failed.

### getData(center: Point2D, radius: double) -> boolean
Gets all of the data defining the circle.
- **center** (Point2D): The output point defining the center position of the circle.
- **radius** (double): The output radius of the circle.
- **Returns** (boolean): Returns true if successful.

### set(center: Point2D, radius: double) -> boolean
Sets all of the data defining the circle.
- **center** (Point2D): A point that defines the center position of the circle.
- **radius** (double): The radius of the circle.
- **Returns** (boolean): Returns true if redefining the circle is successful

### transformBy(matrix: Matrix2D) -> boolean
Transforms this curve in 2D space.
- **matrix** (Matrix2D): A 2D matrix that defines the transform to apply to the curve.
- **Returns** (boolean): Return true if the transform was successful.

## Properties

### asNurbsCurve : NurbsCurve2D [read-only]
Returns a NURBS curve that is geometrically identical to the circle.

### center : Point2D [read-write]
Gets and sets the center position of the circle.

### curveType : Curve2DTypes [read-only]
Returns the type of geometry this curve represents.

### evaluator : CurveEvaluator2D [read-only]
Returns an evaluator object that lets you perform additional evaluations on the curve.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### radius : double [read-write]
Gets and sets the radius of the circle.
