# FusionArchiveImportOptions
Namespace: adsk.core
Inherits: ImportOptions
Since: September 2015

Defines that a Fusion Archive import is to be done and specifies the various options.

**Accessed from:** ImportManager.createFusionArchiveImportOptions

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### filename : string [read-write]
Gets and sets the filename or URL of the file to be imported.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isViewFit : boolean [read-write]
Specifies if the camera should be adjusted to fit the geometry of the import. This defaults to true, which will cause a change in the current view. Setting this to false will leave the view as-is and just import the geometry.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Import Manager API Sample**: Demonstrates how to import different formats to Fusion document
