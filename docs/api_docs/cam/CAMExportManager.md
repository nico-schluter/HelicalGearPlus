# CAMExportManager
Namespace: adsk.cam
Inherits: Base
Since: November 2021

Export manager used to export the setup's models in one of the formats defined the ExportOptions objects. The export is currently restricted to additive setups only and the availability of the export option and its settings depends on the chosen machine.

**Accessed from:** CAM.exportManager

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create3MFOptions() -> CAM3MFExportOptions
Creates a new 3MF export option.
- **Returns** (CAM3MFExportOptions): Returns new CAM3MFExportOptions.

### createCAMAdditiveBuildExportOptions() -> CAMAdditiveBuildExportOptions
Creates a new export option based on the print setting's export formats. FFF and DED machines are not supported, their export files are generated using posts.
- **Returns** (CAMAdditiveBuildExportOptions): Returns new CAMAdditiveBuildExportOptions.

### execute(exportOptions: CAMExportOptions) -> boolean
Executes an export based on the export options.
- **exportOptions** (CAMExportOptions): The export options defining the export type and necessary meta data.
- **Returns** (boolean): Returns true if the export finished successfully.

### executeWithExportFuture(exportOptions: CAMExportOptions) -> CAMExportFuture
Executes an export based on the export options
- **exportOptions** (CAMExportOptions): The export options defining the export type and necessary meta data.
- **Returns** (CAMExportFuture): Returns a CAMExportFuture object if the export has started successfully.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
