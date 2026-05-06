# FusionUnitsManager
Namespace: adsk.fusion
Inherits: UnitsManager
Since: August 2014

Utility class used to work with Values and control default design units. Internal values are held in SI units (e.g. seconds, radians, kg for time, angle, mass) with the exception that all lengths are in cm rather than meter and this affects derived units (e.g. velocity is cm/s, volume is cm^3). Units are specified flexibly via strings (e.g. "cm", "in", "inch", "cm^3", "cm*cm*cm", "mph", "mps" "m/s").

**Accessed from:** Design.fusionUnitsManager, FlatPatternProduct.fusionUnitsManager, WorkingModel.fusionUnitsManager

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### convert(valueInInputUnits: double, inputUnits: string, outputUnits: string) -> double
Converts a value from one unit to another. The input and output unit specifiers must be compatible. For example, "in" (inches) and "cm" (centimeters) will work because they both define length. So Convert(1.5, "in", "ft") -> 0.125 Convert(1.5, unitsManager.defaultLengthUnits, "cm") -> depends on the current default distance units, with "mm" it gives 0.15 So Convert(1.5, "in", "kg") -> -1 and GetLastError returns ExpressionError (to denote error) So Convert(1, "in", "internalUnits") -> 2.54 So Convert(1, "internalUnits", "in") -> 0.3937...
- **valueInInputUnits** (double): The value to convert
- **inputUnits** (string): The units of the value to convert
- **outputUnits** (string): The units to convert the value to
- **Returns** (double): Returns -1 AND GetLastError returns ExpressionError in the event of an error.

### evaluateExpression(expression: string, units: string) -> double
Gets the value (in internal units) of the expression.
- **expression** (string): EvaluateExpression("1cm + 1in") -> 3.54 EvaluateExpression("1") -> -> depends on the DistanceUnits, with "mm" it gives 0.1
- **units** (string): If not supplied the units will default to the default length specified in the preferences.

This is an optional argument whose default value is "DefaultDistance".
- **Returns** (double): Returns -1 AND GetLastError will return ExpressionError in the event of an error.

### formatInternalValue(internalValue: double, displayUnits: string, showUnits: boolean) -> string
This function is retired. See more information in the 'Remarks' section below.

Formats the internal value as a string. The output string is formatted using the current unit settings in preferences. The preferences control the number of decimal places, whether units are abbreviated and several other things. FormatInternalValue(1.5, "in") -> "0.591 in" FormatInternalValue(1.5, "in", false) -> "0.591" FormatInternalValue(1.5, "mm", true) -> "15.00 mm" FormatInternalValue(1.5) -> depends on DistanceUnits, might be "15.0 mm"
- **internalValue** (double): The internal value to format.
- **displayUnits** (string): The units to display the value in. If not supplied the units will default to the default length specified in the preferences.

This is an optional argument whose default value is "DefaultDistance".
- **showUnits** (boolean): Specify false to exclude units from the format. The default is true.

This is an optional argument whose default value is True.
- **Returns** (string): Returns an empty string if the units are incorrectly specified.

### formatUnits(units: string) -> string
Formats the unit according to the user preferences "centimeter" -> "cm" "inch" -> "in" "cm* cm *cm / s" -> , "cm^3 / s"
- **units** (string): The unit to use when converting the value into a string.
- **Returns** (string): Returns an empty string and GetLastError returns ExpressionError in the event of an error.

### formatValue(value: double, units: string, precision: integer, showTrailingZeros: BooleanOptions, minimumPrecision: integer, showUnits: boolean) -> string
Given a floating point number this method evaluates it as a value of a specific unit type and returns an appropriate string. By default, the current unit settings defined in the user preferences is used, but you can set the method arguments to override the defaults to specify the formatting you want. The input value always uses internal units, which are centimeters for length, radians for angles, and mass is in kilograms.

This method is useful whenever you have a value you've gotten from Fusion or computed on your own and need to display it to the user as a string. This method does the conversion and also takes into account the units and the formatting the user has specified in their preferences.

Below are some examples of various formatting where the user preferences for general precision is four decimal places, and the angular precision is one decimal place. Also, trailing zeros are set to be hidden and the minimum precision is two decimal places when trailing zeros are turned off. The design units are specified to be "inch".

Here, only the value is supplied and the default is to assume the units are the current design length unit and use the preference settings to format it so there are four decimal places shown and the unit name is included. formatValue(1.5) -> "0.5906 in"

In this example, an angle is specified by using "deg" as the unit, and the result showing one decimal place, which is what's defined in the user preference, and it shows the unit name. formatValue(0.7853981633974483096, "deg") -> "45.0 deg"

This example converts the input value of 1.5 cm to mm where eight decimal places are shown, trailing zeros are shown, and the unit name is shown. The fourth argument of minimum precision is ignored, since it is only used when showTrailing zeros is False. formatValue(1.5, "mm", 8, BooleanOptions.TrueBooleanOption, 0, True) - > "15.00000000 mm"
- **value** (double): A floating point value that is assumed to use the internal unit type, which are centimeters for length, radians for angles, and mass is in kilograms.
- **units** (string): The units the value represents. The default value for this argument is "DefaultDistance" which means it will use the default distance units defined for the active design.

This is an optional argument whose default value is "DefaultDistance".
- **precision** (integer): This specifies the number of decimal places to display. The default value is -1 which indicates the precision specified in preferences should be used. A maximum of 9 can be used and any larger numbers will be forced to 9.

This is an optional argument whose default value is -1.
- **showTrailingZeros** (BooleanOptions): Specifies if trailing zeros should be shown or not. The default value is to use the preference setting.

This is an optional argument whose default value is BooleanOptions.DefaultBooleanOption.
- **minimumPrecision** (integer): When trailing zeros are not displayed, this specifies a minimum precision where some trailing zeros are still shown. The default value is -1 which indicates the minimum precision specified in preferences should be used. A maximum of 8 can be used, and any larger numbers will be forced to 8.

This is an optional argument whose default value is -1.
- **showUnits** (boolean): This specifies whether the unit name or symbol should be included in the result.

This is an optional argument whose default value is True.
- **Returns** (string): Returns the formatted string or an empty string in case of an error.

### isValidExpression(expression: string, units: string) -> boolean
Checks to see if the given expression is valid.
- **expression** (string): The expression to validate.
- **units** (string): The units to use when validating the expression.
- **Returns** (boolean): Returns True if it is a valid expression.

### standardizeExpression(expression: string, units: string) -> string
Standardizes the expression in terms of spacing and user preferences. StandardizeExpression("1.5") -> depends on distance units, but with might be "1.5 mm" StandardizeExpression("1.5", "in") -> "1.5 in" StandardizeExpression("1.5 cm + 1.50001 centimeter") -> "1.5 cm + 1.50001 cm" StandardizeExpression("1.5", "m * m * m / s") -> "1.5 m^3 /s"
- **expression** (string): The expression to standardize
- **units** (string): The units to apply to the standardized expression. If not supplied the units will default to the default length specified in the preferences.

This is an optional argument whose default value is "DefaultDistance".
- **Returns** (string): Returns an empty string AND GetLastError returns ExpressionError in the event of an error.

## Properties

### defaultLengthUnits : string [read-only]
Returns the unit strings for the current default length unit as specified in preferences. - e.g. "cm" or "in" This is the string that is being used by Fusion to represent the current length unit and is affected by the preference settings that let the user choose whether abbreviations and symbols can be used. This means that inch length units can be returned as inch, in, or ". If you need a consistent way of determining the current length unit, the distanceDisplayUnits of the FusionUnitsManager object returns an enum value.

### design : Design [read-only]
Returns the parent design

### distanceDisplayUnits : DistanceUnits [read-write]
Gets and sets the default distance units for this design. Setting this property has the side effect of changing the unitSystem property to custom.

### internalUnits : string [read-only]
Returns a string that represents internal units - i.e. "internalUnits". This can be used when performing conversions via Convert.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### massDisplayUnits : MassUnits [read-write]
Gets and sets the default mass units for this design. Setting this property has the side effect of changing the unitSystem property to custom.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### product : Product [read-only]
Returns the parent Product.

### unitSystem : UnitSystems [read-write]
Gets and sets the pre-defined combination of length and mass units to use for the units in the design. The distanceDisplayUnits and massDisplayUnits properties provide a way to get the current setting for distance and mass and to modify them to other values besides the predefined combinations. When a custom unit system is specified, any combination of distance and mass can be specified.
