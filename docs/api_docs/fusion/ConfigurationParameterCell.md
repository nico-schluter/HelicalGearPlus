# ConfigurationParameterCell
Namespace: adsk.fusion
Inherits: ConfigurationCell
Since: January 2024

Represents a single cell within a configuration table that controls the value of a parameter. Get the parent column to get the parameter being controlled.

**Accessed from:** ConfigurationParameterColumn.getCell, ConfigurationParameterColumn.getCellByRowId, ConfigurationParameterColumn.getCellByRowName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### expression : string [read-write]
Gets and sets the expression that defines the value of the associated parameter when the parent row is active. This works for both numeric and text parameters. This property behaves as read-only when the table is obtained from a DataFile object.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentColumn : ConfigurationParameterColumn [read-only]
Returns the column this cell is in. From the column, you can get the parameter object being controlled.

### parentRow : ConfigurationRow [read-only]
Returns the row this cell is in.

### textValue : string [read-write]
Gets and sets the text value of the parameter when it is a text parameter. This can be determined by checking the valueType property. Setting this value will cause the current expression to be overwritten. This property behaves as read-only when the table is obtained from a DataFile object.

### value : double [read-write]
Gets and sets the real value (a double) of the parameter in database units. Setting this property will overwrite any existing expression. This property behaves as read-only when the table is obtained from a DataFile object. This property is only valid for numeric parameters and will fail for text parameters. You can determine the value type of the parameter by using the valueType property. Use the textValue property to get and set the value of text parameters.

### valueType : ParameterValueTypes [read-only]
Returns the type of value this parameter cell is. For a numeric parameter, you can get the value using the value property. For a text parameter, you can get the value using the textValue property.
