# SplitButtonControl
Namespace: adsk.core
Inherits: ToolbarControl
Since: August 2014

A split button has two active areas that the user can click; the main button portion and the drop-down arrow. Clicking the main button, executes the displayed command. Clicking the drop-down displays the drop-down with additional commands.

**Accessed from:** ToolbarControls.addSplitButton

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes the ToolbarControl
- **Returns** (boolean): Returns a boolean indicating if the deletion was successful.

## Properties

### additionalDefinitions : array [read-write]
Gets or sets the command definitions used to define the buttons associated with the split button.

### defaultCommandDefinition : CommandDefinition [read-only]
Gets the command definition that is used as the default command on the main portion of the split button.

### id : string [read-only]
Gets the unique ID of this control. The ID is unique with respect to the other controls within the same panel, toolbar, or drop-down control.

### index : uinteger [read-only]
Gets the position of this control within the list of controls within the panel, toolbar, or drop-down control.

### isLastUsedShown : boolean [read-only]
Gets if this button behaves where the last executed command becomes the command on the main portion of the split button.

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
- **Write user interface to a file API Sample**: Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic User-Interface Customization with Fusion's API
