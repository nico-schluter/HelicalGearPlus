# MachineToolStationInput
Namespace: adsk.cam
Inherits: Base
Since: July 2025

Object representing the set of inputs required to create a new MachineToolStation.

**Accessed from:** MachinePartInput.createToolStationInput, MachinePartInput.toolStationInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### coolants : array [read-write]
The coolants that this tool station can use. See MachineToolStationCoolant for possible values.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maxToolDiameter : double [read-write]
The maximum diameter in cm of the tool that can be held by this tool station.

### maxToolLength : double [read-write]
The maximum length in cm of the tool that can be held by this tool station.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### toolInterface : string [read-write]
The type of interface that this tool station uses. (e.g. BT40, CAPTO C5, HSK A100, SK50, etc.) Note: All newline characters will be removed, and if the string contains only ASCII characters, it will be converted to uppercase.
