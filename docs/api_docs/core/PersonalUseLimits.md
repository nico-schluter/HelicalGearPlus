# PersonalUseLimits
Namespace: adsk.core
Inherits: Base
Since: May 2021

Object that provides information about file limits associated with a "Fusion for Personal Use license".

**Accessed from:** Data.personalUseLimits

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### editableFileCount : integer [read-only]
Returns the current number of documents that are set by the user to be editable.

### editableFiles : array [read-only]
Returns a list of the DataFile objects that have been set by the user to be editable.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maxEditableFileCount : integer [read-only]
Returns the maximum number of documents that can be set by the user to be editable.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
