# Material
Namespace: adsk.core
Inherits: Base
Since: August 2014

A material.

**Accessed from:** BRepBody.material, Component.material, ConfigurationMaterialCell.material, FavoriteMaterials.add, FavoriteMaterials.item, FavoriteMaterials.itemById, FavoriteMaterials.itemByName, FlatPatternComponent.material, Material.copyTo, MaterialPreferences.defaultMaterial, Materials.addByCopy, Materials.item, Materials.itemById, Materials.itemByName, MeshBody.material, PlasticRule.material

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copyTo(target: Base) -> Material
This function is retired. See more information in the 'Remarks' section below.

Copies this material to the specified target.
- **target** (Base): The target can be a Design or MaterialFavorites object.
- **Returns** (Material): Returns the new copy of the material or null if the copy failed.

### deleteMe() -> boolean
Deletes the material from the Design. This method only applies to materials in a Design that are unused
- **Returns** (boolean): Returns true if the delete was successful.

## Properties

### appearance : Appearance [read-only]
Gets the Appearance of this material.

### description : string [read-write]
Gets and sets the description associated with this material. Setting the description is only valid for materials in a document or the favorites list.

### id : string [read-only]
Returns the unique internal ID of this material.

### isUsed : boolean [read-only]
Returns true if this material is used in the Design

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### materialProperties : Properties [read-only]
Returns the collection of material properties associated with this material.

### name : string [read-write]
Returns the name of this Material. This is the name of the material as seen in the user interface. The name can only be edited if the material is in a Design or the favorites list.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Returns the Parent object (a Library or a Design).
