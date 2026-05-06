# ConfigurationCustomThemeTables
Namespace: adsk.fusion
Inherits: Base
Since: January 2024

Provides access to the custom theme tables associated with a configuration table and provides the functionality to create new custom theme tables.

**Accessed from:** ConfigurationTopTable.customThemeTables

## Methods

### add(columns: ConfigurationColumn[]) -> ConfigurationCustomThemeTable
Creates a new custom theme table using the specified columns.
- **columns** (ConfigurationColumn[]): An array of ConfigurationColumn objects used to create a new custom theme table. The columns must exist within the top configuration table, and they cannot include any ConfigurationThemeColumn, ConfigurationPropertyColumn, ConfigurationAppearanceColumn, ConfigurationMaterialColumn, ConfigurationPlasticRuleColumn, or ConfigurationSheetMetalRuleColumn objects. The specified columns will be removed from the main table, and a new ConfigurationThemeColumn will be created in the top table to reference the newly created custom theme table.
- **Returns** (ConfigurationCustomThemeTable): Returns the newly created ConfigurationCustomThemeTable or null if the creation fails.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ConfigurationCustomThemeTable
A method that returns the specified custom theme table using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ConfigurationCustomThemeTable): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of custom theme tables associated with the top table.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
