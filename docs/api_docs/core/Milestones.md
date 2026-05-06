# Milestones
Namespace: adsk.core
Inherits: Base
Since: March 2024

Returns the milestones associated with a DataFile.

**Accessed from:** DataFile.milestones, DesignDataFile.milestones

## Methods

### asArray() -> Milestone
Get the current list of all milestones.
- **Returns** (Milestone): Returns the current list of all milestones.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Milestone
Returns the specified milestone.
- **index** (uinteger): The index of the milestone to return. The first milestone in the list has an index of 0.
- **Returns** (Milestone): Returns the specified file or null if an invalid index was specified.

### itemByName(name: string) -> Milestone
Returns the milestone specified using its name..
- **name** (string): The name of the milestone to return.
- **Returns** (Milestone): Returns the Milestone object or null if a milestone with the specified name is not found.

## Properties

### count : uinteger [read-only]
The number of data items in this collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
