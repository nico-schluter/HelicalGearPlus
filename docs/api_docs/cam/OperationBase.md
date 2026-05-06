# OperationBase
Namespace: adsk.cam
Inherits: Base
Since: January 2016

Base class object representing all operations, folders, patterns and setups.

**Accessed from:** CAMFolder.createFromCAMTemplate, CAMFolder.createFromCAMTemplate2, CAMFolder.createFromTemplateXML, CAMHoleRecognition.allOperations, CAMPattern.createFromCAMTemplate, CAMPattern.createFromCAMTemplate2, CAMPattern.createFromTemplateXML, NCProgram.filteredOperations, NCProgram.operations, NCProgramInput.operations, Operations.add, Setup.createFromCAMTemplate, Setup.createFromCAMTemplate2, Setup.createFromTemplateXML

## Methods

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

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this object.

### error : string [read-only]
Returns a message corresponding to any active error associated with the value of this parameter.

### generatedDataCollection : GeneratedDataCollection [read-only]
Get the generated data associated with a given operation base instance. The type of data depends on the strategy type and might not be available for all strategy types. The available types can be found in GeneratedData.cs

### hasError : boolean [read-only]
Gets if errors were encountered when generating the operation.

### hasWarning : boolean [read-only]
Gets if problems were encountered when generating the operation.

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

### name : string [read-write]
Gets and sets the name of the operation as seen in the browser. This name is unique as compared to the names of all other operations in the document.

### notes : string [read-write]
Gets and sets the notes of the operation.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### operationId : integer [read-only]
Returns the id of the operation. This id is unique as compared to the ids of all other operations in the document. This id will not change when changing the order or parent of the operation. This id will remain valid when the document is saved and reloaded.

### parameters : CAMParameters [read-only]
Gets the CAMParameters collection for this operation.

### parentSetup : Setup [read-only]
Gets the Setup this operation belongs to.

### strategy : string [read-only]
Gets the name of the strategy associated with this operation.

### warning : string [read-only]
Returns a message corresponding to any active warning associated with the value of this parameter.

## Samples
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
