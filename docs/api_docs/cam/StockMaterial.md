# StockMaterial
Namespace: adsk.cam
Inherits: Base
Since: September 2024

Represents a StockMaterial.

**Accessed from:** DocumentStockMaterialLibrary.item, Setup.stockMaterial, StockMaterial.createFromJson, StockMaterialLibrary.childStockMaterials, StockMaterialLibrary.stockMaterialAtURL

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createFromJson(json: string) -> StockMaterial
Creates a StockMaterial object from given JSON string.
- **json** (string): The JSON should fully define the StockMaterial and contain all StockMaterial parameters. If the JSON contains more than one StockMaterial, only the first StockMaterial is loaded.
- **Returns** (StockMaterial): Returns the newly created StockMaterial.

### toJson() -> string
Generates and returns a JSON string that contains a description of this StockMaterial.
- **Returns** (string): Returns a JSON string that contains a description of this StockMaterial.

## Properties

### category : string [read-write]
Gets and sets the category of the stock material.

### designators : array [read-write]
Gets a list of designators of the stock material.

### hardness : double [read-write]
Get and sets the hardness of the stock materials. NOTE: the hardness can be NaN if not set. and user can set the hardness to NaN.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets and sets the name of the stock material.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
