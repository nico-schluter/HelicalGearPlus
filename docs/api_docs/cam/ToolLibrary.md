# ToolLibrary
Namespace: adsk.cam
Inherits: Base
Since: April 2023

ToolLibrary represents a collection of Tool objects.

**Accessed from:** DocumentToolLibrary.createEmpty, DocumentToolLibrary.createFromJson, ToolLibraries.toolLibraryAtURL, ToolLibrary.createEmpty, ToolLibrary.createFromJson, ToolQueryResult.toolLibrary

## Methods

### add(tool: Tool) -> boolean
Inserts a Tool at the end of the ToolLibrary.
- **tool** (Tool): The Tool that should be added.
- **Returns** (boolean): Returns true for successful insertion, false otherwise

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createEmpty() -> ToolLibrary
Creates an empty ToolLibrary.
- **Returns** (ToolLibrary): Returns the newly created ToolLibrary.

### createFromJson(json: string) -> ToolLibrary
Creates a ToolLibrary by given JSON-string. Raises an error if the given JSON is invalid.
- **json** (string): The JSON contains all tools that should be added to the new ToolLibrary
- **Returns** (ToolLibrary): Returns the newly created ToolLibrary.

### createQuery() -> ToolQuery
Creates a new ToolQuery that is used to query the library for tools matching the query.
- **Returns** (ToolQuery): Returns a new ToolQuery. The query is predefined by given parameter.

### item(index: uinteger) -> Tool
Get Tool by index in ToolLibrary.
- **index** (uinteger): Index of the Tool in the ToolLibrary.
- **Returns** (Tool): Returns the Tool in the ToolLibrary by given index.

### remove(index: uinteger) -> boolean
Remove Tool by index from ToolLibrary.
- **index** (uinteger): Index of the Tool in the ToolLibrary that should be removed.
- **Returns** (boolean): Returns true for successful deletion, false otherwise

### toJson() -> string
Generate and return JSON string that contains all tools of that list.
- **Returns** (string): Returns JSON string that contains all tools of that list.

## Properties

### count : uinteger [read-only]
The number of tools in the ToolLibrary.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

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
