# Materials
Namespace: adsk.core
Inherits: Base
Since: August 2014

Collection of materials within a Library or Design.

**Accessed from:** Design.materials, FlatPatternProduct.materials, MaterialLibrary.materials, WorkingModel.materials

## Methods

### addByCopy(materialToCopy: Material, name: string) -> Material
Add a Material to a Design by copying an existing Material from Favorites, a Library or from the Materials stored in the Design. This method currently only applies to the Materials collection from a Design and cannot be used to copy a Material to a library.
- **materialToCopy** (Material): The Material you want to copy. The Material to copy can be from Favorites, a Library or from the materials stored in the Design.
- **name** (string): The Material name to apply to the copy.
- **Returns** (Material): Returns the newly created Material or null if the copy operation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: integer) -> Material
Returns the specified Material using an index into the collection.
- **index** (integer): The index of the material to return where the first item in the collection is 0.
- **Returns** (Material): Returns the specified material or null if an invalid index is specified.

### itemById(id: string) -> Material
Returns the Material by it's internal unique ID.
- **id** (string): The ID of the material to return.
- **Returns** (Material): Returns the specified material or null if there isn't a matching ID.

### itemByName(name: string) -> Material
Returns the specified Material using the name as seen in the user interface. This often isn't a reliable way of accessing a specific material because materials are not required to be unique.
- **name** (string): The name of the material to return,.
- **Returns** (Material): Returns the specified material or null if there isn't a matching name.

## Properties

### count : uinteger [read-only]
The number of Materials in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
