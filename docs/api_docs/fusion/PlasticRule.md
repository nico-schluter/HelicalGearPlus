# PlasticRule
Namespace: adsk.fusion
Inherits: Base
Since: January 2024

A plastic rule.

**Accessed from:** ConfigurationPlasticRuleCell.plasticRule, PlasticRules.addByCopy, PlasticRules.item, PlasticRules.itemByName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes the rule from the design or library. If the rule is in the library and set as the default rule, you cannot delete it. If the rule is in a design and is used by a component you cannot delete it.
- **Returns** (boolean): Returns true if the delete was successful.

## Properties

### clearance : PlasticRuleValue [read-only]
The clearance used for plastic features. When using a float to set the value, it is defined in centimeters. When using a string to set the expression, the units can be defined as part of the expression or it defaults to the units associated with the rule if no units are specified.

### draftAngle : PlasticRuleValue [read-only]
The draft angle used for plastic features. When using a float to set the value, it is defined in radians. When using a string to set the expression it uses degrees.

### isDefault : boolean [read-write]
This gets and sets which rule in a library is the default rule. This is only valid for rules in a library and will fail for rules in a design.

### isUsed : boolean [read-only]
Indicates if this rule is currently being used by a component. This is only valid for rules in a design.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### knifeEdgeThreshold : PlasticRuleValue [read-only]
The minimal thickness where an edge is considered a knife edge. This is used by the Design Advice command when analyzing the part for manufacturability.

When using a float to set the value, it is defined in centimeters. When using a string to set the expression, the units can be defined as part of the expression or it defaults to the units associated with the rule if no units are specified.

### material : Material [read-write]
Gets and sets the material assigned to this plastic rule

### maximumThickness : double [read-write]
The maximum thickness of the part in centimeters. This is used by the Design Advice command when analyzing the part for manufacturability.

### minimumDraftAngle : double [read-write]
The minimum draft angle allowed in radians. This is used by the Design Advice command when analyzing the part for manufacturability.

### minimumThickness : double [read-write]
The minimum thickness of the part in centimeters. This is used by the Design Advice command when analyzing the part for manufacturability.

### name : string [read-write]
The name of the plastic rule. When setting the name, it must be unique with respect to other plastic rules in the design or library.

### nominalRadius : PlasticRuleValue [read-only]
The nominal radius used for plastic features. When using a float to set the value, it is defined in centimeters. When using a string to set the expression, the units can be defined as part of the expression or it defaults to the units associated with the rule if no units are specified.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentDesign : Design [read-only]
Returns the parent design for a plastic rule in a design or it returns null if the plastic rule is in the library.

### revealHeight : PlasticRuleValue [read-only]
The reveal height used for plastic features. When using a float to set the value, it is defined in centimeters. When using a string to set the expression, the units can be defined as part of the expression or it defaults to the units associated with the rule if no units are specified.

### thickness : PlasticRuleValue [read-only]
The thickness used for plastic features. This value must be within the range specified by the minimumThickness and maximumThickness properties. This is used by the plastic commands when a wall thickness is needed.

When using a float to set the value, it is defined in centimeters. When using a string to set the expression, the units can be defined as part of the expression or it defaults to the units associated with the rule if no units are specified.

### thicknessVariation : PlasticRuleValue [read-only]
The maximum thickness of the part. This is used by the Design Advice command when analyzing the part for manufacturability.

When using a float to set the value, it is defined in centimeters. When using a string to set the expression, the units can be defined as part of the expression or it defaults to the units associated with the rule if no units are specified.

### units : string [read-only]
Gets the units this rule uses to display values in the dialog. Rules currently only use mm or inch and the units are permanently associated with a rule and cannot be modified.
