# Tool
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Represents a Tool.

**Accessed from:** CAMTemplateOperationInput.tool, DocumentToolLibrary.item, DocumentToolLibrary.toolsBySetupOrFolder, Operation.tool, OperationInput.tool, Tool.createFromJson, Tool.createFromP21, ToolLibrary.item, ToolQueryResult.tool

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createFromJson(json: string) -> Tool
Creates a Tool object from given JSON string.
- **json** (string): The JSON should fully define the tool and contain all tool parameters. If the JSON contains more than one tool, only the first Tool is loaded.
- **Returns** (Tool): Returns the newly created Tool.

### createFromP21(p21: string) -> Tool
Creates a Tool object given a string containing a tool defined using the P21 format. Throws an error if the given string does not conform to the P21 format.
- **p21** (string): Creates a Tool object from the given P21 string.
- **Returns** (Tool): Returns the newly created Tool.

### toJson() -> string
Generates and returns a JSON string that contains a description of this tool.
- **Returns** (string): Returns a JSON string that contains a description of this tool.

## Properties

### description : string [read-only]
Gets the descriptive text about the tool. Includes various pieces of information depending on the tool type. Usually contains the tool number, data describing the tool geometry and the description. In the UI, the same information is displayed in the operation tree or in the tool library table.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parameters : CAMParameters [read-only]
Gets the CAMParameters collection associated with this tool. This defines all of the settings that describe the details of the tool.

### presets : ToolPresets [read-only]
Gets the ToolPresets collection associated with this tool.

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
