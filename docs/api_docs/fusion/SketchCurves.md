# SketchCurves
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

A collection of sketch curves in a sketch. This also provides access to collections for the specific types of curves where you can get the curves based on type and create new curves.

**Accessed from:** Sketch.sketchCurves

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SketchCurve
Function that returns the specified sketch curve using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SketchCurve): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of sketch curves in the sketch.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### sketchArcs : SketchArcs [read-only]
Returns the sketch arcs collection associated with this sketch. This provides access to the existing sketch arcs and supports the creation of new sketch arcs.

### sketchCircles : SketchCircles [read-only]
Returns the sketch circles collection associated with this sketch. This provides access to the existing sketch circles and supports the creation of new sketch circles.

### sketchConicCurves : SketchConicCurves [read-only]
Returns the conic curves collection associated with this sketch. This provides access to the existing conic curves and supports the creation of new conic curves.

### sketchControlPointSplines : SketchControlPointSplines [read-only]
Returns the control point splines collection associated with this sketch. This provides access to the existing control point splines and supports the creation of new control point splines.

### sketchEllipses : SketchEllipses [read-only]
Returns the sketch ellipses collection associated with this sketch. This provides access to the existing sketch ellipses and supports the creation of new sketch ellipses.

### sketchEllipticalArcs : SketchEllipticalArcs [read-only]
Returns the sketch elliptical arcs collection associated with this sketch. This provides access to the existing sketch elliptical arcs and supports the creation of new sketch elliptical arcs.

### sketchFittedSplines : SketchFittedSplines [read-only]
Returns the sketch splines collection associated with this sketch. This provides access to the existing sketch splines and supports the creation of new sketch splines.

### sketchFixedSplines : SketchFixedSplines [read-only]
Returns the fixed sketch splines collection associated with this sketch. This provides access to the existing fixed sketch splines and supports the creation of new fixed sketch splines.

### sketchLines : SketchLines [read-only]
Returns the sketch lines collection associated with this sketch. This provides access to the existing sketch lines and supports the creation of new sketch lines.

## Samples
- **API Sample that demonstrates creating sketch lines in various ways.**: Demonstrates several ways to create sketch lines, including as the result of creating a rectangle.
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
- **Simple Extrusion Sample**: Creates a new extrusion feature, resulting in a new component.
- **Simple Revolve Feature Sample**: Creates a new revolve feature, resulting in a new component.
