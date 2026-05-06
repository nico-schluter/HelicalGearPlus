# Workspaces
Namespace: adsk.core
Inherits: Base
Since: August 2014

Provides access to all of the existing workspaces.

**Accessed from:** UserInterface.workspaces

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Workspace
Returns the specified work space using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Workspace): Returns the specified item or null if an invalid index was specified.

### itemById(id: string) -> Workspace
Returns the Workspace of the specified ID.
- **id** (string): The ID of the workspace to get.
- **Returns** (Workspace): Returns the specified workspace or null in the case where there isn't a workspace with the specified ID.

## Properties

### count : uinteger [read-only]
Gets the number of workspaces in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Customizing the UI using the API Sample**: Demonstrates how to work with tabs, panels, and command in the user interface. The full source for C++ and Python samples can be downloaded. This is especially useful for getting the resource files.
- **Write user interface to a file API Sample**: Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic User-Interface Customization with Fusion's API
