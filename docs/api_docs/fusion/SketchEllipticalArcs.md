# SketchEllipticalArcs
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

The collection of elliptical arcs in a sketch. This provides access to the existing elliptical arcs and supports the methods to create new elliptical arcs.

**Accessed from:** SketchCurves.sketchEllipticalArcs

## Methods

### addByAngle(centerPoint: Base, majorAxis: Vector3D, minorAxis: Vector3D, startAngle: double, sweepAngle: double) -> SketchEllipticalArc
Creates an elliptical sketch arc where the sweep of the arc is defined by the start and sweep angles.
- **centerPoint** (Base): The center point of the ellipse. This can be either an existing SketchPoint or a Point3D object.
- **majorAxis** (Vector3D): The direction of the major axis. The magnitude of this vector defines the major radius.
- **minorAxis** (Vector3D): The direction of the minor axis. The magnitude of this vector defines the minor radius. This vector should be perpendicular to the major axis.
- **startAngle** (double): The start angle of the elliptical arc in radians, where 0 is along the major axis.
- **sweepAngle** (double): The sweep angle of the elliptical arc in radians, where a positive value is counterclockwise.
- **Returns** (SketchEllipticalArc): Returns the newly created SketchEllipticalArc or null if the creation failed.

### addByEndPoints(centerPoint: Base, majorAxis: Vector3D, minorAxis: Vector3D, startPoint: Base, endPoint: Base) -> SketchEllipticalArc
Creates an elliptical sketch arc where the sweep of the arc is defined by two points.
- **centerPoint** (Base): The center point of the ellipse. This can be either an existing SketchPoint or a Point3D object.
- **majorAxis** (Vector3D): The direction of the major axis. The magnitude of this vector defines the major radius.
- **minorAxis** (Vector3D): The direction of the minor axis. The magnitude of this vector defines the minor radius. This vector should be perpendicular to the major axis.
- **startPoint** (Base): The start point of the elliptical arc. This can be either an existing SketchPoint or a Point3D object. The point should lie on the defined ellipse.
- **endPoint** (Base): The end point of the elliptical arc. This can be either an existing SketchPoint or a Point3D object. The point should lie on the defined ellipse and the elliptical arc is defined by a counterclockwise sweep from the start point to the end point.
- **Returns** (SketchEllipticalArc): Returns the newly created SketchEllipticalArc or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SketchEllipticalArc
Function that returns the specified sketch elliptical arc using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SketchEllipticalArc): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of elliptical arcs in the sketch.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
