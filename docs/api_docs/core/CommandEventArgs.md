# CommandEventArgs
Namespace: adsk.core
Inherits: EventArgs
Since: August 2014

Provides a set of arguments from a firing CommandEvent to a CommandEventHandler's notify callback method.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### command : Command [read-only]
Gets the Command object.

### executeFailed : boolean [read-write]
Used during the execute event to get or set that the execute operations failed and the commands transaction should be aborted. This property should be ignored for all events besides the Execute event.

### executeFailedMessage : string [read-write]
Used during the execute event to get or set a description of an execute failure. This property should be ignored for all events besides the Execute event.

### firingEvent : Event [read-only]
The event that the firing is in response to.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isValidResult : boolean [read-write]
Used during the commandStarting event to get or set that the result of preview is valid and the command can reuse the result when OK is hit. This property should be ignored for all events besides the executePreview event.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### terminationReason : CommandTerminationReason [read-only]
Gets the termination reason of the command. It's only valid on the destroy event.

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.
