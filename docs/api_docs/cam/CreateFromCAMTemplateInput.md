# CreateFromCAMTemplateInput
Namespace: adsk.cam
Inherits: Base
Since: October 2023

Object that contains the settings used by createFromCAMTemplate.

**Accessed from:** CreateFromCAMTemplateInput.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create() -> CreateFromCAMTemplateInput
Creates an empty input object to be passed into createFromCAMTemplate
- **Returns** (CreateFromCAMTemplateInput): The newly created input object.

## Properties

### camTemplate : CAMTemplate [read-write]
Gets and sets the template to be instantiated.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### mode : AutomaticGenerationModes [read-write]
Gets and sets the mode to be used for generation. Defaults to Skip Generation.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Additive Manufacturing SLA API Sample**: Demonstrates how to automate the creation of an additive SLA manufacturing setup.


To run the sample script, have a design with one or more components open in Fusion’s DESIGN workspace. This script will switch the UI from the DESIGN workspace to the MANUFACTURE workspace, create a new Manufacturing Model, and create an Additive setup using that manufacturing model as an input.


The setup will select a SLA 3D printer from Fusion’s machine library and a print setting from the print setting library. All components in the Manufacturing model will be automatically oriented and arranged within the build area of the selected SLA machine. This script will also create support structures, based on the orientation of each component.


The support and orientation operations are created from a template. The script further demonstrates how to wrap script code into a command such that only one undo entry is created for the entire script instead of one entry per internal action.
