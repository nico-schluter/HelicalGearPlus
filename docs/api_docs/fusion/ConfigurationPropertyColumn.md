# ConfigurationPropertyColumn
Namespace: adsk.fusion
Inherits: ConfigurationColumn
Since: January 2024

Represents a property column in a configuration table.

**Accessed from:** ConfigurationColumns.addPropertyColumn, ConfigurationPropertyCell.parentColumn

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this column from the table. Property columns cannot be deleted. If the table was obtained from a DataFile, this method will fail.
- **Returns** (boolean): Returns true if the deletion was successful.

### getCell(rowIndex: uinteger) -> ConfigurationPropertyCell
Gets the cell in this column at the specified row. The first row has an index of 0 and does not include the header row.
- **rowIndex** (uinteger): The index of the row to return the cell for. The first row has an index of 0.
- **Returns** (ConfigurationPropertyCell): Returns the specified cell if successful and null if an invalid index was specified.

### getCellByRowId(rowId: string) -> ConfigurationPropertyCell
Gets the cell in this column at the row specified by its ID.
- **rowId** (string): The ID of the row to return the cell for.
- **Returns** (ConfigurationPropertyCell): Returns the specified cell if successful and null if the id is not found.

### getCellByRowName(rowName: string) -> ConfigurationPropertyCell
Gets the cell in this column at the row specified by its name.
- **rowName** (string): The name of the row to return the cell for.
- **Returns** (ConfigurationPropertyCell): Returns the specified cell if successful and null if the name is not found.

## Properties

### id : string [read-only]
The id of the column. This is constant and cannot be changed by the user.

### index : uinteger [read-only]
The index position of this column within the table. The first column is at index 0 and does not include the "Name" column.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentProperty : Property [read-only]
Returns the property whose value is controlled by this column.

### parentTable : ConfigurationTable [read-only]
Returns the parent table this column is in.

### rowCount : uinteger [read-only]
Returns the number of rows in this column.

### title : string [read-write]
The title of this column. In a top table, this can only be edited for suppression, visibility, parameter, and theme table columns. It behaves as read-only for all other types. In a theme table, the title of all the columns can be modified except for the column that represents the root component for materials and appearances.

If the table was obtained from a DataFile, this property behaves as read-only for all the columns.
