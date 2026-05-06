# ToolbarControl
Namespace: adsk.core
Inherits: Base
Since: August 2014

The base class for all toolbar controls.

**Accessed from:** ToolbarControlList.item, ToolbarControlList.itemById, ToolbarControls.item, ToolbarControls.itemById

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes the ToolbarControl
- **Returns** (boolean): Returns a boolean indicating if the deletion was successful.

## Properties

### id : string [read-only]
Gets the unique ID of this control. The ID is unique with respect to the other controls within the same panel, toolbar, or drop-down control.

### index : uinteger [read-only]
Gets the position of this control within the list of controls within the panel, toolbar, or drop-down control.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-write]
Gets or sets if this control is currently visible.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Gets the Parent object. When associated with a toolbar (right or left QAT or the NavBar) this returns the parent Toolbar object. When associated with a panel it returns the parent ToolbarPanel object. When associated with a control (DropDownControl) it returns the parent control.

## Samples
- **Customizing the UI using the API Sample**: Demonstrates how to work with tabs, panels, and command in the user interface. The full source for C++ and Python samples can be downloaded. This is especially useful for getting the resource files.
