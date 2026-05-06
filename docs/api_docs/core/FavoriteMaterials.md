# FavoriteMaterials
Namespace: adsk.core
Inherits: Base
Since: August 2014

Collection of the favorite materials.

**Accessed from:** Application.favoriteMaterials

## Methods

### add(material: Material) -> Material
Adds an existing material to the Favorites list
- **material** (Material): The material to be added to the favorites list. This can come from a Library or from a Design.
- **Returns** (Material): Returns the Material added to the favorites list or null if the operation failed.

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
