# BRepFaces
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

BRepFace collection.

**Accessed from:** ArrangeFeature.faces, BaseFeature.faces, BossFeature.faces, BoundaryFillFeature.faces, BoxFeature.faces, BRepBody.faces, BRepEdge.faces, BRepFace.tangentiallyConnectedFaces, BRepLump.faces, BRepShell.faces, BRepVertex.faces, ChamferFeature.faces, CircularPatternFeature.faces, CoilFeature.faces, CombineFeature.faces, CopyPasteBody.faces, CornerClosureFeature.faces, CustomFeature.faces, CutPasteBody.faces, CylinderFeature.faces, DeleteFaceFeature.faces, DeriveFeature.faces, DraftFeature.faces, EmbossFeature.faces, ExtendFeature.faces, ExtrudeFeature.endFaces, ExtrudeFeature.faces, ExtrudeFeature.sideFaces, ExtrudeFeature.startFaces, Feature.faces, FilletFeature.faces, FlangeFeature.faces, FlatPattern.faces, FlatPattern.sideFaces, FormFeature.faces, HemFeature.faces, HoleFeature.endFaces, HoleFeature.faces, HoleFeature.sideFaces, LoftFeature.faces, LoftFeature.sideFaces, MeshCombineFaceGroupsFeature.faces, MeshCombineFeature.faces, MeshConvertFeature.faces, MeshFeature.faces, MeshGenerateFaceGroupsFeature.faces, MeshReduceFeature.faces, MeshRemeshFeature.faces, MeshRemoveFeature.faces, MeshRepairFeature.faces, MeshReverseNormalFeature.faces, MeshSeparateFeature.faces, MeshShellFeature.faces, MeshSmoothFeature.faces, MirrorFeature.faces, MoveFeature.faces, OffsetFacesFeature.faces, OffsetFeature.faces, PatchFeature.faces, PathPatternFeature.faces, PipeFeature.endFaces, PipeFeature.faces, PipeFeature.sideFaces, PipeFeature.startFaces, RectangularPatternFeature.faces, RefoldFeature.faces, RemoveFeature.faces, ReplaceFaceFeature.faces, ReverseNormalFeature.faces, RevolveFeature.endFaces, RevolveFeature.faces, RevolveFeature.sideFaces, RevolveFeature.startFaces, RibFeature.faces, RipFeature.faces, RuledSurfaceFeature.faces, RuleFilletFeature.faces, ScaleFeature.faces, ShellFeature.faces, SilhouetteSplitFeature.faces, SphereFeature.faces, SplitBodyFeature.faces, SplitFaceFeature.faces, StitchFeature.faces, SurfaceDeleteFaceFeature.faces, SweepFeature.endFaces, SweepFeature.faces, SweepFeature.sideFaces, SweepFeature.startFaces, TessellateFeature.faces, ThickenFeature.faces, ThreadFeature.faces, TorusFeature.faces, TrimFeature.faces, UnfoldFeature.faces, UnstitchFeature.faces, UntrimFeature.faces, VolumetricCustomFeature.faces, VolumetricModelToMeshFeature.faces, WebFeature.faces

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> BRepFace
Function that returns the specified face using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (BRepFace): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
The number of faces in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
