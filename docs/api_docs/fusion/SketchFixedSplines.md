# SketchFixedSplines
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

The collection of fixed splines in a sketch. Fixed splines are splines that were created as the result of some operation (i.e. intersection) and is not directly editable.

**Accessed from:** SketchCurves.sketchFixedSplines

## Methods

### addByNurbsCurve(nurbsCurve: NurbsCurve3D) -> SketchFixedSpline
Creates a new fixed spline using the input NurbsCurve3D to define the shape. The resulting curve is not editable by the user but can be updated via the API using the replaceGeometry method on the SketchFixedSpline object.
- **nurbsCurve** (NurbsCurve3D): A NurbsCurve3D object that defines a valid NURBS curve.
- **Returns** (SketchFixedSpline): Returns the newly created SketchFixedSpline object if the creation was successful or null if it failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SketchFixedSpline
Function that returns the specified sketch fixed spline using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SketchFixedSpline): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of fitted splines in the sketch.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **SketchFixedSplines.addByNurbsCurve**: Demonstrates the SketchFixedSplines.addByNurbsCurve method.
