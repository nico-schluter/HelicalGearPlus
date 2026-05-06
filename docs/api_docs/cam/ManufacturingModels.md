# ManufacturingModels
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Referenced from CAM product to access manufacturing models in document.

**Accessed from:** CAM.manufacturingModels

## Methods

### add(input: ManufacturingModelInput) -> ManufacturingModel
Create a new ManufacturingModel.
- **input** (ManufacturingModelInput): A ManufacturingModelInput object that defines the desired ManufacturingModel. Use the createInput method to create a new ManufacturingModelInput object and then use methods on it to define the ManufacturingModel.
- **Returns** (ManufacturingModel): Returns the newly created ManufacturingModel.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput() -> ManufacturingModelInput
Create a new ManufacturingModelInput object. Use properties and methods on this object to define the ManufacturingModel you want to create and then use the Add method, passing in the ManufacturingModelInput object.
- **Returns** (ManufacturingModelInput): Returns new ManufacturingModelInput object.

### item(index: uinteger) -> ManufacturingModel
Get ManufacturingModel by index in collection.
- **Returns** (ManufacturingModel): Returns ManufacturingModel at given index.

### itemById(id: string) -> ManufacturingModel
Returns ManufacturingModel with given id.
- **id** (string): The id of the ManufacturingModel.
- **Returns** (ManufacturingModel): Returns ManufacturingModel with the specified id or null if no ManufacturingModel has that id.

### itemByName(name: string) -> ManufacturingModel
Returns all ManufacturingModel with given name (as appears in the browser).
- **name** (string): The name (as it appears in the browser) of the ManufacturingModel.
- **Returns** (ManufacturingModel): Returns all ManufacturingModel with the specified name.

### syncAllManufacturingModels() -> boolean
Checks wether changes to the original design have been made. If so, all manufacturing models are synchronized with their sources.
- **Returns** (boolean): Returns true if any manufacturing model needed an update.

## Properties

### count : uinteger [read-only]
The number of items in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Additive Manufacturing FFF API Sample**: Demonstrates how to automate the creation of an additive FFF manufacturing setup and generate a toolpath.


To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive setup using that manufacturing model as an input.


The setup will select an FFF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically oriented and arranged within the build area of the selected FFF machine. This script will also create support structures, if required, based on the orientation of each component. Finally, the script generates the toolpath for the active setup and lets the user choose if they wish to post process the resulting toolpath or if they want to simulate it.
- **Additive Manufacturing MJF API Sample**: Demonstrates how to automate the creation of an additive MJF manufacturing setup and arrange components within the build volume of a 3D printer.


To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive Arrange using that manufacturing model as an input.


The setup will select an MJF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically arranged within the build volume of the selected MJF machine.
- **Additive Manufacturing SLA API Sample**: Demonstrates how to automate the creation of an additive SLA manufacturing setup.


To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive setup using that manufacturing model as an input.


The setup will select a SLA 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically oriented and arranged within the build area of the selected SLA machine. This script will also create support structures, based on the orientation of each component.


The support and orientation operations are created from a template. The script further demonstrates how to wrap script code into a command such that only one undo entry is created for the entire script instead of one entry per internal action.
