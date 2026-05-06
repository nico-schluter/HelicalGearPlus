# MachineFromLibraryInput
Namespace: adsk.cam
Inherits: MachineInput
Since: April 2023

Object used as input to create a machine from library URL. Used by "Machine.create(MachineInput)" method. The object holds the data needed to create a machine from the specified library URL

**Accessed from:** MachineFromLibraryInput.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(url: URL) -> MachineFromLibraryInput
Creates a MachineFromLibraryInput object to be used as input for Machine.create method, in order to create a machine from a library location.
- **url** (URL): The URL path to the library machine.
- **Returns** (MachineFromLibraryInput): Returns newly created MachineFromLibraryInput object in a valid state.

## Properties

### ignoreSimulationModel : boolean [read-write]
Gets and sets whether or not to ignore the simulation model when creating or loading the machine. If set to true the simulation model will not be set on the new machine.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### url : URL [read-only]
The URL path to the library machine.
