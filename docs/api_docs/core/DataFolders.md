# DataFolders
Namespace: adsk.core
Inherits: Base
Since: January 2015

Collection object the provides a list of data folders.

**Accessed from:** DataFolder.dataFolders

## Methods

### add(name: string) -> DataFolder
Creates a new folder within the parent folder.
- **name** (string): The name of the folder. This must be unique with respect to the other folders within the parent folder.
- **Returns** (DataFolder): Returns the created DataFolder or null if the creation failed.

### asArray() -> DataFolder
Get the current list of all folders.
- **Returns** (DataFolder): Returns the current list of all folders.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> DataFolder
Returns the specified folder.
- **index** (uinteger): The index of the folder to return. The first folder in the list has an index of 0.
- **Returns** (DataFolder): Returns the item or null if an invalid index was specified.

### itemById(id: string) -> DataFolder
Returns the folder specified using the ID of the folder.
- **id** (string): The ID of the folder to return. This is the same ID used by the APS Data Management API.
- **Returns** (DataFolder): Returns the folder or null if a folder with the specified ID is not found.

### itemByName(name: string) -> DataFolder
Returns the folder specified using the name of the folder.
- **name** (string): The name of the folder to return.
- **Returns** (DataFolder): Returns the folder or null if a folder of the specified name is not found.

## Properties

### count : uinteger [read-only]
The number of folders in this collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
