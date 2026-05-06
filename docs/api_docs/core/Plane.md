# Plane
Namespace: adsk.core
Inherits: Surface
Since: August 2014

Transient plane. A transient plane is not displayed or saved in a document. Transient planes are used as a wrapper to work with raw plane information. A transient plane has no boundaries or size, but is infinite and is represented by a position, a normal, and an orientation in space. They are created statically using the create method of the Plane class.

**Accessed from:** Canvas.plane, CanvasInput.plane, ConstructionPlane.geometry, ConstructionPlaneByPlaneDefinition.plane, OffsetStartDefinition.profilePlane, Plane.copy, Plane.create, Plane.createUsingDirections, Profile.plane, ProfilePlaneStartDefinition.profilePlane

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Plane
Creates and returns an independent copy of this Plane object.
- **Returns** (Plane): Returns a new Plane object that is a copy of this Plane object.

### create(origin: Point3D, normal: Vector3D) -> Plane
Creates a transient plane object by specifying an origin and a normal direction.
- **origin** (Point3D): The origin point of the plane.
- **normal** (Vector3D): The normal direction of the plane.
- **Returns** (Plane): Returns the new plane object or null if the creation failed.

### createUsingDirections(origin: Point3D, uDirection: Vector3D, vDirection: Vector3D) -> Plane
Creates a transient plane object by specifying an origin along with U and V directions.
- **origin** (Point3D): The origin point of the plane.
- **uDirection** (Vector3D): The U direction for the plane.
- **vDirection** (Vector3D): The V direction for the plane.
- **Returns** (Plane): Returns the new plane object or null if the creation failed.

### intersectWithCurve(curve: Curve3D) -> ObjectCollection
Intersect this plane with a curve to get the intersection point(s).
- **curve** (Curve3D): The intersecting curve. The curve can be a Line3D, InfininteLine3D, Circle3D, Arc3D, EllipticalArc3D, Ellipse3D, or NurbsCurve3D.
- **Returns** (ObjectCollection): Returns a collection of the intersection points.

### intersectWithLine(line: InfiniteLine3D) -> Point3D
Creates a 3D point at the intersection of this plane and a line.
- **line** (InfiniteLine3D): The line to intersect with.
- **Returns** (Point3D): Returns a Point3D object or null if the plane and line do not intersect (are parallel).

### intersectWithPlane(plane: Plane) -> InfiniteLine3D
Creates an infinite line at the intersection of this plane with another plane.
- **plane** (Plane): The plane to intersect with.
- **Returns** (InfiniteLine3D): Returns an InfiniteLine3D object or null if the planes do not intersect (are parallel).

### intersectWithSurface(surface: Surface) -> ObjectCollection
Intersect this plane with a surface to get the intersection point(s).
- **surface** (Surface): The intersecting surface. The surface can be a Plane, Cone, Cylinder, EllipticalCone, EllipticalCylinder, Sphere, Torus, or a NurbsSurface.
- **Returns** (ObjectCollection): Returns a collection of the intersection points.

### isCoPlanarTo(plane: Plane) -> boolean
Checks if this plane is coplanar with another plane.
- **plane** (Plane): The plane to compare with for co-planarity.
- **Returns** (boolean): Returns true if the planes are coplanar.

### isParallelToLine(line: Line3D) -> boolean
Checks if this plane is parallel to a line.
- **line** (Line3D): The line to compare with for parallelism.
- **Returns** (boolean): Returns true if the plane and line are parallel.

### isParallelToPlane(plane: Plane) -> boolean
Checks if this plane is parallel to another plane.
- **plane** (Plane): The plane to compare with for parallelism.
- **Returns** (boolean): Returns true if the planes are parallel.

### isPerpendicularToLine(line: Line3D) -> boolean
Checks if this plane is perpendicular to a line.
- **line** (Line3D): The line to compare with for perpendicularity.
- **Returns** (boolean): Returns true if the plane and line are perpendicular.

### isPerpendicularToPlane(plane: Plane) -> boolean
Checks if this plane is perpendicular to another plane.
- **plane** (Plane): The plane to compare with for perpendicularity.
- **Returns** (boolean): Returns true if the planes are perpendicular.

### setUVDirections(uDirection: Vector3D, vDirection: Vector3D) -> boolean
Sets the U and V directions of the plane.
- **uDirection** (Vector3D): The U direction for the plane.
- **vDirection** (Vector3D): The V direction for the plane.
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

### normal : Vector3D [read-write]
Gets and sets the normal of the plane.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### origin : Point3D [read-write]
Gets and sets the origin point of the plane.

### surfaceType : SurfaceTypes [read-only]
Returns the surface type.

### uDirection : Vector3D [read-only]
Gets the U Direction of the plane.

### vDirection : Vector3D [read-only]
Gets the V Direction of the plane.
