# ToolbarControlList
Namespace: adsk.core
Inherits: Base
Since: August 2014

Provides access to a list of toolbar controls.

**Accessed from:** ToolbarPanel.promotedControls

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ToolbarControl
Returns the ToolbarControl at the specified index. When iterating by index, the controls are returned in the same order as they are shown in the user interface.
- **index** (uinteger): The index of the control within the collection to return. The first item in the collection has in index of 0.
- **Returns** (ToolbarControl): Returns the ToolbarControl at the specified index or null if an invalid index was specified.

### itemById(id: string) -> ToolbarControl
Returns the ToolbarControl at the specified ID.
- **id** (string): The ID of the control within the collection to return.
- **Returns** (ToolbarControl): Returns the ToolbarControl with the specified ID or null if no control has this ID.

## Properties

### count : uinteger [read-only]
Gets the number of toolbar controls.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
