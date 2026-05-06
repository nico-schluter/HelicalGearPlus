# DocumentStockMaterialLibrary
Namespace: adsk.cam
Inherits: Base
Since: September 2024

DocumentStockMaterialLibrary provides access to stock materials used by the document.

**Accessed from:** CAM.documentStockMaterialLibrary

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> StockMaterial
Get StockMaterial by index in DocumentStockMaterialLibrary.
- **index** (uinteger): Index of the StockMaterial in the DocumentStockMaterialLibrary.
- **Returns** (StockMaterial): Returns the StockMaterial in the DocumentStockMaterialLibrary by given index.

### setupsByStockMaterial(stockMaterial: StockMaterial) -> Setup
Returns all setups that use the given StockMaterial. The StockMaterial must exist in the document StockMaterial library. Raises an error if the StockMaterial is not in the document.
- **stockMaterial** (StockMaterial): The StockMaterial to search for setups. The StockMaterial must exist in the document.
- **Returns** (Setup): Returns setups using a specific StockMaterial.

### update(stockMaterial: StockMaterial) -> boolean
Update the given StockMaterial in the document StockMaterial library. The update applies all changes to the stockMaterial in the document stockMaterial library and therefore on all setups that use the stockMaterial. Will error if the stockMaterial does not exist in the document stockMaterial library.
- **stockMaterial** (StockMaterial): The StockMaterial that should be updated.
- **Returns** (boolean): Returns true if the update was successful.

## Properties

### count : uinteger [read-only]
The number of StockMaterial in the DocumentStockMaterialLibrary.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
