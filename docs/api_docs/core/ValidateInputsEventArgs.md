# ValidateInputsEventArgs
Namespace: adsk.core
Inherits: EventArgs
Since: August 2014

Provides a set of arguments from a firing ValidateInputsEvent to a ValidateInputsEventHandler's notify callback method.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### areInputsValid : boolean [read-write]
Used with AreInputsValid event to specify if the all of the inputs for the command are valid or not. If you set this to false, indicating they are not valid, the OK button for the dialog is disabled forcing the user to correct the inputs before continuing. If you set this to true the OK button will be enabled, as long as the inputs satisfy their own requirements. For example, if a SelectionCommandInput is defined to have at minimum number of entities selected, that requirement must be met, or if a ValueCommandInput has an invalid value specified, the OK button will still be disabled.

### firingEvent : Event [read-only]
The event that the firing is in response to.

### inputs : CommandInputs [read-only]
Returns the collection of command inputs that are associated with the command this event is being fired for.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
