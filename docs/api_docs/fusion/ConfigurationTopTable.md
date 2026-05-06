# ConfigurationTopTable
Namespace: adsk.fusion
Inherits: ConfigurationTable
Since: January 2024

API object representing the top configuration table associated with a configured design.

When obtained from the DataFile object of a configured design, the functionality is limited because it's not loaded in Fusion, and there is no access to the Fusion objects represented in the table. For example, any properties that return a Component or Parameter will return null because those objects aren't available.

**Accessed from:** Design.configurationTopTable, Design.createConfiguredDesign, FlatPatternProduct.configurationTopTable, FlatPatternProduct.createConfiguredDesign, WorkingModel.configurationTopTable, WorkingModel.createConfiguredDesign

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getCell(column: uinteger, row: uinteger)
Returns the cell at the specified row and column.
- **column** (uinteger): The index of the column the cell is in. An index of 0 is the first column and does not include the name column.
- **row** (uinteger): The index of the row the cell is in. An index of 0 is the first row and does not include the header row.

### moveColumns(columns: ConfigurationColumn[], targetTable: ConfigurationCustomThemeTable) -> ConfigurationColumn
Moves the specified columns from one table to another.
- **columns** (ConfigurationColumn[]): An array of the columns within the top table you want to move.
- **targetTable** (ConfigurationCustomThemeTable): The table you want to move the columns to. The target must be a custom theme table.
- **Returns** (ConfigurationColumn): Returns an array of the columns created due to the move.

## Properties

### activeRow : ConfigurationRow [read-only]
Returns the row that is currently active. To set the active row, use the activate method on the ConfigurationRow object.

### appearanceTable : ConfigurationAppearanceTable [read-only]
Returns the appearance table associated with this top table. The returned table can be empty and not have any columns. In this case, the table is not displayed in the user interface. Use the returned table to add columns.

### columns : ConfigurationColumns [read-only]
Returns the columns defined for this table and provides the functionality to create new columns.

### customThemeTables : ConfigurationCustomThemeTables [read-only]
Returns any custom theme tables associated with this top table.

### id : string [read-only]
Returns the unique ID of this table.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### materialTable : ConfigurationMaterialTable [read-only]
Returns the material table associated with this top table. The returned table can be empty and not have any columns. In this case, the table is not displayed in the user interface. Use the returned table to add columns.

### name : string [read-only]
Gets the name of the table as seen in the user interface.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### plasticRuleTable : ConfigurationPlasticRuleTable [read-only]
Returns the plastic rule table associated with this top table. The returned table can be empty and not have any columns. In this case, the table is not displayed in the user interface. Use the returned table to add columns.

### rows : ConfigurationRows [read-only]
Returns the rows (configurations) defined for this table and provides the functionality to create new rows.

### sheetMetalRuleTable : ConfigurationSheetMetalRuleTable [read-only]
Returns the sheet metal rule table associated with this top table. The returned table can be empty and not have any columns. In this case, the table is not displayed in the user interface. Use the returned table to add columns.
