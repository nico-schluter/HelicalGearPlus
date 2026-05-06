# DataProject
Namespace: adsk.core
Inherits: Base
Since: January 2015

Represents the master branch project within a hub.

**Accessed from:** Data.activeProject, DataFile.parentProject, DataFolder.parentProject, DataProjects.add, DataProjects.asArray, DataProjects.item, DataProjects.itemById, DesignDataFile.parentProject

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### id : string [read-only]
Returns the unique ID for this project. This is the same id used in the APS Data Management API in an unencoded form and will look something like this: "a.45637".

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets and sets the name of the project.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentHub : DataHub [read-only]
Returns the parent DataHub of this project.

### rootFolder : DataFolder [read-only]
Returns the project's root folder. This provides access to all of the folders and the files in the top level of the project.
