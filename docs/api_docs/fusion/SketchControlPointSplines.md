# SketchControlPointSplines
Namespace: adsk.fusion
Inherits: Base
Since: July 2022

The collection of control point splines in a sketch.

**Accessed from:** SketchCurves.sketchControlPointSplines

## Methods

### add(controlPoints: Base[], degree: SplineDegrees) -> SketchControlPointSpline
Creates a new control point spline.
- **controlPoints** (Base[]): An array of points that define the control points of the curve's polygon. They can be any combination of existing SketchPoint or Point3D objects.
- **degree** (SplineDegrees): Specifies the degree of the spline. Only degree 3 and degree 5 can be specified while creating the spline.
- **Returns** (SketchControlPointSpline): Returns the newly created SketchControlPointSpline object if the creation was successful or null if it failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SketchControlPointSpline
Function that returns the specified sketch control point spline using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SketchControlPointSpline): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of control point splines in the sketch.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
