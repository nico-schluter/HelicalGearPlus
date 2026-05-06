# NCProgramInput
Namespace: adsk.cam
Inherits: Base
Since: April 2023

The NCProgramInput holds all necessary information to create a new NC program. It is needed for the NCPrograms.add method to instantiate a new NC program.

**Accessed from:** NCPrograms.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### displayName : string [read-write]
Optionally specify the display name that appears in the browser-tree to override the default.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### operations : array [read-write]
Gets and sets the operations which will be included in the NC program. Valid input contains any number of operations, setups or folders. For setups and folders all child operations will be added. Operations will be post processed in setup order, with operations from the same setup grouped together. Setting the nc_program_orderByTool BooleanParameterValue on the parameters property to true will reorder operations across multiple setups to reduce the number of tool changes. When the list of operations is associated to one setup and the setup has defined its job_programName or job_programComment parameters, then those values are applied to the nc_program_name and nc_program_comment parameters accordingly.

### parameters : CAMParameters [read-only]
Get all parameters for the current NC program. Parameters are initialized by user defaults. Configure operation parameters before creation for a better performance.

## Samples
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
- **Turning Workflow API Sample**: Turning Workflow API Sample
This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
