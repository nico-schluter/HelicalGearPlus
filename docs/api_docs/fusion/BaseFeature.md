# BaseFeature
Namespace: adsk.fusion
Inherits: Feature
Since: September 2015

The BaseFeature class represents a direct edit feature within a parametric design.

**Accessed from:** ArrangeFeature.baseFeature, BaseFeature.baseFeature, BaseFeature.createForAssemblyContext, BaseFeature.nativeObject, BaseFeatures.add, BaseFeatures.item, BaseFeatures.itemByName, BossFeature.baseFeature, BossFeatureInput.targetBaseFeature, BoundaryFillFeature.baseFeature, BoundaryFillFeatureInput.targetBaseFeature, BoxFeature.baseFeature, BRepBody.baseFeature, CanvasInput.targetBaseFeature, ChamferFeature.baseFeature, ChamferFeatureInput.targetBaseFeature, CircularPatternFeature.baseFeature, CircularPatternFeatureInput.targetBaseFeature, CoilFeature.baseFeature, CoilFeatureInput.targetBaseFeature, CombineFeature.baseFeature, CombineFeatureInput.targetBaseFeature, ConstructionAxis.baseFeature, ConstructionPlane.baseFeature, ConstructionPoint.baseFeature, CopyPasteBody.baseFeature, CornerClosureFeature.baseFeature, CustomFeature.baseFeature, CutPasteBody.baseFeature, CylinderFeature.baseFeature, DecalInput.targetBaseFeature, DeleteFaceFeature.baseFeature, DeriveFeature.baseFeature, DraftFeature.baseFeature, DraftFeatureInput.targetBaseFeature, EmbossFeature.baseFeature, EmbossFeatureInput.targetBaseFeature, ExtendFeature.baseFeature, ExtendFeatureInput.targetBaseFeature, ExtrudeFeature.baseFeature, ExtrudeFeatureInput.targetBaseFeature, Feature.baseFeature, FilletFeature.baseFeature, FilletFeatureInput.targetBaseFeature, FlangeFeature.baseFeature, FlatPattern.baseFeature, FormFeature.baseFeature, FullRoundFilletFeatureInput.targetBaseFeature, HemFeature.baseFeature, HoleFeature.baseFeature, HoleFeatureInput.targetBaseFeature, LoftFeature.baseFeature, LoftFeatureInput.targetBaseFeature, MeshCombineFaceGroupsFeature.baseFeature, MeshCombineFaceGroupsFeatureInput.targetBaseFeature, MeshCombineFeature.baseFeature, MeshCombineFeatureInput.targetBaseFeature, MeshConvertFeature.baseFeature, MeshConvertFeatureInput.targetBaseFeature, MeshFeature.baseFeature, MeshGenerateFaceGroupsFeature.baseFeature, MeshGenerateFaceGroupsFeatureInput.targetBaseFeature, MeshReduceFeature.baseFeature, MeshReduceFeatureInput.targetBaseFeature, MeshRemeshFeature.baseFeature, MeshRemeshFeatureInput.targetBaseFeature, MeshRemoveFeature.baseFeature, MeshRemoveFeatureInput.targetBaseFeature, MeshRepairFeature.baseFeature, MeshRepairFeatureInput.targetBaseFeature, MeshReverseNormalFeature.baseFeature, MeshReverseNormalFeatureInput.targetBaseFeature, MeshSeparateFeature.baseFeature, MeshSeparateFeatureInput.targetBaseFeature, MeshShellFeature.baseFeature, MeshShellFeatureInput.targetBaseFeature, MeshSmoothFeature.baseFeature, MeshSmoothFeatureInput.targetBaseFeature, MirrorFeature.baseFeature, MirrorFeatureInput.targetBaseFeature, MoveFeature.baseFeature, MoveFeatureInput.targetBaseFeature, OffsetFacesFeature.baseFeature, OffsetFacesFeatureInput.targetBaseFeature, OffsetFeature.baseFeature, OffsetFeatureInput.targetBaseFeature, PatchFeature.baseFeature, PatchFeatureInput.targetBaseFeature, PathPatternFeature.baseFeature, PathPatternFeatureInput.targetBaseFeature, PipeFeature.baseFeature, PipeFeatureInput.targetBaseFeature, RectangularPatternFeature.baseFeature, RectangularPatternFeatureInput.targetBaseFeature, RefoldFeature.baseFeature, RemoveFeature.baseFeature, ReplaceFaceFeature.baseFeature, ReplaceFaceFeatureInput.targetBaseFeature, ReverseNormalFeature.baseFeature, RevolveFeature.baseFeature, RevolveFeatureInput.targetBaseFeature, RibFeature.baseFeature, RipFeature.baseFeature, RuledSurfaceFeature.baseFeature, RuledSurfaceFeatureInput.targetBaseFeature, RuleFilletFeature.baseFeature, RuleFilletFeatureInput.targetBaseFeature, ScaleFeature.baseFeature, ScaleFeatureInput.targetBaseFeature, ShellFeature.baseFeature, ShellFeatureInput.targetBaseFeature, SilhouetteSplitFeature.baseFeature, SilhouetteSplitFeatureInput.targetBaseFeature, SphereFeature.baseFeature, SplitBodyFeature.baseFeature, SplitBodyFeatureInput.targetBaseFeature, SplitFaceFeature.baseFeature, SplitFaceFeatureInput.targetBaseFeature, StitchFeature.baseFeature, StitchFeatureInput.targetBaseFeature, SurfaceDeleteFaceFeature.baseFeature, SweepFeature.baseFeature, SweepFeatureInput.targetBaseFeature, TessellateFeature.baseFeature, TessellateFeatureInput.targetBaseFeature, ThickenFeature.baseFeature, ThickenFeatureInput.targetBaseFeature, ThreadFeature.baseFeature, ThreadFeatureInput.targetBaseFeature, TorusFeature.baseFeature, TrimFeature.baseFeature, TrimFeatureInput.targetBaseFeature, UnfoldFeature.baseFeature, UnstitchFeature.baseFeature, UntrimFeature.baseFeature, VolumetricCustomFeature.baseFeature, VolumetricModelToMeshFeature.baseFeature, WebFeature.baseFeature

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> BaseFeature
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (BaseFeature): Returns the proxy object or null if this is not the NativeObject.

### deleteMe() -> boolean
Deletes the feature. This works for both parametric and non-parametric features.
- **Returns** (boolean): Returns a bool indicating if the delete was successful or not.

### dissolve() -> boolean
Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.
- **Returns** (boolean): Returns a bool indicating if the dissolve was successful or not.

### finishEdit() -> boolean
Exits from edit mode in the user-interface. If this base feature in not in edit mode, then nothing happens.
- **Returns** (boolean): Returns true if successful.

### startEdit() -> boolean
Set the user-interface so that the base body is in edit mode.
- **Returns** (boolean): Returns true if successful.

### updateBody(sourceBody: BRepBody, newBody: BRepBody) -> boolean
Update an existing source BRepBody created by this BaseFeature. The input BRepBody definition will be copied into the existing BRepBody.
- **sourceBody** (BRepBody): The source BRepBody to update. The source bodies of a BaseFeature are only available from the bodies collection of the BaseFeature when the BaseFeature is in edit mode.
- **newBody** (BRepBody): The BRepBody whose definition will be used to replace the existing source body's definition.
- **Returns** (boolean): Returns true if the body was updated, or false if the update failed.

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

### constructionAxes : array [read-only]
Returns an array of the construction axes associated with this base feature.

### constructionPlanes : array [read-only]
Returns an array of the construction planes associated with this base feature.

### constructionPoints : array [read-only]
Returns an array of the construction points associated with this base feature.

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

### isParametric : boolean [read-only]
Indicates if this feature is parametric or not.

### isSuppressed : boolean [read-write]
Gets and sets if this feature is suppressed. This is only valid for parametric features.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### linkedFeatures : FeatureList [read-only]
Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface.

### meshBodies : array [read-only]
Returns an array of the mesh bodies associated with this base feature.

### name : string [read-write]
Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric).

### nativeObject : BaseFeature [read-only]
The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentComponent : Component [read-only]
Returns the parent component that owns this feature.

### sketches : array [read-only]
Returns an array of the sketches associated with this base feature.

### sourceBodies : array [read-only]
Returns the B-Rep bodies owned by the base feature.

When a body is added to a base feature, that body is owned by the base feature and is only seen in the UI when the base feature is active. This body is referred to as a "source body". Fusion creates a parametric copy of the body when you exit the base feature. This copy is referred to as the "result body," and it is used for subsequent modeling operations. The result bodies can be obtained by using the bodies property of the BaseFeature object.

You can map between the source and result bodies by using their position within the bodies returned. To get a valid list of result bodies, you should roll the timeline to immediately after the base feature node in the timeline. Otherwise, subsequent operations could have done something to cause one or more bodies to no longer be available.

### timelineObject : TimelineObject [read-only]
Returns the timeline object associated with this feature.

## Samples
- **BaseFeature Sample**: Creates a new base feature.
