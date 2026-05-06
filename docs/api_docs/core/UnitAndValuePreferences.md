# UnitAndValuePreferences
Namespace: adsk.core
Inherits: Base
Since: August 2014

The UnitAndValuePreferences object provides access to unit and value precision related preferences.

**Accessed from:** Preferences.unitAndValuePreferences

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### angularPrecision : integer [read-write]
Gets and sets the angular precision. This value specifies the number of decimals to display.

### areAbbreviationsForUnitDisplayed : boolean [read-write]
Gets and sets if abbreviations are used for units display.

### areSymbolsForUnitDisplayed : boolean [read-write]
Gets and sets if symbols are used for units display.

### areTrailingZerosHidden : boolean [read-write]
Gets and sets if trailing zeros are hidden when displaying numbers.

### degreeDisplayFormat : DegreeDisplayFormats [read-write]
Gets and sets the degree display format.

### footAndInchDisplayFormat : FootAndInchDisplayFormats [read-write]
Gets and sets the foot and inch display format.

### generalPrecision : integer [read-write]
Gets and sets the general precision for distance values. This value specifies the number of decimals to display.

### isPeriodDecimalPoint : boolean [read-write]
Gets and sets if the decimal is a period or comma.

### isScientificNotationUsed : boolean [read-write]
Gets and sets if scientific notation is used when displaying numbers.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### materialDisplayUnit : MaterialDisplayUnits [read-write]
Gets and sets the units types to use when displaying values.

### minimumPrecisionWhenHidingZeros : integer [read-write]
Gets and sets the minimum number of digits to the right of the decimal to display before hiding trailing zeros.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### scientificNotationPrecision : integer [read-write]
Gets and sets the number scientific notation precision. This value specifies the number of decimals to display.

### useScientficNotationAbove : integer [read-write]
Gets and sets the number of whole digits that will be displayed before switching to scientific notation.

### useScientficNotationBelow : integer [read-write]
Gets and sets the number of non zero decimal places that will be displayed before switching to scientific notation.
