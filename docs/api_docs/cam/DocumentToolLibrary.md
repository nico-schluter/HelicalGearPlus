# DocumentToolLibrary
Namespace: adsk.cam
Inherits: ToolLibrary
Since: April 2023

DocumentToolLibrary provides access to tools used by the document. It supports adding, updating and deleting tools in the document tool library.

**Accessed from:** CAM.documentToolLibrary

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

### operationsByTool(tool: Tool) -> Operation
Returns all operations that use the given tool. The tool must exist in the document tool library. Raises an error if the tool is not in the document.
- **tool** (Tool): The tool to search for in operations. The tool must exist in the document.
- **Returns** (Operation): Returns operations using a specific tool.

### remove(index: uinteger) -> boolean
Remove Tool by index from ToolLibrary.
- **index** (uinteger): Index of the Tool in the ToolLibrary that should be removed.
- **Returns** (boolean): Returns true for successful deletion, false otherwise

### toJson() -> string
Generate and return JSON string that contains all tools of that list.
- **Returns** (string): Returns JSON string that contains all tools of that list.

### toolsBySetupOrFolder(setupOrFolder: OperationBase) -> Tool
Returns all tools used in a given setup or folder. Given setup or folder must belong to the document of the DocumentToolLibrary. Raises an error if given operation is not in the document.
- **setupOrFolder** (OperationBase): The setup or folder to get tools from. Must belong to the document.
- **Returns** (Tool): Returns tools used by a specific setup or folder.

### update(tool: Tool, updateFeedAndSpeed: boolean) -> boolean
Update the given tool in the document tool library. The update applies all changes to the tool in the document tool library and therefore on all operations that use the tool. Will error if the tool does not exist in the document tool library.
- **tool** (Tool): The tool that should be updated.
- **updateFeedAndSpeed** (boolean): Setting updateFeedAndSpeed to true will override the feed and speed parameters of operations within the document which use the given tool.
- **Returns** (boolean): Returns true if the update was successful.

## Properties

### count : uinteger [read-only]
The number of tools in the ToolLibrary.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
