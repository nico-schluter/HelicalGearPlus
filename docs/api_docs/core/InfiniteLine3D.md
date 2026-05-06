# InfiniteLine3D
Namespace: adsk.core
Inherits: Curve3D
Since: August 2014

Transient 3D infinite line. An infinite line is defined by a position and direction in space and has no start or end points. They are created statically using the create method of the InfiniteLine3D class.

**Accessed from:** ConstructionAxis.geometry, ConstructionAxisByLineDefinition.axis, InfiniteLine3D.copy, InfiniteLine3D.create, Line3D.asInfiniteLine, Plane.intersectWithPlane, RotaryMachineAxis.rotationAxis, RotaryMachineAxisInput.rotationAxis

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> InfiniteLine3D
Creates and returns a copy of this line object.
- **Returns** (InfiniteLine3D): Returns an independent copy of this line object.

### create(origin: Point3D, direction: Vector3D) -> InfiniteLine3D
Creates a transient 3D infinite line.
- **origin** (Point3D): The origin point of the line.
- **direction** (Vector3D): The direction of the line.
- **Returns** (InfiniteLine3D): Returns the new InfiniteLine3D object or null if the creation failed.

### getData(origin: Point3D, direction: Vector3D) -> boolean
Gets all of the data defining the infinite line.
- **origin** (Point3D): The output origin point of the line.
- **direction** (Vector3D): The output direction of the line.
- **Returns** (boolean): Returns true if successful.

### intersectWithCurve(curve: Curve3D) -> ObjectCollection
Intersect this line with a curve to get the intersection point(s).
- **curve** (Curve3D): The intersecting curve. The curve can be a Line3D, InfininteLine3D, Circle3D, Arc3D, EllipticalArc3D, Ellipse3D, or NurbsCurve3D.
- **Returns** (ObjectCollection): Returns a collection of the intersection points.

### intersectWithSurface(surface: Surface) -> ObjectCollection
Intersect this line with a surface to get the intersection point(s).
- **surface** (Surface): The intersecting surface. The surface can be a Plane, Cone, Cylinder, EllipticalCone, EllipticalCylinder, Sphere, Torus, or a NurbsSurface.
- **Returns** (ObjectCollection): Returns a collection of the intersection points.

### isColinearTo(line: InfiniteLine3D) -> boolean
Compare this line with another to check for collinearity.
- **line** (InfiniteLine3D): The line to compare with for collinearity.
- **Returns** (boolean): Returns true if the two lines are collinear.

### set(origin: Point3D, direction: Vector3D) -> boolean
Sets all of the data defining the infinite line.
- **origin** (Point3D): The origin point of the line.
- **direction** (Vector3D): The direction of the line.
- **Returns** (boolean): Returns true if successful.

### transformBy(matrix: Matrix3D) -> boolean
Transforms this curve in 3D space.
- **matrix** (Matrix3D): A 3D matrix that defines the transform to apply to the curve.
- **Returns** (boolean): Return true if the transform was successful.

## Properties

### curveType : Curve3DTypes [read-only]
Returns the type of geometry this curve represents.

### direction : Vector3D [read-write]
Gets and sets the direction of the line.

### evaluator : CurveEvaluator3D [read-only]
Returns an evaluator object that lets you perform additional evaluations on the curve.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### origin : Point3D [read-write]
Gets and sets the origin point of the line.
