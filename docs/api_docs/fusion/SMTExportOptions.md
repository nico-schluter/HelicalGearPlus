# SMTExportOptions
Namespace: adsk.fusion
Inherits: ExportOptions
Since: January 2015

Defines that an SMT export is to be done and specifies the various options.

**Accessed from:** ExportManager.createSMTExportOptions

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### filename : string [read-write]
Gets and sets the filename that the exported file will be written to. This can be empty in the case of STL export and sending the result to the mesh editor.

### geometry : Base [read-write]
Specifies the geometry to export. This can be an Occurrence, or the root Component. For STL, OBJ, and 3MF export, it can be a BRepBody. For DXF export, it can be a sketch of flat pattern.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### version : integer [read-write]
Gets and set the version of the SMT format to write to. The default is to use the current version of the Autodesk Shape Manager kernel that Fusion is using. Specifying an invalid version will result in an assert.

Valid versions are 218 up to the current version, which is what this property returns by default when a new SMTExportOptions object is created.

## Samples
- **ExportManager API Sample**: Demonstrates how to export f3d to different formats.
