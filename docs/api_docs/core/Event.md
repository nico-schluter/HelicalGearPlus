# Event
Namespace: adsk.core
Inherits: Base
Since: August 2014

Objects can have several Event properties that fire when some 'event' occurs. Clients can attach EventHandlers to one or more Events and they get notified when the 'event' occurs.

This is a base class - classes like DocumentEvent add type safety (i.e. only allow the correct type of handler to be added to them).

**Accessed from:** ActiveSelectionEventArgs.firingEvent, ApplicationCommandEventArgs.firingEvent, ApplicationEventArgs.firingEvent, CameraEventArgs.firingEvent, CommandCreatedEventArgs.firingEvent, CommandEventArgs.firingEvent, CustomEventArgs.firingEvent, CustomFeatureEventArgs.firingEvent, DataEventArgs.firingEvent, DocumentEventArgs.firingEvent, EventArgs.firingEvent, HTMLEventArgs.firingEvent, HttpEventArgs.firingEvent, InputChangedEventArgs.firingEvent, KeyboardEventArgs.firingEvent, MarkingMenuEventArgs.firingEvent, MFGDMDataEventArgs.firingEvent, MouseEventArgs.firingEvent, NavigationEventArgs.firingEvent, RenderEventArgs.firingEvent, SelectionEventArgs.firingEvent, SetupChangeEventArgs.firingEvent, SetupEventArgs.firingEvent, UserInterfaceGeneralEventArgs.firingEvent, ValidateInputsEventArgs.firingEvent, WebRequestEventArgs.firingEvent, WorkspaceEventArgs.firingEvent

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

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
