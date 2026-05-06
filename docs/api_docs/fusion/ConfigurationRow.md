# ConfigurationRow
Namespace: adsk.fusion
Inherits: Base
Since: January 2024

Represents a row in a configuration table. The header row is not considered a standard row but is information associated with each column.

For a top table, each row represents a configuration, and for a theme table, each row represents a theme.

**Accessed from:** ConfigurationAppearanceCell.parentRow, ConfigurationCell.parentRow, ConfigurationFeatureAspectBooleanCell.parentRow, ConfigurationFeatureAspectStringCell.parentRow, ConfigurationInsertCell.parentRow, ConfigurationInsertCell.row, ConfigurationInsertStandardDesignCell.parentRow, ConfigurationJointSnapCell.parentRow, ConfigurationMaterialCell.parentRow, ConfigurationParameterCell.parentRow, ConfigurationPlasticRuleCell.parentRow, ConfigurationPropertyCell.parentRow, ConfigurationRow.copy, ConfigurationRows.add, ConfigurationRows.item, ConfigurationRows.itemById, ConfigurationRows.itemByName, ConfigurationSheetMetalRuleCell.parentRow, ConfigurationSuppressCell.parentRow, ConfigurationThemeCell.parentRow, ConfigurationThemeCell.referencedTableRow, ConfigurationTopTable.activeRow, ConfigurationVisibilityCell.parentRow, Occurrence.configurationRow

## Methods

### activate() -> boolean
Causes this row to become the active row in the table.
- **Returns** (boolean): Returns true if the activation was successful.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy(name: string) -> ConfigurationRow
Creates a new row by copying this row.
- **name** (string): The name to use for the new row. An empty string indicates that Fusion should use the default naming scheme.

Names must be unique with respect to other rows in this table. If you specify a name that exists, Fusion will append a counter to ensure uniqueness. For example, if "Small" is already used and you name another row "Small", you will end up with "Small (1)".
- **Returns** (ConfigurationRow): Returns the newly created row or null in the case of failure.

### deleteMe() -> boolean
Deletes this row from the table. The first row of the top table cannot be deleted, and this method will fail.
- **Returns** (boolean): Returns true if the deletion was successful.

### generate() -> ConfigurationFuture
Causes this row to be generated.
- **Returns** (ConfigurationFuture): Returns a future that can be used to determine when the generation is complete. Null is returned in the case where starting the generation fails.

### getCellByColumnId(columnId: string) -> ConfigurationCell
Gets the cell in this row at the column with the specified ID.
- **columnId** (string): The ID of the column the cell is in.
- **Returns** (ConfigurationCell): Returns the specified cell if successful or null if a column with the specified ID does not exist.

### getCellByColumnIndex(columnIndex: uinteger) -> ConfigurationCell
Gets the cell in this row at the specified column index. The first column has an index of 0 and does not include the name column.
- **columnIndex** (uinteger): The index of the column to return the cell for. The first column has an index 0.
- **Returns** (ConfigurationCell): Returns the specified cell if successful and null if an invalid index was specified.

## Properties

### id : string [read-only]
Gets the unique ID that identifies this row. The ID remains constant for this row as long as the row exists. This is different than the name, which the user can change.

### index : uinteger [read-only]
The index position of this row within the table. The first row is at index 0 and does not include the header row.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets and sets the name of this row. Names must be unique with respect to other rows in this table. If you specify a name that exists, Fusion will append a counter to ensure uniqueness. For example, if "Small" is already used and you name another row "Small", you will end up with "Small (1)".

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentTable : ConfigurationTable [read-only]
Returns the configuration table this row is a member of.
