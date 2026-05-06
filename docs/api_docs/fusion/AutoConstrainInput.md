# AutoConstrainInput
Namespace: adsk.fusion
Inherits: Base
Since: January 2026

The AutoConstrainInput object is used to define the various options when adding dimension and geometric constraints to help constrain a sketch.

**Accessed from:** Sketch.createAutoConstrainInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### datumPoint : SketchPoint [read-write]
Gets and sets an optional datum point that the dimensions will be based on. This defaults to null, which indicates there is no datum point specified. When no datum point is provided, AutoConstrain will automatically select an appropriate datum based on the sketch content and geometry.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentSketch : Sketch [read-only]
Returns the Sketch this object is associated with and where the dimension and geometric constraints will be added when the autoConstrain method is called. This property is read-only and is set when the input object is created by the sketch's createAutoConstrainInput method.
