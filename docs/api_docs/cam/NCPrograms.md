# NCPrograms
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Container for all NC programs. Referenced from CAM product to access NC programs in a document, similar to what Setups is for all setup objects.

**Accessed from:** CAM.ncPrograms

## Methods

### add(input: NCProgramInput) -> NCProgram
Creates a new NC program.
- **input** (NCProgramInput): NCProgramInput which will be used to create the NC program.
- **Returns** (NCProgram): Returns the created NC program.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput() -> NCProgramInput
Create a new NCProgramInput object. Use properties and methods on this object to define the NC program you want to create and then use the Add method, passing in the NCProgramInput object.
- **Returns** (NCProgramInput): Returns a new NCProgramInput object.

### item(index: uinteger) -> NCProgram
Function that returns the specified NC program using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (NCProgram): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> NCProgram
Returns the NC program with the specified name.
- **name** (string): The name (as it appears in the browser) of the operation.
- **Returns** (NCProgram): Returns the specified NC program or null in the case where there is no NC program with the specified name. If there are multiple NC programs with the same name, the first item in the tree will be returned.

### itemByOperationId(id: integer) -> NCProgram
Returns the NC program with the specified operation id.
- **id** (integer): The id of the NC program.
- **Returns** (NCProgram): Returns the specified NC program or null in the case where there is no NC program with the specified operation id.

## Properties

### count : uinteger [read-only]
The number of items in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
- **Turning Workflow API Sample**: Turning Workflow API Sample
This sample script starts by opening a simple component which is then used to describe a basic turning workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
