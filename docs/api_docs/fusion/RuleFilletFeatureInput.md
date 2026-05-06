# RuleFilletFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: November 2025

This class defines the methods and properties that pertain to the definition of a rule fillet feature.

**Accessed from:** FilletFeatures.createRuleFilletInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setAsymmetricOffsets(offsetOne: ValueInput, offsetTwo: ValueInput) -> boolean
Sets the fillet to be an asymmetric fillet and defines the two offsets.
- **offsetOne** (ValueInput): A ValueInput object that defines the offset distance of the fillet in the first direction. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string, then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **offsetTwo** (ValueInput): A ValueInput object that defines the offset distance of the fillet in the second direction. If the ValueInput uses a real, then it is interpreted as centimeters. If it is a string, then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **Returns** (boolean): Returns true if successful.

### setByAllEdges(facesOrFeatures: Base[]) -> boolean
Method that adds an array of BRepFace and/or Feature objects to have all their edges to be filleted. Calling this method will set ruleType to RuleFilletRuleTypes.AllEdgesRuleFilletRuleType.
- **facesOrFeatures** (Base[]): Input faces and/or features to have all their edges to be filleted.
- **Returns** (boolean): Returns true if the operation was successful.

### setByBetweenFacesOrFeatures(facesOrFeaturesOne: Base[], facesOrFeaturesTwo: Base[]) -> boolean
Method that adds two sets of BRepFace and/or Feature objects to have the edges between them filleted. Call this method will set ruleType to RuleFilletRuleTypes.BetweenFacesOrFeaturesRuleFilletRuleType.
- **facesOrFeaturesOne** (Base[]): Input first array of BRepFace and/or Feature objects.
- **facesOrFeaturesTwo** (Base[]): Input second array of BRepFace and/or Feature objects.
- **Returns** (boolean): Returns true if the operation was successful.

## Properties

### asymmetricOffsetOne : ValueInput [read-only]
Returns the current first offset for an asymmetric fillet. Use setAsymmetricOffsets to set the offsets. Returns null in the case where the fillet is a constant radius fillet.

### asymmetricOffsetTwo : ValueInput [read-only]
Returns the current second offset for an asymmetric fillet. Use setAsymmetricOffsets to set the offsets. Returns null in the case where the fillet is a constant radius fillet.

### facesOrFeatures : array [read-only]
Gets an array of BRepFace and/or Feature objects that are to have all their edges filleted. This is applicable only when ruleType is RuleFilletRuleTypes.AllEdgesRuleFilletRuleType. This is set by the setByAllEdges method.

### facesOrFeaturesOne : array [read-only]
Gets the first array of BRepFace and/or Feature objects for between faces/features rule fillet. This is applicable only when ruleType is RuleFilletRuleTypes.BetweenFacesOrFeaturesRuleFilletRuleType. This is set by the setByBetweenFacesOrFeatures method.

### facesOrFeaturesTwo : array [read-only]
Gets the second array of BRepFace and/or Feature objects for between faces/features rule fillet. This is applicable only when ruleType is RuleFilletRuleTypes.BetweenFacesOrFeaturesRuleFilletRuleType. This is set by the setByBetweenFacesOrFeatures method.

### isRollingBallCorner : boolean [read-write]
Gets and sets if a rolling ball or setback solution is to be used in any corners. A value of true will create a rolling ball fillet.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### radius : ValueInput [read-write]
Gets and sets the radius of the fillet. Setting this will set the fillet to a constant radius fillet and any asymmetric information will be lost. Returns null in the case the fillet is asymmetric.

### ruleType : RuleFilletRuleTypes [read-only]
Gets the rule type for the rule fillet.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

### topologyType : RuleFilletTopologyTypes [read-write]
Gets and sets the topology type of the rule fillet.
