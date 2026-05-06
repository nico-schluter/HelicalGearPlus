# DataProjects
Namespace: adsk.core
Inherits: Base
Since: January 2015

Collection object that provides a list of all available projects.

**Accessed from:** Data.dataProjects, DataHub.dataProjects

## Methods

### add(name: string, purpose: string, contributors: string) -> DataProject
Creates a new project in the parent hub.
- **name** (string): The name of the project. This is the name visible to the user.
- **purpose** (string): Optional description of the purpose of the project. An empty string can be used to not specify a purpose.

This is an optional argument whose default value is "".
- **contributors** (string): Optional list of contributors where the list consists of email addresses separated by a comma. An empty string can be used to not specify any contributors.

This is an optional argument whose default value is "".
- **Returns** (DataProject): Returns the created DataProject object or null if the creation failed.

### asArray() -> DataProject
Get the current list of all projects.
- **Returns** (DataProject): Returns the current list of all projects.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> DataProject
Returns the specified project.
- **index** (uinteger): The index of the project to return. The first project in the list has an index of 0.
- **Returns** (DataProject): Returns the specified item or null if an invalid index was specified.

### itemById(id: string) -> DataProject
Returns the project specified using the ID of the project.
- **id** (string): The ID of the project to return. This is the same ID used by the APS Data Management API.
- **Returns** (DataProject): Returns the project or null if a project with the specified ID is not found.

## Properties

### count : uinteger [read-only]
The number of projects in this collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
