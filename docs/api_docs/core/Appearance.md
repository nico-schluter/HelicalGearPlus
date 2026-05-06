# Appearance
Namespace: adsk.core
Inherits: Base
Since: August 2014

An appearance.

**Accessed from:** Appearances.addByCopy, Appearances.item, Appearances.itemById, Appearances.itemByName, BRepBody.appearance, BRepFace.appearance, ConfigurationAppearanceCell.appearance, CustomGraphicsAppearanceColorEffect.appearance, FavoriteAppearances.add, FavoriteAppearances.item, FavoriteAppearances.itemById, FavoriteAppearances.itemByName, Material.appearance, MaterialPreferences.appearanceOverride, MeshBody.appearance, Occurrence.appearance

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copyTo(target: Base) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Copies this appearance to the specified target.
- **target** (Base): The target can be a Design or FavoriteAppearances object.
- **Returns** (boolean): Returns true if the copy was successful.

### deleteMe() -> boolean
Deletes the Appearance from the Design. This method is only valid for appearances that are in a Design and are unused.
- **Returns** (boolean): Returns true if the delete was successful.

## Properties

### appearanceProperties : Properties [read-only]
returns the collection of Properties that define this appearance

### hasTexture : boolean [read-only]
Property that indicates if this appearance has a texture associated with it.

### id : string [read-only]
The unique internal ID of this Appearance.

### isUsed : boolean [read-only]
Returns true if this Appearance is used in the Design.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Returns the name of this Appearance. This is the localized name shown in the UI.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Property that returns the Parent object of this Appearance (a MaterialLibrary, Design, or AppearanceFavorites collection).

### usedBy : ObjectCollection [read-only]
Returns a collection of the entities currently using this appearance. This property is only valid for an appearance in a Design and where the IsUsed property returns true. The collection returned can contain

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
