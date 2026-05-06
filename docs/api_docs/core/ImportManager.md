# ImportManager
Namespace: adsk.core
Inherits: Base
Since: September 2015

Provides access to functionality to support importing various modeling formats into Fusion.

**Accessed from:** Application.importManager

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createDXF2DImportOptions(filename: string, planarEntity: Base) -> DXF2DImportOptions
Creates a DXF2DImportOptions object that is used to import 2D data to create sketches. Creation of the createDXF2DImportOptions object does not perform the import. You must pass this object to the ImportManager.importToTarget method to perform the import. The sketches created as a result of the import are available through the 'results' property of the DXF2DImportOptions.
- **filename** (string): The filename of the DXF file to be imported.
- **planarEntity** (Base): The construction plane or planar face that defines the plane that the resulting sketches will be created on.
- **Returns** (DXF2DImportOptions): The created DXF2DImportOptions object or null if the creation failed.

### createFusionArchiveImportOptions(filename: string) -> FusionArchiveImportOptions
Creates a FusionArchiveImportOptions object that imports a design from a Fusion archive format. The creation of the FusionArchiveImportOptions object does not perform the import. You must pass this object to one of the ImportManager import methods to perform the import. The FusionArchiveImportOptions object supports the available options when importing from a Fusion archive format. This method only supports f3d files. For f3z files, you should use the DataFolder.uploadFile method.
- **filename** (string): The filename or URL of the Fusion archive file to be imported. Only f3d files can be imported. For f3z files, you should use the DataFolder.uploadFile method.
- **Returns** (FusionArchiveImportOptions): The created FusionArchiveImportOptions object or null if the creation failed.

### createIGESImportOptions(filename: string) -> IGESImportOptions
Creates an IGESImportOptions object that is used to import a design from IGES format. Creation of the IGESImportOptions object does not perform the import. You must pass this object to one of the ImportManager import methods to perform the import. The IGESImportOptions supports any available options when importing from IGES format.
- **filename** (string): The filename or URL of the IGES file to be imported.
- **Returns** (IGESImportOptions): The created IGESImportOptions object or null if the creation failed.

### createSATImportOptions(filename: string) -> SATImportOptions
Creates an SATImportOptions object that's used to import a design from SAT format. Creation of the SATImportOptions object does not perform the import. You must pass this object to one of the ImportManager import methods to perform the import. The SATImportOptions supports any available options when importing from SAT format.
- **filename** (string): The filename or URL of the SAT file to be imported.
- **Returns** (SATImportOptions): The created SATImportOptions object or null if the creation failed.

### createSMTImportOptions(filename: string) -> SMTImportOptions
Creates an SMTImportOptions object that's used to import a design from SMT format. Creation of the SMTImportOptions object does not perform the import. You must pass this object to one of the ImportManager import methods to perform the import. The SMTImportOptions supports any available options when importing from SMT format.
- **filename** (string): The filename or URL of the SMT file to be imported.
- **Returns** (SMTImportOptions): The created SMTImportOptions object or null if the creation failed.

### createSTEPImportOptions(filename: string) -> STEPImportOptions
Creates an STEPImportOptions object that's used to import a design from STEP format. Creation of the STEPImportOptions object does not perform the import. You must pass this object to one of the ImportManager import methods to perform the import. The STEPImportOptions supports any available options when importing from STEP format.
- **filename** (string): The filename or URL of the STEP file to be imported.
- **Returns** (STEPImportOptions): The created STEPImportOptions object or null if the creation failed.

### createSVGImportOptions(fullFilename: string) -> SVGImportOptions
Creates a SVGImportOptions object that is used to import SVG data into a sketch. Creation of the SVGImportOptions object does not perform the import. You must pass this object to the importToTarget or importToTarget2 methods to perform the import and provide the sketch you want to import to as the target.
- **fullFilename** (string): The full filename, including the path, of the SVG file.
- **Returns** (SVGImportOptions): The created SVGImportOptions object or null if the creation failed.

### importToNewDocument(importOptions: ImportOptions) -> Document
Executes the import operation to import a file (of the format specified by the input ImportOptions object) to a new document.

This method does not support the DXF2DImportOptions or SVGImportOptions objects. Use ImportToTarget or ImportToTarget2 for those types.
- **importOptions** (ImportOptions): An ImportOptions object that is created using one of the create methods on the ImportManager object. This defines the type of file and any available options supported for that file type.
- **Returns** (Document): Returns the newly created Document object or null if the creation failed. A new unnamed, unsaved document will be opened in Fusion 360 as a result.

### importToTarget(importOptions: ImportOptions, target: Base) -> boolean
Executes the import operation to import a file (of the format specified by the input ImportOptions object) into an existing component in an existing design.
- **importOptions** (ImportOptions): An ImportOptions object that is created using one of the create methods on the ImportManager object. This defines the type of file and any available options supported for that file type. Supplying a DXF2DImportOptions object will result in the creation of one or more sketches (depending on the layers in the DXF file) in the target component.
- **target** (Base): For most import types this will be a Component. For SVGImportOptions this is the sketch you want to import the SVG data into.
- **Returns** (boolean): Returns true if the import was successful.

### importToTarget2(importOptions: ImportOptions, target: Base) -> ObjectCollection
Executes the import operation to import a file (of the format specified by the input ImportOptions object) into an existing component in an existing design and returns the imported objects.
- **importOptions** (ImportOptions): An ImportOptions object that is created using one of the create methods on the ImportManager object. This defines the type of file and any available options supported for that file type. Supplying a DXF2DImportOptions object will result in the creation of one or more sketches (depending on the layers in the DXF file) in the target component.
- **target** (Base): For most import types this will be a Component. For SVGImportOptions this is the sketch you want to import the SVG data into.
- **Returns** (ObjectCollection): Returns an ObjectCollection containing the results of whatever was created as a result of the import. null is returned in the case of failure.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Import Manager API Sample**: Demonstrates how to import different formats to Fusion document
