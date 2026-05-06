# ToolbarTabs
Namespace: adsk.core
Inherits: Base
Since: August 2019

Provides access to a set of toolbar tabs.

**Accessed from:** Workspace.toolbarTabs

## Methods

### add(id: string, name: string) -> ToolbarTab
Creates a new ToolbarTab. The tab is initially empty. This method appends the tab to the end of the collection.
- **id** (string): The unique id for this tab. The id must be unique with respect to all of the tabs.
- **name** (string): The displayed name of this tab. This is the name visible in the user interface.
- **Returns** (ToolbarTab): Returns the newly created tab or null in the case the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ToolbarTab
Returns the specified toolbar tab using an index into the collection. When iterating by index, the tabs are returned in the same order as they are shown in the user interface.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ToolbarTab): Returns the specified item or null if an invalid index was specified.

### itemById(id: string) -> ToolbarTab
Returns the ToolbarTab at the specified ID.
- **id** (string): The Id of the tab within the collection to return.
- **Returns** (ToolbarTab): Returns the ToolbarTab of the specified id or null if no tab has the specified id.

## Properties

### count : uinteger [read-only]
Gets the number of ToolbarTabs.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Customizing the UI using the API Sample**: Demonstrates how to work with tabs, panels, and command in the user interface. The full source for C++ and Python samples can be downloaded. This is especially useful for getting the resource files.
- **Write user interface to a file API Sample**: Writes out the full structure of the Fusion user interface. This information is useful when editing the user-interface, as discussed in the usre manual topic User-Interface Customization with Fusion's API
