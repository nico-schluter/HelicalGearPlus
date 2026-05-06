# MaterialLibrary
Namespace: adsk.core
Inherits: Base
Since: August 2014

A material library.

**Accessed from:** MaterialLibraries.item, MaterialLibraries.itemById, MaterialLibraries.itemByName, MaterialLibraries.load

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### unload() -> boolean
Unloads this material from Fusion. Only non-native material libraries can be unloaded. You can determine this by checking the isNative property.
- **Returns** (boolean): Returns True if the library was successfully unloaded.

## Properties

### appearances : Appearances [read-only]
Returns the appearances defined within this library.

### id : string [read-only]
The unique internal ID of this Library.

### isNative : boolean [read-only]
Gets if this is a native material library. Native libraries are those that are delivered with Fusion and are always available. And non-native libraries are user created. If This returns True then there are some limitations to what can be done with the library. For example, if this is a native material library it cannot be unloaded.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### materials : Materials [read-only]
Returns the materials defined within this library.

### name : string [read-only]
Property that gets the name of this Library. This is the localized name shown in the user interface.

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
