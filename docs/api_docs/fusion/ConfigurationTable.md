# ConfigurationTable
Namespace: adsk.fusion
Inherits: Base
Since: January 2024

The base class of all configuration tables.

**Accessed from:** ConfigurationFeatureAspectColumn.parentTable, ConfigurationInsertColumn.parentTable, ConfigurationInsertStandardDesignColumn.parentTable, ConfigurationJointSnapColumn.parentTable, ConfigurationParameterColumn.parentTable, ConfigurationPropertyColumn.parentTable, ConfigurationRow.parentTable, ConfigurationSuppressColumn.parentTable, ConfigurationThemeColumn.parentTable, ConfigurationThemeColumn.referencedTable, ConfigurationVisibilityColumn.parentTable

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getCell(column: uinteger, row: uinteger)
Returns the cell at the specified row and column.
- **column** (uinteger): The index of the column the cell is in. An index of 0 is the first column and does not include the name column.
- **row** (uinteger): The index of the row the cell is in. An index of 0 is the first row and does not include the header row.

## Properties

### id : string [read-only]
Returns the unique ID of this table.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### rows : ConfigurationRows [read-only]
Returns the rows (configurations) defined for this table and provides the functionality to create new rows.
