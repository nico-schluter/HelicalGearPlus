# Status
Namespace: adsk.core
Inherits: Base
Since: July 2021

Used to communicate the current status of an object or operation. This provides the status and any error messages that might accompany an error or warning.

**Accessed from:** CustomFeatureEventArgs.computeStatus, DataEventArgs.status

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isError : boolean [read-only]
If true, An error occurred that has prevented the operation from successfully completing. This takes into account all of the child status messages.

### isOK : boolean [read-only]
If true, the operation was successful without any warnings or errors. This takes into account all of the child status messages.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isWarning : boolean [read-only]
If true, the operation has succeeded but with an unusual result. This takes into account all of the child status messages.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### statusMessages : StatusMessages [read-only]
the status messages associated with this status. These messages are displayed to the user in the alert dialog. Each status message can have children status messages that will be displayed as a tree structure in the alert dialog.
