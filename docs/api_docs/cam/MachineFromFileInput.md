# MachineFromFileInput
Namespace: adsk.cam
Inherits: MachineInput
Since: April 2023

Object used as input to create a machine from a local file. It is used by the Machine.create method. The object holds the data needed to create a machine from a local machine file.

**Accessed from:** MachineFromFileInput.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(filePath: string) -> MachineFromFileInput
Creates a MachineFromFileInput object to be used as input for Machine.create method.
- **filePath** (string): The path to a machine file to be processed. The filePath is expected to be an absolute path to the machine file on disk.
- **Returns** (MachineFromFileInput): The newly created "MachineFromFileInput" object in a valid state.

## Properties

### filePath : string [read-only]
The path to a file to act as a base for creating a machine from. The filePath is expected to be an absolute path to the local machine file.

### ignoreSimulationModel : boolean [read-write]
Whether or not to ignore the simulation model when creating/loading the machine. If set to true the simulation model will not be set on the new machine.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
