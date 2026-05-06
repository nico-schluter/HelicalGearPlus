# Appearances
Namespace: adsk.core
Inherits: Base
Since: August 2014

A collection of appearances.

**Accessed from:** Design.appearances, FlatPatternProduct.appearances, MaterialLibrary.appearances, WorkingModel.appearances

## Methods

### addByCopy(appearanceToCopy: Appearance, name: string) -> Appearance
Add an Appearance to a Design by copying an existing Appearance from Favorites, a Library or from the appearances stored in the Design. This method currently only applies to the Appearances collection from a Design and cannot be used to copy an Appearance to a library.
- **appearanceToCopy** (Appearance): The Appearance you want to copy. The Appearance to copy can be from Favorites, a Library or from the appearances stored in the Design.
- **name** (string): The Appearance name to apply to the copy.
- **Returns** (Appearance): Returns the newly created Appearance or null if the copy operation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: integer) -> Appearance
Returns the specified Appearance using an index into the collection.
- **index** (integer): The index of the appearance to return where the first item in the collection is 0.
- **Returns** (Appearance): Returns the specified appearance or null if an invalid index is specified.

### itemById(id: string) -> Appearance
Returns the Appearance by it's internal unique ID.
- **id** (string): The ID of the appearance to return.
- **Returns** (Appearance): Returns the specified appearance or null if there isn't a matching ID.

### itemByName(name: string) -> Appearance
Returns the specified Appearance using the name as seen in the user interface. This often isn't a reliable way of accessing a specific appearance because appearances are not required to be unique.
- **name** (string): The name of the appearance to return,.
- **Returns** (Appearance): Returns the specified appearance or null if there isn't a matching name.

## Properties

### count : uinteger [read-only]
The number of Materials in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Avoid Machine Surface Settings API Sample**: This sample script demonstrates how to use Machine/Avoid/Gouge/Fixture functionality.
The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a curved surface with a through slot, a countersunk hole and a raised, circular and filleted upstand from the surface. The model is supported by two rectangular blocks, themselves mounted on a fixture plate. A setup is included with a single operation running a 3-axis diagonal raster over the model, supports and fixture. The operation machines the fixture, the supporting blocks, the upper surface of the upstand and the area within the slot and hole, something we would like to avoid.
The script duplicates the original operation and then proceeds to create a series of MachineAvoidGroups. These are labelled as either Machine in the case of 2 cap surfaces for the slot and hole, Fixture for the fixture plate, Gouge for the supporting blocks and Avoid for the top face of the upstand. Additionally, both AxialOffset and RadialOffset can be specified for the Machine, Avoid and Fixture passes.
- **Create Engravings Selection Sets API Sample**: This sample script demonstrates how to find and machine engravings in the Z+ direction using pocket recognition.
The script will first open an example model via its URN. Using pocket recognition, it will identify pockets that may be engravings based on their dimensions.
We assume here that an engraving pocket is:Made with a flat bottom face and no fillet.A closed pocket.Have a Z height less than 2 mm
We demonstrate creating selection sets in both design and manufacture workspaces and use one of the selection sets as an operation geometry selection input to generate an engraving operation.
The engraving toolpath can be seen by expanding the setup and selecting the operation.
- **Material API Sample**: Demonstrates using materials and appearance using the API.

To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. The sample also used an external appearance library which you can get here. Copy that to any location on your computer and edit the path in the script. When running the script, have a design open that contains a body in the root component.
