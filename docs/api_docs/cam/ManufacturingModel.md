# ManufacturingModel
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Represents a ManufacturingModel within a CAM design. A Manufacturing Model is a derive of the Design scene, which can be augmented without any effects of the original Design.

**Accessed from:** ManufacturingModel.duplicate, ManufacturingModels.add, ManufacturingModels.item, ManufacturingModels.itemById, ManufacturingModels.itemByName

## Methods

### activate() -> boolean
Makes the ManufacturingModel the active edit target in the user interface. This is the same as enabling the radio button next to the occurrence in the browser.
- **Returns** (boolean): Returns true if the activation was successful.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this ManufacturingModel. If this is part of a setup, the reference to this will be lost. The deletion makes that reference invalid.
- **Returns** (boolean): Returns true if the delete is successful.

### duplicate() -> ManufacturingModel
Creates and returns a copy of the ManufacturingModel, within its parent collection. The newly created ManufacturingModel will have a new unique name assigned.
- **Returns** (ManufacturingModel): Returns the newly created ManufacturingModel copy.

### syncManufacturingModel() -> boolean
Checks whether changes to the original design have been made. If so, the given manufacturing model is synchronized with its source.
- **Returns** (boolean): Returns true if the manufacturing model needed an update.

## Properties

### id : string [read-only]
Gets the unique identifier of the ManufacturingModel within the document.

### isActive : boolean [read-only]
Gets whether this ManufacturingModel is active in the user interface. This is the same as checking the state of the radio button next to the ManufacturingModel in the browser. To activate the ManufacturingModel use the Activate method.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets or sets the display name of the ManufacturingModel. This is the name that will be shown in the browser and other locations.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### occurrence : Occurrence [read-only]
Returns the occurrence for that ManufacturingModel.

## Samples
- **Additive Manufacturing MJF API Sample**: Demonstrates how to automate the creation of an additive MJF manufacturing setup and arrange components within the build volume of a 3D printer.


To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive Arrange using that manufacturing model as an input.


The setup will select an MJF 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically arranged within the build volume of the selected MJF machine.
