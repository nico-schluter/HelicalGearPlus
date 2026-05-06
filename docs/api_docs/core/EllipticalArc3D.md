# EllipticalArc3D
Namespace: adsk.core
Inherits: Curve3D
Since: August 2014

Transient 3D elliptical arc. A transient elliptical arc is not displayed or saved in a document. Transient 3D elliptical arcs are used as a wrapper to work with raw 3D elliptical arc information. They are created statically using the create method of the EllipticalArc3D class.

**Accessed from:** EllipticalArc3D.copy, EllipticalArc3D.create, SketchEllipticalArc.geometry, SketchEllipticalArc.worldGeometry

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> EllipticalArc3D
Creates and returns a copy of this EllipticalArc3D object.
- **Returns** (EllipticalArc3D): Returns a new EllipticalArc3D object that is a copy of this Arc3D object.

### create(center: Point3D, normal: Vector3D, majorAxis: Vector3D, majorRadius: double, minorRadius: double, startAngle: double, endAngle: double) -> EllipticalArc3D
Creates a transient 3D elliptical arc.
- **center** (Point3D): The center point of the elliptical arc.
- **normal** (Vector3D): The normal vector of the elliptical arc.
- **majorAxis** (Vector3D): The major axis of the elliptical arc.
- **majorRadius** (double): The major radius of the of the elliptical arc.
- **minorRadius** (double): The minor radius of the of the elliptical arc.
- **startAngle** (double): The start angle of the elliptical arc in radians, where 0 is along the major axis.
- **endAngle** (double): The end angle of the elliptical arc in radians, where 0 is along the major axis.
- **Returns** (EllipticalArc3D): Returns the newly created elliptical arc or null if the creation failed.

### getData(center: Point3D, normal: Vector3D, majorAxis: Vector3D, majorRadius: double, minorRadius: double, startAngle: double, endAngle: double) -> boolean
Gets all of the data defining the elliptical arc.
- **center** (Point3D): The output center point of the elliptical arc.
- **normal** (Vector3D): The output normal vector of the elliptical arc.
- **majorAxis** (Vector3D): The output major axis of the elliptical arc.
- **majorRadius** (double): The output major radius of the of the elliptical arc.
- **minorRadius** (double): The output minor radius of the of the elliptical arc.
- **startAngle** (double): The output start angle of the elliptical arc in radians, where 0 is along the major axis.
- **endAngle** (double): The output end angle of the elliptical arc in radians, where 0 is along the major axis.
- **Returns** (boolean): Returns true if successful.

### set(center: Point3D, normal: Vector3D, majorAxis: Vector3D, majorRadius: double, minorRadius: double, startAngle: double, endAngle: double) -> boolean
Sets all of the data defining the elliptical arc.
- **center** (Point3D): The center point of the elliptical arc.
- **normal** (Vector3D): The normal vector of the elliptical arc.
- **majorAxis** (Vector3D): The major axis of the elliptical arc.
- **majorRadius** (double): The major radius of the of the elliptical arc.
- **minorRadius** (double): The minor radius of the of the elliptical arc.
- **startAngle** (double): The start angle of the elliptical arc in radians, where 0 is along the major axis.
- **endAngle** (double): The end angle of the elliptical arc in radians, where 0 is along the major axis.
- **Returns** (boolean): Returns true if successful.

### transformBy(matrix: Matrix3D) -> boolean
Transforms this curve in 3D space.
- **matrix** (Matrix3D): A 3D matrix that defines the transform to apply to the curve.
- **Returns** (boolean): Return true if the transform was successful.

## Properties

### asNurbsCurve : NurbsCurve3D [read-only]
Returns a NURBS curve that is geometrically identical to the elliptical arc.

### center : Point3D [read-write]
Gets and sets the center point of the elliptical arc.

### curveType : Curve3DTypes [read-only]
Returns the type of geometry this curve represents.

### endAngle : double [read-write]
Gets and sets the end angle of the elliptical arc.

### evaluator : CurveEvaluator3D [read-only]
Returns an evaluator object that lets you perform additional evaluations on the curve.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### majorAxis : Vector3D [read-write]
Gets and sets the major axis of the elliptical arc.

### majorRadius : double [read-write]
Gets and sets the major radius of the elliptical arc.

### minorRadius : double [read-write]
Gets and sets the minor radius of the elliptical arc.

### normal : Vector3D [read-only]
Gets the normal of the elliptical arc.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### startAngle : double [read-write]
Gets and sets the start angle of the elliptical arc.
