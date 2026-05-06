# MachineAxisConfigurations
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Collection of axis configuration objects.

**Accessed from:** ControllerConfigurationMachineElement.axisConfigurations

## Methods

### addLinear(partId: string) -> LinearMachineAxisConfiguration
Add a new linear axis configuration for a kinematics part.
- **partId** (string): ID used to label this axis configuration and link to a part in the kinematics tree. partID must match a part of type AxisMachinePartType in the kinematics tree and the part must be a linear axis.
- **Returns** (LinearMachineAxisConfiguration): Returns the newly created LinearMachineAxisConfiguration or null if creation failed.

### addRotary(partId: string) -> RotaryMachineAxisConfiguration
Add a new rotary axis configuration for a kinematics part.
- **partId** (string): ID used to label this axis configuration and link to a part in the kinematics tree. partID must match a part of type AxisMachinePartType in the kinematics tree and the part must be a rotary axis.
- **Returns** (RotaryMachineAxisConfiguration): Returns the newly created RotaryMachineAxisConfiguration or null if creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: integer) -> MachineAxisConfiguration
Get the configuration at index in this collection
- **index** (integer): Index of configuration.
- **Returns** (MachineAxisConfiguration): Returns the MachineAxisConfiguration at index.

### itemById(id: string) -> MachineAxisConfiguration
Get the configuration with the given ID
- **id** (string): The ID for the configuration to get.
- **Returns** (MachineAxisConfiguration): Return the MachineAxisConfiguration with the given ID, or null if the given ID does not match any configuration in the collection.

## Properties

### count : uinteger [read-only]
Get the number of configurations in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
