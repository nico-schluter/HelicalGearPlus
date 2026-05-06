# Features
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

The features collection which provides access to all existing features. This collection provides direct access to all features regardless of type. It also provides access to type specific collections where you can get features of a specific type and also create new features of that type.

**Accessed from:** Component.features, FlatPatternComponent.features

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createPath(curve: Base, isChain: boolean) -> Path
Method that creates a Path used to define the shape of a Sweep feature. A Path is a contiguous set of curves that can be a combination of sketch curves and model edges.
- **curve** (Base): A SketchCurve or an ObjectCollection containing multiple sketch entities and/or BRepEdge objects. If a single sketch curve or edge is input the isChain argument is checked to determine if connected curves (they do not need to be tangent) should be automatically found. If multiple curves are provided the isChain argument is always treated as false so you must provide all of the curves in the object collection that you want included in the path. The provided curves must all connect together in a single path.

The input curves can be from multiple sketches and bodies and they need to geometrically connect for a valid path to be created.
- **isChain** (boolean): Optional argument, that defaults to true. If this argument is set to true, all curves and edges that are end point connected to the single input curve will be found and used to create the path. This argument is only used when the first argument is a single SketchCurve/BRepEdge object.

This is an optional argument whose default value is True.
- **Returns** (Path): Returns the newly created Path.

### item(index: uinteger) -> Feature
Function that returns the specified feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Feature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> Feature
Function that returns the specified feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the same name seen in the timeline.
- **Returns** (Feature): Returns the specified item or null if a feature matching the name was not found.

## Properties

### arrangeFeatures : ArrangeFeatures [read-only]
Returns the collection that provides access to the Arrange features within the component and supports the creation of new Arrange features.

### baseFeatures : BaseFeatures [read-only]
Returns the collection that provides access to the existing base features and supports the creation of new base features. A base feature represents a body that is non-parametric.

### bossFeatures : BossFeatures [read-only]
Returns the collection that provides access to the boss features within the component and supports the creation of new boss features.

### boundaryFillFeatures : BoundaryFillFeatures [read-only]
Returns the collection that provides access to the Boundary Fill features within the component and supports the creation of new Boundary Fill features.

### boxFeatures : BoxFeatures [read-only]
Returns the collection that provides access to the existing box features.

### chamferFeatures : ChamferFeatures [read-only]
Returns the collection that provides access to the chamfer features within the component and supports the creation of new chamfer features.

### circularPatternFeatures : CircularPatternFeatures [read-only]
Returns the collection that provides access to the circular pattern features within the component and supports the creation of new circular pattern features.

### coilFeatures : CoilFeatures [read-only]
Returns the collection that provides access to the Coil Primitive features within the component.

### combineFeatures : CombineFeatures [read-only]
Returns the collection that provides access to the combine features within the component and supports the creation of new combine features.

### copyPasteBodies : CopyPasteBodies [read-only]
Returns the collection that provides access to the existing copy-paste features and supports the creation of new copy-paste features.

### cornerClosureFeatures : CornerClosureFeatures [read-only]
Returns the collection that provides access to the existing Corner Closure features.

### count : uinteger [read-only]
Returns the number of features in the collection.

### customFeatures : CustomFeatures [read-only]
Returns the collection that provides access to the custom features within the component and supports the creation of new custom features.

### cutPasteBodies : CutPasteBodies [read-only]
Returns the collection that provides access to the existing cut-paste features and supports the creation of new cut-paste features.

### cylinderFeatures : CylinderFeatures [read-only]
Returns the collection that provides access to the existing cylinder features.

### deleteFaceFeatures : DeleteFaceFeatures [read-only]
Returns the collection that provides access to the existing Delete Face features.

### deriveFeatures : DeriveFeatures [read-only]
Returns the collection that provides access to the Derive features within the component and supports the creation of new Derive features.

### draftFeatures : DraftFeatures [read-only]
Returns the collection that provides access to the draft features within the component and supports the creation of new draft features.

### embossFeatures : EmbossFeatures [read-only]
Returns the collection that provides access to the emboss features within the component and supports the creation of new emboss features.

### extendFeatures : ExtendFeatures [read-only]
Returns the collection that provides access to the Extend features within the component and supports the creation of new Extend features.

### extrudeFeatures : ExtrudeFeatures [read-only]
Returns the collection that provides access to the extrude features within the component and supports the creation of new extrude features.

### filletFeatures : FilletFeatures [read-only]
Returns the collection that provides access to the fillet features within the component and supports the creation of new fillet features.

### flangeFeatures : FlangeFeatures [read-only]
Returns the collection that provides access to the existing flange features.

### formFeatures : FormFeatures [read-only]
Returns the collection that provides access to the existing form features.

### hemFeatures : HemFeatures [read-only]
Returns the collection that provides access to the existing Hem features.

### holeFeatures : HoleFeatures [read-only]
Returns the collection that provides access to the hole features within the component and supports the creation of new hole features.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### loftFeatures : LoftFeatures [read-only]
Returns the collection that provides access to the existing loft features and supports the creation of new loft features.

### mergeFacesFeatures : MergeFacesFeatures [read-only]
Returns the collection object that supports the ability to merge faces. Merging faces is currently limited to a Direct Modeling design or a body in a base feature. The result of merging faces is a direct B-Rep modification, and the change is not represented as a feature in the browser.

### meshCombineFaceGroupsFeatures : MeshCombineFaceGroupsFeatures [read-only]
Returns the collection that provides access to the mesh combine face groups features within the component and supports the creation of new mesh combine face groups features.

### meshCombineFeatures : MeshCombineFeatures [read-only]
Returns the collection that provides access to the mesh combine features within the component and supports the creation of new mesh combine features.

### meshConvertFeatures : MeshConvertFeatures [read-only]
Returns the collection that provides access to the mesh convert features within the component and supports the creation of new mesh convert features.

### meshGenerateFaceGroupsFeatures : MeshGenerateFaceGroupsFeatures [read-only]
Returns the collection that provides access to the mesh generate facegroup features within the component and supports the creation of new mesh generate facegroup features.

### meshReduceFeatures : MeshReduceFeatures [read-only]
Returns the collection that provides access to the mesh reduce features within the component and supports the creation of new mesh reduce features.

### meshRemeshFeatures : MeshRemeshFeatures [read-only]
Returns the collection that provides access to the mesh remesh features within the component and supports the creation of new mesh remesh features.

### meshRemoveFeatures : MeshRemoveFeatures [read-only]
Returns the collection that provides access to the mesh remove features within the component and supports the creation of new mesh remove features.

### meshRepairFeatures : MeshRepairFeatures [read-only]
Returns the collection that provides access to the mesh repair features within the component and supports the creation of new mesh repair features.

### meshReverseNormalFeatures : MeshReverseNormalFeatures [read-only]
Returns the collection that provides access to the mesh reverse normal features within the component and supports the creation of new mesh reverse normal features.

### meshSeparateFeatures : MeshSeparateFeatures [read-only]
Returns the collection that provides access to the mesh separate features within the component and supports the creation of new mesh separate features.

### meshShellFeatures : MeshShellFeatures [read-only]
Returns the collection that provides access to the mesh shell features within the component and supports the creation of new mesh shell features.

### meshSmoothFeatures : MeshSmoothFeatures [read-only]
Returns the collection that provides access to the mesh smooth features within the component and supports the creation of new mesh smooth features.

### mirrorFeatures : MirrorFeatures [read-only]
Returns the collection that provides access to the mirror features within the component and supports the creation of new mirror features.

### moveFeatures : MoveFeatures [read-only]
Returns the collection that provides access to the Move features within the component and supports the creation of new Move features.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### offsetFacesFeatures : OffsetFacesFeatures [read-only]
Returns the collection that provides access to the existing Offset Face features.

### offsetFeatures : OffsetFeatures [read-only]
Returns the collection that provides access to the Offset features within the component and supports the creation of new Offset features.

### patchFeatures : PatchFeatures [read-only]
Returns the collection that provides access to the Patch features within the component and supports the creation of new Patch features.

### pathPatternFeatures : PathPatternFeatures [read-only]
Returns the collection that provides access to the path pattern features within the component and supports the creation of new path pattern features.

### pipeFeatures : PipeFeatures [read-only]
Returns the collection that provides access to the existing pipe features.

### rectangularPatternFeatures : RectangularPatternFeatures [read-only]
Returns the collection that provides access to the rectangular pattern features within the component and supports the creation of new rectangular pattern features.

### refoldFeatures : RefoldFeatures [read-only]
Returns the collection that provides access to the existing refold features.

### removeFeatures : RemoveFeatures [read-only]
Returns the collection that provides access to the Remove features within the component and supports the creation of new Remove features.

### replaceFaceFeatures : ReplaceFaceFeatures [read-only]
Returns the collection that provides access to the replaceFace features within the component and supports the creation of new replaceFace features.

### reverseNormalFeatures : ReverseNormalFeatures [read-only]
Returns the collection that provides access to the Reverse Normal features within the component and supports the creation of new Reverse Normal features.

### revolveFeatures : RevolveFeatures [read-only]
Returns the collection that provides access to the revolve features within the component and supports the creation of new revolved features.

### ribFeatures : RibFeatures [read-only]
Returns the collection that provides access to the existing rib features.

### ripFeatures : RipFeatures [read-only]
Returns the collection that provides access to the existing Rip features.

### ruledSurfaceFeatures : RuledSurfaceFeatures [read-only]
Returns the collection that provides access to the Ruled Surface features within the component and supports the creation of new Ruled Surface features.

### ruleFilletFeatures : RuleFilletFeatures [read-only]
This function is retired. See more information in the 'Remarks' section below.

Returns the collection that provides access to the existing rule fillet features.

### scaleFeatures : ScaleFeatures [read-only]
Returns the collection that provides access to the scale features within the component and supports the creation of new scale features.

### shellFeatures : ShellFeatures [read-only]
Returns the collection that provides access to the shell features within the component and supports the creation of new shell features.

### silhouetteSplitFeatures : SilhouetteSplitFeatures [read-only]
Returns the collection that provides access to the Parting Line Split features within the component and supports the creation of new Parting Line Split features

### sphereFeatures : SphereFeatures [read-only]
Returns the collection that provides access to the existing sphere features.

### splitBodyFeatures : SplitBodyFeatures [read-only]
Returns the collection that provides access to the SplitBody features within the component and supports the creation of new SplitBody features

### splitFaceFeatures : SplitFaceFeatures [read-only]
Returns the collection that provides access to the SplitFace features within the component and supports the creation of new SplitFace features

### stitchFeatures : StitchFeatures [read-only]
Returns the collection that provides access to the Stitch features within the component and supports the creation of new Stitch features.

### surfaceDeleteFaceFeatures : SurfaceDeleteFaceFeatures [read-only]
Returns the collection that provides access to the existing Surface Delete Face features.

### sweepFeatures : SweepFeatures [read-only]
Returns the collection that provides access to the sweep features within the component and supports the creation of new sweep features.

### tessellateFeatures : TessellateFeatures [read-only]
Returns the collection that provides access to the tessellate features within the component and supports the creation of new tessellate features.

### thickenFeatures : ThickenFeatures [read-only]
Returns the collection that provides access to the Thicken features within the component and supports the creation of new Thicken features.

### threadFeatures : ThreadFeatures [read-only]
Returns the collection that provides access to the thread features within the component and supports the creation of new thread features.

### torusFeatures : TorusFeatures [read-only]
Returns the collection that provides access to the existing torus features.

### trimFeatures : TrimFeatures [read-only]
Returns the collection that provides access to the Trim features within the component and supports the creation of new Trim features.

### unfoldFeatures : UnfoldFeatures [read-only]
Returns the collection that provides access to the existing unfold features.

### unstitchFeatures : UnstitchFeatures [read-only]
Returns the collection that provides access to the Unstitch features within the component and supports the creation of new Unstitch features.

### untrimFeatures : UntrimFeatures [read-only]
Returns the collection that provides access to the Untrim features within the component and supports the creation of new Untrim features.

### volumetricCustomFeatures : VolumetricCustomFeatures [read-only]
Returns the collection that provides access to volumetric custom features within the component and supports the creation of new volumetric custom features.

### volumetricModelToMeshFeatures : VolumetricModelToMeshFeatures [read-only]
Returns the collection that provides access to the Volumetric Model to Mesh features within the component and supports the creation of new Volumetric Model to Mesh features.

### webFeatures : WebFeatures [read-only]
Returns the collection that provides access to the existing web features.

## Samples
- **Loft Feature API Sample**: Demonstrates creating a new loft feature.
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
