# ValueInput
Namespace: adsk.core
Inherits: Base
Since: August 2014

A ValueInput provides a flexible way of specifying a string, a double, a boolean, or object reference. No semantics are associated with a ValueInput (e.g. is the string valid, can the string be converted to a double) - it is merely a way of supplying information in either string, double, boolean or object reference form as a function parameter. ValueInput objects are typically used to specify things like an extrude depth, or hole diameter, etc.

**Accessed from:** Arrange2DEnvelopeInput.frameWidth, Arrange2DEnvelopeInput.objectSpacing, Arrange2DEnvelopeInput.placementClearance, Arrange2DPlaneEnvelopeInput.envelopeSpacing, Arrange2DPlaneEnvelopeInput.frameWidth, Arrange2DPlaneEnvelopeInput.length, Arrange2DPlaneEnvelopeInput.objectSpacing, Arrange2DPlaneEnvelopeInput.originXOffset, Arrange2DPlaneEnvelopeInput.originYOffset, Arrange2DPlaneEnvelopeInput.placementClearance, Arrange2DPlaneEnvelopeInput.quantity, Arrange2DPlaneEnvelopeInput.width, Arrange2DProfileOrFaceEnvelopeInput.frameWidth, Arrange2DProfileOrFaceEnvelopeInput.objectSpacing, Arrange2DProfileOrFaceEnvelopeInput.placementClearance, Arrange3DEnvelopeInput.ceilingClearance, Arrange3DEnvelopeInput.frameWidth, Arrange3DEnvelopeInput.height, Arrange3DEnvelopeInput.length, Arrange3DEnvelopeInput.objectSpacing, Arrange3DEnvelopeInput.originXOffset, Arrange3DEnvelopeInput.originYOffset, Arrange3DEnvelopeInput.placementClearance, Arrange3DEnvelopeInput.width, ArrangeDefinition2DInput.globalQuantity, ArrangeDefinition2DInput.grainDirection, ArrangeEnvelopeInput.frameWidth, ArrangeEnvelopeInput.objectSpacing, ArrangeEnvelopeInput.placementClearance, AsymmetricFilletEdgeSetInput.offsetOne, AsymmetricFilletEdgeSetInput.offsetTwo, AsymmetricFilletEdgeSetInput.tangencyWeight, BossFeatureInput.offset, BossFeatureSideInput.alignmentDepth, BossFeatureSideInput.alignmentDiameter, BossFeatureSideInput.alignmentDraftAngle, BossFeatureSideInput.alignmentRootRadius, BossFeatureSideInput.alignmentTipRadius, BossFeatureSideInput.diameter, BossFeatureSideInput.draftAngle, BossFeatureSideInput.holeCountersinkAngle, BossFeatureSideInput.holeDepth, BossFeatureSideInput.holeDiameter, BossFeatureSideInput.holeDraftAngle, BossFeatureSideInput.holeEndRadius, BossFeatureSideInput.holeMajorDepth, BossFeatureSideInput.holeMajorDiameter, BossFeatureSideInput.holeMajorDraftAngle, BossFeatureSideInput.holeMajorRootRadius, BossFeatureSideInput.holeMajorTipRadius, BossFeatureSideInput.holeStartRadius, BossFeatureSideInput.offsetClearance, BossFeatureSideInput.ribChamferAngle, BossFeatureSideInput.ribCount, BossFeatureSideInput.ribCutSize, BossFeatureSideInput.ribDraftAngle, BossFeatureSideInput.ribLength, BossFeatureSideInput.ribOffset, BossFeatureSideInput.ribOuterDraftAngle, BossFeatureSideInput.ribRootRadius, BossFeatureSideInput.ribRotation, BossFeatureSideInput.ribThickness, BossFeatureSideInput.ribTipRadius, BossFeatureSideInput.ribTotalAngle, BossFeatureSideInput.rootRadius, BossFeatureSideInput.tipRadius, ChordLengthFilletEdgeSetInput.chordLength, ChordLengthFilletEdgeSetInput.tangencyWeight, CircularPatternConstraintInput.quantity, CircularPatternConstraintInput.totalAngle, CircularPatternFeatureInput.quantity, CircularPatternFeatureInput.totalAngle, CoilFeatureInput.angle, CoilFeatureInput.diameter, CoilFeatureInput.height, CoilFeatureInput.pitch, CoilFeatureInput.revolutions, CoilFeatureInput.sectionSize, ConstantRadiusFilletEdgeSetInput.radius, ConstantRadiusFilletEdgeSetInput.tangencyWeight, CornerClosureInputDefinition.miterGap, DraftFeatureInput.angleOne, DraftFeatureInput.angleTwo, EmbossFeatureInput.depth, EmbossFeatureInput.horizontalDistance, EmbossFeatureInput.rotationAngle, EmbossFeatureInput.verticalDistance, ExtendFeatureInput.distance, ExtrudeFeatureInput.taperAngle, ExtrudeFeatureInput.taperAngleOne, ExtrudeFeatureInput.taperAngleTwo, ExtrudeFeatureInput.thinExtrudeWallThicknessOne, ExtrudeFeatureInput.thinExtrudeWallThicknessTwo, FilletEdgeSetInput.tangencyWeight, GeometricRelationship.offsetOrAngleValue, HoleFeatureInput.threadLength, HoleFeatureInput.threadOffset, HoleFeatureInput.tipAngle, JointInput.angle, JointInput.offset, JointOriginInput.angle, JointOriginInput.globalOrientParamOne, JointOriginInput.globalOrientParamTwo, JointOriginInput.offsetX, JointOriginInput.offsetY, JointOriginInput.offsetZ, MeshConvertFeatureInput.numberOfFaces, MeshGenerateFaceGroupsFeatureInput.angleThreshold, MeshGenerateFaceGroupsFeatureInput.boundaryTolerance, MeshGenerateFaceGroupsFeatureInput.minimumFaceGroupSize, MeshReduceFeatureInput.facecount, MeshReduceFeatureInput.maximumDeviation, MeshReduceFeatureInput.proportion, MeshRemeshFeatureInput.density, MeshRemeshFeatureInput.shapePreservation, MeshRepairFeatureInput.density, MeshRepairFeatureInput.offset, MeshShellFeatureInput.thickness, MeshSmoothFeatureInput.smoothness, MirrorFeatureInput.stitchTolerance, MotionLinkInput.valueOne, MotionLinkInput.valueTwo, NamedValues.getByIndex, NamedValues.getValueByName, OffsetConstraintInput.offset, OffsetFacesFeatureInput.distance, OffsetFeatureInput.distance, PathPatternFeatureInput.distance, PathPatternFeatureInput.quantity, PipeFeatureInput.distanceOne, PipeFeatureInput.distanceTwo, PipeFeatureInput.sectionSize, PipeFeatureInput.sectionThickness, RectangularPatternConstraintInput.distanceOne, RectangularPatternConstraintInput.distanceTwo, RectangularPatternConstraintInput.quantityOne, RectangularPatternConstraintInput.quantityTwo, RectangularPatternFeatureInput.distanceOne, RectangularPatternFeatureInput.distanceTwo, RectangularPatternFeatureInput.quantityOne, RectangularPatternFeatureInput.quantityTwo, RuledSurfaceFeatureInput.angle, RuledSurfaceFeatureInput.distance, RuleFilletFeatureInput.asymmetricOffsetOne, RuleFilletFeatureInput.asymmetricOffsetTwo, RuleFilletFeatureInput.radius, ScaleFeatureInput.scaleFactor, ScaleFeatureInput.xScale, ScaleFeatureInput.yScale, ScaleFeatureInput.zScale, ShellFeatureInput.insideThickness, ShellFeatureInput.outsideThickness, SketchTextInput.height2, StitchFeatureInput.tolerance, SweepFeatureInput.distanceOne, SweepFeatureInput.distanceTwo, SweepFeatureInput.taperAngle, SweepFeatureInput.twistAngle, TessellateFeatureInput.aspectRatio, TessellateFeatureInput.maximumEdgeLength, TessellateFeatureInput.normalDeviation, TessellateFeatureInput.surfaceDeviation, ThickenFeatureInput.thickness, ThreadFeatureInput.threadLength, ThreadFeatureInput.threadOffset, ThreeBendCornerClosureInputDefinition.miterGap, ThreeBendCornerClosureInputDefinition.threeBendReliefRadius, TwoBendCornerClosureInputDefinition.miterGap, TwoBendCornerClosureInputDefinition.twoBendReliefSize, UntrimFeatureInput.extensionDistance, ValueInput.createByBoolean, ValueInput.createByObject, ValueInput.createByReal, ValueInput.createByString, VariableRadiusFilletEdgeSetInput.endRadius, VariableRadiusFilletEdgeSetInput.startRadius, VariableRadiusFilletEdgeSetInput.tangencyWeight, VolumetricModelToMeshFeatureInput.elementSize, VolumetricModelToMeshFeatureInput.smallShellThreshold

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createByBoolean(booleanValue: boolean) -> ValueInput
Creates a new ValueInput object that contains a boolean value.
- **booleanValue** (boolean): Boolean value.
- **Returns** (ValueInput): Returns the newly created ValueInput object or null if the creation failed.

### createByObject(objectReference: Base) -> ValueInput
Creates a new ValueInput object that contains a reference to any Fusion object.
- **objectReference** (Base): The Fusion object that you want to create the ValueInput for.
- **Returns** (ValueInput): Returns the newly created ValueInput object or null if the creation failed.

### createByReal(realValue: double) -> ValueInput
Creates a new ValueInput object using a double. For example, if you create a value using the double value 2 and use it as input for a length, it will be interpreted as 2 cm because centimeters are the internal unit for length. Values defined by a real are always interpreted to be in the appropriate internal unit. For example, if the value 2 is used to define the depth of an extrusion (a length value), it will be 2 cm because cm is the internal unit for lengths. If the value 2 is used to define the angle of the extrude, it will be 2 radians because radians are the internal unit for angles.
- **realValue** (double): a double value
- **Returns** (ValueInput): Returns the newly created ValueInput object or null if the creation failed.

### createByString(stringValue: string) -> ValueInput
When a string is used to create a value it needs to be evaluated as an expression so its value can be determined using the UnitsManager class. The units of an expression can be explicitly defined or will default to the current default units. For example, if you create an expression with the string "6" and specify it as a length, it will use the current active units. If the current active units are defined as inches the expression will be interpreted as 6 inches. You can specify the units as part of the string (i.e. "6 mm"). You can also use equations in the string (i.e. "6 + 5mm")

In order for an expression to be valid, its units must be compatible with the value it represents. For example if you specify "5 in + 3 cm" as an expression to supply the value of an angle, it will fail because the units of the expression define a length.
- **stringValue** (string): The expression string
- **Returns** (ValueInput): Returns the newly created ValueInput object or null if the creation failed.

## Properties

### booleanValue : boolean [read-only]
Gets the boolean value, if there is one. Returns false AND GetLastError returns ValueNotOfType if there is no boolean value. You can use the valueType property to determine which value type is currently used.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectReference : Base [read-only]
Gets the object being referenced, if there is one. Returns null AND GetLastError returns ValueNotOfType if there is no object reference. You can use the valueType property to determine which value type is currently used.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### realValue : double [read-only]
Gets the real value, if there is one. Returns -1 AND GetLastError returns ValueNotOfType if there is no real value. You can use the valueType property to determine which value type is currently used.

### stringValue : string [read-only]
Gets the string value, if there is one. Returns an empty string AND GetLastError returns ValueNotOfType if there is no string value. You can use the valueType property to determine which value type is currently used.

### valueType : ValueTypes [read-only]
Returns the type of value this ValueInput currently represents.

## Samples
- **Loft Feature API Sample**: Demonstrates creating a new loft feature.
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
- **Simple Extrusion Sample**: Creates a new extrusion feature, resulting in a new component.
- **Simple Revolve Feature Sample**: Creates a new revolve feature, resulting in a new component.
