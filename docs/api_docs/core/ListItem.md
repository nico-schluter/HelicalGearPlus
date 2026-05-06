# ListItem
Namespace: adsk.core
Inherits: Base
Since: January 2015

Represents a single item in a check box list or a drop-down command input.

**Accessed from:** ButtonRowCommandInput.selectedItem, DropDownCommandInput.selectedItem, ListControlDefinition.lastSelected, ListItems.add, ListItems.addSeparator, ListItems.item, RadioButtonGroupCommandInput.selectedItem

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this item from the list. In cases where there is the concept of active item in the list, like with a DropDownCommandInput, this method will fail if the item you're attempting to delete is currently active. You need to make another item active first, and then you can delete the item.
- **Returns** (boolean): Returns true if the delete was successful.

## Properties

### icon : string [read-write]
Gets or sets the location for the icon file used for this item in the list. This is the path to a directory that contains the image files associated with this item. This is only valid when this is a standard list or button row and is ignored for check box lists, radio control lists, and radio button groups.

### index : integer [read-only]
Gets the index position within the list of this item.

### isSelected : boolean [read-write]
Gets or sets whether this item is selected. If the item is being displayed as a check box, this controls whether it is checked or not. If it's a drop-down list or button row it controls whether this is the single selected item. Setting a drop-down list, button row item, or radio button from a group to be selected will unselect the currently selected item. For a standard list, this will get or set the single item currently selected. For a separator, setting this property is ignored and it will always return false.

### isSeparator : boolean [read-only]
Gets if this control is a separator.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets or sets the name of this item as displayed in the list. If this control is a separator (isSeparator is true) or it's a button row, setting this property is ignored and getting it will return an empty string.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentList : Base [read-only]
Gets the parent CheckBoxListControlDefinition or object.

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.
