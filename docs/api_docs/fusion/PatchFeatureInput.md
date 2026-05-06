# PatchFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: July 2016

This class defines the methods and properties that pertain to the definition of a patch feature.

**Accessed from:** PatchFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getContinuity(edges: BRepEdge[], continuity: integer[], weight: double[], isContinuityDirectionFlipped: boolean[]) -> boolean
Gets the continuity used for each edge in the boundary.
- **edges** (BRepEdge[]): Output array containing all of the BRepEdge objects in the boundary.
- **continuity** (integer[]): Output array the same size as the edges array that defines the continuity to apply to the edge in the same index in the edges array. The values are obtained from the SurfaceContinuityTypes enum and passed in as an integers.
- **weight** (double[]): Output array the same size as the edges array that defines the weight applied to the edge in the same index in the edges array. If the continuity of an edge is ConnectedSurfaceContinuityType, the weight value should be ignored.
- **isContinuityDirectionFlipped** (boolean[]): Output array the same size as the edges array that defines which of the two faces the edge connects to is used in computing the continuity direction. If the continuity is ConnectedSurfaceContinuityType or the edge is an open edge and only connected to a single face, the value should be ignored.

If false, the face associated with the first co-edge returned by the edge is used.
- **Returns** (boolean): Returns true if successful.

### setContinuity(continuity: integer[], weight: double[], isContinuityDirectionFlipped: boolean[]) -> boolean
Sets the continuity to use for each edge in the boundary. The arrays for the arguments correspond to B-Rep edges in the boundary. You can use the getContinuity method to get the list of edges to know their order. This order applies to the arrays provided for the arguments.
- **continuity** (integer[]): An array whose size of the number of B-Rep edges in the boundary. You can use the getContinuity method to get the list of edges, so you know the number and order of the edges. The continuity array defines the type of continuity to apply to the edge at the same index. The values are obtained from the SurfaceContinuityTypes enum and passed in as an integer.
- **weight** (double[]): An array whose size is the number of B-Rep edges in the boundary. You can use the getContinuity method to get the list of edges, so you know the number and order of the edges. The weight array defines the weight to apply to the edge at the same index. If the continuity of an edge is ConnectedSurfaceContinuityType, the weight value is ignored.
- **isContinuityDirectionFlipped** (boolean[]): An array whose size is the number of B-Rep edges in the boundary. You can use the getContinuity method to get the list of edges, so you know the number and order of the edges. The isContinuityDirectionFlipped array defines which of the two faces the edge connects to and is used in computing the continuity direction. If the continuity is ConnectedSurfaceContinuityType, or the edge is an open edge and only connected to a single face, the value is ignored.

If false, the face associated with the first co-edge returned by the edge is used.
- **Returns** (boolean): Returns true if successful.

## Properties

### boundaryCurve : Base [read-write]
Gets and sets the input geometry that will be used to define the boundary. This can be a sketch profile, a single sketch curve, a single B-Rep edge, an ObjectCollection, or a Path object.

If a single open sketch curve or B-Rep edge is input, Fusion will automatically find connected sketch curves or B-Rep edges to define a closed loop.

If an ObjectCollection is used as input, it must be a set of curves that define a closed shape.

If a Path is used as input, it must define a closed shape.

### continuity : SurfaceContinuityTypes [read-write]
This function is retired. See more information in the 'Remarks' section below.

Gets and sets the type of surface continuity to use when matching boundary edges to face edges. When a new PatchFeatureInput is created, this is initialized to ConnectedSurfaceContinuityType. This value is ignored when creating a patch for sketch curves.

### creationOccurrence : Occurrence [read-write]
For geometry to be transformed correctly, an Occurrence for creation needs to be specified when the Patch feature is created based on geometry (e.g., a profile, edges, faces) in another component AND (the Patch feature) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

### groupContinuity : SurfaceContinuityTypes [read-write]
Gets and sets the type of surface continuity to use for all edges when the isGroupEdges property is true. The continuity is used to determine how the patch connects to any B-Rep edges in the boundary. It is ignored for any sketch curves in the boundary. The property defaults to ConnectedSurfaceContinuityType. The value of this property is ignored if the isGroupEdges property is false.

### groupIsContinuityDirectionFlipped : boolean [read-write]
Gets and sets the continuity direction for all edges when the isGroupEdges property is true. It is ignored for any sketch curves in the boundary. The property defaults to false. The value of this property is ignored if the isGroupEdges property is false.

### groupWeight : double [read-write]
Gets and sets the weight to use for all edges when the isGroupEdges property is true. It is ignored for any sketch curves in the boundary. The property defaults to 0.5. The value of this property is ignored if the isGroupEdges property is false.

### interiorRailsAndPoints : ObjectCollection [read-write]
Gets and sets any interior curves or points the patch should fit through. Valid entities include object collections of connected curves, paths, sketch curves, sketch points, B-Rep edges, and construction points.

When getting this property, the returned ObjectCollection can contain individual edges, sketch curves, sketch points, construction points, vertices, and ObjectCollection objects that represent a group of the curves and points listed above.

Can be set to null to remove any interior rails and points from the patch.

### isGroupEdges : boolean [read-write]
Gets and sets if the edges in the boundary curve are treated as a group, and they all use the same continuity. If this property is True (which is the default), the continuity property controls the continuity for all edges. If this property is false; the continuity is set for each edge using the setContinuity method.

When this property is set to true, the continuity and weight of the first edge will be used for all edges. When set to false, each edge will initially have the same continuity and weight. This is typically set to false as a side-effect of calling the setContinuity method.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### operation : FeatureOperations [read-write]
Gets and sets the type of operation performed by the patch feature. Only 'NewBodyFeatureOperation' and 'NewComponentFeatureOperation' are valid operations for patch features.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

## Samples
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
