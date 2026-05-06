# PlasticRules
Namespace: adsk.fusion
Inherits: Base
Since: January 2024

A collection of plastic rules.

**Accessed from:** Design.designPlasticRules, Design.libraryPlasticRules, FlatPatternProduct.designPlasticRules, FlatPatternProduct.libraryPlasticRules, WorkingModel.designPlasticRules, WorkingModel.libraryPlasticRules

## Methods

### addByCopy(existingPlasticRule: PlasticRule, name: string) -> PlasticRule
Creates a new plastic rule by copying an existing rule. The new rule can then be edited to define the rule characteristics you want.
- **existingPlasticRule** (PlasticRule): The existing PlasticRule object you want to copy. This can be a rule from the library or the design.
- **name** (string): The name to assign to the new plastic rule. This name must be unique with respect to other plastic rules in the design or library it's created in.
- **Returns** (PlasticRule): Returns the new PlasticRule object or will assert in the case where it fails.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> PlasticRule
Function that returns the specified plastic rule using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (PlasticRule): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> PlasticRule
Function that returns the specified plastic rule using the name of the rule.
- **name** (string): The name of the rule within the collection to return. This is the name seen in the Plastic Rules dialog.
- **Returns** (PlasticRule): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of plastic rules in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
