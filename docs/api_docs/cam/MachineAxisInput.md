# MachineAxisInput
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Object that defines the properties required to create a machine axis object.

**Accessed from:** MachinePartInput.axisInput, MachinePartInput.createAxisInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### axisType : MachineAxisTypes [read-only]
The type of axis. This axis type determines which parameters of this object are valid to be accessed or modified.

### homePosition : double [read-write]
Specifies the value that this axis returns to when the machine is homed. Units are cm for linear axes or radians for rotary axes.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
The user facing name of this axis.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### physicalRange : MachineAxisRange [read-write]
Range of possible values for this axis. Units are cm for linear axes or radians for rotary axes.

### toolChangePosition : double [read-write]
Specifies the value that this axis returns to, prior to a tool change. Units are cm for linear axes or radians for rotary axes.
