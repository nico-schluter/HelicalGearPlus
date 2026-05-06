# ThreeBendCornerClosureFeatureDefinition
Namespace: adsk.fusion
Inherits: CornerClosureFeatureDefinition
Since: January 2026

The definition for a three bend corner closure.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### bendTransition : CornerBendTransitionTypes [read-write]
Gets and sets the bend transition type for the corner closure.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### dominantEdge : BRepEdge [read-write]
Gets the dominant edge for the corner closure.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

After setting the edge, the definitionType property on CornerClosureFeature should be examined to determine whether the corner is two-bend or three-bend, as after the setting another edge the type of corner might be altered.

### isExtendAligned : boolean [read-write]
Gets and sets whether the corner closure extends aligned to the edges.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### isUseSheetMetalRuleDefaults : boolean [read-write]
Gets and sets whether to use default values from the Sheet Metal Rule for all three-bend relief parameters (shape and radius).

When set to true, the relief shape and radius are retrieved from the active Sheet Metal Rule. When set to false (default), the explicitly set values for these parameters are used.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

The default value is false.

### isUseSheetMetalRuleMiterGap : boolean [read-write]
Gets and sets whether to use the miter gap value from the Sheet Metal Rule.

When set to true, the miter gap value is retrieved from the active Sheet Metal Rule. When set to false (default), the explicitly set miterGap value is used.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

The default value is false.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### miterGap : ModelParameter [read-only]
Gets the miter gap for the corner closure.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### submissiveEdge : BRepEdge [read-write]
Gets and sets the submissive edge for the corner closure.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

After setting the edge, the definitionType property on CornerClosureFeature should be examined to determine whether the corner is two-bend or three-bend, as after the setting another edge the type of corner might be altered.

### threeBendReliefRadius : ModelParameter [read-only]
Gets the radius of the three-bend relief.

### threeBendReliefShape : CornerThreeBendReliefShapeTypes [read-write]
Gets and sets the relief shape for the three-bend corner.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
