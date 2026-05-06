# SheetMetalRules
Namespace: adsk.fusion
Inherits: Base
Since: November 2022

A collection of sheet metal rules.

**Accessed from:** Design.designSheetMetalRules, Design.librarySheetMetalRules, FlatPatternProduct.designSheetMetalRules, FlatPatternProduct.librarySheetMetalRules, WorkingModel.designSheetMetalRules, WorkingModel.librarySheetMetalRules

## Methods

### addByCopy(existingSheetMetalRule: SheetMetalRule, name: string) -> SheetMetalRule
Creates a new sheet metal rule by copying an existing rule. The new rule can then be edited to define the rule characteristics you want.
- **existingSheetMetalRule** (SheetMetalRule): The existing SheetMetalRule object you want to copy. This can be a rule from the library or the design.
- **name** (string): The name to assign to the new sheet metal rule. This name must be unique with respect to other sheet metal rules in the design or library it's created in.
- **Returns** (SheetMetalRule): Returns the new SheetMetalRule object or will assert in the case where it fails.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SheetMetalRule
Function that returns the specified sheet metal rule using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SheetMetalRule): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> SheetMetalRule
Function that returns the specified sheet metal rule using the name of the rule.
- **name** (string): The name of the rule within the collection to return. This is the name seen in the Sheet Metal Rules dialog.
- **Returns** (SheetMetalRule): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of sheet metal rules in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Sheet Metal Rules Sample**: Demonstrates creating adding a sheet metal rule.
