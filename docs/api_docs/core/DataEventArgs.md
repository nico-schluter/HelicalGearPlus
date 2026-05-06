# DataEventArgs
Namespace: adsk.core
Inherits: EventArgs
Since: January 2022

The DataEventArgs provides information associated with a data event. Note that some properties are not available on every event.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### file : DataFile [read-only]
Gets the DataFile object associated with this event. If there isn't a DataFile associated with the event, this property will return null.

### filename : string [read-only]
Gets the filename associated with the operation. If there isn't an associated filename, an empty string is returned. For a download operation, this will be the full filename of the downloaded file.

### firingEvent : Event [read-only]
The event that the firing is in response to.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### status : Status [read-only]
Returns a Status object that provides additional information about the success or failure of the operation.
