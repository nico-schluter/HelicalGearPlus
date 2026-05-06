# BossFeature
Namespace: adsk.fusion
Inherits: Feature
Since: October 2022

Object that represents an existing boss feature in a design. For history free model this interface has limited functionality.

**Accessed from:** BossFeature.createForAssemblyContext, BossFeature.nativeObject, BossFeatures.add, BossFeatures.item, BossFeatures.itemByName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> BossFeature
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (BossFeature): Returns the proxy object or null if this isn't the NativeObject.

### createInput() -> BossFeatureInput
Creates object with inputs this feature represents. To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True).
- **Returns** (BossFeatureInput): Returns BossFeatureInput this feature represent if successful.

### deleteMe() -> boolean
Deletes the feature. This works for both parametric and non-parametric features.
- **Returns** (boolean): Returns a bool indicating if the delete was successful or not.

### dissolve() -> boolean
Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.
- **Returns** (boolean): Returns a bool indicating if the dissolve was successful or not.

### update(input: BossFeatureInput) -> boolean
Changes the boss feature (or boss connection) to the input provided. To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True).
- **input** (BossFeatureInput): The object defines inputs the feature will be set to.
- **Returns** (boolean): Returns true if successful.

## Properties

### alignmentDepth : ModelParameter [read-only]
Returns the model parameter controlling the step depth used for alignment of its counterparts.

### alignmentDiameter : ModelParameter [read-only]
Returns the model parameter controlling the step diameter used for alignment of its counterparts.

### alignmentDraftAngle : ModelParameter [read-only]
Returns the model parameter controlling the step draft angle.

### alignmentRootRadius : ModelParameter [read-only]
Returns the model parameter controlling blend radius of the boss alignment root.

### alignmentTipRadius : ModelParameter [read-only]
Returns the model parameter controlling blend radius of the boss alignment top face.

### alignmentType : BossAlignmentTypes [read-only]
Returns the current boss alignment shape this feature represents.

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this face.

### baseFeature : BaseFeature [read-only]
If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null.

### bodies : BRepBodies [read-only]
Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.

For a BaseFeature, this property has two different behaviors depending on if the BaseFeature is active for edit or not. When the base feature is active, this property returns the bodies owned by the base feature or the source bodies. When the base feature is not active, this property returns the result bodies.

When a body is added to a base feature, that body is owned by the base feature and is only seen in the UI when the base feature is active. This body is referred to as a "source body". Fusion creates a parametric copy of the body when you exit the base feature. This copy is referred to as the "result body," and it is used for subsequent modeling operations.

You can map between the source and result bodies by using their position within the bodies returned. To get a valid list of result bodies, you should roll the timeline to immediately after the base feature node in the timeline. Otherwise, subsequent operations could have done something to cause one or more bodies to no longer be available.

### diameter : ModelParameter [read-only]
Returns the model parameter controlling the shank diameter.

### direction : Vector3D [read-only]
Returns the direction of the boss feature with respect to selected position point. For selected sketch point this direction represents a Z-axis of the sketch.

### draftAngle : ModelParameter [read-only]
Returns the model parameter controlling the shank draft angle.

### entityToken : string [read-only]
Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### errorOrWarningMessage : string [read-only]
Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string.

### faces : BRepFaces [read-only]
Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available.

### healthState : FeatureHealthStates [read-only]
Returns the current health state of the feature.

### holeCountersinkAngle : ModelParameter [read-only]
Returns the model parameter controlling countersink angle for countersink hole. If hole type is not set to countersink hole or boss shape is to BossBlank this parameter is unused.

### holeDepth : ModelParameter [read-only]
Returns the model parameter controlling the hole depth with respect to hole extent type. If hole extent type is set to BossHoleThrough parameter not used. If hole extent type is BossBlindFull the parameter is a distance from farthest face. If hole extent type is set to BossBlindDepth the parameter is a distance from start face of the hole.

### holeDiameter : ModelParameter [read-only]
Returns the model parameter controlling the hole diameter.

### holeDraftAngle : ModelParameter [read-only]
Returns the model parameter controlling hole draft angle.

### holeEndRadius : ModelParameter [read-only]
Returns the model parameter controlling blend radius of the hole end.

### holeExtentType : BossHoleExtentTypes [read-only]
Returns the current type of hole extent this feature represents.

### holeMajorDepth : ModelParameter [read-only]
Returns the model parameter controlling major hole depth for counterbore and countersink hole. If hole type is set to simple hole or boss shape is to BossBlank this parameter is unused.

### holeMajorDiameter : ModelParameter [read-only]
Returns the model parameter controlling major hole diameter for counterbore and countersink hole. If hole type is set to simple hole or boss shape is to BossBlank this parameter is unused.

### holeMajorDraftAngle : ModelParameter [read-only]
Returns the model parameter controlling major hole draft angle for counterbore and countersink hole. If hole type is set to simple hole or boss shape is to BossBlank this parameter is unused.

### holeMajorRootRadius : ModelParameter [read-only]
Returns the model parameter controlling blend radius of major hole counterbore root.

### holeMajorTipRadius : ModelParameter [read-only]
Returns the model parameter controlling blend radius of major hole counterbore.

### holeStartRadius : ModelParameter [read-only]
Returns the model parameter controlling blend radius of the hole start.

### holeType : HoleTypes [read-only]
Returns the current type of hole this feature represents.

### innerRadius : ModelParameter [read-only]
Returns the model parameter for inner radius - reference for parametric expressions.

### isDirectionFlipped : boolean [read-write]
Gets and sets if the direction of the boss (or boss connection) is flipped.

### isGeometryOpposite : boolean [read-only]
Gets if this boss feature instance represents a bottom side where screw thread engages with the part. If this feature instance represents a geometry where screw head engages it returns false.

### isParametric : boolean [read-only]
Indicates if this feature is parametric or not.

### isSuppressed : boolean [read-write]
Gets and sets if this feature is suppressed. This is only valid for parametric features.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### linkedFeatures : FeatureList [read-only]
Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface.

### name : string [read-write]
Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric).

### nativeObject : BossFeature [read-only]
The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### offset : ModelParameter [read-only]
Returns the model parameter controlling the offset from the selected parting plane.

### offsetClearance : ModelParameter [read-only]
Returns the model parameter controlling the offset clearance from the selected parting plane and offset.

### parentComponent : Component [read-only]
Returns the parent component that owns this feature.

### positionDefinition : BossPositionDefinition [read-only]
Returns a BossPositionDefinition object that provides access to the information used to define the position of the boss feature.

### ribBlendRadius : ModelParameter [read-only]
Returns the model parameter controlling size of rib root blend radius.

### ribChamferAngle : ModelParameter [read-only]
Returns the model parameter controlling size of rib chamfer angle.

### ribCount : ModelParameter [read-only]
Returns the model parameter controlling number of ribs.

### ribCutSize : ModelParameter [read-only]
Returns the model parameter controlling size of rib chamfer or fillet.

### ribDraftAngle : ModelParameter [read-only]
Returns the model parameter controlling ribs draft angle.

### ribLength : ModelParameter [read-only]
Returns the model parameter controlling ribs length measured from the shank axis.

### ribOffset : ModelParameter [read-only]
Returns the model parameter controlling ribs offset from the top face or alignment face.

### ribOuterDraftAngle : ModelParameter [read-only]
Returns the model parameter controlling size of rib outer draft angle.

### ribRotation : ModelParameter [read-only]
Returns the model parameter controlling rotation angle of the first rib from the reference vector. For selected sketch point(s) the direction of reference vector is X-axis of the parent sketch.

### ribThickness : ModelParameter [read-only]
Returns the model parameter controlling ribs thickness.

### ribTipRadius : ModelParameter [read-only]
Returns the model parameter controlling size of rib tip blend radius.

### ribTotalAngle : ModelParameter [read-only]
Returns the model parameter controlling total angle for ribs distribution.

### ribType : BossRibShapeTypes [read-only]
Returns the current type of ribs shape this feature represents.

### rootRadius : ModelParameter [read-only]
Returns the model parameter controlling blend radius of the boss shank.

### screwDiameter : ModelParameter [read-only]
Returns the model parameter for screw diameter - reference for parametric expressions.

### screwHeadAngle : ModelParameter [read-only]
Returns the model parameter for countersink head angle - reference for parametric expressions.

### screwHeadDiameter : ModelParameter [read-only]
Returns the model parameter for screw head diameter - reference for parametric expressions.

### shapeType : BossShapeTypes [read-only]
Returns the current boss shape this feature represents.

### taperAngle : ModelParameter [read-only]
Returns the model parameter for taper angle - plastic part rule reference.

### thickness : ModelParameter [read-only]
Returns the model parameter for thickness - plastic part rule reference.

### timelineObject : TimelineObject [read-only]
Returns the timeline object associated with this feature.

### tipRadius : ModelParameter [read-only]
Returns the model parameter controlling blend radius of the boss shank top face.
