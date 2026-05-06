# RuleFilletSettings
Namespace: adsk.fusion
Inherits: Base
Since: November 2025

The settings for the rule fillet feature.

**Accessed from:** FilletFeature.ruleFilletSettings

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setByAllEdges(facesOrFeatures: Base[]) -> boolean
Method that adds an array of BRepFace and/or Feature objects to have all their edges filleted. Calling this method will set ruleType to RuleFilletRuleTypes.AllEdgesRuleFilletRuleType.
- **facesOrFeatures** (Base[]): Input faces and/or features to have all their edges to be filleted.
- **Returns** (boolean): Returns true if the operation was successful.

### setByBetweenFacesOrFeatures(facesOrFeaturesOne: Base[], facesOrFeaturesTwo: Base[]) -> boolean
Method that adds two sets of BRepFace and/or Feature objects to have the edges between them filleted. Call this method will set ruleType to RuleFilletRuleTypes.BetweenFacesOrFeaturesRuleFilletRuleType.
- **facesOrFeaturesOne** (Base[]): Input first array of BRepFace and/or Feature objects.
- **facesOrFeaturesTwo** (Base[]): Input second array of BRepFace and/or Feature objects.
- **Returns** (boolean): Returns true if the operation was successful.

### setToAsymmetric(offsetOne: ValueInput, offsetTwo: ValueInput)
Changes the radius type to be asymmetric.
- **offsetOne** (ValueInput): Input ValueInput object that defines the first offset of the asymmetric rule fillet. If the ValueInput uses a real value then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current document units for length.
- **offsetTwo** (ValueInput): Input ValueInput object that defines the second offset of the asymmetric rule fillet. If the ValueInput uses a real value then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current document units for length.

### setToConstantRadius(radius: ValueInput)
Changes the radius type to be constant.
- **radius** (ValueInput): Input ValueInput object that defines the radius of the rule fillet. If the ValueInput uses a real value then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current document units for length.

## Properties

### asymmetricOffsetOne : ModelParameter [read-only]
Gets the parameter controlling the first offset of this asymmetric rule fillet. This property will return null when isConstantRadius is true. To edit the offset, use properties on the parameter to change the value of the parameter.

### asymmetricOffsetTwo : ModelParameter [read-only]
Gets the parameter controlling the second offset of this asymmetric rule fillet. This property will return null when isConstantRadius is true. To edit the offset, use properties on the parameter to change the value of the parameter.

### facesOrFeatures : array [read-only]
Gets an array of BRepFace and/or Feature objects that have all their edges filleted. This returns an empty array if ruleType is not RuleFilletRuleTypes.AllEdgesRuleFilletRuleType.

To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True).

### facesOrFeaturesOne : array [read-only]
Gets the first array of BRepFace and/or Feature objects for between faces/features rule fillet. This returns an empty array if ruleType is not RuleFilletRuleTypes.BetweenFacesOrFeaturesRuleFilletRuleType.

To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True).

### facesOrFeaturesTwo : array [read-only]
Gets the second array of BRepFace and/or Feature objects for between faces/features rule fillet. This returns an empty array if ruleType is not RuleFilletRuleTypes.BetweenFacesOrFeaturesRuleFilletRuleType.

To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True).

### isConstantRadius : boolean [read-only]
Gets and sets if the rule fillet is a constant or asymmetric radius type.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### radius : ModelParameter [read-only]
Gets the parameter controlling the radius of a constant radius rule fillet. This property will return null when isConstantRadius is false. To edit the radius, use properties on the parameter to change the value of the parameter.

### ruleType : RuleFilletRuleTypes [read-only]
Gets the rule type for the rule fillet.

### topologyType : RuleFilletTopologyTypes [read-write]
Gets and sets the topology type of the rule fillet.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True).
