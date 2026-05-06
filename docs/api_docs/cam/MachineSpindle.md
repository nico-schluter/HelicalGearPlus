# MachineSpindle
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Object representing a spindle on the machine

**Accessed from:** MachinePart.spindle

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### description : string [read-write]
The description of this spindle.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maxSpeed : double [read-write]
Specifies the maximum speed (rpm) for this spindle.

### minSpeed : double [read-write]
Specifies the minimum speed (rpm) for this spindle.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### peakTorque : double [read-write]
Specifies the peak torque (Nm) for this spindle.

### peakTorqueSpeed : double [read-write]
Specifies the speed (rpm) at which this spindle reaches peak torque (Nm).

### power : double [read-write]
Specifies the power (kW) for this spindle.
