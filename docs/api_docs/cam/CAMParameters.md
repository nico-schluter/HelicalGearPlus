# CAMParameters
Namespace: adsk.cam
Inherits: Base
Since: September 2020

Collection that provides access to the parameters of an existing operation.

**Accessed from:** CAMAdditiveContainer.parameters, CAMFolder.parameters, CAMHoleRecognition.parameters, CAMPattern.parameters, CAMTemplateOperationInput.parameters, NCProgram.parameters, NCProgram.postParameters, NCProgramInput.parameters, Operation.parameters, OperationBase.parameters, OperationInput.parameters, PostProcessingMachineElement.postParameters, PrintSetting.parameters, PrintSettingItem.parameters, Setup.parameters, SetupInput.parameters, Tool.parameters, ToolPreset.parameters

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> CAMParameter
Function that returns the specified parameter using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (CAMParameter): Returns the specified item or null if an invalid index was specified.

### itemByName(internalName: string) -> CAMParameter
Returns the parameter of the specified id (internal name).
- **internalName** (string): The id (internal name) of the parameter.
- **Returns** (CAMParameter): Returns the specified parameter or null in the case where there is no parameter with the specified id.

### resetToSystemDefaults() -> boolean
Resets each parameter to its system default.
- **Returns** (boolean): Returns true if the reset was successful.

## Properties

### count : uinteger [read-only]
The number of items in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **CAM Parameter Modification API Sample**: Demonstrates changing parameters of existing toolpaths.
- **Create Setups From Hole Recognition API Sample**: This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.
The Fusion Manufacturing Extension is required for Hole Recognition.
The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector.
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
- **Turning Workflow API Sample**: Turning Workflow API Sample
This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
