# MarkingMenuEvent
Namespace: adsk.core
Inherits: Event
Since: January 2017

A MarkingMenuEvent is fired when the marking menu and context menu are displayed. For example, in response to the markingMenuDisplaying event.

**Accessed from:** UserInterface.markingMenuDisplaying

## Methods

### add(handler: MarkingMenuEventHandler) -> boolean
Add a handler to be notified when the event occurs.
- **handler** (MarkingMenuEventHandler): The handler object to be called when this event is fired.
- **Returns** (boolean): Returns true if the addition of the handler was successful.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### remove(handler: MarkingMenuEventHandler) -> boolean
Removes a handler from the event.
- **handler** (MarkingMenuEventHandler): The handler object to be removed from the event.
- **Returns** (boolean): Returns true if removal of the handler was successful.

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
