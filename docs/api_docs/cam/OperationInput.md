# OperationInput
Namespace: adsk.cam
Inherits: Base
Since: April 2023

The OperationInput holds all necessary informations to create a new Operation. Can be added to the Operations instance for creation.

**Accessed from:** Operations.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### displayName : string [read-write]
Optionally specify the display name that appears in the browser-tree to override the default.

### generationMode : AutomaticGenerationModes [read-write]
Defines the automatic generation during the creation of the operation. Can be used to force or skip the generation of the new operation. By default the newly created operation will not be generated. The default value is SkipGeneration.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parameters : CAMParameters [read-only]
Get all parameters for the current strategy. Parameters are initialized by user defaults. Configure operation parameters before creation for a better performance.

### strategy : string [read-only]
Get the current strategy

### tool : Tool [read-write]
Optionally specify the tool used by the operation. The ToolLibraries allows the access to Local and Fusion tools. Setting the tool will overwrite tool parameters in the parameters property.

### toolPreset : ToolPreset [read-write]
Optionally specify the preset of the tool. If no preset is specified, the operation gets its default feed and speed. The Tool provides access to available presets. Use one of those presets to override the default. Setting the tool will overwrite a subset of tool parameters in the parameters property. An invalid preset will cause a failure during the creation of the operation.

## Samples
- **Hole and Pocket Recognition API Sample**: This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.
The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.
RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.
The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.
This script works only if the Manufacturing Extension is active.
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
- **Turning Workflow API Sample**: Turning Workflow API Sample
This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
