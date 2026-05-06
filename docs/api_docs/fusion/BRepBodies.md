# BRepBodies
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

The BRepBodies collection provides access to all of the B-Rep bodies within a component.

**Accessed from:** ArrangeFeature.bodies, BaseComponent.bRepBodies, BaseFeature.bodies, BossFeature.bodies, BoundaryFillFeature.bodies, BoxFeature.bodies, ChamferFeature.bodies, CircularPatternFeature.bodies, CoilFeature.bodies, CombineFeature.bodies, Component.bRepBodies, CopyPasteBody.bodies, CornerClosureFeature.bodies, CustomFeature.bodies, CutPasteBody.bodies, CylinderFeature.bodies, DeleteFaceFeature.bodies, DeriveFeature.bodies, DraftFeature.bodies, EmbossFeature.bodies, ExtendFeature.bodies, ExtrudeFeature.bodies, Feature.bodies, FilletFeature.bodies, FlangeFeature.bodies, FlatPattern.bodies, FlatPatternComponent.bRepBodies, FormFeature.bodies, HemFeature.bodies, HoleFeature.bodies, LoftFeature.bodies, MeshCombineFaceGroupsFeature.bodies, MeshCombineFeature.bodies, MeshConvertFeature.bodies, MeshFeature.bodies, MeshGenerateFaceGroupsFeature.bodies, MeshReduceFeature.bodies, MeshRemeshFeature.bodies, MeshRemoveFeature.bodies, MeshRepairFeature.bodies, MeshReverseNormalFeature.bodies, MeshSeparateFeature.bodies, MeshShellFeature.bodies, MeshSmoothFeature.bodies, MirrorFeature.bodies, MoveFeature.bodies, Occurrence.bRepBodies, OffsetFacesFeature.bodies, OffsetFeature.bodies, PatchFeature.bodies, PathPatternFeature.bodies, PipeFeature.bodies, RectangularPatternFeature.bodies, RefoldFeature.bodies, RemoveFeature.bodies, ReplaceFaceFeature.bodies, ReverseNormalFeature.bodies, RevolveFeature.bodies, RibFeature.bodies, RipFeature.bodies, RuledSurfaceFeature.bodies, RuleFilletFeature.bodies, ScaleFeature.bodies, ShellFeature.bodies, SilhouetteSplitFeature.bodies, SphereFeature.bodies, SplitBodyFeature.bodies, SplitFaceFeature.bodies, StitchFeature.bodies, SurfaceDeleteFaceFeature.bodies, SweepFeature.bodies, TemporaryBRepManager.createFromFile, TessellateFeature.bodies, ThickenFeature.bodies, ThreadFeature.bodies, TorusFeature.bodies, TrimFeature.bodies, UnfoldFeature.bodies, UnstitchFeature.bodies, UntrimFeature.bodies, VolumetricCustomFeature.bodies, VolumetricModelToMeshFeature.bodies, WebFeature.bodies

## Methods

### add(body: BRepBody, targetBaseFeature: BaseFeature) -> BRepBody
Creates a new BRepBody object. The input can be a persisted or transient BRepBody and the result is a persisted BRepBody. In a direct modeling design, the BRepBody is created within the component the BRepBodies collection was obtained from. In a parametric modeling design, the new BRepBody is created within the specified Base Feature.

Because of a current limitation, if you want to create a BRepBody in a parametric model, you must first call the edit method of the base feature, then use the add method to create the body, and finally call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.
- **body** (BRepBody): The input BRepBody. Typically this is a transient BRepBody but that's not a requirement. In any case, there is not any association back to the original BRepBody.
- **targetBaseFeature** (BaseFeature): The BaseFeature object that this BRep body will be associated with. This is an optional requirement. It is required in a parametric modeling design but is ignored in a direct modeling design.

This is an optional argument whose default value is null.
- **Returns** (BRepBody): Returns the newly created BRepBody or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> BRepBody
Function that returns the specified body using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (BRepBody): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> BRepBody
Returns a specific body using the name of the body within the collection.
- **name** (string): The name of the body, as seen in the browser, to return.
- **Returns** (BRepBody): The BRepBody or null if a body with the defined name is not found.

## Properties

### count : uinteger [read-only]
Returns the number of bodies in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Get Volume of Active Design API Sample**: Traverses through the active design and totals the volume of every body within the design.
