# DataObjectFuture
Namespace: adsk.core
Inherits: Future
Since: September 2024

Used to check the state of getting data associated with an object where the associated data typically exists on the cloud.

**Accessed from:** DataFile.dataObject, DataFile.thumbnail

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### dataObject : DataObject [read-only]
Returns the DataObject when the data has become available, (state returns FinishedFutureState). Returns null if the operation is still running or has failed.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### state : FutureStates [read-only]
Returns the current state of the process associated with this future.
