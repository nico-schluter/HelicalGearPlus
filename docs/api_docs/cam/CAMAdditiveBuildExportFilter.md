# CAMAdditiveBuildExportFilter
Namespace: adsk.cam
Inherits: Base
Since: October 2023

Export filter used by CAMAdditiveMachineBuildFileExportOptions.

**Accessed from:** CAMAdditiveBuildExportOptions.exportFilters

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### extension : string [read-only]
The extension of the file format, including a leading "."

### id : string [read-only]
The id of the file format.

### isMultiFileExport : boolean [read-only]
True if the export outputs multiple files. If so, fullFilename should point to a directory, not a file.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
The name of the file format. Might indicate whether a file format is binary or not.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
