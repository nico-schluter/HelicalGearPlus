# SketchFittedSplines
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

The collection of fitted splines in a sketch. This provides access to the existing fitted splines and supports the methods to create new fitted splines.

**Accessed from:** SketchCurves.sketchFittedSplines

## Methods

### add(fitPoints: ObjectCollection) -> SketchFittedSpline
Creates a new fitted spline through the specified points.
- **fitPoints** (ObjectCollection): A collection of points that the curve will fit through. They can be any combination of existing SketchPoint or Point3D objects.
- **Returns** (SketchFittedSpline): Returns the newly created SketchFittedSpline object if the creation was successful or null if it failed.

### addByNurbsCurve(nurbsCurve: NurbsCurve3D) -> SketchFittedSpline
This function is retired. See more information in the 'Remarks' section below.

Creates a new fitted spline using the input NurbsCurve3D to define the shape. Fit points are created to create a curve that exactly matches the input curve.
- **nurbsCurve** (NurbsCurve3D): A NurbsCurve3D object that defines a valid NURBS curve.
- **Returns** (SketchFittedSpline): Returns the newly created SketchFittedSpline object if the creation was successful or null if it failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SketchFittedSpline
Function that returns the specified sketch fitted spline using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SketchFittedSpline): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of fitted splines in the sketch.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **SketchFittedSplines.add**: Demonstrates the SketchFittedSplines.add method.
- **Sketch spline through points creation and relative functions API Sample**: Create a sketch spline with points and use some operations for spline tangent handle & curvature handle.
