# NCProgramPostProcessOptions
Namespace: adsk.cam
Inherits: Base
Since: May 2023

The NCProgramPostProcessOptions provides settings to control the post processing of NC programs. It is needed for the NCPrograms.postProcess method for posting toolpaths and generating CNC files and setup sheets.

**Accessed from:** NCProgramPostProcessOptions.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create() -> NCProgramPostProcessOptions
Creates a new NCProgramPostProcessOptions object to be used as an input argument by the postProcess() method.
- **Returns** (NCProgramPostProcessOptions): Returns the newly created NCProgramPostProcessOptions object or null if the creation failed.

## Properties

### fusionHubExecutionBehavior : FusionHubExecutionBehaviors [read-write]
Gets and sets the post process behavior for exporting to Fusion Hub. Uses fusionHubExecutionBehavior_ExportWithRelationship by default.

### isFailOnToolNumberDuplication : boolean [read-write]
Toggles whether the post processing should abort if two tools with the same tool number have been detected. True by default. If true, an exception will be thrown if at least two tools map to the same tool number. If false, the post processor will not perform a tool change if the tool number is the same, which may mean that the wrong tool is used for an operation.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### postProcessExecutionBehavior : PostProcessExecutionBehaviors [read-write]
Gets and sets the post process behavior with regards to the operations' error or out of date states. Uses PostProcessExecutionBehavior_OmitInvalidAndEmptyOperations by default.

## Samples
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
