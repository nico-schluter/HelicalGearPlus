# BRepFace
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Represent a connected region on a single geometric surface.

**Accessed from:** BRepFace.createForAssemblyContext, BRepFace.nativeObject, BRepFaces.item, BRepLoop.face, ConstructionAxisCircularFaceDefinition.circularFace, ConstructionAxisPerpendicularAtPointDefinition.face, ConstructionPlaneTangentAtPointDefinition.tangentFace, Decal.faces, DecalInput.faces, DeleteFaceFeature.deletedFaces, DraftFeature.inputFaces, DraftFeatureInput.inputFaces, EmbossFeature.inputFaces, EmbossFeatureInput.inputFaces, FaceRipFeatureDefinition.ripFace, FlatPattern.bottomFace, FlatPattern.topFace, FullRoundFilletFaceSet.centerFace, FullRoundFilletFaceSet.sideOneFaces, FullRoundFilletFaceSet.sideTwoFaces, LoftFeature.endFace, LoftFeature.startFace, MergeFacesFeatureInput.inputFaces, OffsetFacesFeature.inputFaces, OffsetFacesFeatureInput.faces, PatternElement.faces, Profile.face, RecognizedPocket.faces, RecognizedPocket.sharedFaces, SurfaceDeleteFaceFeature.deletedFaces, SweepFeature.guideSurfaces, SweepFeatureInput.guideSurfaces, TangentRelationshipInput.faceOne, ThreadFeature.inputCylindricalFace, ThreadFeatureInput.inputCylindricalFace, UntrimFeature.facesToUntrim, UntrimFeatureInput.facesToUntrim

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### convert(options: BRepConvertOptions) -> BRepBody
Creates a new body where this face and its edges are converted to different types of geometry based on the input options.

The tempId on the faces, edges, and vertices on the new body will match with the corresponding tempId on the original body. In cases where the face is split as a result of the conversion there can be more than one face or edge in the new body that matches to a single face or edge in the original body.
- **options** (BRepConvertOptions): Input options that define how the conversion should be done. These are bitwise options so they can be combined.
- **Returns** (BRepBody): Returns the new converted body or null in the case of failure.

### createForAssemblyContext(occurrence: Occurrence) -> BRepFace
Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context for the created proxy.
- **Returns** (BRepFace): Returns the new BRepFace proxy or null if this isn't the NativeObject.

### isPointOnFace(point: Point3D, tolerance: double) -> boolean
Checks if input point is on this BRepFace. This takes into account any boundaries so if the point is within a void area of the face, this will return false.
- **point** (Point3D): The input point to check.
- **tolerance** (double): Specifies how close the point must be to the face to be considered on the face. Defaults to the point tolerance which can be obtained using the Application.pointTolerance property. The value is in centimeters.

This is an optional argument whose default value is 0.0.
- **Returns** (boolean): Returns true if the point lies on the face.

## Properties

### appearance : Appearance [read-write]
Read-write property that gets and sets the current appearance of the face. Setting this property will result in applying an override appearance to the face and the AppearanceSourceType property will return OverrideAppearanceSource. Setting this property to null will remove any override.

### appearanceSourceType : AppearanceSourceTypes [read-only]
Read-write property that gets the source of the appearance for the face. If this returns OverrideAppearanceSource, an override exists on this face. The override can be removed by setting the Appearance property to null.

### area : double [read-only]
Returns the area in cm ^ 2.

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this BRepFace object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this face.

### body : BRepBody [read-only]
Returns the parent body of the face.

### boundingBox : BoundingBox3D [read-only]
Returns the bounding box of this face

### centroid : Point3D [read-only]
Returns a point at the centroid (aka, geometric center) of the face.

### edges : BRepEdges [read-only]
Returns the BRepEdges used by this face

### entityToken : string [read-only]
Returns a token for the BRepFace object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same face.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

This is only valid for faces that exist in the design, (the isTemporary property is false).

### evaluator : SurfaceEvaluator [read-only]
Returns a SurfaceEvaluator to allow geometric evaluations across the face's surface. This evaluator differs from the evaluator available from the Surface obtained from the geometry property by being bounded by the topological boundaries of this face.

### geometry : Surface [read-only]
Returns the underlying surface geometry of this face

### isParamReversed : boolean [read-only]
Gets if the normal of this face is reversed with respect to the surface geometry associated with this face.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### loops : BRepLoops [read-only]
Returns the BRepLoops owned by this face

### meshManager : MeshManager [read-only]
Returns a MeshManager object that allows access to existing and new meshes of this face.

### nativeObject : BRepFace [read-only]
The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### pointOnFace : Point3D [read-only]
Returns a sample point guaranteed to lie on the face's surface, within the face's boundaries, and not on a boundary edge.

### shell : BRepShell [read-only]
Returns the parent shell of the face.

### tangentiallyConnectedFaces : BRepFaces [read-only]
Returns the set of faces that are tangentially adjacent to this face. In other words, it is the set of faces that are adjacent to this face's edges and have a smooth transition across those edges.

### tempId : integer [read-only]
Returns the temporary ID of this face. This ID is only good while the document remains open and as long as the owning BRepBody is not modified in any way. The findByTempId method of the BRepBody will return the entity in the body with the given ID.

### vertices : BRepVertices [read-only]
Returns the BRepVertices used by this face

## Samples
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
