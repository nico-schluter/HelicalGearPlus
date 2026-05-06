# DropDownControl
Namespace: adsk.core
Inherits: ToolbarControl
Since: August 2014

Represents a drop-down control.

**Accessed from:** ToolbarControls.addDropDown

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes the ToolbarControl
- **Returns** (boolean): Returns a boolean indicating if the deletion was successful.

## Properties

### controls : ToolbarControls [read-only]
Gets the associated ToolbarControls collection. Through this you can add additional controls to the drop-down.

### id : string [read-only]
Gets the unique ID of this control. The ID is unique with respect to the other controls within the same panel, toolbar, or drop-down control.

### index : uinteger [read-only]
Gets the position of this control within the list of controls within the panel, toolbar, or drop-down control.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-write]
Gets or sets if this control is currently visible.

### name : string [read-write]
Gets or sets the Name displayed for this drop down. This isn't used when the drop-down is in a toolbar because an icon is used in that case.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Gets the Parent object. When associated with a toolbar (right or left QAT or the NavBar) this returns the parent Toolbar object. When associated with a panel it returns the parent ToolbarPanel object. When associated with a control (DropDownControl) it returns the parent control.

### resourceFolder : string [read-write]
This argument defines the resource folder that contains the images used for the icon when icons are used in the drop-down. Icons can be defined using either PNG or SVG files. More information about icons can be found in the user manual topic User Interface Customization.

## Samples
- **Customizing the UI using the API Sample**: Demonstrates how to work with tabs, panels, and command in the user interface. The full source for C++ and Python samples can be downloaded. This is especially useful for getting the resource files.
- **Write user interface to a file API Sample**: Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic User-Interface Customization with Fusion's API
