# STLExportOptions
Namespace: adsk.fusion
Inherits: ExportOptions
Since: January 2015

Defines that a STL export is to be done and specifies the various options.

**Accessed from:** ExportManager.createSTLExportOptions

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### aspectRatio : double [read-write]
Gets and sets the minimum aspect ratio for that triangles that are generated for the mesh. Setting this property will automatically set the meshRefinement to MeshRefinementCustom. The default is the value associated with medium mesh refinement.

### availablePrintUtilities : array [read-only]
Returns a list of the known available print utilities. These strings can be used to set the PrintUtility property to specify which print utility to open the STL file in.

### filename : string [read-write]
Gets and sets the filename that the exported file will be written to. This can be empty in the case of STL export and sending the result to the mesh editor.

### geometry : Base [read-write]
Specifies the geometry to export. This can be an Occurrence, or the root Component. For STL, OBJ, and 3MF export, it can be a BRepBody. For DXF export, it can be a sketch of flat pattern.

### isBinaryFormat : boolean [read-write]
Indicates if the STL file is to be an ASCII or binary STL format. The default is true.

### isOneFilePerBody : boolean [read-write]
If the input is an Occurrence or the root Component, this specifies if a single file should be created containing all of the bodies within that occurrence or component or if multiple files should be created; one for each body. If multiple files are created, the body name is appended to the filename. The default is false.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maximumEdgeLength : double [read-write]
Gets and sets the maximum length of any mesh edge. This is defined in centimeter. Setting this property will automatically set the meshRefinement to MeshRefinementCustom. The default is the value associated with medium mesh refinement.

### meshRefinement : MeshRefinementSettings [read-write]
Gets and sets the current simple mesh refinement settings. Setting this property will reset the surfaceDeviation, normalDeviation, maximumEdgeLength, and aspectRatio to values that correspond to the specified mesh refinement. The default is MeshRefinementMedium.

### normalDeviation : double [read-write]
Gets and sets the current normal deviation, or the angle the mesh normals at the vertices can deviate from the actual surface normals. This is defined in radians. Setting this property will automatically set the meshRefinement to MeshRefinementCustom. The default is the value associated with medium mesh refinement.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### printUtility : string [read-write]
Specifies which print utility to use when opening the STL file if the sendToPrintUtility property is true. The value of this property can be one of the strings returned by the availalbePrintUtilities property, which will specify one of the know print utilities. You can also specify a custom print utility by specifying the full path to the print utility executable. The default value of this property is the last setting specified in the user-interface.

### sendToPrintUtility : boolean [read-write]
Gets and sets whether the created STL file will be sent to the print utility specified by the printUtility property. If this is false a filename must be defined.

### surfaceDeviation : double [read-write]
Gets and sets the current surface deviation, or the distance the mesh can deviate from the actual surface. This is defined in centimeter. Setting this property will automatically set the meshRefinement to MeshRefinementCustom. The default is the value associated with medium mesh refinement.

### unitType : DistanceUnits [read-write]
Gets and sets the units to use for the created STL file. When the STLExportOptions object is created, this property is initialized with the default units specified for the Design.

## Samples
- **Export to other formats API Sample**: Demonstrates exporting the active design to IGES, STEP, SAT, SMT, F3D and STL formats. To run this sample, have a design open and run the script. It will write out the translated files to a temp directory, which will it show in a message box.
- **STLExport API Sample**: Demonstrates how to export f3d to STL format.
