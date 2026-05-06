# DocumentEventArgs
Namespace: adsk.core
Inherits: EventArgs
Since: August 2014

The DocumentEventArgs provides information associated with a document event. Note that some properties are not available on every event - for example, the Document is not available on the DocumentOpening event because the Document is not yet available.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### cancelReason : string [read-write]
Gets and sets the description of the reason why the operation is being canceled. This property is only used if isOperationCancelled is set to true.

### document : Document [read-only]
Provides access to the document that is open. Can be null in the case where the event is fired before the document has been opened or after it has been closed.

### firingEvent : Event [read-only]
The event that the firing is in response to.

### fullPath : string [read-only]
The full path to the file.

### isOperationCancelled : boolean [read-write]
Gets and sets if the operation for this event is to be canceled. The description of the reason for canceling the operation can be set with the cancelReason property. This is only supported for the documentSaving event.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
