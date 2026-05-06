# CommandControl
Namespace: adsk.core
Inherits: ToolbarControl
Since: August 2014

Represents a button, check box, or radio control list in a panel, toolbar, or drop-down.

**Accessed from:** ToolbarControls.addCommand

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes the ToolbarControl
- **Returns** (boolean): Returns a boolean indicating if the deletion was successful.

### promote(byDefault: boolean, positionID: string, isBefore: boolean) -> boolean
Promote the command to the parent panel and optionally position it relative to an already- promoted control.
- **byDefault** (boolean): If true, then the control will be promoted in the panel by default if the UI is reset. If false, then the promotion is cleared on reset.

This is an optional argument whose default value is False.
- **positionID** (string): If provided, then when this control is promoted, it will be positioned in the panel relative to the already-promoted control with this ID.

This is an optional argument whose default value is "".
- **isBefore** (boolean): If a positionID is provided, then this specifies whether the promoted control is placed before or after the control referenced by the positionID parameter.

This is an optional argument whose default value is True.
- **Returns** (boolean): True if this control was successfully promoted or was already promoted. False if promotion failed, which may happen if the control is not in a panel.

## Properties

### commandDefinition : CommandDefinition [read-only]
Gets the command definition associated with this button. The command definition defines all of the resource information used to display this button and receives the event when the button is clicked.

### id : string [read-only]
Gets the unique ID of this control. The ID is unique with respect to the other controls within the same panel, toolbar, or drop-down control.

### index : uinteger [read-only]
Gets the position of this control within the list of controls within the panel, toolbar, or drop-down control.

### isPromoted : boolean [read-write]
Gets or sets if this command has been promoted to the parent panel. This property is ignored in the case where this control isn't in a panel.

The promote method provides more options over how the control is promoted.

### isPromotedByDefault : boolean [read-write]
Gets or sets if this command is a default command in the panel. This defines the default state of the panel if the UI is reset. This property is ignored in the case where this control isn't in a panel.

The promote method provides more options over how the control is promoted.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-write]
Gets or sets if this control is currently visible.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Gets the Parent object. When associated with a toolbar (right or left QAT or the NavBar) this returns the parent Toolbar object. When associated with a panel it returns the parent ToolbarPanel object. When associated with a control (DropDownControl) it returns the parent control.
