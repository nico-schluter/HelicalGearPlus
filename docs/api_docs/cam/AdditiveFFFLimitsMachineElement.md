# AdditiveFFFLimitsMachineElement
Namespace: adsk.cam
Inherits: MachineElement
Since: July 2023

Machine element representing limits for fused filament fabrication (FFF) machine motion and temperatures.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### staticTypeId() -> string
Identifying name for all elements of this type. Pass this to the itemByType or itemById methods of MachineElements to filter to elements of this type.
- **Returns** (string): Returns identifier of this type.

## Properties

### elementId : string [read-only]
Identifier for this element. Unique within an element type.

### homePosition : Point3D [read-write]
Position of the machine home location.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maximumBedTemperature : double [read-write]
Maximum bed temperature in degrees C.

### maximumXYAcceleration : double [read-write]
Maximum supported acceleration for motion in the X or Y axes in cm/s^2.

### maximumXYSpeed : double [read-write]
Maximum supported speed for motion in the X or Y axes in cm/s.

### maximumZAcceleration : double [read-write]
Maximum supported acceleration for motion in the Z axis in cm/s^2.

### maximumZSpeed : double [read-write]
Maximum supported speed for motion in the Z axis in cm/s.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parkPosition : Point3D [read-write]
Position machine moves to when "parked".

### typeId : string [read-only]
Identifier for this type of machine element.
