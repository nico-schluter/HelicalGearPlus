# MachineElements
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Collection of machine elements. These elements contain the properties that define the machine.

**Accessed from:** Machine.elements

## Methods

### addElement(input: MachineElementInput) -> MachineElement
Add a new machine element to the machine.
- **input** (MachineElementInput): A specialization of MachineElementInput class that contains the properties required to create a new machine element.
- **Returns** (MachineElement): The created MachineElement

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### countByType(typeId: string) -> uinteger
Number of elements of specified type.
- **typeId** (string): Element typeId to filter. See staticTypeId for the desired element type.
- **Returns** (uinteger): Returns the number of elements of the requested type. Returns zero if no elements match the specified type ID.

### createMachineElementInput(type: MachineElementInputType) -> MachineElementInput
Create a new MachineElementInput object for the specified type. This is intedned to be used to create/add new machine elements.
- **type** (MachineElementInputType): The type of machine element to create the input for
- **Returns** (MachineElementInput): A MachineElementInput object

### defaultItemByType(typeId: string) -> MachineElement
Returns the default item of the given type. In most cases this will be the element with an element ID of "default".
- **typeId** (string): Element typeId to get the default for. See staticTypeId for the desired element type.
- **Returns** (MachineElement): Returns the specified Element or null if no matching type ID is found.

### item(index: integer) -> MachineElement
Get the element at a particular index in the collection.
- **index** (integer): Index of element.
- **Returns** (MachineElement): Returns the element at the given index.

### itemById(typeId: string, elementId: string) -> MachineElement
Gets an element of a specific type by ID.
- **typeId** (string): Element typeId to filter. See staticTypeId for the desired element type.
- **elementId** (string): Element ID to select.
- **Returns** (MachineElement): Returns an element of the desired type with the specified ID or null in the case where no match is found.

### itemsByType(typeId: string) -> MachineElement
Gets the element of specified type.
- **typeId** (string): Element typeId to filter. See staticTypeId for the desired element type.
- **Returns** (MachineElement): Returns a list of elements filtered to the specified type or an empty array if there is no match with the specified typeId.

## Properties

### count : uinteger [read-only]
Total number of elements in collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Additive Manufacturing MJF API Sample**: Demonstrates how to automate the creation of an additive MJF manufacturing setup and arrange components within the build volume of a 3D printer.


To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive Arrange using that manufacturing model as an input.


The setup will select an MJF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically arranged within the build volume of the selected MJF machine.
