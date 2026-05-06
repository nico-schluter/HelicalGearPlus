# ListItems
Namespace: adsk.core
Inherits: Base
Since: January 2015

Provides access to the list of items in a check box list. This object supports the ability to add items to the list and iterate through the existing items.

**Accessed from:** ButtonRowCommandInput.listItems, DropDownCommandInput.listItems, ListControlDefinition.listItems, RadioButtonGroupCommandInput.listItems

## Methods

### add(name: string, isSelected: boolean, icon: string, beforeIndex: integer) -> ListItem
Adds a new item to the list.
- **name** (string): The name of this item as it is displayed in the list.
- **isSelected** (boolean): Sets whether this item is selected or not. If this list is associated with a control or input that can only have one item selected any other selected items will be unselected and this one will be the only selected item.
- **icon** (string): The path to the folder containing the image files to use for the icon. This is an optional argument but is required in the case of ButtonRowCommandInput objects. It is optional in the case of a DropDownCommandInput whose style is LabeledIconDropDownStyle and for ListControlType whose type is not RadioButtonListType. In other cases it is not used and is ignored.

Icons can be defined using either PNG or SVG files. More information about icons can be found in the user manual topic User Interface Customization.

This is an optional argument whose default value is "".
- **beforeIndex** (integer): The position of the item within the list. This value indicates the index of the current item to insert this new item just before. For example, a value of 0 will insert it before the first item in the list. An index of -1 will position the button at the bottom of the list.

This is an optional argument whose default value is -1.
- **Returns** (ListItem): Returns the new ListControlItem or null in the case of a failure.

### addSeparator(beforeIndex: integer) -> ListItem
Adds a separator to the list. This is not supported for button rows.
- **beforeIndex** (integer): The position of the item within the list. This value indicates the index of the current item to insert this new item just before. For example, a value of 0 will insert it before the first item in the list. An index of -1 will position the button at the bottom of the list.
- **Returns** (ListItem): Returns the new ListControlItem or null in the case of a failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### clear() -> boolean
Clears all of the items from the list.
- **Returns** (boolean): Returns true if successful.

### item(index: uinteger) -> ListItem
Returns the specified check box list item using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ListItem): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Gets the number of items in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.
