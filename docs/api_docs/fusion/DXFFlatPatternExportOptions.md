# DXFFlatPatternExportOptions
Namespace: adsk.fusion
Inherits: ExportOptions
Since: November 2022

Defines that a DXF export of a flat pattern is to be done and specifies the various options.

**Accessed from:** ExportManager.createDXFFlatPatternExportOptions

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### convertToPolylineTolerance : double [read-write]
Specifies the tolerance when converting a spline to polylines. This value is only used when the isSplineConvertedToPolyline property is true and otherwise it is ignored. The units for this value are centimeters. Defaults to 0.01 cm.

### filename : string [read-write]
Gets and sets the filename that the exported file will be written to. This can be empty in the case of STL export and sending the result to the mesh editor.

### geometry : Base [read-write]
Specifies the geometry to export. This can be an Occurrence, or the root Component. For STL, OBJ, and 3MF export, it can be a BRepBody. For DXF export, it can be a sketch of flat pattern.

### isCenterLinesExported : boolean [read-write]
Specifies if the center lines (bend line) of the flat pattern are exported in the DXF. Defaults to true.

### isExtentLinesExported : boolean [read-write]
Specifies if the bend extent lines of the flat pattern are exported in the DXF. Defaults to true.

### isSplineConvertedToPolyline : boolean [read-write]
Specifies if splines are converted to polylines. If true, the convertToPolylineTolerance value is used to specify the accuracy of the conversion. Defaults to false.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### units : DistanceUnits [read-write]
Gets and sets the units that will be used for the DXF file. This defaults to be the same as the default units of the design.
