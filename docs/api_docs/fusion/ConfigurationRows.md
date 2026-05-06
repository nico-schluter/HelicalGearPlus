# ConfigurationRows
Namespace: adsk.fusion
Inherits: Base
Since: January 2024

Returns a collection of the rows in the table. The header row is not included in this list.

**Accessed from:** ConfigurationAppearanceTable.rows, ConfigurationCustomThemeTable.rows, ConfigurationMaterialTable.rows, ConfigurationPlasticRuleTable.rows, ConfigurationSheetMetalRuleTable.rows, ConfigurationTable.rows, ConfigurationTopTable.rows

## Methods

### add(name: string) -> ConfigurationRow
Adds a new row to the table. For the top table, this creates a new configuration. For theme tables, this creates a new theme. The new row is added to the bottom of the table, and the cell values are copied from the row above it. You can also use the ConfigurationRow.copy method to create a new row by copying any existing row.
- **name** (string): The name of the new row. An empty string can be provided, which will cause Fusion to use a default naming scheme to create a name.
- **Returns** (ConfigurationRow): Returns the newly created row.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ConfigurationRow
A method that returns the specified row using an index into the collection. These are returned in the same order as in the table; the first row is the default row.
- **index** (uinteger): The index of the row to return, where the first row is index 0. The headers do not count as a row.
- **Returns** (ConfigurationRow): Returns the specified row or null if an invalid index was specified.

### itemById(id: string) -> ConfigurationRow
A method that returns the row with the specified ID.
- **id** (string): The id of the row to return.
- **Returns** (ConfigurationRow): Returns the specified row or null if a row with the specified ID does not exist.

### itemByName(name: string) -> ConfigurationRow
A method that returns the row with the specified name.
- **name** (string): The name of the row to return.
- **Returns** (ConfigurationRow): Returns the specified row or null if the named row does not exist.

## Properties

### count : uinteger [read-only]
Returns the number of rows in the table where the header row is not included.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
