# Components
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

The Components collection object provides access to existing components in a design.

**Accessed from:** Design.allComponents, FlatPatternProduct.allComponents, WorkingModel.allComponents

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Component
Function that returns the specified component using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Component): Returns the specified item or null if an invalid index was specified.

### itemById(id: string) -> Component
Returns the Component that has the specified ID.
- **id** (string): The ID of the Component to get. This is the same id used by PIM (Product Information Model).
- **Returns** (Component): Returns the specified Component or null in the case where there isn't a Component with the specified ID in this Design.

### itemByName(name: string) -> Component
Function that returns the specified component by name.
- **name** (string): The name of the component within the collection to return.
- **Returns** (Component): Returns the specified component or null if the name is not found.

## Properties

### count : uinteger [read-only]
The number of components in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Library Item API Sample**: Demonstrates how to examine library items using the API.

To use the sample, create a new Python or C++ script and copy and paste this code, replacing the existing default code. The script will search for and record all components and library items in the current project. They are displayed in a dialog when the script has finished.
