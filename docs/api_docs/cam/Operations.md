# Operations
Namespace: adsk.cam
Inherits: Base
Since: January 2016

Collection that provides access to the individual operations within an existing setup, folder or pattern.

**Accessed from:** CAMFolder.operations, CAMHoleRecognition.operations, CAMPattern.operations, GenerateToolpathFuture.operations, Setup.operations

## Methods

### add(input: OperationInput) -> OperationBase
Create a new Operation.
- **input** (OperationInput): The OperationInput object defines the desired Operation. Use the createInput method to create a new OperationInput object and then use methods on it to define the Operation. The new Operation will be appended at the end of the current list of Operations. Throws an error if the strategy type is incompatible with the setup.
- **Returns** (OperationBase): Returns the newly created Operation.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(strategy: string) -> OperationInput
Creates a new OperationInput object, which is used to define the operation you want to create. Use properties and methods on the returned OperationInput object to define the desired operation and then pass it into the add method to create the operation.
- **strategy** (string): The name of the strategy type that you want to create. Use the compatibleStrategies property of Operations object to get a list of the names of the strategies.
- **Returns** (OperationInput): Returns a new OperationInput object or will fail if an invalid strategy is specified.

### item(index: uinteger) -> Operation
Function that returns the specified operation using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Operation): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> Operation
Returns the operation with the specified name (as appears in the browser).
- **name** (string): The name (as it appears in the browser) of the operation.
- **Returns** (Operation): Returns the specified operation or null in the case where there is no operation with the specified name.

### itemByOperationId(id: integer) -> Operation
Returns the operation with the specified operation id.
- **id** (integer): The id of the operation.
- **Returns** (Operation): Returns the specified operation or null in the case where there is no operation with the specified operation id.

## Properties

### compatibleStrategies : array [read-only]
Gets a list of the strategies that are compatible with the parent setup. This only returns strategies that are allowed to be added based on the active Setup or CAMFolder.

Note: There may be cases where a compatible strategy might not be allowed to be created due to licensing or other issues like disabled preview features.

### count : uinteger [read-only]
The number of items in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
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
- **Post Toolpaths API Sample**: Demonstrates posting toolpaths in the active document.
- **Turning Workflow API Sample**: Turning Workflow API Sample
This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
