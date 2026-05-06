# DataHubs
Namespace: adsk.core
Inherits: Base
Since: September 2016

Collection object that provides a list of all available hubs.

**Accessed from:** Data.dataHubs

## Methods

### asArray() -> DataHub
Get the current list of all hubs.
- **Returns** (DataHub): Returns the current list of all hubs.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> DataHub
Returns the specified hub.
- **index** (uinteger): The index of the hub to return. The first hub in the list has an index of 0.
- **Returns** (DataHub): Returns the specified item or null if an invalid index was specified.

### itemById(id: string) -> DataHub
Returns the hub specified using the ID of the hub.
- **id** (string): The ID of the hub to return. This is the same ID used by the APS Data Management API.
- **Returns** (DataHub): Returns the hub or null if a hub with the specified ID is not found.

## Properties

### count : uinteger [read-only]
The number of hubs in this collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
