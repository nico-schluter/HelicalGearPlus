# PropertyGroup
Namespace: adsk.core
Inherits: Base
Since: January 2024

Represents a group of properties and provides access to the properties.

**Accessed from:** PropertyGroups.item, PropertyGroups.itemById, PropertyGroups.itemByName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: integer) -> Property
Returns the specified property from the group using an index into the group.
- **index** (integer): The index of the property within the group where the first item is 0.
- **Returns** (Property): Returns the specified group or null if an invalid index was specified.

### itemById(id: string) -> Property
Returns the specified property from the group using the unique ID of the property. The ID is consistent and can't be modified by the user and isn't affected by localization.
- **id** (string): The unique ID of the property.
- **Returns** (Property): Returns the specified Property or null if the ID doesn't match a property within the collection.

### itemByName(name: string) -> Property
Returns the specified Property using the name of the property.
- **name** (string): The name of the property to return. This is the name as seen in the user interface and may be localized.
- **Returns** (Property): Returns the specified property or null if the name doesn't match a property within the group.

## Properties

### count : uinteger [read-only]
Returns the number of properties within the group.

### id : string [read-only]
Returns the unique ID of this property.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Returns the name of this group as seen in the user interface. This name is localized and can change based on the current language

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Returns the parent of this group. Typically this will be a Component.

## Samples
- **Library Item API Sample**: Demonstrates how to examine library items using the API.

To use the sample, create a new Python or C++ script and copy and paste this code, replacing the existing default code. The script will search for and record all components and library items in the current project. They are displayed in a dialog when the script has finished.
