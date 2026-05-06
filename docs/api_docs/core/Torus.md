# Torus
Namespace: adsk.core
Inherits: Surface
Since: August 2014

Transient torus. A transient torus is not displayed or saved in a document. A transient torus is used as a wrapper to work with raw torus information. A transient torus is a full torus with no boundaries. They are created statically using the create method of the Torus class.

**Accessed from:** Torus.copy, Torus.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Torus
Creates and returns an independent copy of this Torus object.
- **Returns** (Torus): Returns a new Torus object that is a copy of this Torus object.

### create(origin: Point3D, axis: Vector3D, majorRadius: double, minorRadius: double) -> Torus
Creates a transient torus object.
- **origin** (Point3D): The origin point (center) of the torus.
- **axis** (Vector3D): The center axis of the torus.
- **majorRadius** (double): The major radius of the torus.
- **minorRadius** (double): The minor radius of the torus.
- **Returns** (Torus): Returns the new Torus object or null if the creation failed.

### getData(origin: Point3D, axis: Vector3D, majorRadius: double, minorRadius: double) -> boolean
Gets all of the data defining the torus.
- **origin** (Point3D): The output origin point (center) of the torus.
- **axis** (Vector3D): The output center axis of the torus.
- **majorRadius** (double): The output major radius of the torus.
- **minorRadius** (double): The output minor radius of the torus.
- **Returns** (boolean): Returns true if successful.

### set(origin: Point3D, axis: Vector3D, majorRadius: double, minorRadius: double) -> boolean
Sets all of the data defining the torus.
- **origin** (Point3D): The origin point (center) of the torus.
- **axis** (Vector3D): The center axis of the torus.
- **majorRadius** (double): The major radius of the torus.
- **minorRadius** (double): The minor radius of the torus.
- **Returns** (boolean): Returns true if successful.

### transformBy(matrix: Matrix3D) -> boolean
Updates this surface by transforming it with a given input matrix.
- **matrix** (Matrix3D): A 3D matrix that defines the transform to apply to the surface.
- **Returns** (boolean): Returns true if the transform was successful.

## Properties

### axis : Vector3D [read-write]
Gets and sets the center axis of the torus.

### evaluator : SurfaceEvaluator [read-only]
Returns the surface evaluator.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### majorRadius : double [read-write]
Gets and sets the major radius of the torus.

### minorRadius : double [read-write]
Gets and sets the minor radius of the torus.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### origin : Point3D [read-write]
Gets and sets the origin point (center) of the torus.

### surfaceType : SurfaceTypes [read-only]
Returns the surface type.
