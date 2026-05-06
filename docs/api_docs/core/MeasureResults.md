# MeasureResults
Namespace: adsk.core
Inherits: Base
Since: December 2017

Provides measurement results from the various measurement methods available on the MeasureManager object.

**Accessed from:** MeasureManager.measureAngle, MeasureManager.measureMinimumDistance

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### positionOne : Point3D [read-only]
For a distance measurement, this is the point on the first entity where the measurement was made from. For an angle measurement this is one of the three points defining the angle.

### positionThree : Point3D [read-only]
This point is only used for angle measurements and is one of the three points defining the angle.

### positionTwo : Point3D [read-only]
For a distance measurement, this is the point on the second entity where the measurement was made to. For an angle measurement this is one of the three points defining the angle.

### value : double [read-only]
The measurement value. If the measurement is a distance this value will be in centimeters. If it's an angle then it will be in radians.

## Samples
- **Measure Sample**: Measure related functions
