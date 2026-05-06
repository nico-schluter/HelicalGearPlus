# SheetMetalRuleValue
Namespace: adsk.fusion
Inherits: Base
Since: November 2022

Used to get and set the current value of a value associated with a sheet metal rule. A value can be gotten or set using a string or a double. A string can contain equations and unit specifiers whereas a double defines the size in centimeters. In the user-interface, the user is always setting the string expression. However, when programming it is typically more convenient to set it using an explicit value. When the value is set using a double, Fusion creates an equivalent expression.

**Accessed from:** SheetMetalRule.bendRadius, SheetMetalRule.gap, SheetMetalRule.reliefDepth, SheetMetalRule.reliefRemnant, SheetMetalRule.reliefWidth, SheetMetalRule.thickness, SheetMetalRule.threeBendReliefRadius, SheetMetalRule.twoBendReliefSize

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### expression : string [read-write]
Gets and sets the expression of the sheet metal rule value. This can be an equation that includes the name "Thickness" and can also include length unit specifiers. For example, a valid expression is "Thickness / 2 + 1 mm". If no units are specified, the unit is implied and uses the units associated with the rule which can be mm or inch. For example an expression of "3" will be 3 inches if the rule units are inches or 3 mm if the rule units are millimeters.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### value : double [read-write]
Gets and sets the value of the sheet metal rule value in centimeters. Setting this value will create a new expression that is equivalent to the new value.

## Samples
- **Sheet Metal Rules Sample**: Demonstrates creating adding a sheet metal rule.
