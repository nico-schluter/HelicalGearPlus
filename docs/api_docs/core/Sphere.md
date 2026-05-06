# Sphere
Namespace: adsk.core
Inherits: Surface
Since: August 2014

Transient sphere. A transient sphere is not displayed or saved in a document. Transient spheres are used as a wrapper to work with raw sphere information. A transient sphere is a full sphere defined by a point and a radius. They are created statically using the create method of the Sphere class.

**Accessed from:** Sphere.copy, Sphere.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Sphere
Creates and returns an independent copy of this Sphere object.
- **Returns** (Sphere): Returns a new Sphere object that is a copy of this Sphere object.

### create(origin: Point3D, radius: double) -> Sphere
Creates a transient sphere object.
- **origin** (Point3D): The origin point (center) of the sphere.
- **radius** (double): The radius of the sphere.
- **Returns** (Sphere): Returns the new Sphere object or null if the creation failed.

### getData(origin: Point3D, radius: double) -> boolean
Gets all of the data defining the sphere.
- **origin** (Point3D): The output origin point (center) of the sphere.
- **radius** (double): The output radius of the sphere.
- **Returns** (boolean): Returns true if successful.

### set(origin: Point3D, radius: double) -> boolean
Sets all of the data defining the sphere.
- **origin** (Point3D): The origin point (center) of the sphere.
- **radius** (double): The radius of the sphere.
- **Returns** (boolean): Returns true if successful.

### transformBy(matrix: Matrix3D) -> boolean
Updates this surface by transforming it with a given input matrix.
- **matrix** (Matrix3D): A 3D matrix that defines the transform to apply to the surface.
- **Returns** (boolean): Returns true if the transform was successful.

## Properties

### evaluator : SurfaceEvaluator [read-only]
Returns the surface evaluator.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### origin : Point3D [read-write]
Gets and sets the origin point (center) of the sphere.

### radius : double [read-write]
Gets and sets the radius of the sphere.

### surfaceType : SurfaceTypes [read-only]
Returns the surface type.
