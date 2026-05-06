# SketchConicCurves
Namespace: adsk.fusion
Inherits: Base
Since: January 2015

The collection of conic curves in a sketch. This provides access to the existing conic curves and supports the method to create new conic curves.

**Accessed from:** SketchCurves.sketchConicCurves

## Methods

### add(startPoint: Base, endPoint: Base, apexPoint: Base, rhoValue: double) -> SketchConicCurve
Creates a new conic curve.
- **startPoint** (Base): The start point of the conic curve. This can be either an existing SketchPoint or a Point3D object.
- **endPoint** (Base): The end point of the conic curve. This can be either an existing SketchPoint or a Point3D object.
- **apexPoint** (Base): The apex point of the conic curve. This can be either an existing SketchPoint or a Point3D object.
- **rhoValue** (double): Double that specifies the rho value for the conic. This value must be greater than zero and less than one.
- **Returns** (SketchConicCurve): Returns the new conic curve or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SketchConicCurve
Function that returns the specified conic curve using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SketchConicCurve): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of conic curves in the sketch.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
