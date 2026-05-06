# ToolPreset
Namespace: adsk.cam
Inherits: Base
Since: April 2023

A Preset defines the material specific properties of a Tool.

**Accessed from:** CAMTemplateOperationInput.toolPreset, Operation.toolPreset, OperationInput.toolPreset, ToolPresets.add, ToolPresets.item, ToolPresets.itemsByName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### id : string [read-write]
Gets and sets the identifier of that Preset. The id can be used to select a Preset for a Operation.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets and sets the name of that Preset.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parameters : CAMParameters [read-only]
Gets the CAMParameters collection for this Preset.

## Samples
- **Manufacturing Workflow API Sample**: Manufacturing Workflow API Sample
This sample script starts by creating a simple component which is then used to describe a milling workflow. It creates a setup, a few operations, pick some tools from a Fusion sample tool library using loops and queries and ends up post-processing the operations out using an NC Program.
