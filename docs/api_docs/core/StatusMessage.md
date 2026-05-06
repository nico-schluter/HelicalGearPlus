# StatusMessage
Namespace: adsk.core
Inherits: Base
Since: July 2021

Defines the message associated with a Status object.

**Accessed from:** StatusMessages.addError, StatusMessages.addWarning, StatusMessages.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### childStatusMessages : StatusMessages [read-only]
Returns the collection of status codes that are children of this status message.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### message : string [read-write]
The user visible message being used. Setting this message for custom feature errors or warnings is currently ignored.

### messageId : string [read-write]
Gets and sets the ID of the message being used. This is a predefined ID within the Fusion message string table.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### statusMessageType : StatusMessageTypes [read-only]
Returns the type of message this StatusMessage represents.
