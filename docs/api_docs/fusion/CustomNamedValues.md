# CustomNamedValues
Namespace: adsk.fusion
Inherits: Base
Since: July 2021

A collection of named values. The values are strings that Fusion stores but can be anything you choose. If you have several things you need to save you can choose to combine the data into a JSON or XML representation and save it as a single custom value or create a new custom value or each unique value you want to store. Fusion doesn't care what the value is or what it represents but only saves and provides access to it.

**Accessed from:** CustomFeature.customNamedValues

## Methods

### addOrSetValue(id: string, value: string) -> boolean
Adds or updates a value. If the specified ID does not exist, a new named value is added. If the ID does exist, the named value is updated with the specified value.
- **id** (string): The ID of the value to create or change.
- **value** (string): The string to assign to the value.
- **Returns** (boolean): Returns true is successful and false if it failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### idByIndex(index: uinteger) -> string
Function that returns the name of a value specified by its index.
- **index** (uinteger): The index of the item within the collection to return the name of. The first item in the collection has an index of 0 and the last item is the count of this collection minus 1.
- **Returns** (string): Returns the ID of the specified item or asserts if an out of bounds index is used.

### isExistingValue(id: string) -> boolean
Function that returns if a value with the specified ID exists or not.
- **id** (string): The ID of the value to check if it exists.
- **Returns** (boolean): Returns true if a value with the ID exists.

### remove(id: string) -> boolean
Removes the specified value from the collection.
- **id** (string): The ID of the value to remove.
- **Returns** (boolean): Returns true if the value was successfully removed and false if it failed. Failure is typically because the specified ID does not exist within the collection.

### value(id: string) -> string
Function that returns the specified value given its ID.
- **id** (string): The ID of the value, which was assigned when the value was created.
- **Returns** (string): Returns the value or an empty string if the specified ID was not found.

## Properties

### count : uinteger [read-only]
The number of values in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
