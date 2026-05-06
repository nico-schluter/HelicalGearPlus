# RigidGroupList
Namespace: adsk.fusion
Inherits: Base
Since: January 2016

A list of rigid groups.

**Accessed from:** Occurrence.rigidGroups

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> RigidGroup
Function that returns the specified rigid group using an index into the list.
- **index** (uinteger): The index of the item within the list to return. The first item in the list has an index of 0.
- **Returns** (RigidGroup): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> RigidGroup
Function that returns the specified rigid group using a name.
- **name** (string): The name of the item within the list to return.
- **Returns** (RigidGroup): Returns the specified item or null if an invalid name was specified.

## Properties

### count : uinteger [read-only]
Returns number of rigid groups in the list.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
