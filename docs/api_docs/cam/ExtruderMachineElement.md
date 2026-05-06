# ExtruderMachineElement
Namespace: adsk.cam
Inherits: MachineElement
Since: January 2026

Machine element representing an extruder on a fused filament fabrication (FFF) machine. A machine can have multiple extruders and thus multiple ExtruderMachineElement elements.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe()
Delete this extruder element from the machine. Throws an exception when trying to delete the last remaining element.

### staticTypeId() -> string
Identifying name for all elements of this type. Pass this to the itemByType or itemById methods of MachineElements to filter to elements of this type.
- **Returns** (string): Returns identifier of this type.

## Properties

### elementId : string [read-only]
Identifier for this element. Unique within an element type.

### filamentDiameter : double [read-write]
Filament diameter of this extruder in cm.

### isFanAvailable : boolean [read-write]
Flag indicating if a fan, whose speed is settable in the post, is available.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Name of this extruder. Depending on the post, this may be output in the resulting gcode as a comment.

### nozzleDiameter : double [read-write]
Nozzle diameter of this extruder in cm.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### offset : Vector3D [read-write]
Offset relative to the main extruder. The first extruder has an index of 0 and usually an offset of (0,0,0).

### temperature : double [read-write]
The maximum temperature this extruder can reach in degrees C.

### typeId : string [read-only]
Identifier for this type of machine element.

### volumePerSecond : double [read-write]
The maximum volume output measured in cm^3/s.
