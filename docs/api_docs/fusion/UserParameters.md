# UserParameters
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Provides access to the User Parameters within a design and provides methods to create new user parameters.

**Accessed from:** Design.userParameters, FlatPatternProduct.userParameters, UserParameter.userParameters, WorkingModel.userParameters

## Methods

### add(name: string, value: ValueInput, units: string, comment: string) -> UserParameter
Adds a new user parameter to the collection.
- **name** (string): The name of the parameter. This is the name shown in the parameters dialog
- **value** (ValueInput): ValueInput object that specifies the value of the parameter. If the ValueInput was created using a real, the value will be interpreted using the internal unit for the unit type specified by the "units" argument. For example, if the ValueInput was created using the real value 5 and the input to the "units" argument is any valid length unit, the value will be interpreted as 5 centimeters since centimeters is the internal unit for lengths. If the "units" argument is a valid angle unit the value will be interpreted as 5 radians.

If the ValueInput was created using a string, the string is used as-is for the expression of the parameter. For value parameters, this means if there are units as part of the string, it must evaluate to the same unit type as that specified by the "units" argument and if no units are specified it will use the current default units specified for the current document. For example, if the ValueInput was created with the string "5 in", then the "units" argument must define any valid length so they are compatible. If the ValueInput was created with the string "5", any unit type can be used and the result will be 5 of that unit.

If the "units" argument is "Text" then a text parameter will be created using the value provided as the expression.

When using a ValueInput created using a string, it's the same as creating a parameter in the user-interface. You can specify any valid expression, i.e. "5", "5 in", "5 in / 2", "5 + Length", etc. and you can choose from many different types of units. The only requirement is that the units must match in type. For example, they must both be lengths, or they must both be angles.

When creating a Boolean parameter, you should use the createByBoolean method of the ValueInput object.
- **units** (string): The units to use for the value of the parameter. The use of any of the measurement units will result in the creation of a numeric parameter. The units specified must match the units specified (if any) in the ValueInput object.

To create a parameter with no units, you can specify an empty string as the units, which will also create a numeric parameter. To create a text parameter, use "Text" as the unit type.
- **comment** (string): The comment to display in the parameters dialog. Specify an empty string ("") for no comment
- **Returns** (UserParameter): Returns the newly created UserParameter or null if the creation failed.

### asArray() -> UserParameter
Returns the user parameters in the design as an array.
- **Returns** (UserParameter): Returns an array of the user parameters in the design.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### exportUserParameters(userParameterArray: UserParameter[], filename: string) -> boolean
Function that exports a list of user parameters to a csv file.
- **userParameterArray** (UserParameter[]): The array of user parameters to export.
- **filename** (string): The full filename (path and file) of the file to write the parameters to.
- **Returns** (boolean): Returns whether the export was successful.

### importUserParameters(filename: string) -> boolean
Function that imports a list of user parameters from a csv file.

The format of the csv file is as follows: It must have at least two rows - Header followed by a row of parameter. It must be encoded in UTF8 format. It must contain at least six columns - name, unit, expression, value, comment, and favorite where favorite is either true or false. The columns must only have a comma delimiter. Any locale will work but no thousands. expression column support double quotes. comment can either be single line or multi line. If multi line, it must be in double quotes.

Here is an example of a csv file with two rows Name,Unit,Expression,Value,Comments,Favorite p1,mm,32 mm,32,the first parameter,FALSE

The function exportUserParameters could be used to see what a csv file looks like.
- **filename** (string): The full filename (path and file) of the file to read the parameters from.
- **Returns** (boolean): Returns whether the import was successful.

### item(index: uinteger) -> UserParameter
Function that returns the specified User Parameter using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (UserParameter): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> UserParameter
Function that returns the specified User Parameter using the name of the parameter as it is displayed in the parameters dialog.
- **name** (string): The name of the User Parameter as it is displayed in the parameters dialog
- **Returns** (UserParameter): Returns the specified item or null if an invalid name was specified.

## Properties

### count : uinteger [read-only]
Returns the number of parameters in the collection.

### design : Design [read-only]
Returns the design that owns the user parameters collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Set parameters from a csv file and export to STEP**: Reads data from a .csv file and sets user parameters in the model and then exports the model to STEP. When setting parameters be aware that this sample is setting user parameters. It's also possible to set model parameters but that's not demonstrated here. Also when accessing parameters, it is case sensitive so the names you use in your program much exactly match the names in the model.
