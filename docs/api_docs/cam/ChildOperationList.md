# ChildOperationList
Namespace: adsk.cam
Inherits: Base
Since: January 2016

Provides access to the collection of child operations, folders and patterns of an existing setup.

**Accessed from:** CAMFolder.children, CAMHoleRecognition.children, CAMPattern.children, Setup.children

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Base
Returns the specified item using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Base): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> Base
Returns the operation, folder or pattern with the specified name (the name seen in the browser).
- **name** (string): The name of the operation, folder or pattern as seen in the browser.
- **Returns** (Base): Returns the specified item or null in the case where there is no item with the specified name.

### itemByOperationId(id: integer) -> Base
Returns the operation, folder or pattern with the specified operation id.
- **id** (integer): The id of the operation, folder or pattern.
- **Returns** (Base): Returns the specified item or null in the case where there is no item with the specified operation id.

## Properties

### count : uinteger [read-only]
Gets the number of objects in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
