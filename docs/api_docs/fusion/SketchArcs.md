# SketchArcs
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

The collection of arcs in a sketch. This provides access to the existing arcs and supports the methods to create new arcs.

**Accessed from:** SketchCurves.sketchArcs

## Methods

### addByCenterStartEnd(centerPoint: Base, startPoint: Base, endPoint: Base, normal: Vector3D) -> SketchArc
Creates a sketch arc that is centered at the specified point and between the two input points.
- **centerPoint** (Base): The center point of the arc. This can be either an existing SketchPoint or a Point3D object.
- **startPoint** (Base): The start point of the arc. This can be either an existing SketchPoint or a Point3D object.
- **endPoint** (Base): The end point of the arc. This can be either an existing SketchPoint or a Point3D object. If the end point does not lie on the arc, a new point would be created such that it lies on the arc.
- **normal** (Vector3D): An optional argument that specifies the normal of the plane the arc will be created on. If not supplied, a vector in the positive Z direction will be used, which results in the creation of an arc that is parallel to the X-Y plane of the sketch. However, you can specify a normal vector to orient the arc in any orientation. The normal also helps to control the sweep direction of the arc, where the sweep direction is always counterclockwise from the start to the end point, where counterclockwise is defined using the right-hand rule around the normal vector.

This is an optional argument whose default value is null.
- **Returns** (SketchArc): Returns the newly created SketchArc or null in the case of a failure.

### addByCenterStartSweep(centerPoint: Base, startPoint: Base, sweepAngle: double) -> SketchArc
Creates a sketch arc that is always parallel to the x-y plane of the sketch and is centered at the specified point.
- **centerPoint** (Base): The center point of the arc. This can be either an existing SketchPoint or a Point3D object.
- **startPoint** (Base): The start point of the arc. The distance between this point and the center defines the radius of the arc. This can be either an existing SketchPoint or a Point3D object.
- **sweepAngle** (double): The sweep of the arc. This is defined in radians and a positive value defines a counter-clockwise sweep.
- **Returns** (SketchArc): Returns the newly created SketchArc object or null if the creation failed.

### addByThreePoints(startPoint: Base, point: Point3D, endPoint: Base) -> SketchArc
Creates a sketch arc that passes through the three points.
- **startPoint** (Base): The start point of the arc. This can be either an existing SketchPoint or a Point3D object.
- **point** (Point3D): A point along the arc. This is a Point3D object.
- **endPoint** (Base): The end point of the arc. This can be either an existing SketchPoint or a Point3D object.
- **Returns** (SketchArc): Returns the newly created SketchArc or null in the case of a failure.

### addFillet(firstEntity: SketchCurve, firstEntityPoint: Point3D, secondEnitity: SketchCurve, secondEntityPoint: Point3D, radius: double) -> SketchArc
Creates a fillet between two sketch entities The side (quadrant) the fillet is created on is determined by the points specified. The point for each entity can be its startSketchPoint or endSketchPoint
- **firstEntity** (SketchCurve): The first curve for the fillet definition. The curve must be open.
- **firstEntityPoint** (Point3D): A point on or closer to one end of the first curve that indicates the side to create the fillet on
- **secondEnitity** (SketchCurve): The second curve for the fillet definition. The curve must be open.
- **secondEntityPoint** (Point3D): A point on or closer to one end of the second curve that indicates the side to create the fillet on
- **radius** (double): radius of the arc in centimeters
- **Returns** (SketchArc): Returns the newly created SketchArc object (fillet) if the operation was successful or null if it failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SketchArc
Function that returns the specified sketch arc using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SketchArc): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of arcs in the sketch.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **SketchArcs.addByCenterStartSweep**: Demonstrates the SketchArcs.addByCenterStartSweep method.
- **SketchArcs.addByThreePoints**: Demonstrates the SketchArcs.addByThreePoints method.
- **SketchArcs.addFillet**: Demonstrates the SketchArcs.addFillet method.
- **SketchArcs.breakCurve**: Demonstrates the SketchArc.breakCurve method.
- **SketchArcs.extend**: Demonstrates the SketchArc.extend method.
- **SketchArcs.split**: Demonstrates the SketchArc.split method.
- **Sketch fillet and offset API Sample**: Demonstrates the creation of a fillet in a sketch and offset a set of curves.
