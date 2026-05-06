# TwoBendCornerClosureInputDefinition
Namespace: adsk.fusion
Inherits: CornerClosureInputDefinition
Since: January 2026

Defines the input properties required for creating a two-bend corner closure feature. This input definition provides a structured way to organize and validate the parameters before passing them to the setTwoBendCornerClosure method.

**Accessed from:** TwoBendCornerClosureInputDefinition.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create() -> TwoBendCornerClosureInputDefinition
Creates a TwoBendCornerClosureParameters object that can be used to define parameters for a two-bend corner closure. Use properties on this object to set the relief shape, relief size, relief placement, miter gap, alignment settings, and bend transition type before passing it to the setTwoBendCornerClosure method.
- **Returns** (TwoBendCornerClosureInputDefinition): Returns the newly created TwoBendCornerClosureParameters object or null if the creation failed.

## Properties

### bendTransition : CornerBendTransitionTypes [read-write]
Gets and sets the bend transition type for the corner closure. This determines how the bend transitions are handled at the corner intersection. The default value is TrimToBendCornerBendTransitionType.

### isExtendAligned : boolean [read-write]
Gets and sets a value indicating whether the corner closure extends aligned to the edges. When true, the corner closure will extend in alignment with the adjacent edges. When false, the corner closure will use the default extension behavior. The default value is true.

### isUseSheetMetalRuleDefaults : boolean [read-write]
Gets and sets whether to use default relief values from the Sheet Metal Rule. When true, all relief parameters (shape, size, and placement) are taken from the active Sheet Metal Rule, and any values set in twoBendReliefShape, twoBendReliefSize, and twoBendReliefPlacement properties are ignored. When false (default), the relief parameters must be explicitly set using the respective properties. The default value is false.

### isUseSheetMetalRuleMiterGap : boolean [read-write]
Gets and sets whether to use the miter gap value from the Sheet Metal Rule. When true, the miter gap value is taken from the active Sheet Metal Rule and any value set in the miterGap property is ignored. When false (default), the behavior depends on the miterGap property: - If miterGap is set: uses the specified value - If miterGap is not set (null): uses the value from the Sheet Metal Rule as a fallback The default value is false.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### miterGap : ValueInput [read-write]
Gets and sets the gap distance for the miter in the corner closure. This value defines the spacing between the sheets at the corner miter joint. If this property is not set (null) and useSheetMetalRuleMiterGap is false, the miter gap value will be taken from the Sheet Metal Rule as a fallback.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### twoBendReliefPlacement : CornerTwoBendReliefPlacementTypes [read-write]
Gets and sets the placement of the two-bend relief. This parameter controls where the relief feature is positioned relative to the bend intersection. This parameter is only valid when the twoBendReliefShape is RoundCornerTwoBendReliefShapeType or SquareCornerTwoBendReliefShapeType. For other relief shapes, this value is ignored. This property is ignored when useSheetMetalRuleDefaults is set to true. The default value is TangentCornerTwoBendReliefPlacementType.

### twoBendReliefShape : CornerTwoBendReliefShapeTypes [read-write]
Gets and sets the relief shape for the two-bend corner. This defines the geometric shape used to relieve stress at the corner where two bends meet. This property is ignored when useSheetMetalRuleDefaults is set to true. The default value is RoundCornerTwoBendReliefShapeType.

### twoBendReliefSize : ValueInput [read-write]
Gets and sets the size of the two-bend relief. This parameter is only valid when the twoBendReliefShape is RoundCornerTwoBendReliefShapeType or SquareCornerTwoBendReliefShapeType. For other relief shapes, this value is ignored. This property is ignored when useSheetMetalRuleDefaults is set to true.
