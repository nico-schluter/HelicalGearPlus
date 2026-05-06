# CheckBoxControlDefinition
Namespace: adsk.core
Inherits: ControlDefinition
Since: August 2014

Represents the information used to define a check box. This isn't the visible check box control but is the information needed to create a check box control and fully defines a check box except for it's position within the user interface.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isChecked : boolean [read-write]
Gets or sets whether the check box is checked. Changing this will result in changing any associated controls and will execute the associated command.

### isEnabled : boolean [read-write]
Gets or sets if this definition is enabled or not. This has the effect of enabling and disabling any associated controls.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-write]
Gets or sets if this definition is visible or not. This has the effect of making any associated controls visible or invisible in the user interface.

### name : string [read-write]
Gets or sets the name for this control. This is the visible name displayed in the user interface.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
