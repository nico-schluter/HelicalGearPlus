# AutoConstrainResult
Namespace: adsk.fusion
Inherits: Base
Since: January 2026

Provides the result information after a sketch auto constrain operation has been executed. This object contains details about what constraints and dimensions were added and whether the sketch was successfully fully constrained.

**Accessed from:** Sketch.autoConstrain

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### addedConstraints : array [read-only]
Returns an array of the GeometricConstraint objects that were added to constrain the sketch. If no geometric constraints were added during the auto constrain operation, this property returns an empty array.

### addedDimensions : array [read-only]
Returns an array of the SketchDimension objects that were added to constrain the sketch. If no dimensions were added during the auto constrain operation, this property returns an empty array.

### isFullyConstrained : boolean [read-only]
Indicates if the auto constrain operation successfully auto constrained the sketch. Returns true if the sketch is fully constrained after the operation, false otherwise. A value of false may indicate that additional constraints are needed or that the current sketch geometry cannot be fully constrained with the current settings.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
