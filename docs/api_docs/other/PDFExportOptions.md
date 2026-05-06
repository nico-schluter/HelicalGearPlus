# PDFExportOptions
Namespace: adsk.drawing
Inherits: DrawingExportOptions
Since: December 2020

Defines the inputs needed to export the drawing as PDF.

**Accessed from:** DrawingExportManager.createPDFExportOptions

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### filename : string [read-write]
Gets and sets the filename that the exported file will be written to.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### openPDF : boolean [read-write]
Specifies that the PDF file will be opened after export.

### sheetRange : string [read-write]
Defines the range of sheets to export. This can be a string like "1-3" or "1-2,5" where you can define a range of sheets and also specific sheets. Setting this property will automatically set the sheetsToExport setting to SelectedPDFSheets.

### sheetsToExport : PDFSheetsExport [read-write]
Defines which sheets to export. Defaults to AllPDFSheets which will create a single PDF file containing all sheets in the drawing.

the SelectedPDFSheets and CurrentPDFSheet options are dependent on the current selections in the user interface.

To set this to RangePDFSheets, use the sheetRange property to define the range of sheets to print.

### useLineWeights : boolean [read-write]
Specifies if line weights should be used in the exported PDF file.
