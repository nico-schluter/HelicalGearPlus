# CAM3MFExportMetadataOptions
Namespace: adsk.cam
Inherits: Base
Since: May 2023

Class providing read and write access to meta data of a 3MF file.

**Accessed from:** CAM3MFExportOptions.metadata

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### copyright : string [read-write]
Copyright of the 3MF File

### creationDate : string [read-write]
Creation date of the 3MF File

### description : string [read-write]
Description of the 3MF File

### designer : string [read-write]
Designer of the 3MF File

### enabled : boolean [read-write]
Enable or disable the integration of Metadata in the 3mf. This is true by default.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### licenseTerms : string [read-write]
License terms of the 3MF File

### modificationDate : string [read-write]
Modification date of the 3MF File

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### title : string [read-write]
Title of the 3MF File
