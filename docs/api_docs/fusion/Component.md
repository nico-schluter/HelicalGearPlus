# Component
Namespace: adsk.fusion
Inherits: BaseComponent
Since: August 2014

Represents a component in the data model. A component represents a set of geometry, features, and parameters that make up an item in the design. A component can be referenced multiple times into a design with a Occurrence object.

**Accessed from:** ArrangeFeature.parentComponent, AsBuiltJoint.parentComponent, AssemblyConstraint.parentComponent, BaseFeature.parentComponent, BossFeature.parentComponent, BoundaryFillFeature.parentComponent, BoxFeature.parentComponent, BRepBody.parentComponent, ChamferFeature.parentComponent, CircularPatternFeature.parentComponent, CoilFeature.parentComponent, CombineFeature.parentComponent, ComponentList.item, Components.item, Components.itemById, Components.itemByName, ConfigurationPlasticRuleColumn.component, ConfigurationSheetMetalRuleColumn.component, ConstructionAxes.component, ConstructionAxis.component, ConstructionPlane.component, ConstructionPlanes.component, ConstructionPoint.component, ConstructionPoints.component, CopyPasteBody.parentComponent, CornerClosureFeature.parentComponent, CustomFeature.parentComponent, CustomFeatureParameter.component, CutPasteBody.parentComponent, CylinderFeature.parentComponent, DeleteFaceFeature.parentComponent, DeriveFeature.parentComponent, Design.activeComponent, Design.rootComponent, DraftFeature.parentComponent, EmbossFeature.parentComponent, ExtendFeature.parentComponent, ExtrudeFeature.parentComponent, Feature.parentComponent, FilletFeature.parentComponent, FlangeFeature.parentComponent, FlatPattern.parentComponent, FlatPatternProduct.activeComponent, FlatPatternProduct.rootComponent, FormFeature.parentComponent, HemFeature.parentComponent, HoleFeature.parentComponent, Joint.parentComponent, JointOrigin.parentComponent, LoftFeature.parentComponent, MeshBody.parentComponent, MeshCombineFaceGroupsFeature.parentComponent, MeshCombineFeature.parentComponent, MeshConvertFeature.parentComponent, MeshFeature.parentComponent, MeshGenerateFaceGroupsFeature.parentComponent, MeshReduceFeature.parentComponent, MeshRemeshFeature.parentComponent, MeshRemoveFeature.parentComponent, MeshRepairFeature.parentComponent, MeshReverseNormalFeature.parentComponent, MeshSeparateFeature.parentComponent, MeshShellFeature.parentComponent, MeshSmoothFeature.parentComponent, MirrorFeature.parentComponent, ModelParameter.component, ModelParameters.component, MotionLink.parentComponent, MoveFeature.parentComponent, Occurrence.component, Occurrence.sourceComponent, OffsetFacesFeature.parentComponent, OffsetFeature.parentComponent, PatchFeature.parentComponent, PathPatternFeature.parentComponent, PipeFeature.parentComponent, RectangularPatternFeature.parentComponent, RefoldFeature.parentComponent, RemoveFeature.parentComponent, ReplaceFaceFeature.parentComponent, ReverseNormalFeature.parentComponent, RevolveFeature.parentComponent, RibFeature.parentComponent, RigidGroup.parentComponent, RipFeature.parentComponent, RuledSurfaceFeature.parentComponent, RuleFilletFeature.parentComponent, ScaleFeature.parentComponent, ShellFeature.parentComponent, SilhouetteSplitFeature.parentComponent, Sketch.parentComponent, SphereFeature.parentComponent, SplitBodyFeature.parentComponent, SplitFaceFeature.parentComponent, StitchFeature.parentComponent, SurfaceDeleteFaceFeature.parentComponent, SweepFeature.parentComponent, TangentRelationship.parentComponent, TessellateFeature.parentComponent, ThickenFeature.parentComponent, ThreadFeature.parentComponent, TorusFeature.parentComponent, TrimFeature.parentComponent, UnfoldFeature.parentComponent, UnstitchFeature.parentComponent, UntrimFeature.parentComponent, VolumetricCustomFeature.parentComponent, VolumetricModel.parentComponent, VolumetricModelToMeshFeature.parentComponent, WebFeature.parentComponent, WorkingModel.activeComponent, WorkingModel.rootComponent, WorkingModel.sourceComponent

## Methods

### allOccurrencesByComponent(component: Component) -> OccurrenceList
Returns all occurrences, at any level of the assembly, that reference the specified component. The returned list is read-only.
- **component** (Component): The component that is being referenced by the occurrences that will be returned.
- **Returns** (OccurrenceList): The occurrences referenced by the specified component.

### boundingBox2(entityTypes: BoundingBoxEntityTypes) -> BoundingBox3D
Returns the bounding box of the specified entity types within the component.
- **entityTypes** (BoundingBoxEntityTypes): Bitwise value that specifies the types of entities to include in the calculation of the bounding box.
- **Returns** (BoundingBox3D): Returns a BoundingBox3D object if the calculation was successful and null in the case where there is no valid geometry and the bounding box is empty.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createBRepEdgeProfile(edges: Base, chainEdges: boolean) -> Profile
Creates a profile based on the outside open edges of a BRepFace.
- **edges** (Base): A single BRepEdge object or an ObjectCollection containing multiple BRepEdge objects, or a BRepLoop object. If a single edge is input, the chainEdges argument is checked to determine if connected edges (they do not need to be tangent) should be automatically found. If multiple edges are provided the chainEdges argument is always treated as false so you must provide all of the edges in the object collection that you want included in the profile. and the edges must all connect together in a single path. if a BRepLoop object is provided, all of the edges in the loop are included in the profile and the chainEdges argument is ignored.
- **chainEdges** (boolean): If true, this finds any edges that connect to the single input edge and automatically includes them in the profile. If false, only the edges provided will be used to define the profile. This argument is ignored and treated as false if multiple edges or a BRepLoop is input.

This is an optional argument whose default value is True.
- **Returns** (Profile): Returns the new Profile object or null in the case of a failure.

### createFlatPattern(stationaryFace: BRepFace) -> FlatPattern
Creates a flat pattern of the sheet metal folded body. The isSheetMetal property of the BRepBody object can be used to determine if a particular body can be flattened. Creating a flat pattern will fail if a flat pattern already exists in the component. You can determine if a flat pattern already exists by checking if the flatPattern property returns a FlatPattern object or null.
- **stationaryFace** (BRepFace): A planar face in the sheet metal body that is on the top or bottom of the part and not an edge face. This face will be positioned on the X-Y plane of the flat pattern and the rest of the model will be flattened relative to this face. The face must exist on a body that is owned by this component.
- **Returns** (FlatPattern): Returns the newly created flat pattern.

### createOpenProfile(curves: Base, chainCurves: boolean) -> Profile
Creates an open profile based on the input curve(s).
- **curves** (Base): A SketchCurve or an ObjectCollection containing multiple sketch entities. If a single sketch curve is input the chainCurves argument is checked to determine if connected curves (they do not need to be tangent) should be automatically found. If multiple curves are provided the chainCurves argument is always treated as false so you must provide all of the curves in the object collection that you want included in the profile. The provided curves must all connect together in a single path.

The input curves do not need to be in the same sketch, but they do need to geometrically connect for a valid profile to be created.
- **chainCurves** (boolean): If true, this finds any curves within the same sketch that connect to the single input curve and automatically includes them in the profile. If false, only the curves provided will be used to define the profile. This argument is ignored and treated as false if multiple curves are input.

This is an optional argument whose default value is True.
- **Returns** (Profile): Returns the new Profile object or null in the case of a failure.

### createThumbnail(width: integer, height: integer, imageType: string) -> DataObject
Creates a thumbnail for this component. This can be a root component to get a thumbnail that represents the associated file, or it can be any sub component to get a thumbnail of a subset of the complete assembly or individual parts.
- **width** (integer): Optional argument to define the width of the thumbnail in pixels. A default width of 256 pixels is used if no width is specified.

This is an optional argument whose default value is 256.
- **height** (integer): Optional argument to define the height of the thumbnail in pixels. A default height of 256 pixels is used if no height is specified.

This is an optional argument whose default value is 256.
- **imageType** (string): Optional argument to define the type of image data to create. The default of PNG is used if no type is specified. Valid types include "PNG", "JPG", "TIF", and "BMP".

This is an optional argument whose default value is "PNG".
- **Returns** (DataObject): Returns a DataObject that you can use to save the thumbnail to a file or to access the binary data of the bitmap directly.

### findBRepUsingPoint(point: Point3D, entityType: BRepEntityTypes, proximityTolerance: double, visibleEntitiesOnly: boolean) -> ObjectCollection
Finds all the entities of the specified type at the specified location.
- **point** (Point3D): Input coordinate that specifies the component space point at which to find the entities.
- **entityType** (BRepEntityTypes): The type of B-Rep entity wanted. You can also take advantage of B-Rep topology to infer other that other entities were found. For example, If you get a BRepEdge it implies that the faces the edge connects were also found. If a BRepVertex is returned it implies the edges that the vertex connects were found and the faces that the edges connect were found.
- **proximityTolerance** (double): Specifies the tolerance for the search. All entities within this distance from the search point that match the filter will be returned. If not specified a default tolerance is used.

This is an optional argument whose default value is -1.0.
- **visibleEntitiesOnly** (boolean): indicates whether or not invisible objects should be included in the search. Defaults to True indicating that invisible objects will be ignored.

This is an optional argument whose default value is True.
- **Returns** (ObjectCollection): Returns an ObjectCollection containing the entities found. The returned collection can be empty indicating nothing was found.

### findBRepUsingRay(originPoint: Point3D, rayDirection: Vector3D, entityType: BRepEntityTypes, proximityTolerance: double, visibleEntitiesOnly: boolean, hitPoints: ObjectCollection) -> ObjectCollection
Finds all the B-Rep entities that are intersected by the specified ray. This can return BRepFace, BrepEdge, and BRepVertex objects.
- **originPoint** (Point3D): Input point that defines the origin of the ray. The search for entities begins at this point.
- **rayDirection** (Vector3D): Input vector that defines the direction of the ray. The ray is infinite so the length of the vector is ignored.
- **entityType** (BRepEntityTypes): The type of B-Rep entity wanted. You can also take advantage of B-Rep topology to infer other intersections. For example, If you get a BRepEdge it implies that the faces the edge connects were also intersected. If a BRepVertex is returned it implies the edges that the vertex connects were intersected and the faces that the edges connect were intersected.
- **proximityTolerance** (double): Optional argument that specifies the tolerance for the search. All entities within this distance from the ray and of the specified type will be returned. If not specified a default small tolerance is used.

This is an optional argument whose default value is -1.0.
- **visibleEntitiesOnly** (boolean): Optional argument that indicates whether or not invisible entities should be included in the search. Defaults to True indicating that invisible entities will be ignored.

This is an optional argument whose default value is True.
- **hitPoints** (ObjectCollection): An ObjectCollection of Point3D objects that represent the coordinates where the ray hit the found entity. There will be the same number of hit points as returned entities and they will be in the collections in the same order. In other words, hit point 1 corresponds with found entity 1, hit point 2 corresponds with found entity 2, and so on. Because of the proximity tolerance the hitPoint may not actually lie on the entity but will be within the proximity tolerance to it. It's an optional out argument, returns the hit points if an existing ObjectCollection is input. You can create a new ObjectCollection by using the static create method on the ObjectCollection class.

This is an optional argument whose default value is null.
- **Returns** (ObjectCollection): Returns an ObjectCollection containing the entities found. The returned collection can be empty indicating nothing was found. The points are returned in an order where they are arranged based on their distance from the origin point where the closest point is first. If an entity is hit more than once, the entity is returned once for the first intersection.

### getPhysicalProperties(accuracy: CalculationAccuracy) -> PhysicalProperties
Returns the PhysicalProperties object that has properties for getting the area, density, mass, volume, moments, etc of this component.
- **accuracy** (CalculationAccuracy): Specifies the desired level of computational accuracy of the property calculations. The default value of 'LowCalculationAccuracy' returns results within a +/- 1% error margin.

This is an optional argument whose default value is CalculationAccuracy.LowCalculationAccuracy.
- **Returns** (PhysicalProperties): Returns a PhysicalProperties object that can be used to get the various physical property related values.

### occurrencesByComponent(component: Component) -> OccurrenceList
Returns all occurrences at the top-level of this component that reference the specified component. The returned list is read-only.
- **component** (Component): The component that is being referenced by the occurrences that will be returned.
- **Returns** (OccurrenceList): The occurrences referenced by the specified component.

### saveCopyAs(name: string, dataFolder: DataFolder, description: string, tag: string) -> DataFileFuture
Performs a Save Copy As on this component. This saves the specified component as a new document in the specified location.
- **name** (string): The name to use for the new document. If this is an empty string, Fusion will use the name of the component being saved.
- **dataFolder** (DataFolder): The data folder to save the new document to.
- **description** (string): The description string of the document. This can be an empty string.
- **tag** (string): The tag string of the document. This can be an empty string.
- **Returns** (DataFileFuture): Returns a DataFileFuture object that can be used to track the progress of the upload and get the resulting DataFile once it's available on A360.

### transformOccurrences(occurrences: Occurrence[], transforms: Matrix3D[], ignoreJoints: boolean) -> boolean
Transforms a set of occurrences in one step. This provides better performance than transforming them one at a time. This method is only valid when called on the root component because Fusion flattens the entire assembly structure when manipulating the assembly so all transforms are relative to the root component.
- **occurrences** (Occurrence[]): An array of Occurrence objects that you want to transform. These must all be in the context of the root component which means proxies must be used for occurrences that are in sub-components.
- **transforms** (Matrix3D[]): An array of Matrix3D objects that defines the transform to apply to each occurrence. This array must be the same size as the array provided for the occurrences argument and the transform will be applied to the occurrence at the same index in the occurrences array.
- **ignoreJoints** (boolean): Specifies if the joints are to be ignored and the occurrences are to be positioned based on then specified transform or if the joints should be used and the occurrence is transformed the best it can while still honoring the joints.
- **Returns** (boolean): Returns true if the transform was successful.

## Properties

### activeSheetMetalRule : SheetMetalRule [read-write]
Gets and sets the active sheet metal rule. This can return null in the case where the component has never contained any sheet metal related data.

### allAsBuiltJoints : array [read-only]
Returns all joint origins in this component and any sub components. The joint origins returned are all in the context of this component so any joint origins in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including joint origins, when manipulating an assembly.

### allAssemblyConstraints : array [read-only]
Returns all assembly constraints in this component and any sub components. The assembly constraints returned are all in the context of this component so any joints in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including joints, when manipulating an assembly.

### allJointOrigins : array [read-only]
Returns all as-built joints in this component and any sub components. The as-built joints returned are all in the context of this component so any as-built joints in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including as-built joints, when manipulating an assembly.

### allJoints : array [read-only]
Returns all joints in this component and any sub components. The joints returned are all in the context of this component so any joints in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including joints, when manipulating an assembly.

### allOccurrences : OccurrenceList [read-only]
Returns all of the occurrences in the assembly regardless of their level within the assembly structure. The returned list is read-only.

### allRigidGroups : array [read-only]
Returns all rigid groups in this component and any sub components. The rigid groups returned are all in the context of this component so any rigid groups in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including rigid groups, when manipulating an assembly.

### allTangentRelationships : array [read-only]
Returns all tangent relationships in this component and any sub components. The tangent relationships returned are all in the context of this component so any tangent relationships in sub components will be proxies. This is primarily useful when used from the root component because Fusion flattens the assembly structure, including tangent relationships, when manipulating an assembly.

### asBuiltJoints : AsBuiltJoints [read-only]
Returns the collection of as-built joints associated with this component.

### assemblyConstraints : AssemblyConstraints [read-only]
Returns the collection of assembly constraints associated with this component.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this face.

### boundingBox : BoundingBox3D [read-only]
Returns the bounding box of this component. This is always in world space of the component. The boundingBox2 method provides greater control over which types of entities you want included in the bounding box calculation.

### bRepBodies : BRepBodies [read-only]
Returns the B-Rep bodies collection associated with this component.

### canvases : Canvases [read-only]
Returns the canvases collection associated with this component. This provides access to the existing canvases and supports the creation of new canvases.

### componentColor : Color [read-write]
Gets and sets the color associated with a component. This color is only used when the "Display Component Colors" command is enabled. Enabling the display of component colors is done through the command or API using the Application.isComponentColorsDisplayed property. When this is on, all bodies in a component will display using the color assigned to the component. Fusion randomly assigns a color to a component when it is created. This property allows you to get and change the assigned default color. Setting this property to null results in a new color being randomly assigned by Fusion. This is the equivalent of the "Cycle Component Color" command available in the context menu of a component.

### constructionAxes : ConstructionAxes [read-only]
Returns the construction axes collection associated with this component. This provides access to the existing construction axes and supports the creation of new construction axes.

### constructionPlanes : ConstructionPlanes [read-only]
Returns the construction planes collection associated with this component. This provides access to the existing construction planes and supports the creation of new construction planes.

### constructionPoints : ConstructionPoints [read-only]
Returns the construction points collection associated with this component. This provides access to the existing construction points and supports the creation of new construction points.

### customGraphicsGroups : CustomGraphicsGroups [read-only]
Returns the customGraphicsGroups object in this component.

### dataComponent : DataComponent [read-only]
Returns the DataComponent associated with this component. The DataComponent provides ID information that can be used to access this component using the MFG DM API. These ID's don't exist until a component has been saved. The ID's are generated by MFG DM API on the cloud, so there will be a slight delay after saving before the ID's are available. This property returns null in the case the MFG DM API information doesn't exist yet.

When opening a design, the MFG DM API information is obtained from the cloud and as a result may not be available immediately after opening a document. Again, this property will return null in this case too. Essentially, null is returned in all cases where good ID information is not yet available.

### decals : Decals [read-only]
Returns the decals collection associated with this component. This provides access to the existing decals and supports the creation of new decals.

### description : string [read-write]
Gets and sets the description associated with this component.

### entityToken : string [read-only]
Returns a token for the Component object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same component.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### features : Features [read-only]
Returns the collection that provides access to all of the features associated with this component.

### flatPattern : FlatPattern [read-only]
Gets the existing flat pattern or returns null in the case where a flat pattern doesn't exist in this component.

### id : string [read-only]
Returns the persistent ID of the component. This ID is created with the component and does not change. Because this ID does not change, different revisions of the same design or copies of the design asset/file will retain this ID. If components from different designs have the same ID, it indicates they are either different revisions or a copy of the design was made. Therefore, this ID will always be unique within a single design, but may not be unique in an assembly where externally referenced designs include different revisions or copies of a design.

The ID is also the same ID used by PIM (Product Information Model).

### isBodiesFolderLightBulbOn : boolean [read-write]
Gets and sets if the light bulb of the bodies folder as seen in the browser is on or off. This controls the visibility of the solid/surface bodies and the mesh bodies in this component.

### isCanvasFolderLightBulbOn : boolean [read-write]
Gets and sets if the light bulb of the canvas folder as seen in the browser is on or off. This controls the visibility of all the canvases in the component.

### isConstructionFolderLightBulbOn : boolean [read-write]
Gets and sets if the light bulb of the construction folder as seen in the browser is on or off. This controls the visibility of the (non-origin) construction geometry (i.e. planes, points, axes).

### isDecalFolderLightBulbOn : boolean [read-write]
Gets and sets whether the light bulb of the decal folder, as seen in the browser, is on or off. This controls the visibility of all the decals in the component.

### isJointOriginsFolderLightBulbOn : boolean [read-write]
Gets and sets if the light bulb of the joint origins folder as seen in the browser is on or off. This controls the visibility of the joint origins in this occurrence. The light bulb for the folder is component specific and will turn off the joints for all occurrences referencing the component.

### isJointsFolderLightBulbOn : boolean [read-write]
Gets and sets if the light bulb of the joints folder as seen in the browser is on or off. This controls the visibility of the joints in this occurrence. The light bulb for the folder is component specific and will turn off the joints for all occurrences referencing the component.

### isLibraryItem : boolean [read-only]
Gets whether the component was created from a fasteners library item."

### isOriginFolderLightBulbOn : boolean [read-write]
Gets and sets if the light bulb of the origin folder as seen in the browser is on or off. This controls the visibility of the origin construction geometry.

### isSketchFolderLightBulbOn : boolean [read-write]
Gets and sets if the light bulb of the sketch folder as seen in the browser is on or off. This controls the visibility of the sketches in this component.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### jointOrigins : JointOrigins [read-only]
Returns the collection of joint origins associated with this component.

### joints : Joints [read-only]
Returns the collection of joints associated with this component.

### material : Material [read-write]
Gets and sets the physical material assigned to this component.

### meshBodies : MeshBodies [read-only]
Returns the mesh bodies collection associated with this component.

### mfgdmModelId : string [read-only]
Returns the MFGDM model ID for this component.

### modelParameters : ModelParameters [read-only]
Returns the collection of model parameters in the Component.

### motionLinks : MotionLinks [read-only]
Returns the collection of MotionLinks associated with this component.

### name : string [read-write]
Property that gets and sets the name of this component. This is the name shown in the browser for each occurrence referencing this component.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### occurrences : Occurrences [read-only]
Property that returns the Occurrences collection associated with this component. This provides access to the occurrences at the top-level of this component and provides the functionality to add new occurrences.

### opacity : double [read-write]
Gets and sets the opacity override assigned to this component. A value of 1.0 specifies that is it completely opaque and a value of 0.0 specifies that is it completely transparent.

This is only applicable for a non-root local component.

This value is not necessarily related to what the user sees because the opacity is inherited. For example, if you have TopComponent and it has a component in it called SubComponent and you set the opacity of TopComponent to be 0.5, SubComponent will also be shown as slightly transparent even though the opacity property for it will return 1.0. Because a component can be referenced as an occurrence in other components and they can have different opacity settings, it's possible that different instances of the same component can display using different opacity levels. To get the opacity that it is being displayed with use the Occurrence.visibleOpacity property.

### orientedMinimumBoundingBox : OrientedBoundingBox3D [read-only]
Returns an oriented bounding box that is best oriented to tightly fit all B-Rep bodies in the component. All other geometry types are ignored.

### originConstructionPoint : ConstructionPoint [read-only]
Returns the origin construction point.

### parentDesign : Design [read-only]
Returns the parent product this component is owned by.

### partNumber : string [read-write]
Gets and sets the part number associated with this component. Setting this to an empty string will reset it to be the same as the component name.

### physicalProperties : PhysicalProperties [read-only]
Returns the PhysicalProperties object that has properties for getting the area, density, mass, volume, moments, etc of this component. Property values will be calculated using the 'LowCalculationAccuracy' setting when using this property to get the PhysicalProperties object. To specify a higher calculation tolerance, use the getPhysicalProperties method instead.

### preciseBoundingBox : BoundingBox3D [read-only]
Returns a bounding box that tightly fits around all B-Rep bodies in the component. All other geometry types are ignored.

### propertyGroups : PropertyGroups [read-only]
Returns the PropertyGroups object associated with this component.

### revisionId : string [read-only]
Returns the current revision ID of the component. This ID changes any time the component is modified in any way. By getting and saving the ID when you create any data that is dependent on the component, you can then compare the saved ID with the current ID to determine if the component has changed to know if you should update your data.

### rigidGroups : RigidGroups [read-only]
Returns the collection of rigid groups associated with this component.

### sketches : Sketches [read-only]
Returns the sketches collection associated with this component. This provides access to the existing sketches and supports the creation of new sketches.

### tangentRelationships : TangentRelationships [read-only]
Returns the collection of tangent relationships associated with this component.

### xConstructionAxis : ConstructionAxis [read-only]
Returns the X origin construction axis.

### xYConstructionPlane : ConstructionPlane [read-only]
Returns the XY origin construction plane.

### xZConstructionPlane : ConstructionPlane [read-only]
Returns the XZ origin construction plane.

### yConstructionAxis : ConstructionAxis [read-only]
Returns the Y origin construction axis.

### yZConstructionPlane : ConstructionPlane [read-only]
Returns the YZ origin construction plane.

### zConstructionAxis : ConstructionAxis [read-only]
Returns the Z origin construction axis.

## Samples
- **Create Setups From Hole Recognition API Sample**: This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.
The Fusion Manufacturing Extension is required for Hole Recognition.
The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector.
- **Library Item API Sample**: Demonstrates how to examine library items using the API.

To use the sample, create a new Python or C++ script and copy and paste this code, replacing the existing default code. The script will search for and record all components and library items in the current project. They are displayed in a dialog when the script has finished.
- **Loft Feature API Sample**: Demonstrates creating a new loft feature.
- **Set Vise Origin As Setup WCS Origin API Sample**: This sample script demonstrates how to define our setup WCS origin relative to our vise origin from either a component, a sketch point or a joint origin.
The Work Coordinate System is a reference point set in our CAM workspace and on our machine. All machine coordinates are drawn from the WCS. This script demonstrates defining the WCS by each of 4 alternative methods:
Setup by default with no origin defined.
Setup using vise origin as WCS origin.
Setup using a sketch point as WCS origin.
Setup using a joint origin as WCS origin.
