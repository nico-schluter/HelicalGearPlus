# ConfigurationSheetMetalRuleCell
Namespace: adsk.fusion
Inherits: ConfigurationCell
Since: January 2024

Represents a single cell within a configuration table that controls which sheet metal rule is assigned to a component.

**Accessed from:** ConfigurationSheetMetalRuleColumn.getCell, ConfigurationSheetMetalRuleColumn.getCellByRowId, ConfigurationSheetMetalRuleColumn.getCellByRowName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentColumn : ConfigurationSheetMetalRuleColumn [read-only]
Returns the column this cell is in.

### parentRow : ConfigurationRow [read-only]
Returns the row this cell is in.

### sheetMetalRule : SheetMetalRule [read-write]
Gets and sets the sheet metal rule defined for this cell.
