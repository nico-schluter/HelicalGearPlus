# Toolbars
Namespace: adsk.core
Inherits: Base
Since: August 2014

Provides access to the toolbars. These are currently the right and left QAT's and the NavBar.

**Accessed from:** UserInterface.toolbars

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Toolbar
Returns the specified toolbar using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Toolbar): Returns the specified item or null if an invalid index was specified.

### itemById(id: string) -> Toolbar
Returns the Toolbar of the specified ID.
- **id** (string): The Id of the toolbar to return.
- **Returns** (Toolbar): Returns the toolbar with the specified ID or null if there's not a toolbar with the specified ID.

## Properties

### count : uinteger [read-only]
Gets the number of Toolbar objects in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
