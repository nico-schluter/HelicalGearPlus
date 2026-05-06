# CAMTemplateOperationInput
Namespace: adsk.cam
Inherits: Base
Since: March 2025

A CAMTemplateOperationInput provides access to Operation Template parameters for editing, in much the same way as OperationInput provides access to Operation parameters for editing. Operation Template parameters are slightly different from Operation parameters, for instance in terms of how tools and geometry selections can be specified, so an OperationInput for a given strategy type has a slightly different set of parameters from a CAMTemplateOperationInput for that same strategy type.

**Accessed from:** CAMTemplateOperations.get, CAMTemplateOperations.makeInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### isGeometryIndexEnabled(index: integer)
Get whether a geometry index is selected.

### setGeometryIndexEnabled(index: integer, enabled: boolean)
Set whether a geometry index is selected.

## Properties

### displayName : string [read-write]
Optionally specify the display name that appears in the browser-tree to override the default.

### geometryIndexCount : integer [read-only]
Get the number of geometry indices that can be selected.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parameters : CAMParameters [read-only]
Get all parameters for the current strategy. Parameters are initialized by user defaults. Configure operation parameters before creation for a better performance.

### strategy : string [read-only]
Get the current strategy

### tool : Tool [read-write]
Optionally specify the tool used by the operation. The ToolLibraries allows the access to Local and Fusion tools.

### toolPreset : ToolPreset [read-write]
Optionally specify the preset of the tool. If no preset is specified, the operation gets its default feed and speed. The Tool provides access to available presets. Use one of those presets to override the default. An invalid preset will cause a failure during the creation of the operation.
