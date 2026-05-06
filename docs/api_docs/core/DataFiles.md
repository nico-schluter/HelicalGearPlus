# DataFiles
Namespace: adsk.core
Inherits: Base
Since: January 2015

Returns the items within a folder. This includes everything in a folder except for other folders.

**Accessed from:** DataFile.childReferences, DataFile.parentReferences, DataFile.versions, DataFolder.dataFiles, DesignDataFile.childReferences, DesignDataFile.parentReferences, DesignDataFile.versions

## Methods

### asArray() -> DataFile
Get the current list of all files.
- **Returns** (DataFile): Returns the current list of all files.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> DataFile
Returns the specified data file.
- **index** (uinteger): The index of the file to return. The first file in the list has an index of 0.
- **Returns** (DataFile): Returns the specified file or null if an invalid index was specified.

### itemById(id: string) -> DataFile
Returns the file specified using the ID or version ID of the file.
- **id** (string): The ID or version ID of the file to return. This is the same ID used by the APS Data Management API.
- **Returns** (DataFile): Returns the file or null if a file with the specified ID is not found.

## Properties

### count : uinteger [read-only]
The number of data items in this collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
