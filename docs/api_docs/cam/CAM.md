# CAM
Namespace: adsk.cam
Inherits: Product
Since: January 2016

Object that represents the CAM environment of a Fusion document.

## Methods

### checkAllToolpaths() -> boolean
Checks if all the operations (includes those nested in sub-folders or patterns) in the document are valid and up to date.
- **Returns** (boolean): Returns true if the all operations are valid

### checkToolpath(operations: Base) -> boolean
Checks if the operations (including those nested in sub-folders or patterns) are valid and up to date.
- **operations** (Base): An Operation, Setup, Folder, or Pattern object. You can also use an ObjectCollection to specify multiple objects of any of the supported types.
- **Returns** (boolean): Returns true if the operations are valid

### checkValidity()
Checks whether the models used by the operations have changed in the mean time and invalidates the affected operations if needed. Should be used for cases where the automatic detection does not work yet, for instance when design changes are expected before a Manufacture API call. Also recommended at the beginning of a script or the beginning of an event handler.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### clearAllToolpaths() -> boolean
Clears all the toolpaths in the document, including those nested in sub-folders or patterns.
- **Returns** (boolean): Return true if successful.

### clearToolpath(operations: Base) -> boolean
Clears all the toolpaths for the specified objects, including those nested in sub-folders or patterns.
- **operations** (Base): An Operation, Setup, Folder, or Pattern object. You can also use and ObjectCollection to specify multiple objects of any combination of types.
- **Returns** (boolean): Return true if successful.

### deleteEntities(entities: ObjectCollection) -> boolean
Deletes the specified set of entities that are associated with this product.
- **entities** (ObjectCollection): An ObjectCollection containing the list of entities to delete.
- **Returns** (boolean): Returns True if any of the entities provided in the list were deleted. If entities were specified that can't be deleted or aren't owned by this product, they are ignored.

### export3MFForDefaultAdditiveSetup(filepath: string, addSimulationInfo: boolean, simPostProcess: boolean, simSplitSurrogates: boolean, simKeepThickeningStructure: boolean) -> boolean
This function is retired. See more information in the 'Remarks' section below.

This method is only valid for an additive setup and exports the default additive setup's models as a 3MF file. The 3MF also contains machine and support information.
- **addSimulationInfo** (boolean): This is an optional argument whose default value is False.
- **simPostProcess** (boolean): This is an optional argument whose default value is False.
- **simSplitSurrogates** (boolean): This is an optional argument whose default value is False.
- **simKeepThickeningStructure** (boolean): This is an optional argument whose default value is False.
- **Returns** (boolean): True on success, false on errors or wrong setup type

### findAttributes(groupName: string, attributeName: string) -> Attribute
Find attributes attached to objects in this product that match the group and or attribute name. This does not find attributes attached directly to the Product or Document objects but finds the attributes attached to entities within the product.

The search string for both the groupName and attributeName arguments can be either an absolute name value, or a regular expression. With an absolute name, the search string must match the entire groupName or attributeName, including case. An empty string will match everything. For example if you have an attribute group named "MyStuff" that contains the attribute "Length1", using the search string "MyStuff" as the group name and "Length1" as the attribute name will find the attributes with those names. Searching for "MyStuff" as the group name and "" as the attribute name will find all attributes that have "MyStuff" as the group name.

Regular expressions provide a more flexible way of searching. To use a regular expression, prefix the input string for the groupName or attributeName arguments with "re:". The regular expression much match the entire group or attribute name. For example if you have a group that contains attributes named "Length1", "Length2", "Width1", and "Width2" and want to find any of the length attributes you can use a regular expression using the string "re:Length.*". For more information on attributes see the Attributes topic in the user manual.
- **groupName** (string): The search string for the group name. See above for more details.
- **attributeName** (string): The search string for the attribute name. See above for more details.
- **Returns** (Attribute): An array of Attribute objects that were found. An empty array is returned if no attributes were found.

### generateAllSetupSheets(format: SetupSheetFormats, folder: string, openDocument: boolean) -> boolean
Generates all of the setup sheets for all of the operations in the document
- **format** (SetupSheetFormats): The document format for the setup sheet. Valid options are HTMLFormat and ExcelFormat. Limitation: "ExcelFormat" can be used in windows OS only.
- **folder** (string): The destination folder to locate the setup sheet documents in.
- **openDocument** (boolean): An option to allow to open the document instantly after the generation. By default, the document is opened.

This is an optional argument whose default value is True.
- **Returns** (boolean): Returns true if successful

### generateAllToolpaths(skipValid: boolean) -> GenerateToolpathFuture
Generates or regenerates all the operations in the document, including those nested in sub-folders or patterns.
- **skipValid** (boolean): Option to skip valid operations and only regenerate invalid operations.
- **Returns** (GenerateToolpathFuture): Return GenerateToolpathFuture that includes the status of operation generation.

### generateSetupSheet(operations: Base, format: SetupSheetFormats, folder: string, openDocument: boolean) -> boolean
Generate the setup sheets for the specified objects
- **operations** (Base): An Operation, Setup, Folder, or Pattern object. You can also use an ObjectCollection to specify multiple objects of any of the supported types.
- **format** (SetupSheetFormats): The document format for the setup sheet. Valid options are HTMLFormat and ExcelFormat. Limitation: "ExcelFormat" can be used in windows OS only.
- **folder** (string): The destination folder to locate the setup sheet documents in.
- **openDocument** (boolean): An option to allow to open the document instantly after the generation. By default, the document is opened.

This is an optional argument whose default value is True.
- **Returns** (boolean): Returns true if successful

### generateTemplateXML(operations: Base) -> string
Generates a template for the specified Operations, Setups, or Folders and returns the template as an XML string.
- **operations** (Base): An Operation, Setup or Folder object from which to generate the template. You can also specify a collection of any combination of these object types.
- **Returns** (string): Returns the template XML as a string.

### generateToolpath(operations: Base) -> GenerateToolpathFuture
Generates or regenerates all the specified objects, including those nested in sub-folders or patterns.
- **operations** (Base): An Operation, Setup, Folder, or Pattern object. You can also use an ObjectCollection to specify multiple objects of any of the supported types.
- **Returns** (GenerateToolpathFuture): Return GenerateToolpathFuture that includes the status of the operation generation.

### getMachiningTime(operations: Base, feedScale: double, rapidFeed: double, toolChangeTime: double) -> MachiningTime
Get the machining time for the specified objects.
- **operations** (Base): An Operation, Setup, Folder, or Pattern object. You can also use an ObjectCollection to specify multiple objects of any of the supported types.
- **feedScale** (double): The feed scale value (%) to use.
- **rapidFeed** (double): The rapid feed rate in centimeters per second.
- **toolChangeTime** (double): The tool change time in seconds.
- **Returns** (MachiningTime): Returns a MachiningTime object that has properties holding the calculation results.

### postProcess(operations: Base, input: PostProcessInput) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Post all of the toolpaths (including those nested in sub-folders or patterns) for the specified objects. If post processing fails, an error message can be retrieved from the error log explaining the reason for the failure.
- **operations** (Base): An Operation, Setup, Folder, or Pattern object. You can also use an ObjectCollection to specify multiple objects of any of the supported types.
- **input** (PostProcessInput): The PostProcessInput object that defines the post options and parameters.
- **Returns** (boolean): Returns true if successful

### postProcessAll(input: PostProcessInput) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Post all of the toolpaths (includes those nested in sub-folders or patterns) in the document. If post processing fails, an error message can be retrieved from the error log explaining the reason for the failure.
- **input** (PostProcessInput): The PostProcessInput object that defines the post options and parameters.
- **Returns** (boolean): Returns true if successful.

## Properties

### allMachines : array [read-only]
Gets an array containing all the machines in the document.

### allOperations : ObjectCollection [read-only]
Gets a collection containing all of the operations in the document. This includes all operations nested in folders and patterns.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this product.

### customGraphicsGroups : CustomGraphicsGroups [read-only]
Returns the customGraphicsGroups object associated with the CAM product.

### designRootOccurrence : Occurrence [read-only]
The CAM product has its own root component which has a single occurrence that references the Design root occurrence. This property returns this occurrence.

### documentStockMaterialLibrary : DocumentStockMaterialLibrary [read-only]
Gets the document StockMaterialLibrary. The StockMaterialLibrary contains all stock materials used by any setup inside the document. Changes to the original StockMaterialLibrary will not affect any setup because the document StockMaterialLibrary is an independent copy. You can only get a valid DocumentStockMaterialLibrary when you have access to Stock Materials private preview feature and enable the feature flag.

### documentToolLibrary : DocumentToolLibrary [read-only]
Gets the document ToolLibrary. The ToolLibrary contains all tools used by any operation inside the document. Changes to the original ToolLibrary will not affect any operation because the document ToolLibrary is an independent copy.

### exportManager : CAMExportManager [read-only]
Returns the Export Manager which provides access to the functionality to export in various formats.

### genericPostFolder : string [read-only]
Gets the installed post folder.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### manufacturingModels : ManufacturingModels [read-only]
Returns the collection of manufacturing models in the document.

### namedViews : NamedViews [read-only]
Returns the NamedViews object associated with this product. The NamedViews collection provides access to the named views defined in this product and supports the creation of new named views.

### ncPrograms : NCPrograms [read-only]
Returns the collection of NC programs in the document.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentDocument : Document [read-only]
Returns the parent Document object.

### personalPostFolder : string [read-only]
Gets the personal post folder.

### productType : string [read-only]
Returns the product type name of this product. A list of all of the possible product types can be obtained by using the Application.supportedProductTypes property.

### selectionSets : SelectionSets [read-only]
Returns the SelectionSets object associated with this product. If the product does not support selection sets, null is returned. The SelectionSets object is used to create and access existing selection sets.

### setups : Setups [read-only]
Returns the Setups collection that provides access to existing setups.

### temporaryFolder : string [read-only]
Gets the folder for temporary files.

### unitsManager : UnitsManager [read-only]
Returns the UnitsManager object associated with this product.

### workspaces : WorkspaceList [read-only]
Returns the workspaces associated with this product.

## Events

### setupActivated
The SetupActivated event fires when a setup is activated.

### setupActivating
The SetupActivating event fires before a setup is activated.

### setupChanged
The SetupChanged event fires when a setup is modified.

### setupCreated
The SetupCreated event fires when a new setup is created.

### setupDeactivated
The SetupDeactivated event fires when a setup is deactivated.

### setupDeactivating
The SetupDeactivating event fires before a setup is deactivated.

### setupDestroying
The setupDestroying event fires before a setup is destroyed.

## Samples
- **Generate Setup Sheets API Sample**: Demonstrates generating the setup sheets for an existing toolpath..
- **Generate Toolpaths API Sample**: Demonstrates generating the toolpaths in the active document.
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
- **Create CAM Operation From Template API Sample**: Demonstrates adding a new toolpath into the document using an existing CAM template. You can view the template here, although it will be loaded automatically. Run the sample script within any Fusion project containing at least one setup. A new facing operation will be created at the end of each setup discovered.
- **Post Toolpaths API Sample**: Demonstrates posting toolpaths in the active document.
- **Turning Workflow API Sample**: Turning Workflow API Sample
This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
