# FeatureList
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

Provides access to a list of features. This is used in the API to return a list of features from an API call.

**Accessed from:** ArrangeFeature.linkedFeatures, BaseFeature.linkedFeatures, BossFeature.linkedFeatures, BoundaryFillFeature.linkedFeatures, BoxFeature.linkedFeatures, ChamferFeature.linkedFeatures, CircularPatternFeature.linkedFeatures, CoilFeature.linkedFeatures, CombineFeature.linkedFeatures, CopyPasteBody.linkedFeatures, CornerClosureFeature.linkedFeatures, CustomFeature.linkedFeatures, CutPasteBody.linkedFeatures, CylinderFeature.linkedFeatures, DeleteFaceFeature.linkedFeatures, DeriveFeature.linkedFeatures, DraftFeature.linkedFeatures, EmbossFeature.linkedFeatures, ExtendFeature.linkedFeatures, ExtrudeFeature.linkedFeatures, Feature.linkedFeatures, FilletFeature.linkedFeatures, FlangeFeature.linkedFeatures, FlatPattern.linkedFeatures, FormFeature.linkedFeatures, HemFeature.linkedFeatures, HoleFeature.linkedFeatures, LoftFeature.linkedFeatures, MeshCombineFaceGroupsFeature.linkedFeatures, MeshCombineFeature.linkedFeatures, MeshConvertFeature.linkedFeatures, MeshFeature.linkedFeatures, MeshGenerateFaceGroupsFeature.linkedFeatures, MeshReduceFeature.linkedFeatures, MeshRemeshFeature.linkedFeatures, MeshRemoveFeature.linkedFeatures, MeshRepairFeature.linkedFeatures, MeshReverseNormalFeature.linkedFeatures, MeshSeparateFeature.linkedFeatures, MeshShellFeature.linkedFeatures, MeshSmoothFeature.linkedFeatures, MirrorFeature.linkedFeatures, MoveFeature.linkedFeatures, OffsetFacesFeature.linkedFeatures, OffsetFeature.linkedFeatures, PatchFeature.linkedFeatures, PathPatternFeature.linkedFeatures, PipeFeature.linkedFeatures, RectangularPatternFeature.linkedFeatures, RefoldFeature.linkedFeatures, RemoveFeature.linkedFeatures, ReplaceFaceFeature.linkedFeatures, ReverseNormalFeature.linkedFeatures, RevolveFeature.linkedFeatures, RibFeature.linkedFeatures, RipFeature.linkedFeatures, RuledSurfaceFeature.linkedFeatures, RuleFilletFeature.linkedFeatures, ScaleFeature.linkedFeatures, ShellFeature.linkedFeatures, SilhouetteSplitFeature.linkedFeatures, SphereFeature.linkedFeatures, SplitBodyFeature.linkedFeatures, SplitFaceFeature.linkedFeatures, StitchFeature.linkedFeatures, SurfaceDeleteFaceFeature.linkedFeatures, SweepFeature.linkedFeatures, TessellateFeature.linkedFeatures, ThickenFeature.linkedFeatures, ThreadFeature.linkedFeatures, TorusFeature.linkedFeatures, TrimFeature.linkedFeatures, UnfoldFeature.linkedFeatures, UnstitchFeature.linkedFeatures, UntrimFeature.linkedFeatures, VolumetricCustomFeature.linkedFeatures, VolumetricModelToMeshFeature.linkedFeatures, WebFeature.linkedFeatures

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Feature
Returns the specified folder.
- **index** (uinteger): The index of the feature to return. The first feature in the list has an index of 0.
- **Returns** (Feature): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
The number of features in this collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
