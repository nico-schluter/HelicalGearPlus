# CAMPatterns
Namespace: adsk.cam
Inherits: Base
Since: January 2016

Collection that provides access to the patterns within an existing setup, folder or pattern.

**Accessed from:** CAMFolder.patterns, CAMPattern.patterns, Setup.patterns

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> CAMPattern
Function that returns the specified pattern using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (CAMPattern): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> CAMPattern
Returns the pattern with the specified name (as appears in the browser).
- **name** (string): The name (as it appears in the browser) of the pattern.
- **Returns** (CAMPattern): Returns the specified pattern or null in the case where there is no pattern with the specified name.

### itemByOperationId(id: integer) -> CAMPattern
Returns the pattern with the specified operation id.
- **id** (integer): The id of the pattern.
- **Returns** (CAMPattern): Returns the specified pattern or null in the case where there is no pattern with the specified operation id.

## Properties

### count : uinteger [read-only]
The number of items in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
