# ConfigurationCustomThemeTable
Namespace: adsk.fusion
Inherits: ConfigurationTable
Since: January 2024

API object representing a custom theme configuration table associated with a top table.

**Accessed from:** ConfigurationCustomThemeTables.add, ConfigurationCustomThemeTables.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe(deleteColumns: boolean) -> boolean
Deletes this custom theme table from the configuration.
- **deleteColumns** (boolean): If true, this deletes the columns in the custom theme table. If false, it moves them back to the top table.
- **Returns** (boolean): Returns true if the delete was successful.

### getCell(column: uinteger, row: uinteger)
Returns the cell at the specified row and column.
- **column** (uinteger): The index of the column the cell is in. An index of 0 is the first column and does not include the name column.
- **row** (uinteger): The index of the row the cell is in. An index of 0 is the first row and does not include the header row.

### moveColumns(columns: ConfigurationColumn[], targetTable: ConfigurationTable) -> ConfigurationColumn
Moves the specified columns from one table to another.
- **columns** (ConfigurationColumn[]): An array of the columns within this table that you want to move.
- **targetTable** (ConfigurationTable): The table you want to move the columns to. The target must be either a top table or a custom theme table.
- **Returns** (ConfigurationColumn): Returns an array of the columns created due to the move.

## Properties

### columns : ConfigurationColumns [read-only]
Returns the columns in this table.

### id : string [read-only]
Returns the unique ID of this table.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets and sets the name of the table as seen in the user interface.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentTableColumn : ConfigurationThemeColumn [read-only]
Returns the column in the top table that references this custom theme table.

### rows : ConfigurationRows [read-only]
Returns the rows (configurations) defined for this table and provides the functionality to create new rows.
