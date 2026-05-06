# EllipticalCone
Namespace: adsk.core
Inherits: Surface
Since: August 2014

Transient elliptical cone. A transient elliptical cone is not displayed or saved in a document. A transient elliptical cone is used as a wrapper to work with raw elliptical cone information. A transient elliptical cone has no boundaries. The cone always goes to a point in its narrowing direction, and is infinite in its widening direction. They are created statically using the create method of the EllipticalCone class.

**Accessed from:** EllipticalCone.copy, EllipticalCone.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> EllipticalCone
Creates and returns an independent copy of this EllipticalCone object.
- **Returns** (EllipticalCone): Returns a new EllipticalCone object that is a copy of this EllipticalCone object.

### create(origin: Point3D, axis: Vector3D, majorAxisDirection: Vector3D, majorRadius: double, minorRadius: double, halfAngle: double) -> EllipticalCone
Creates a transient elliptical cone object.
- **origin** (Point3D): The origin point (center) of the base of the cone.
- **axis** (Vector3D): The center axis (along the length) of the cone that defines its normal direction.
- **majorAxisDirection** (Vector3D): The direction of the major axis of the ellipse that defines the cone.
- **majorRadius** (double): The major radius of the ellipse that defines the cone.
- **minorRadius** (double): The minor radius of the ellipse that defines the cone.
- **halfAngle** (double): The taper half-angle of the cone.
- **Returns** (EllipticalCone): Returns the new EllipticalCone object or null if the creation failed.

### getAxes(axis: Vector3D, majorAxisDirection: Vector3D)
Gets the center axis of the cone that defines its normal direction and the major axis direction of the ellipse that defines it.
- **axis** (Vector3D): The output center axis (along the length) of the cone that defines its normal direction.
- **majorAxisDirection** (Vector3D): The output direction of the major axis of the ellipse that defines the cone.

### getData(origin: Point3D, axis: Vector3D, majorAxisDirection: Vector3D, majorRadius: double, minorRadius: double, halfAngle: double) -> boolean
Gets the data that defines the Elliptical Cone.
- **origin** (Point3D): The output origin point (center) of the base of the cone.
- **axis** (Vector3D): The output center axis (along the length) of the cone that defines its normal direction.
- **majorAxisDirection** (Vector3D): The output direction of the major axis of the ellipse that defines the cone.
- **majorRadius** (double): The output major radius of the ellipse that defines the cone.
- **minorRadius** (double): The output minor radius of the ellipse that defines the cone.
- **halfAngle** (double): The output taper half-angle of the cone.
- **Returns** (boolean): Returns true if successful.

### set(origin: Point3D, axis: Vector3D, majorAxisDirection: Vector3D, majorRadius: double, minorRadius: double, halfAngle: double) -> boolean
Sets the data that defines the Elliptical Cone.
- **origin** (Point3D): The origin point (center) of the base of the cone.
- **axis** (Vector3D): The center axis (along the length) of the cone that defines its normal direction.
- **majorAxisDirection** (Vector3D): The direction of the major axis of the ellipse that defines the cone.
- **majorRadius** (double): The major radius of the ellipse that defines the cone.
- **minorRadius** (double): The minor radius of the ellipse that defines the cone.
- **halfAngle** (double): The taper half-angle of the cone.
- **Returns** (boolean): Returns true if successful.

### setAxes(axis: Vector3D, majorAxisDirection: Vector3D) -> boolean
Sets the center axis of the cone and the major axis direction of the ellipse that defines it.
- **axis** (Vector3D): The center axis (along the length) of the cone that defines its normal direction.
- **majorAxisDirection** (Vector3D): The direction of the major axis of the ellipse that defines the cone.
- **Returns** (boolean): Returns true if successful.

### transformBy(matrix: Matrix3D) -> boolean
Updates this surface by transforming it with a given input matrix.
- **matrix** (Matrix3D): A 3D matrix that defines the transform to apply to the surface.
- **Returns** (boolean): Returns true if the transform was successful.

## Properties

### evaluator : SurfaceEvaluator [read-only]
Returns the surface evaluator.

### halfAngle : double [read-write]
Gets and sets the taper half-angle of the elliptical cone. A negative value indicates that the cone is narrowing in the direction of the axis vector, whereas a positive values indicates that it is expanding in the direction of the axis vector.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### majorRadius : double [read-write]
Gets and sets the major radius of the ellipse that defines the cone.

### minorRadius : double [read-write]
Gets and sets the minor radius of the ellipse that defines the cone.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### origin : Point3D [read-write]
Gets and sets the origin point (center) of the base of the cone.

### surfaceType : SurfaceTypes [read-only]
Returns the surface type.
