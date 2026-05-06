# MoveFeature
Namespace: adsk.fusion
Inherits: Feature
Since: March 2015

Object that represents an existing move feature in a design.

**Accessed from:** MoveFeature.createForAssemblyContext, MoveFeature.nativeObject, MoveFeatureDefinition.parentMoveFeature, MoveFeatureFreeMoveDefinition.parentMoveFeature, MoveFeaturePointToPointDefinition.parentMoveFeature, MoveFeaturePointToPositionDefinition.parentMoveFeature, MoveFeatureRotateDefinition.parentMoveFeature, MoveFeatures.add, MoveFeatures.item, MoveFeatures.itemByName, MoveFeatureTranslateAlongEntityDefinition.parentMoveFeature, MoveFeatureTranslateXYZDefinition.parentMoveFeature

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> MoveFeature
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (MoveFeature): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes the feature. This works for both parametric and non-parametric features.
- **Returns** (boolean): Returns a bool indicating if the delete was successful or not.

### dissolve() -> boolean
Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.
- **Returns** (boolean): Returns a bool indicating if the dissolve was successful or not.

### redefineAsFreeMove(transform: Matrix3D) -> boolean
Redefines the move feature to be described by an arbitrary translation and orientation which is defined using a transformation matrix.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **transform** (Matrix3D): The transformation matrix that defines the transform to apply. The matrix must be an orthogonal matrix; that is the axes are perpendicular to each other and there isn't any scaling or mirroring defined.
- **Returns** (boolean): Returns true if the re-definition is successful.

### redefineAsPointToPoint(originPoint: Base, targetPoint: Base) -> boolean
Redefines the move feature to be a translation from one point to another.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **originPoint** (Base): The first point that defines the start position of the move.
- **targetPoint** (Base): The second point that defines the direction and distance of the move.
- **Returns** (boolean): Returns true if the redefinition is successful.

### redefineAsPointToPosition(point: Base, xDistance: ValueInput, yDistance: ValueInput, zDistance: ValueInput, isDesignSpace: boolean) -> boolean
Redefines a move feature to be described by a point and an offset. The distances define offsets in the X, Y, and Z directions in either design or component space. To not move the input entities at all the offset distances should be set to the current location of the point in either design or component space. Adding or subtracting to those values will then move the entities that distance. It's best to experiment with the command interactively to understand the behavior.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **point** (Base): An entity that defines a point in space. This can be a sketch point, a construction point, or a BRepVertex.
- **xDistance** (ValueInput): A ValueInput object that defines the offset in the X direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units will be used.
- **yDistance** (ValueInput): A ValueInput object that defines the offset in the Y direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units will be used.
- **zDistance** (ValueInput): A ValueInput object that defines the offset in the Z direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units will be used.
- **isDesignSpace** (boolean): Defines if the translation is defined with respect to the design or component space. Design space is the same as the root component space.
- **Returns** (boolean): Returns true if the redefinition is successful.

### redefineAsRotate(axisEntity: Base, angle: ValueInput) -> boolean
Redefines the move feature to be described by an axis and rotation angle.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **axisEntity** (Base): A linear entity that defines the axis of rotation. This can be a linear BRepEdge, ConstructionAxis, or a SketchLine. The natural direction of the entity defines a right-hand rule for the rotation direction.
- **angle** (ValueInput): A ValueInput object that defines the rotation angle. If the ValueInput is created using a real value, the angle is in radians. If it's defined using a string, the default document units will be used.
- **Returns** (boolean): Returns true if the redefinition is successful.

### redefineAsTranslateAlongEntity(linearEntity: Base, distance: ValueInput) -> boolean
Redefines the move feature to be a translation along a specified entity.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **linearEntity** (Base): A linear entity that defines the direction of the move. This can be a linear BRepEdge, ConstructionAxis, or a SketchLine. The entity defines the direction, not the distance. The natural direction of the entity defines the translation direction.
- **distance** (ValueInput): A ValueInput object that defines the offset distance. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units will be used.
- **Returns** (boolean): Returns true if the redefinition is successful.

### redefineAsTranslateXYZ(xDistance: ValueInput, yDistance: ValueInput, zDistance: ValueInput, isDesignSpace: boolean) -> boolean
Redefines the move feature to be described by a translation in X, Y, and Z.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **xDistance** (ValueInput): A ValueInput object that defines the offset in the X direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units will be used.
- **yDistance** (ValueInput): A ValueInput object that defines the offset in the Y direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units will be used.
- **zDistance** (ValueInput): A ValueInput object that defines the offset in the Z direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units will be used.
- **isDesignSpace** (boolean): Defines if the translation is defined with respect to the design or component space. Design space is the same as the root component space.
- **Returns** (boolean): Returns true if the re-definition is successful.

## Properties

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

### definition : MoveFeatureDefinition [read-only]
Returns the MoveFeatureDefinition object which provides access to the information that specifies how this MoveFeature is defined.

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

### inputEntities : ObjectCollection [read-write]
Gets and sets the entities to move. This is done by using an ObjectCollection containing the objects to move. For a parametric model, the collection can contain BRepBody or BRepFace objects but not a combination of both.

To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

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

### nativeObject : MoveFeature [read-only]
The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentComponent : Component [read-only]
Returns the parent component that owns this feature.

### timelineObject : TimelineObject [read-only]
Returns the timeline object associated with this feature.

### transform : Matrix3D [read-write]
This function is retired. See more information in the 'Remarks' section below.

Gets and sets the move transform of the input bodies or faces.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

## Samples
- **Move Feature API Sample**: Demonstrates creating a new move feature.
