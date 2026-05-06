# Toolbar
Namespace: adsk.core
Inherits: Base
Since: August 2014

Provides access to a toolbar in the user interface. A toolbar is a collection of toolbar controls.

**Accessed from:** Toolbars.item, Toolbars.itemById, UserInterface.activeToolbar

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### controls : ToolbarControls [read-only]
Gets the controls in this toolbar.

### id : string [read-only]
Gets the unique ID of the toolbar that can be used programmatically to find a specific toolbar.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentUserInterface : UserInterface [read-only]
Gets the owning UserInterface object.
