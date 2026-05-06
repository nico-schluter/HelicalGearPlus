# CAMAdditiveBuildExportOptions
Namespace: adsk.cam
Inherits: CAMExportOptions
Since: October 2023

Additive buildfile export option. Available with all additive machines except for FFF and DED based machines. Currently picks the first export filter from the print setting's export filter list.

**Accessed from:** CAMExportManager.createCAMAdditiveBuildExportOptions

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### error : string [read-only]
Gets the last encountered error message. When the CAMExportManager's executeWithExportFuture() method is used, this method only returns errors encoutered when setting up the export. Errors thrown afterwards can be retrieved via the CAMExportFuture object. When the CAMExportManager's execute() method is used, any error can be retrieved using this property.

### exportFilters : array [read-only]
Gets a list of available export filters from the setup's print setting. The export object must be set before using this function.

### exportObject : Base [read-write]
The export object we want to export. Depending on the actual export option, this might be geometry, an operation or a setup.

### fullFilename : string [read-write]
The file we want to export to. Needs to contain a valid path, as no intermediate folders are created.

### isThumbnailSupported : boolean [read-only]
Method to check if the exporter implementation supports thumbnail

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### selectedExportFilterId : string [read-write]
Gets and sets the export filter to be used for the export. By default, this is the first entry in the print setting's filter list.

### thumbnailPath : string [read-write]
Path to the thumbnail for the buildfile
