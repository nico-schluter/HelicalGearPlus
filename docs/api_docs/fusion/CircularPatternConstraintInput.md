# CircularPatternConstraintInput
Namespace: adsk.fusion
Inherits: Base
Since: September 2022

This class defines the methods and properties that pertain to the definition of a circular pattern in a sketch.

**Accessed from:** GeometricConstraints.createCircularPatternInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### centerPoint : SketchPoint [read-write]
Gets and sets the sketch point that defines the center of the pattern.

### entities : array [read-write]
Gets and sets the entities to pattern. Sketch points and curves are valid entities to pattern.

### isSuppressed : array [read-write]
Specifies which, if any, instances of the pattern are suppressed. This defaults to all instances being visible. This returns an array of Booleans that indicates if a particular instance in the pattern is suppressed or not. A value of true will result in the associated instance being suppressed.

### isSymmetric : boolean [read-write]
Gets and sets if the angle extent is in one direction or is symmetric.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### quantity : ValueInput [read-write]
Gets and sets quantity of the elements.

### totalAngle : ValueInput [read-write]
Gets and sets total angle. A positive angle is a counter-clockwise direction and a negative angle can be used to reverse the direction. An angle of 360 degrees or 2 pi radians will create a full circular pattern.
