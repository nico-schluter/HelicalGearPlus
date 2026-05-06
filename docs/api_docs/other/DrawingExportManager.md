# DrawingExportManager
Namespace: adsk.drawing
Inherits: Base
Since: December 2020

Provides support to export the drawing in various formats.

**Accessed from:** Drawing.exportManager

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createPDFExportOptions(filename: string) -> PDFExportOptions
Defines the various settings for a STEP export.
- **filename** (string): The name of the file to export to. Use settings on the returned PDFExportOptions object to change other settings.
- **Returns** (PDFExportOptions): Returns a PDFExportOptions object if successful and null if it should fail.

### execute(exportOptions: DrawingExportOptions) -> boolean
Executes the export operation to create the file in the format specified by the input ExportOptions object.
- **exportOptions** (DrawingExportOptions): A DrawingExportOptions object that is created using one of the create methods on the DrawingExportManager object. This defines the type of export and defines the options supported for that file type.
- **Returns** (boolean): Returns true if the export was successful.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
