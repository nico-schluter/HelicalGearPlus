# MachineAxisConfiguration
Namespace: adsk.cam
Inherits: Base
Since: April 2023

MachineAxisConfiguration holds controller settings that differ for each axis.

**Accessed from:** MachineAxisConfigurations.item, MachineAxisConfigurations.itemById

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe()
Delete this axis configuration from the controller configuration.

## Properties

### coordinate : MachineAxisCoordinates [read-write]
Coordinate to use for post processing.

### isReversed : boolean [read-write]
Does the axis move in the opposite direction to usual. For rotary axes this would mean it uses the left hand rule, and for linear axes is moves in the opposite direction.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maxNormalSpeed : double [read-write]
Specifies the maximum normal speed for this axis. This would be called feedrate for a linear axis or rotary speed for a rotary axis. Units are cm/s for linear axes or rad/s for rotary axes.

### maxRapidSpeed : double [read-write]
Specifies the maximum rapid speed for this axis. This would be called feedrate for a linear axis or rotary speed for a rotary axis. Units are cm/s for linear axes or rad/s for rotary axes.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### partId : string [read-only]
ID of the part in the KinematicsMachineElement that this axis configuration modifies.

### type : MachineAxisTypes [read-only]
The type of this axis configuration. Use this to inform a cast to the derived types.
