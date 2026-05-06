# MachineCapabilities
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Object that represents the capabilities of the machine.

**Accessed from:** Machine.capabilities

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### additiveTechnology : AdditiveTechnologies [read-only]
Gets which additive technology the machine supports. Return "NA" if the machine does not support Additive

### isAdditiveSupported : boolean [read-write]
Gets and sets if the machine is capable of additive operations.

### isCuttingSupported : boolean [read-write]
Gets and sets if the machine is capable of subtractive cutting.

### isMillingSupported : boolean [read-write]
Gets and sets if the machine is capable of subtractive milling.

### isTurningSupported : boolean [read-write]
Gets and sets if the machine is capable of subtractive turning.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
