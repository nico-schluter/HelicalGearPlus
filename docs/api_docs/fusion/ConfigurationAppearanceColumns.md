# ConfigurationAppearanceColumns
Namespace: adsk.fusion
Inherits: Base
Since: January 2024

Provides access to the columns in an appearance table. This collection can be empty when no columns have been created. When the table is empty, it is not displayed in the user interface, and adding a column causes the table to be displayed.

**Accessed from:** ConfigurationAppearanceTable.columns

## Methods

### add(entity: Base) -> ConfigurationAppearanceColumn
Adds a new column to the appearance table. If you are adding the first column to the table and it is anything other than the root component, an additional column for the root component will automatically be created as the first column.
- **entity** (Base): The root component, occurrence, or body whose appearance will be controlled by this column.
- **Returns** (ConfigurationAppearanceColumn): Returns the newly created ConfigurationAppearanceColumn object or null if it fails.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ConfigurationAppearanceColumn
A method that returns the specified column using an index into the collection. These are returned in the same order as they appear in the table.
- **index** (uinteger): The index of the column to return, where the first column is index 0. The name column is not included.
- **Returns** (ConfigurationAppearanceColumn): Returns the specified column or null if an invalid index was specified.

### itemById(id: string) -> ConfigurationAppearanceColumn
A method that returns the column with the specified ID.
- **id** (string): The id of the column to return.
- **Returns** (ConfigurationAppearanceColumn): Returns the specified column or null if a column with the specified ID does not exist.

## Properties

### count : uinteger [read-only]
Returns the number of columns in the table where the name column is not included.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
