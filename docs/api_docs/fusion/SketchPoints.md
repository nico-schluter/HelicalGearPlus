# SketchPoints
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

A collection of sketch points.

**Accessed from:** Sketch.sketchPoints

## Methods

### add(point: Point3D) -> SketchPoint
Creates a point at the specified location. This is the equivalent of creating a sketch point using the Point command in the user interface and will create a visible point in the graphics window.
- **point** (Point3D): The coordinate location to create the sketch point.
- **Returns** (SketchPoint): Returns the new sketch point or null if the creation fails.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SketchPoint
Function that returns the specified sketch using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SketchPoint): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of sketch points in the sketch.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **GeometricConstraints.addCoincident**: Demonstrates the GeometricConstraints.addCoincident method.
- **SketchPoint.add**: Demonstrates the SketchPoint.add method.
- **Sketch Point API Sample**: Demonstrates creating a new sketch point.
