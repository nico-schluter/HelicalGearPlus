# RadialMarkingMenu
Namespace: adsk.core
Inherits: Base
Since: January 2017

Represents the marking menu which is the round menu that's displayed when the user right-clicks within Fusion. This supports customizing the contents of the marking menu.

**Accessed from:** MarkingMenuEventArgs.radialMarkingMenu, RadialMarkingMenu.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### clear() -> boolean
Completely clears the contents of the marking menu. If left in this state, the marking menu will not be displayed.
- **Returns** (boolean): Returns true if the clear was successful.

### create(text: string) -> RadialMarkingMenu
This is used to create a sub-menu in a marking menu. This method creates a new, empty marking menu which can then be assigned to a position in the displayed marking menu to define the sub-menu.
- **text** (string): The text that will be displayed in the parent menu to access this menu.
- **Returns** (RadialMarkingMenu): Returns the newly created marking menu or null in the case of a failure.

## Properties

### eastCommand : Base [read-write]
Gets and sets the command definition that's displayed in the East position (right) of the marking menu. Setting this to null indicates that the East position should be empty.

This can also return or be set with a MarkingMenu object which is used to have a sub-menu. New marking menus can be created using the create method and then assigned to the desired position in the marking menu.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### northCommand : Base [read-write]
Gets and sets the command definition that's displayed in the North position (top) of the marking menu. Setting this to null indicates that the North position should be empty.

This can also return or be set with a MarkingMenu object which is used to have a sub-menu. New marking menus can be created using the create method and then assigned to the desired position in the marking menu.

### northeastCommand : Base [read-write]
Gets and sets the command definition that's displayed in the Northeast position (top-right) of the marking menu. Setting this to null indicates that the Northeast position should be empty.

This can also return or be set with a MarkingMenu object which is used to have a sub-menu. New marking menus can be created using the create method and then assigned to the desired position in the marking menu.

### northwestCommand : Base [read-write]
Gets and sets the command definition that's displayed in the Northwest position (upper-left) of the marking menu. Setting this to null indicates that the Northwest position should be empty.

This can also return or be set with a MarkingMenu object which is used to have a sub-menu. New marking menus can be created using the create method and then assigned to the desired position in the marking menu.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### southCommand : Base [read-write]
Gets and sets the command definition that's displayed in the South position (bottom) of the marking menu. Setting this to null indicates that the South position should be empty.

This can also return or be set with a MarkingMenu object which is used to have a sub-menu. New marking menus can be created using the create method and then assigned to the desired position in the marking menu.

### southeastCommand : Base [read-write]
Gets and sets the command definition that's displayed in the Southeast position (bottom-right) of the marking menu. Setting this to null indicates that the Southeast position should be empty.

This can also return or be set with a MarkingMenu object which is used to have a sub-menu. New marking menus can be created using the create method and then assigned to the desired position in the marking menu.

### southwestCommand : Base [read-write]
Gets and sets the command definition that's displayed in the Southwest position (bottom-left) of the marking menu. Setting this to null indicates that the Southwest position should be empty.

This can also return or be set with a MarkingMenu object which is used to have a sub-menu. New marking menus can be created using the create method and then assigned to the desired position in the marking menu.

### text : string [read-write]
Gets and sets the text that is displayed in the parent marking menu to access a sub marking menu. This property is not used for the main marking menu and will return an empty string and setting it will have no effect.

### westCommand : Base [read-write]
Gets and sets the command definition that's displayed in the West position (left) of the marking menu. Setting this to null indicates that the West position should be empty.

This can also return or be set with a MarkingMenu object which is used to have a sub-menu. New marking menus can be created using the create method and then assigned to the desired position in the marking menu.
