# SpunProfileInput
Namespace: adsk.fusion
Inherits: Base
Since: November 2024

The input object that defines the required input to create a spun profile when using the Sketch.createSpunProfile method. Created using the Sketch.createSpunProfileInput method.

**Accessed from:** Sketch.createSpunProfileInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### axis : Base [read-write]
Gets and sets the entity used to define the axis of revolution. The axis can be a sketch line, construction axis, or linear edge. The axis must not be perpendicular to the sketch plane.

### entities : array [read-write]
Gets and sets the entities (BRepBody or BRepFace) used to define the shape of the spun profile.

### flipResult : boolean [read-write]
Gets and sets whether the profile will be created on the opposite side of the axis.

### isAxisProjected : boolean [read-write]
Specifies if the axis will be projected to the sketch plane before making the spun profile. Otherwise, the spun profile will be generated around the axis in space. Defaults to true.

### isCenterlineAdded : boolean [read-write]
Gets and sets whether a resulting spun profile that would be open, will be closed along the axis of rotation. This closes the sketch so it is ready for further design operations, like revolving the sketch for example. Defaults to true.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### tolerance : double [read-write]
Gets and sets the linear tolerance in cm used for creating the spun profile. Defaults to 0.001cm.
