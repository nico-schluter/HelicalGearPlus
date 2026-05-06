# PropertyGroups
Namespace: adsk.core
Inherits: Base
Since: January 2024

A collection of PropertyGroup objects.

**Accessed from:** BaseComponent.propertyGroups, Component.propertyGroups, FlatPatternComponent.propertyGroups

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: integer) -> PropertyGroup
Returns the specified property group from the collection using an index into the collection.
- **index** (integer): The index of the property within the collection where the first item is 0.
- **Returns** (PropertyGroup): Returns the specified item or null if an invalid index was specified.

### itemById(id: string) -> PropertyGroup
Returns the specified property group from the collection using the unique ID of the property group. The ID is consistent and can't be modified by the user and isn't affected by localization.
- **id** (string): The unique ID of the property group.
- **Returns** (PropertyGroup): Returns the specified PropertyGroup or null if the ID doesn't match a group within the collection.

### itemByName(name: string) -> PropertyGroup
Returns the specified PropertyGroup using the name of the group.
- **name** (string): The name of the group to return. This is the name as seen in the user interface. Not all groups have a name.
- **Returns** (PropertyGroup): Returns the specified group or null if the name doesn't match a group within the collection.

## Properties

### count : uinteger [read-only]
Returns the number of properties within the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Library Item API Sample**: Demonstrates how to examine library items using the API.

To use the sample, create a new Python or C++ script and copy and paste this code, replacing the existing default code. The script will search for and record all components and library items in the current project. They are displayed in a dialog when the script has finished.
