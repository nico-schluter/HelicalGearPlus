# Arc3D
Namespace: adsk.core
Inherits: Curve3D
Since: August 2014

Transient 3D arc. A transient arc is not displayed or saved in a document. Transient 3D arcs are used as a wrapper to work with raw 3D arc information. They are created statically using one of the create methods of the Arc3D class.

**Accessed from:** Arc3D.copy, Arc3D.createByCenter, Arc3D.createByThreePoints, SketchArc.geometry, SketchArc.worldGeometry

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Arc3D
Creates and returns an independent copy of this Arc3D object.
- **Returns** (Arc3D): Returns a new Arc3D object that is a copy of this Arc3D object.

### createByCenter(center: Point3D, normal: Vector3D, referenceVector: Vector3D, radius: double, startAngle: double, endAngle: double) -> Arc3D
Creates a transient 3D arc object by specifying a center point and radius.
- **center** (Point3D): The center point of the arc.
- **normal** (Vector3D): The normal vector of the arc. The plane perpendicular to this normal at the center point is the plane of the arc.
- **referenceVector** (Vector3D): A reference vector from which the start and end angles are measured from. This vector must be perpendicular to the normal vector.
- **radius** (double): The radius of the arc.
- **startAngle** (double): The start angle in radians. This angle is measured from the reference vector using the right hand rule around the normal vector.
- **endAngle** (double): The end angle in radians. This angle is measured from the reference vector using the right hand rule around the normal vector.
- **Returns** (Arc3D): Returns the newly created arc or null if the creation failed.

### createByThreePoints(pointOne: Point3D, pointTwo: Point3D, pointThree: Point3D) -> Arc3D
Creates a transient 3D arc by specifying 3 points. A transient arc is not displayed or saved in a document. Transient arcs are used as a wrapper to work with raw 3D arc information.
- **pointOne** (Point3D): The start point of the arc.
- **pointTwo** (Point3D): A point along the arc. This point must not be coincident with the first or third points. This point must not lie on the line between the first and third points.
- **pointThree** (Point3D): The end point of the arc. This point must not be coincident with the first or second points.
- **Returns** (Arc3D): Returns the newly created arc or null if the creation failed.

### getData(center: Point3D, normal: Vector3D, referenceVector: Vector3D, radius: double, startAngle: double, endAngle: double) -> boolean
Gets all of the data defining the arc.
- **center** (Point3D): The output center point of the arc.
- **normal** (Vector3D): The output normal vector.
- **referenceVector** (Vector3D): The output reference vector.
- **radius** (double): The output radius of the arc.
- **startAngle** (double): The output start angle in radians. This angle is measured from the reference vector using the right hand rule around the normal vector.
- **endAngle** (double): The output end angle in radians. This angle is measured from the reference vector using the right hand rule around the normal vector.
- **Returns** (boolean): Returns true if successful

### set(center: Point3D, normal: Vector3D, referenceVector: Vector3D, radius: double, startAngle: double, endAngle: double) -> boolean
Sets all of the data defining the arc.
- **center** (Point3D): The center point of the arc.
- **normal** (Vector3D): The normal vector of the arc. The plane perpendicular to this normal at the center point is the plane of the arc.
- **referenceVector** (Vector3D): A reference vector from which the start and end angles are measured from. This vector must be perpendicular to the normal vector.
- **radius** (double): The radius of the arc.
- **startAngle** (double): The start angle in radians. This angle is measured from the reference vector using the right hand rule around the normal vector.
- **endAngle** (double): The end angle in radians. This angle is measured from the reference vector using the right hand rule around the normal vector.
- **Returns** (boolean): Returns true if successful

### setAxes(normal: Vector3D, referenceVector: Vector3D) -> boolean
Sets the normal and reference vectors of the arc.
- **normal** (Vector3D): The new normal vector.
- **referenceVector** (Vector3D): The new reference vector from which the start and end angles are measured from. The reference vector must be perpendicular to the normal vector.
- **Returns** (boolean): Returns true if successful

### transformBy(matrix: Matrix3D) -> boolean
Transforms this curve in 3D space.
- **matrix** (Matrix3D): A 3D matrix that defines the transform to apply to the curve.
- **Returns** (boolean): Return true if the transform was successful.

## Properties

### asNurbsCurve : NurbsCurve3D [read-only]
Returns a NURBS curve that is geometrically identical to the arc.

### center : Point3D [read-write]
Gets and sets the center position of the arc.

### curveType : Curve3DTypes [read-only]
Returns the type of geometry this curve represents.

### endAngle : double [read-write]
Gets and sets the end angle of the arc in radians. This angle is measured from the reference vector using the right hand rule around the normal vector.

### endPoint : Point3D [read-only]
Gets the end point of the arc.

### evaluator : CurveEvaluator3D [read-only]
Returns an evaluator object that lets you perform additional evaluations on the curve.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### normal : Vector3D [read-only]
Gets the normal of the arc.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### radius : double [read-write]
Gets and sets the radius of the arc.

### referenceVector : Vector3D [read-only]
Gets the reference vector of the arc.

### startAngle : double [read-write]
Gets and sets the start angle of the arc in radians. This angle is measured from the reference vector using the right hand rule around the normal vector.

### startPoint : Point3D [read-only]
Gets the start point of the arc.

## Samples
- **Get Circle and Arc Data from Edge API Sample**: Display the arc and circle geometric information from a selected circular edge.
