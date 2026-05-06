# ApplicationCommandEvent
Namespace: adsk.core
Inherits: Event
Since: November 2015

An event endpoint that supports the connection to ApplicationCommandEventHandlers.

**Accessed from:** UserInterface.commandCreated, UserInterface.commandStarting, UserInterface.commandTerminated

## Methods

### add(handler: ApplicationCommandEventHandler) -> boolean
Adds an event handler object to this event endpoint.
- **handler** (ApplicationCommandEventHandler): The ApplicationCommandEventHandler to be called when this event is triggered.
- **Returns** (boolean): Returns true if the handler was successfully added to the set of event handlers.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### remove(handler: ApplicationCommandEventHandler) -> boolean
Removes a handler from this event endpoint.
- **handler** (ApplicationCommandEventHandler): An ApplicationCommandEventHandler that was previously added to this event with the add method.
- **Returns** (boolean): Returns true if the handler was found and removed from the set of event handlers.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
The name of the event - e.g. "DocumentOpening"

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### sender : Base [read-only]
The object that is firing the event. For example, in the case of a command input event this will return the command.
