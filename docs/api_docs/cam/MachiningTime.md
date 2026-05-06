# MachiningTime
Namespace: adsk.cam
Inherits: Base
Since: September 2017

Object returned when using the getMachiningTime method from the CAM class. Use the properties on this object to get the machining time results.

**Accessed from:** CAM.getMachiningTime

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### feedDistance : double [read-only]
Gets the feed distance in centimeters.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### machiningTime : double [read-only]
Gets the machining time in seconds.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### rapidDistance : double [read-only]
Gets the calculated rapid distance in centimeters.

### toolChangeCount : integer [read-only]
Gets the number of tool changes.

### totalFeedTime : double [read-only]
Get the total feed time in seconds.

### totalRapidTime : double [read-only]
Gets the total rapid feed time in seconds.

### totalToolChangeTime : double [read-only]
Gets the total tool change time in seconds.
