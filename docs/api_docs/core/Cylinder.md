# Cylinder
Namespace: adsk.core
Inherits: Surface
Since: August 2014

Transient cylinder. A transient cylinder is not displayed or saved in a document. A transient cylinder is but is used as a wrapper to work with raw cylinder information. A transient cylinder has no boundaries and is infinite in length. They are created statically using the create method of the Cylinder class.

**Accessed from:** Cylinder.copy, Cylinder.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Cylinder
Creates and returns an independent copy of this Cylinder object.
- **Returns** (Cylinder): Returns a new Cylinder object that is a copy of this Cylinder object.

### create(origin: Point3D, axis: Vector3D, radius: double) -> Cylinder
Creates a transient cylinder object.
- **origin** (Point3D): The origin point (center) of the base of the cylinder.
- **axis** (Vector3D): The center axis (along the length) of the cylinder that defines its normal direction.
- **radius** (double): The radius of the cylinder.
- **Returns** (Cylinder): Returns the new Cylinder object or null if the creation failed.

### getData(origin: Point3D, axis: Vector3D, radius: double) -> boolean
Gets the data that defines the cylinder.
- **origin** (Point3D): The output origin point (center) of the base of the cylinder.
- **axis** (Vector3D): The output center axis (along the length) of the cylinder that defines its normal direction.
- **radius** (double): The output radius of the cylinder.
- **Returns** (boolean): Returns true if successful.

### set(origin: Point3D, axis: Vector3D, radius: double) -> boolean
Sets the data that defines the cylinder.
- **origin** (Point3D): The origin point (center) of the base of the cylinder.
- **axis** (Vector3D): The center axis (along the length) of the cylinder that defines its normal direction.
- **radius** (double): The radius of the cylinder.
- **Returns** (boolean): Returns true if successful.

### transformBy(matrix: Matrix3D) -> boolean
Updates this surface by transforming it with a given input matrix.
- **matrix** (Matrix3D): A 3D matrix that defines the transform to apply to the surface.
- **Returns** (boolean): Returns true if the transform was successful.

## Properties

### axis : Vector3D [read-write]
The center axis (along the length) of the cylinder that defines its normal direction.

### evaluator : SurfaceEvaluator [read-only]
Returns the surface evaluator.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### origin : Point3D [read-write]
The origin point (center) of the base of the cylinder.

### radius : double [read-write]
The radius of the cylinder.

### surfaceType : SurfaceTypes [read-only]
Returns the surface type.
