# Setup
Namespace: adsk.cam
Inherits: OperationBase
Since: January 2016

Object that represents an existing Setup.

**Accessed from:** CAMAdditiveContainer.parentSetup, CAMFolder.parentSetup, CAMHoleRecognition.parentSetup, CAMPattern.parentSetup, DocumentStockMaterialLibrary.setupsByStockMaterial, NCProgram.parentSetup, Operation.parentSetup, OperationBase.parentSetup, Setup.parentSetup, SetupChangeEventArgs.setup, SetupEventArgs.setup, Setups.add, Setups.item, Setups.itemByName, Setups.itemByOperationId

## Methods

### activate() -> boolean
Sets this object as the default container.
- **Returns** (boolean): Returns true if the activation was successful.

### additiveContainerByType(containerType: CAMAdditiveContainerTypes) -> CAMAdditiveContainer
Returns the additive container with the specified type.
- **Returns** (CAMAdditiveContainer): Returns the specified container or null in the case where there is no container with the specified type.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copyAfter(operation: OperationBase) -> boolean
Creates a duplicate of the operation in the tree after the given operation. Throws an exception if a not allowed copy operation is made for example copying a operation out of a setup.
- **operation** (OperationBase): Operation to copy targeted operation after.
- **Returns** (boolean): Returns if copy command was successful.

### copyBefore(operation: OperationBase) -> boolean
Creates a duplicate of the operation in the tree before the given operation. Throws an exception if a not allowed copy operation is made for example copying a operation out of a setup.
- **operation** (OperationBase): Operation to copy targeted operation before.
- **Returns** (boolean): Returns if copy command was successful.

### copyInto(container: OperationBase) -> boolean
Creates a duplicate of the operation into the given container. You can only copy into containers, such as setups or folders. Copied operation will be copied at the end of all operations already in the container. Throws an exception if a not allowed copy operation is made for example copying a setup into a setup.
- **container** (OperationBase): Container to copy targeted operation into.
- **Returns** (boolean): Returns if copy command was successful.

### createFromCAMTemplate(camTemplate: CAMTemplate) -> OperationBase
This function is retired. See more information in the 'Remarks' section below.

Create new operations, folders, or patterns from the specified CAMTemplate. They are added to the end of the parent setup.
- **camTemplate** (CAMTemplate): The CAMTemplate object to use to create the new operation, folder, or pattern.
- **Returns** (OperationBase): Returns an array containing all of the operations, folders and patterns created from the template.

### createFromCAMTemplate2(input: CreateFromCAMTemplateInput) -> OperationBase
Create new operations, folders, or patterns from the specified CAMTemplate. They are added to the end of the parent setup.
- **input** (CreateFromCAMTemplateInput): Input object that contains the template to create from and the generation mode.
- **Returns** (OperationBase): Returns an array containing all of the operations, folders and patterns created from the template.

### createFromTemplate(templateFilePath: string) -> ObjectCollection
This function is retired. See more information in the 'Remarks' section below.

Create and add operations, folders or patterns from the specified template file to the end of this setup.
- **templateFilePath** (string): The full path to the template file.
- **Returns** (ObjectCollection): Returns the collection containing all of the operations, folders and patterns created from the template file.

### createFromTemplateXML(templateXML: string) -> OperationBase
This function is retired. See more information in the 'Remarks' section below.

Create and add operations, folders or patterns from the specified template content XML to the end of this setup.
- **templateXML** (string): The full XML content of the template.
- **Returns** (OperationBase): Returns an array containing all of the operations, folders and patterns created from the template.

### deleteMe() -> boolean
Deletes the operation from the document. In case of a setup or folder, all containing child operations will be deleted as well. Note: Child classes may overwrite this function and throw an exception if the object cannot be deleted.
- **Returns** (boolean): Returns true if the delete was successful.

### duplicate() -> boolean
Creates a duplicate of the operation in the tree after the itself.
- **Returns** (boolean): Returns if duplicate command was successful.

### modifyUtility(utility: ModifyUtilityTypes) -> ModifyUtility
Get ModifyUtility for the current operation by given utility type.
- **utility** (ModifyUtilityTypes): Defines the specific ModifyUtility.
- **Returns** (ModifyUtility): Returns ModifyUtility for specific type or null if the type is not compatible with the operation.

### moveAfter(operation: OperationBase) -> boolean
Move operation in tree after the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup.
- **operation** (OperationBase): Operation to move targeted operation after.
- **Returns** (boolean): Returns if move operation was successful.

### moveBefore(operation: OperationBase) -> boolean
Move operation in tree before the given operation. Throws an exception if a not allowed move is made for example moving a operation out of a setup.
- **operation** (OperationBase): Operation to move targeted operation before.
- **Returns** (boolean): Returns if move operation was successful.

### moveInto(container: OperationBase) -> boolean
Move operation in tree into the given container. This only works with setups, patterns and folders. Moved operation will be moved at the end of all operations already in the container. Throws an exception if a not allowed move is made for example moving a setup into a setup.
- **container** (OperationBase): Container to move targeted operation into.
- **Returns** (boolean): Returns if move operation was successful.

## Properties

### allOperations : ObjectCollection [read-only]
Returns an ObjectCollection containing all of the operations in this setup. This includes all operations nested in folders and patterns.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this object.

### children : ChildOperationList [read-only]
Returns a collection containing all of the immediate (top level) child operations, folders and patterns in this setup, in the order they appear in the browser.

### error : string [read-only]
Returns a message corresponding to any active error associated with the value of this parameter.

### fixtureEnabled : boolean [read-write]
Set this value to enable the use of fixtures for this setup. To then set the fixture models themselves use the `fixtures` property.

### fixtures : ObjectCollection [read-write]
Gets and sets the fixtures associated with the setup, which are represented by an ObjectCollection of models, where a model can be an Occurrence, BRepBody, or MeshBody. To be able to set models as fixtures, the fixturesEnabled property has to be set first.

### folders : CAMFolders [read-only]
Returns the Folders collection that provides access to existing folders in this setup.

### generatedDataCollection : GeneratedDataCollection [read-only]
Get the generated data associated with a given operation base instance. The type of data depends on the strategy type and might not be available for all strategy types. The available types can be found in GeneratedData.cs

### hasError : boolean [read-only]
Gets if errors were encountered when generating the operation.

### hasWarning : boolean [read-only]
Gets if problems were encountered when generating the operation.

### isActive : boolean [read-only]
Gets if this setup is active.

### isLightBulbOn : boolean [read-write]
Gets if this operation is currently visible in the graphics window. Use the isLightBulbOn to change if the eye icon beside the operation node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children so this property does not indicate if the operation is actually visible, just that it should be visible if all of its parent nodes are also visible. Use the isVisible property to determine if it's actually visible.

### isOptional : boolean [read-write]
Gets and sets the "Optional" property value of the operation. Gets/sets true if the operation is optional.

### isProtected : boolean [read-write]
Gets and sets the "protected" property value of the operation. Gets/sets true if the operation is protected.

### isSelected : boolean [read-only]
Gets if this operation is selected in the 'Setups' browser.

### isSuppressed : boolean [read-write]
Gets and sets the "Suppressed" property value of the operation. Gets/sets true if the operation is suppressed.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-only]
Gets if this operation is currently visible in the graphics window. Use the isLightBulbOn to change if the eye icon beside the operation node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children. This property indicates the final result and whether this operation is actually visible or not.

### machine : Machine [read-write]
Gets and sets the Machine associated with the setup. The returned Machine is a transient copy, so the Machine needs to be set to the Setup again to apply any changes.

### models : ObjectCollection [read-write]
Gets and sets the input models associated with the setup. Passing in an empty ObjectCollection will remove all current inputs. Valid collection items are Occurrence, BRepBody, or MeshBody.

### name : string [read-write]
Gets and sets the name of the operation as seen in the browser. This name is unique as compared to the names of all other operations in the document.

### notes : string [read-write]
Gets and sets the notes of the operation.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### operationId : integer [read-only]
Returns the id of the operation. This id is unique as compared to the ids of all other operations in the document. This id will not change when changing the order or parent of the operation. This id will remain valid when the document is saved and reloaded.

### operations : Operations [read-only]
Returns the Operations collection that provides access to existing operations in this setup.

### operationType : OperationTypes [read-only]
Gets the Operation Type. It can be MillingOperation, TurningOperation, JetOperation or AdditiveOperation.

### parameters : CAMParameters [read-only]
Gets the CAMParameters collection for this operation.

### parentSetup : Setup [read-only]
Gets the Setup this operation belongs to.

### patterns : CAMPatterns [read-only]
Returns the Patterns collection that provides access to existing patterns in this setup.

### printSetting : PrintSetting [read-write]
Gets and sets the PrintSetting associated with the setup.

### stockMaterial : StockMaterial [read-write]
Gets/ and sets the Stock material associated with the setup.

### stockMode : SetupStockModes [read-write]
Gets and sets the bodies associated with the setup. Passing in an empty ObjectCollection will remove all current bodies. Valid input is MeshBody and/or BRepBody objects.

### stockSolids : ObjectCollection [read-write]
Gets and sets the stock solids associated with the setup, which are represented by an ObjectCollection of models, where a model can be an Occurrence, BRepBody, or MeshBody. StockMode has to be set to `SolidStock` otherwise this will throw an error.

### strategy : string [read-only]
Gets the name of the strategy associated with this operation.

### visibilityManager : SetupVisibilityManager [read-only]
Visibility manager for this setup.

### warning : string [read-only]
Returns a message corresponding to any active warning associated with the value of this parameter.

### workCoordinateSystem : Matrix3D [read-only]
Gets the Work Coordinate System associated with the setup as 4x4 matrix. From Matrix3D, Orientation and Origin data can be fetched.

## Samples
- **Additive Manufacturing MJF API Sample**: Demonstrates how to automate the creation of an additive MJF manufacturing setup and arrange components within the build volume of a 3D printer.


To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive Arrange using that manufacturing model as an input.


The setup will select an MJF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically arranged within the build volume of the selected MJF machine.
- **CAM Parameter Modification API Sample**: Demonstrates changing parameters of existing toolpaths.
- **Create Setups From Hole Recognition API Sample**: This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.
The Fusion Manufacturing Extension is required for Hole Recognition.
The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector.
- **Generate Setup Sheets API Sample**: Demonstrates generating the setup sheets for an existing toolpath..
- **Generate Toolpaths API Sample**: Demonstrates generating the toolpaths in the active document.
- **Hole and Pocket Recognition API Sample**: This sample script demonstrates three different methods for feature recognition: one for holes and two for pockets.
The script starts by creating a simple component which is then used to demonstrate the three methods. After the features are recognised they are coloured and milling and drilling operations are created for each feature.
RecognizedHoleGroup returns a list of BRepFaces that can be used as selections for the drilling operation. RecognizedPocket also return some BRepFaces but it needs additional processing before the output can be used for creating machining operations.
The sample script demonstrates a couple of different methods, including finding the pocket BRepFaces and creating sketches from the recognized pockets.
This script works only if the Manufacturing Extension is active.
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
- **Create CAM Operation From Template API Sample**: Demonstrates adding a new toolpath into the document using an existing CAM template. You can view the template here, although it will be loaded automatically. Run the sample script within any Fusion project containing at least one setup. A new facing operation will be created at the end of each setup discovered.
- **Post Toolpaths API Sample**: Demonstrates posting toolpaths in the active document.
- **Set Vise Origin As Setup WCS Origin API Sample**: This sample script demonstrates how to define our setup WCS origin relative to our vise origin from either a component, a sketch point or a joint origin.
The Work Coordinate System is a reference point set in our CAM workspace and on our machine. All machine coordinates are drawn from the WCS. This script demonstrates defining the WCS by each of 4 alternative methods:
Setup by default with no origin defined.
Setup using vise origin as WCS origin.
Setup using a sketch point as WCS origin.
Setup using a joint origin as WCS origin.
- **Turning Workflow API Sample**: Turning Workflow API Sample
This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
