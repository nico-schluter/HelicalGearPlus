# SketchEllipses
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

The collection of ellipses in a sketch. This provides access to the existing ellipses and supports the methods to create new ellipses.

**Accessed from:** SketchCurves.sketchEllipses

## Methods

### add(centerPoint: Base, majorAxisPoint: Point3D, point: Point3D) -> SketchEllipse
Creates a sketch ellipse using the center point, a point defining the major axis and a third point anywhere along the ellipse. The created ellipse is parallel to the x-y plane of the sketch.
- **centerPoint** (Base): The center point of the ellipse. This can be either an existing SketchPoint or a Point3D object.
- **majorAxisPoint** (Point3D): A point3D object that defines both the major axis direction and major axis radius.
- **point** (Point3D): A point3D object that the ellipse will pass through.
- **Returns** (SketchEllipse): Returns the newly created SketchEllipse object if the creation was successful or null if it failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SketchEllipse
Function that returns the specified sketch ellipse using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SketchEllipse): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of ellipses in the sketch.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
