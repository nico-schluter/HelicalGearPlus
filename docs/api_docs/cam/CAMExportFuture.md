# CAMExportFuture
Namespace: adsk.cam
Inherits: Base
Since: September 2024

Used to check the state and get back the results of an operation generation.

**Accessed from:** CAMExportManager.executeWithExportFuture

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### error : string [read-only]
Gets the last encountered error message generated on the export thread.

### exportOptions : CAMExportOptions [read-only]
Returns the export option used to define the export associated with this future object.

### isGenerationCompleted : boolean [read-only]
Returns true if the export has finished generating.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### progress : float [read-only]
Returns the progress as a percentage value between 0.0% and 100.0%.

### warning : string [read-only]
Gets the last encountered warning message generated on the export thread.
