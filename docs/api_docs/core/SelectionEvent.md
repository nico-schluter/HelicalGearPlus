# SelectionEvent
Namespace: adsk.core
Inherits: Event
Since: August 2014

An event endpoint that supports the connection to client implemented SelectionEventHandlers.

**Accessed from:** Command.preSelect, Command.preSelectEnd, Command.preSelectMouseMove, Command.preSelectStart, Command.select, Command.selectionEvent, Command.unselect

## Methods

### add(handler: SelectionEventHandler) -> boolean
Adds an event handler to this event endpoint.
- **handler** (SelectionEventHandler): The client implemented SelectionEventHandler to be called when this event is triggered.
- **Returns** (boolean): Returns true if the handler was successfully added to the set of event handlers.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### remove(handler: SelectionEventHandler) -> boolean
Removes a handler from this event endpoint.
- **handler** (SelectionEventHandler): A SelectionEventHandler that was previously added to this event with the add method.
- **Returns** (boolean): Returns true if the handler was found and removed from the set of event handlers.

## Properties

### activeInput : SelectionCommandInput [read-only]
Returns the SelectionCommandInput that is currently active in the command dialog and that the user is selecting entities for. This can be used to determine which set of rules you want to apply to determine if the current entity is selectable or not.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
The name of the event - e.g. "DocumentOpening"

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### sender : Base [read-only]
The object that is firing the event. For example, in the case of a command input event this will return the command.
