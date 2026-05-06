# SheetMetalRule
Namespace: adsk.fusion
Inherits: Base
Since: November 2022

A sheet metal rule.

**Accessed from:** Component.activeSheetMetalRule, ConfigurationSheetMetalRuleCell.sheetMetalRule, FlatPatternComponent.activeSheetMetalRule, SheetMetalRules.addByCopy, SheetMetalRules.item, SheetMetalRules.itemByName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes the rule from the design or library. If the rule is in the library and set as the default rule, you cannot delete it. If the rule is in a design and is used by a component you cannot use it.
- **Returns** (boolean): Returns true if the delete was successful.

## Properties

### bendRadius : SheetMetalRuleValue [read-only]
The interior radius of the bends. Use the returned SheetMetalRuleValue object to get and set the current value of the radius.

### gap : SheetMetalRuleValue [read-only]
The value used for miter, rip, and seam, gaps. Use the returned SheetMetalRuleValue object to get and set the current value of the gap.

### isDefault : boolean [read-write]
This gets and sets which rule in a library is the default rule. This is only valid for rules in a library and will fail for rules in a design.

### isUsed : boolean [read-only]
Indicates if this rule is currently being used by a component. This is only valid for rules in a design.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### kFactor : double [read-write]
The K Factor value that is used when calculating the flat pattern. It must be a value between 0 and 1.

### name : string [read-write]
The name of the sheet metal rule. When setting the name, it should be unique with respect to other sheet metal rules in the design or library.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentDesign : Design [read-only]
Returns the parent design for a sheet metal rule in a design or it returns null if the sheet metal rule is in the library.

### reliefDepth : SheetMetalRuleValue [read-only]
The relief depth used in the flat pattern. Use the returned SheetMetalRuleValue object to get and set the current value of the relief depth.

### reliefRemnant : SheetMetalRuleValue [read-only]
The relief remnant used in the flat pattern. Use the returned SheetMetalRuleValue object to get and set the current value of the relief remnant.

### reliefShape : BendReliefShapes [read-write]
Gets and sets the bend relief shape to use.

### reliefWidth : SheetMetalRuleValue [read-only]
The relief width used in the flat pattern. Use the returned SheetMetalRuleValue object to get and set the current value of the relief width.

### thickness : SheetMetalRuleValue [read-only]
The thickness of the part. Use the returned SheetMetalRuleValue object to get and set the current value of the thickness.

### threeBendReliefRadius : SheetMetalRuleValue [read-only]
The relief size used when three bends meet in the flat pattern and the relief shape is "round with radius". Use the returned SheetMetalRuleValue object to get and set the current value of the relief size.

### threeBendReliefShape : ThreeBendReliefShapes [read-write]
Gets and sets the relief shape to use when three bends intersect.

### twoBendReliefPlacement : TwoBendReliefPlacements [read-write]
Gets and sets the relief placement for a two-bend relief shape. When the relief shape is round, both intersection and tangent are valid placements. For square shape, only intersection is valid. For all other shapes, this property will return NoTwoBendReliefPlacement because the placement option is not used.

### twoBendReliefShape : TwoBendReliefShapes [read-write]
Gets and sets the relief shape to use when two bends intersect.

When set to square or round relief shape, the value of the twoBendReliefPlacement property will be set to IntersectionTwoBendReliefPlacement. For a round relief shape you can change the twoBendReliefPlacment property to TangentTwoBendReliefPlacement.

### twoBendReliefSize : SheetMetalRuleValue [read-only]
The relief size used when two bends meet in the flat pattern and the relief shape is round or square. Use the returned SheetMetalRuleValue object to get and set the current value of the relief size.

### units : string [read-only]
Gets the units this rule uses to display values in the dialog. Rules currently only use mm or inch and the units are permanently associated with a rule and cannot be modified.

## Samples
- **Sheet Metal Rules Sample**: Demonstrates creating adding a sheet metal rule.
