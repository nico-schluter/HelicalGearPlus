# BRepBody
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Represents a B-Rep (Boundary Representation) body.

**Accessed from:** BaseFeature.sourceBodies, BossFeatureInput.participantBodies, BRepBodies.add, BRepBodies.item, BRepBodies.itemByName, BRepBody.convert, BRepBody.copyToComponent, BRepBody.createComponent, BRepBody.createForAssemblyContext, BRepBody.moveToComponent, BRepBody.nativeObject, BRepBodyDefinition.createBody, BRepCell.cellBody, BRepCoEdge.body, BRepEdge.body, BRepFace.body, BRepFace.convert, BRepLoop.body, BRepLump.body, BRepShell.body, BRepVertex.body, BRepWire.offsetPlanarWire, BRepWire.parent, CombineFeature.targetBody, CombineFeatureInput.targetBody, CustomGraphicsBRepBody.bRepBody, ExtrudeFeature.participantBodies, ExtrudeFeatureInput.participantBodies, FlatPattern.bendLinesBody, FlatPattern.extentLinesBody, FlatPattern.flatBody, FlatPattern.foldedBody, HoleFeature.participantBodies, HoleFeatureInput.participantBodies, InterferenceResult.interferenceBody, LoftFeature.participantBodies, LoftFeatureInput.participantBodies, PipeFeature.participantBodies, PipeFeatureInput.participantBodies, RevolveFeature.participantBodies, RevolveFeatureInput.participantBodies, SilhouetteSplitFeature.targetBody, SilhouetteSplitFeatureInput.targetBody, SweepFeature.participantBodies, SweepFeature.solidBody, SweepFeatureInput.participantBodies, SweepFeatureInput.solidBody, TemporaryBRepManager.copy, TemporaryBRepManager.createBox, TemporaryBRepManager.createCylinderOrCone, TemporaryBRepManager.createEllipticalCylinderOrCone, TemporaryBRepManager.createFaceFromPlanarWires, TemporaryBRepManager.createHelixWire, TemporaryBRepManager.createProjectedBodyOutline, TemporaryBRepManager.createRuledSurface, TemporaryBRepManager.createSilhouetteCurves, TemporaryBRepManager.createSphere, TemporaryBRepManager.createTorus, TemporaryBRepManager.createWireFromCurves, TemporaryBRepManager.imprintOverlapBodies, TemporaryBRepManager.planeIntersection, TessellateFeature.inputBodies, TessellateFeatureInput.inputBodies

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### convert(options: BRepConvertOptions) -> BRepBody
Creates a new body where the faces and edges are converted to different types of geometry based on the input options. This is particularly useful when you need a body made up entirely of NURBS surfaces.

The tempId on the faces, edges, and vertices on the new body will match with the corresponding tempId on the original body. In cases where faces are split as a result of the conversion there can be more than one face or edge in the new body that matches to a single face or edge in the original body. The findByTempId method will find the entity with the matching id.
- **options** (BRepConvertOptions): Input options that define how the conversion should be done. These are bitwise options so they can be combined.
- **Returns** (BRepBody): Returns the new converted body or null in the case of failure.

### copy() -> boolean
Copies the body to the clipboard.
- **Returns** (boolean): Returns true if the copy was successful.

### copyToComponent(target: Base) -> BRepBody
Creates a copy of this body into the specified target.
- **target** (Base): The target can be either the root component or an occurrence.

In the case where an occurrence is specified, the body will be copied into the parent component of the target occurrence and the target occurrence defines the transform of how the body will be copied so that the body maintains it's same position with respect to the assembly.

If target is null, then a copy of the body is created in the owning component of the original body.
- **Returns** (BRepBody): Returns the moved BRepBody or null in the case the move failed.

### createComponent() -> BRepBody
Creates a new component and occurrence within the component that currently owns this body. This body is moved into the new component and returned. The newly created component can be obtained by using the parentComponent property of the BRepBody object.

This method is only valid if the IsTransient property is false.
- **Returns** (BRepBody): Returns the BRrepBody in the new component or null in the case the creation failed.

### createForAssemblyContext(occurrence: Occurrence) -> BRepBody
Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.

This method is only valid if the IsTransient property is false.
- **occurrence** (Occurrence): The occurrence that defines the context for the created proxy.
- **Returns** (BRepBody): Returns the new BRepBoy proxy or null if this isn't the NativeObject.

### cut() -> boolean
Cuts the body to the clipboard.
- **Returns** (boolean): Returns true if the cut was successful.

### deleteMe() -> boolean
Deletes the body.
- **Returns** (boolean): Returns true if the delete was successful.

### findByTempId(tempId: integer) -> Base
Returns all of the faces, edges, or vertices that match the input ID.
- **tempId** (integer): The ID of the B-Rep entity to find.
- **Returns** (Base): Returns an array of entities that have the specified ID. This returns an array because it's possible that a body created by converting a body can have multiple entities with the same ID in the case where a curve or face was split. Returns an empty array in the case where no match is found.

### getPhysicalProperties(accuracy: CalculationAccuracy) -> PhysicalProperties
Returns the PhysicalProperties object that has properties for getting the area, density, mass, volume, moments, etc of this body.
- **accuracy** (CalculationAccuracy): Specifies the desired level of computational accuracy of the property calculations. The default value of 'LowCalculationAccuracy' returns results within a +/- 1% error margin.

This is an optional argument whose default value is CalculationAccuracy.LowCalculationAccuracy.
- **Returns** (PhysicalProperties): Returns a PhysicalProperties object that can be used to get the various physical property related values.

### moveToComponent(target: Base) -> BRepBody
Moves this body from it's current component into the root component or the component owned by the specified occurrence.
- **target** (Base): The target can be either the root component or an occurrence.

In the case where an occurrence is specified, the body will be moved into the parent component of the target occurrence and the target occurrence defines the transform of how the body will be copied so that the body maintains it's same position with respect to the assembly.
- **Returns** (BRepBody): Returns the moved BRepBody or null in the case the move failed.

### pointContainment(point: Point3D) -> PointContainment
Determines the relationship of the input point with respect to this body.
- **point** (Point3D): The point to do the containment check for.
- **Returns** (PointContainment): Returns a value from the PointContainment enum indicating the relationship of the input point to the body.

## Properties

### appearance : Appearance [read-write]
Read-write property that gets and sets the current appearance of the body. Setting this property will result in applying an override appearance to the body and the AppearanceSourceType property will return OverrideAppearanceSource. Setting this property to null will remove any override.

### appearanceSourceType : AppearanceSourceTypes [read-only]
Read-write property that gets the source of the appearance for the body. If this returns OverrideAppearanceSource, an override exists on this body. The override can be removed by setting the Appearance property to null.

### area : double [read-only]
Returns the area in cm ^ 2.

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this BRepBody object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object. Also returns null in the case where this body is transient.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this face.

### baseFeature : BaseFeature [read-only]
If this body is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null.

### boundingBox : BoundingBox3D [read-only]
Returns the bounding box of this body.

### concaveEdges : BRepEdges [read-only]
Returns all of the edges that connect concave faces.

### convexEdges : BRepEdges [read-only]
Returns all of the edges that connect convex faces.

### deriveFeature : DeriveFeature [read-only]
Returns the DeriveFeature if this BRepBody is derived from another design. This property returns null if the BRepBody is not derived from another design (i.e. isDerived property returns false).

### edges : BRepEdges [read-only]
Returns a collection of all of the edges in the body.

### entityToken : string [read-only]
Returns a token for the BRepBody object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same body.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

This is only valid for bodies that exist in the design, (the isTemporary property is false).

### faces : BRepFaces [read-only]
Returns a collection of all of the faces in the body.

### isDerived : boolean [read-only]
Returns if this BRepBody is derived from another design. If true, this body cannot be deleted.

### isLightBulbOn : boolean [read-write]
Gets and set if the light bulb beside the body node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children so this property does not indicate if the body is actually visible, just that it should be visible if all of it's parent nodes are also visible. Use the isVisible property to determine if it's actually visible.

### isSelectable : boolean [read-write]
Gets and sets if this body is selectable.

### isSheetMetal : boolean [read-only]
Indicates if this body represents a sheet metal folded part or not and if a flat pattern can be created.

### isSolid : boolean [read-only]
Returns whether this body is closed (solid) or not.

### isTemporary : boolean [read-only]
Indicates if this body is represented in the model or is temporary.

### isTransient : boolean [read-only]
Indicates if this body is represented in the model or is transient.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-write]
Gets if this body is currently visible in the graphics window. Use the isLightBulbOn to change if the light bulb beside the body node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children. This property indicates the final result and whether this body is actually visible or not.

### lumps : BRepLumps [read-only]
Returns a collection of all of the lumps in the body.

### material : Material [read-write]
Gets and sets the material assigned to this body.

### meshManager : MeshManager [read-only]
Returns the mesh manager object for this body.

### name : string [read-write]
Gets and sets the name of the body.

### nativeObject : BRepBody [read-only]
The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### opacity : double [read-write]
Gets and sets the opacity override assigned to this body. A value of 1.0 specifies that is it completely opaque and a value of 0.0 specifies that is it completely transparent.

This value is not necessarily related to what the user sees because the opacity is inherited. For example, if you this body is in a component and that component's opacity is set to something other than 1.0, the body will also be shown as slightly transparent even though the opacity property for the body will return 1.0. Because the component that contains the body can be referenced as an occurrence in other components and they can have different opacity settings, it's possible that different instances of the same body can display using different opacity levels. To get the opacity that it is being displayed with use the BrepBody.visibleOpacity property.

This is the API equivalent of the "Opacity Control" command available for the body in the browser.

### orientedMinimumBoundingBox : OrientedBoundingBox3D [read-only]
Returns an oriented bounding box of the body that is best oriented to tightly fit the body.

### parentComponent : Component [read-only]
Returns the component this body is owned by.

### physicalProperties : PhysicalProperties [read-only]
Returns the PhysicalProperties object that has properties for getting the area, density, mass, volume, moments, etc of this body. Property values will be calculated using the 'LowCalculationAccuracy' setting when using this property to get the PhysicalProperties object. To specify a higher calculation tolerance, use the getPhysicalProperties method on the Design class instead.

### preciseBoundingBox : BoundingBox3D [read-only]
Returns a bounding box that tightly fits this body.

### revisionId : string [read-only]
Returns the current revision ID of the body. This ID changes any time the body is modified in any way. By getting and saving the ID when you create any data that is dependent on the body, you can then compare the saved ID with the current ID to determine if the body has changed to know if you should update your data.

### shells : BRepShells [read-only]
Returns a collection of all of the shells in the body.

### textureMapControl : TextureMapControl [read-only]
Returns the TextureMapControl object associated with this body when there is an appearance assigned to the body that has a texture associated with it. If there isn't a texture, this property will return null. If there is a texture, you can use the returned object to query and modify how the texture is applied to the body.

### vertices : BRepVertices [read-only]
Returns a collection of all of the vertices in the body.

### visibleOpacity : double [read-only]
The user can set an override opacity for components and bodies these opacity overrides combine if children and parent components have overrides. This property returns the actual opacity that is being used to render the body. To set the opacity use the opacity property of the BRepBody object.

### volume : double [read-only]
Returns the volume in cm ^ 3. Returns 0 in the case the body is not solid.

### wires : BRepWires [read-only]
Returns any wire bodies that exist within this body.

## Samples
- **Get Volume of Active Design API Sample**: Traverses through the active design and totals the volume of every body within the design.
