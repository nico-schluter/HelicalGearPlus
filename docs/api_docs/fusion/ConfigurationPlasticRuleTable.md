# ConfigurationPlasticRuleTable
Namespace: adsk.fusion
Inherits: ConfigurationTable
Since: January 2024

Represents a configuration table that defines different plastic rules.

**Accessed from:** ConfigurationPlasticRuleColumn.parentPlasticRuleTable, ConfigurationTopTable.plasticRuleTable

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### clear() -> boolean
Clears the content of the plastic rule table, removes the reference from the top table, and hides it in the user interface.
- **Returns** (boolean): Returns true if successful.

### getCell(column: uinteger, row: uinteger)
Returns the cell at the specified row and column.
- **column** (uinteger): The index of the column the cell is in. An index of 0 is the first column and does not include the name column.
- **row** (uinteger): The index of the row the cell is in. An index of 0 is the first row and does not include the header row.

## Properties

### columns : ConfigurationPlasticRuleColumns [read-only]
Returns the collection that provides access to the columns in this table.

### id : string [read-only]
Returns the unique ID of this table.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
Returns the name of the table as seen in the user interface.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentTableColumn : ConfigurationThemeColumn [read-only]
Returns the column in the top table that references this plastic rule table.

### rows : ConfigurationRows [read-only]
Returns the rows (configurations) defined for this table and provides the functionality to create new rows.
