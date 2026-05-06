# MachinePartInput
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Object representing the set of inputs required to create a new MachinePart. Set an MachineAxisInput object on this object's axisInput parameter to create a new MachineAxis with this part.

**Accessed from:** MachineParts.createPartInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createAxisInput(axisType: MachineAxisTypes) -> MachineAxisInput
Creates a new MachineAxisInput object to be used to create a new MachineAxis. Set this object on to an axis type MachinePartInput to create a new MachineAxis with that part.
- **axisType** (MachineAxisTypes): The type of MachineAxisInput to create.
- **Returns** (MachineAxisInput): Returns a LinearMachineAxisInput or RotaryMachineAxisInput, or null if the creation failed.

### createSpindleInput() -> MachineSpindleInput
Creates a new MachineSpindleInput object to be used to create a new MachineSpindle.
- **Returns** (MachineSpindleInput): Returns new MachineSpindleInput object.

### createToolStationInput() -> MachineToolStationInput
Creates a new MachineToolStationInput object to be used to create a new MachineToolStation.
- **Returns** (MachineToolStationInput): Returns new MachineToolStationInput object.

## Properties

### axisInput : MachineAxisInput [read-write]
Gets or sets an axis input object to create a new MachineAxis with this part. Only valid when partType is Axis.

### id : string [read-write]
Gets or sets the internal ID of the part, used to reference this part for other operations. This ID can be any string. This must be unique with respect to other MachineParts in the Machine.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### partType : MachinePartTypes [read-only]
Get the type of part this input will create.

### spindleInput : MachineSpindleInput [read-write]
Gets or sets an spindle input object to create a new MachineSpindle with this part. Only valid when partType is not Axis.

### toolStationInput : MachineToolStationInput [read-write]
Gets or sets an tool station input object to create a new MachineToolStation with this part. Only valid when partType is not Axis.
