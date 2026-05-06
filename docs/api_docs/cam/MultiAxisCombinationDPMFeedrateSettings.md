# MultiAxisCombinationDPMFeedrateSettings
Namespace: adsk.cam
Inherits: MultiAxisDPMFeedrateSettings
Since: September 2025

Specialization of MultiAxisDPMFeedrateSettings for degrees per minute feedrates that require a combination of linear and rotary movements.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### dpmType : MultiAxisDegreesPerMinuteType [read-only]
The DPM settings type

### feedMode : MultiAxisFeedMode [read-only]
The feedmode to use for the multi axis.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maximumFeedrate : double [read-write]
The maximum feedrate value that can be output.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### outputTolerance : double [read-write]
The tolerance for deciding whether to output a feedrate value or not. It helps to minimize the output of multi-axis feedrate numbers. If the feedrate value is within this tolerance of the previous feedrate value, then it is set to the previous value. Value is in deg/min.

### pulseWeight : double [read-write]
The pulse weight ratio for the rotary axes when DPM feedrates are output as a combination of linear and rotary movements. The pulse weight is a scale factor based on the rotary axes accuracy compared to the linear axes accuracy. For example, it should be set to .1 when the linear axes are output on .0001 increments and the rotary axes on .001 increments.
