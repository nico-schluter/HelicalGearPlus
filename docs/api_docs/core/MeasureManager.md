# MeasureManager
Namespace: adsk.core
Inherits: Base
Since: December 2017

The MeasurementManager class provides some generic measurement utilities that can be used for most entity types.

**Accessed from:** Application.measureManager

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getOrientedBoundingBox(geometry: Base, lengthVector: Vector3D, widthVector: Vector3D) -> OrientedBoundingBox3D
Calculates an oriented bounding box for the input geometry. The bounding box is tight fitting to the input geometry and is particularly useful when you want to calculate a bounding box that is not oriented to be parallel to the model x-y-z plane.

The height direction is automatically determined using the length and width directions.
- **geometry** (Base): The geometry to calculate the bounding box for. This can be any of the B-Rep related entities.
- **lengthVector** (Vector3D): The direction the length of the oriented bounding box will be measured in. The magnitude of the vector is ignored and only the direction is used.
- **widthVector** (Vector3D): The direction the width of the oriented bounding box will be measured in. The magnitude of the vector is ignored and only the direction is used. This must be perpendicular to the length vector.
- **Returns** (OrientedBoundingBox3D): Returns an OrientedBoundingBox3D object which provides the information that defines an oriented bounding box.

### measureAngle(geometryOne: Base, geometryTwo: Base, geometryThree: Base) -> MeasureResults
Measures the angle between the input geometry.
- **geometryOne** (Base): The first geometry to measure the angle to. This can be any 3D point geometry (Construction Point, Vertex, SketchPoint, or Point3D), any 3D linear geometry (Construction Axis, linear BRepEdge, SketchLine, Line3D, or InfiniteLine3D), or any planar geometry (Construction Plane, planar BRepFace, or Plane).
- **geometryTwo** (Base): The second geometry to measure the angle to. This can be any 3D point geometry (Construction Point, Vertex, SketchPoint, or Point3D), any 3D linear geometry (Construction Axis, linear BRepEdge, SketchLine, Line3D, or InfiniteLine3D), or any planar geometry (Construction Plane, planar BRepFace, or Plane).
- **geometryThree** (Base): The optional third geometry to measure the angle to. This is only used when the first two geometries are points and this defines the third point. When three points define a triangle, the apex of the triangle is defined by the second point. A point can be defined by a Construction Point, Vertex, SketchPoint, or Point3D object.

This is an optional argument whose default value is null.
- **Returns** (MeasureResults): A MeasureResults object that contains the angle and the two points on the geometry that the angle that was measured between them in radians.

### measureMinimumDistance(geometryOne: Base, geometryTwo: Base) -> MeasureResults
Measures the minimum distance between the two input geometries.
- **geometryOne** (Base): The first geometry to measure from. This can be an Occurrence, BRepBody, BRepFace, BRepEdge, BRepVertex, ConstructionPlane, ConstructionAxis, ConstructionPoint, and any sketch entity. The only temporary geometry supported is the Plane object.
- **geometryTwo** (Base): The first geometry to measure from. This can be an Occurrence, BRepBody, BRepFace, BRepEdge, BRepVertex, ConstructionPlane, ConstructionAxis, ConstructionPoint, and any sketch entity. The only temporary geometry supported is the Plane object.
- **Returns** (MeasureResults): A MeasureResults object that contains the distance and the two points on the geometry that the distance that was measured between them in centimeters.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Measure Sample**: Measure related functions
