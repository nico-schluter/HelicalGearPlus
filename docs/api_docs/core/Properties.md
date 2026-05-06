# Properties
Namespace: adsk.core
Inherits: Base
Since: August 2014

A collection of properties that are associated with a material or appearance.

**Accessed from:** Appearance.appearanceProperties, AppearanceTexture.properties, Material.materialProperties

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: integer) -> Property
Returns the specified property from the collection using an index into the collection.
- **index** (integer): The index of the property within the collection where the first item is 0.
- **Returns** (Property): Returns the specified item or null if an invalid index was specified.

### itemById(id: string) -> Property
Returns the specified property from the collection using the unique ID of the property.
- **id** (string): The unique ID of the property.
- **Returns** (Property): Returns the specified property or null if the ID doesn't match a property within the collection.

### itemByName(name: string) -> Property
Returns the specified Property using the name of the property.
- **name** (string): The name of the property to return. This is the name as seen in the user interface.
- **Returns** (Property): Returns the specified property or null if the name doesn't match a property within the collection.

## Properties

### count : uinteger [read-only]
Returns the number of properties within the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
