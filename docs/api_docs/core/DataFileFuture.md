# DataFileFuture
Namespace: adsk.core
Inherits: Base
Since: March 2015

Used to check the state and get back the results of a file upload.

**Accessed from:** Component.saveCopyAs, DataFile.copyWithInput, DataFolder.uploadAssembly, DataFolder.uploadFile, FlatPatternComponent.saveCopyAs

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### dataFile : DataFile [read-only]
Returns the DataFile when the upload is complete (uplodeState returns UploadFinished). Returns null if the upload is still running or has failed.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### uploadState : UploadStates [read-only]
Returns the current state of the upload.
