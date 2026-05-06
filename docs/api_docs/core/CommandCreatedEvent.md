# CommandCreatedEvent
Namespace: adsk.core
Inherits: Event
Since: August 2014

Class that needs to be implemented in order to respond to the CommandCreatedEvent event.

**Accessed from:** CommandDefinition.commandCreated

## Methods

### add(handler: CommandCreatedEventHandler) -> boolean
Adds an event handler object to this event endpoint.
- **handler** (CommandCreatedEventHandler): The client implemented CommandCreatedEventHandler to be called when this event is triggered.
- **Returns** (boolean): Returns true if the handler was successfully added to the set of event handlers.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### remove(handler: CommandCreatedEventHandler) -> boolean
Removes a handler from this event endpoint.
- **handler** (CommandCreatedEventHandler): A CommandCreatedEventHandler that was previously added to this event with the add method.
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

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.
- **Customizing the UI using the API Sample**: Demonstrates how to work with tabs, panels, and command in the user interface. The full source for C++ and Python samples can be downloaded. This is especially useful for getting the resource files.
