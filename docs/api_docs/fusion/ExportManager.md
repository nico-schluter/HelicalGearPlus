# ExportManager
Namespace: adsk.fusion
Inherits: Base
Since: January 2015

Provides support for exporting model data to various formats.

**Accessed from:** Design.exportManager, FlatPatternProduct.exportManager, WorkingModel.exportManager

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createC3MFExportOptions(geometry: Base, filename: string) -> C3MFExportOptions
Creates a C3MFExportOptions object that's used to export a design in 3MF format. Creation of the C3MFExportOptions object does not perform the export. You must pass this object to the ExportManager.execute method to perform the export.
- **geometry** (Base): The geometry to export. This can be a BRepBody, Occurrence, or Component object.
- **filename** (string): The filename of the 3MF file to be created. This is optional and can be left out if the mesh will be opened in a mesh editor.

This is an optional argument whose default value is "".
- **Returns** (C3MFExportOptions): The created createC3MFExportOptions object or null if the creation failed.

### createDXFFlatPatternExportOptions(filename: string, flatPattern: FlatPattern) -> DXFFlatPatternExportOptions
Creates a DXFFlatPatternExport object that's used to export a flat pattern in DXF format. Creation of the DXFFlatPatternExport object does not perform the export. You must call the execute method. You can change any additional settings by setting properties on the returned object before calling the execute method.
- **filename** (string): The filename of the DXF file to be created.
- **flatPattern** (FlatPattern): The FlatPattern object to export.
- **Returns** (DXFFlatPatternExportOptions): The created DXFFlatPatternExport object or null if the creation failed.

### createDXFSketchExportOptions(filename: string, sketch: Sketch) -> DXFSketchExportOptions
Creates a DXFSketchExportOptions object that's used to export a sketch in DXF format. Creation of the DXFSketchExportOptions object does not perform the export. You must call the execute method after changing the settings to the desired values.
- **filename** (string): The filename of the DXF file to be created.
- **sketch** (Sketch): The Sketch object to export.
- **Returns** (DXFSketchExportOptions): The created DXFSketchExportOptions object or null if the creation failed.

### createFusionArchiveExportOptions(filename: string, geometry: Base) -> FusionArchiveExportOptions
Creates an FusionArchiveExportOptions object that's used to export a design in Fusion archive format. Creation of the FusionArchiveExportOptions object does not perform the export. You must pass this object to the ExportManager.execute method to perform the export. The FusionArchiveExportOptions supports any available options when exporting to Fusion archive format.
- **filename** (string): The filename of the Fusion archive file to be created.
- **geometry** (Base): The geometry to export. Valid geometry for this is currently a Component object. This argument is optional and if not specified, it results in the root component and it entire contents being exported.

This is an optional argument whose default value is null.
- **Returns** (FusionArchiveExportOptions): The created FusionArchiveExportOptions object or null if the creation failed.

### createIGESExportOptions(filename: string, geometry: Base) -> IGESExportOptions
Creates an IGESExportOptions object that's used to export a design in IGES format. Creation of the IGESExportOptions object does not perform the export. You must pass this object to the ExportManager.execute method to perform the export. The IGESExportOptions supports any available options when exporting to IGES format.
- **filename** (string): The filename of the IGES file to be created.
- **geometry** (Base): The geometry to export. Valid geometry for this is currently a Component object. This argument is optional and if not specified, it results in the root component and it entire contents being exported.

This is an optional argument whose default value is null.
- **Returns** (IGESExportOptions): The created IGESExportOptions object or null if the creation failed.

### createOBJExportOptions(geometry: Base, filename: string) -> OBJExportOptions
Creates an OBJExportOptions object that's used to export a design in OBJ format. Creation of the OBJExportOptions object does not perform the export. You must pass this object to the ExportManager.execute method to perform the export.
- **geometry** (Base): The geometry to export. This can be a BRepBody, Occurrence, or Component object.
- **filename** (string): The filename of the OBJ file to be created. This is optional and can be left out if the mesh will be opened in a mesh editor.

This is an optional argument whose default value is "".
- **Returns** (OBJExportOptions): The created createOBJExportOptions object or null if the creation failed.

### createSATExportOptions(filename: string, geometry: Base) -> SATExportOptions
Creates an SATExportOptions object that's used to export a design in SAT format. Creation of the SATExportOptions object does not perform the export. You must pass this object to the ExportManager.execute method to perform the export. The SATExportOptions supports any available options when exporting to SAT format.
- **filename** (string): The filename of the SAT file to be created.
- **geometry** (Base): The geometry to export. Valid geometry for this is currently a Component object. This argument is optional and if not specified, it results in the root component and it entire contents being exported.

This is an optional argument whose default value is null.
- **Returns** (SATExportOptions): The created SATExportOptions object or null if the creation failed.

### createSMTExportOptions(filename: string, geometry: Base) -> SMTExportOptions
Creates an SMTExportOptions object that's used to export a design in SMT format. Creation of the SMTExportOptions object does not perform the export. You must pass this object to the ExportManager.execute method to perform the export. The SMTExportOptions supports any available options when exporting to SMT format.
- **filename** (string): The filename of the SMT file to be created.
- **geometry** (Base): The geometry to export. Valid geometry for this is currently a Component object. This argument is optional and if not specified, it results in the root component and it entire contents being exported.

This is an optional argument whose default value is null.
- **Returns** (SMTExportOptions): The created SMTExportOptions object or null if the creation failed.

### createSTEPExportOptions(filename: string, geometry: Base) -> STEPExportOptions
Creates an STEPExportOptions object that's used to export a design in STEP format. Creation of the STEPExportOptions object does not perform the export. You must pass this object to the ExportManager.execute method to perform the export. The STEPExportOptions supports any available options when exporting to STEP format.
- **filename** (string): The filename of the STEP file to be created.
- **geometry** (Base): The geometry to export. Valid geometry for this is currently a Component object. This argument is optional and if not specified, it results in the root component and it entire contents being exported.

This is an optional argument whose default value is null.
- **Returns** (STEPExportOptions): The created STEPExportOptions object or null if the creation failed.

### createSTLExportOptions(geometry: Base, filename: string) -> STLExportOptions
Creates an STLExportOptions object that's used to export a design in STL format. Creation of the STLExportOptions object does not perform the export. You must pass this object to the ExportManager.execute method to perform the export.
- **geometry** (Base): The geometry to export. This can be a BRepBody, Occurrence, or Component object.
- **filename** (string): The filename of the STL file to be created. This is optional and can be left out if the mesh will be opened in a mesh editor.

This is an optional argument whose default value is "".
- **Returns** (STLExportOptions): The created createSTLExportOptions object or null if the creation failed.

### createUSDExportOptions(filename: string, geometry: Base) -> USDExportOptions
Creates an USDExportOptions object that's used to export a design in USD format. Creation of the USDExportOptions object does not perform the export. You must pass this object to the ExportManager.execute method to perform the export. The USDExportOptions supports any available options when exporting to USD format.
- **filename** (string): The filename of the USD file to be created.
- **geometry** (Base): The geometry to export. Valid geometry for this is currently a Component object. This argument is optional and if not specified, it results in the root component and it entire contents being exported.

This is an optional argument whose default value is null.
- **Returns** (USDExportOptions): The created USDExportOptions object or null if the creation failed.

### execute(exportOptions: ExportOptions) -> boolean
Executes the export operation to create the file in the format specified by the provided ExportOptions object.
- **exportOptions** (ExportOptions): An ExportOptions object that is created using one of the create methods on the ExportManager object. This defines the type of file and any available options supported for that file type.
- **Returns** (boolean): Returns true if the export was successful.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **ExportManager API Sample**: Demonstrates how to export f3d to different formats.
- **Export to other formats API Sample**: Demonstrates exporting the active design to IGES, STEP, SAT, SMT, F3D and STL formats. To run this sample, have a design open and run the script. It will write out the translated files to a temp directory, which will it show in a message box.
- **Set parameters from a csv file and export to STEP**: Reads data from a .csv file and sets user parameters in the model and then exports the model to STEP. When setting parameters be aware that this sample is setting user parameters. It's also possible to set model parameters but that's not demonstrated here. Also when accessing parameters, it is case sensitive so the names you use in your program much exactly match the names in the model.
- **STLExport API Sample**: Demonstrates how to export f3d to STL format.
