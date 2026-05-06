# HoleFeature
Namespace: adsk.fusion
Inherits: Feature
Since: August 2014

Object that represents an existing hole feature in a design.

**Accessed from:** HoleFeature.createForAssemblyContext, HoleFeature.nativeObject, HoleFeatures.add, HoleFeatures.item, HoleFeatures.itemByName, ThreadFeature.hole

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> HoleFeature
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (HoleFeature): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes the feature. This works for both parametric and non-parametric features.
- **Returns** (boolean): Returns a bool indicating if the delete was successful or not.

### dissolve() -> boolean
Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features.
- **Returns** (boolean): Returns a bool indicating if the dissolve was successful or not.

### setAllExtent(direction: ExtentDirections) -> boolean
Defines the extent of the hole to be through-all. The direction can be either positive, negative.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **direction** (ExtentDirections): The direction of the hole relative to the normal of the sketch plane.
- **Returns** (boolean): Returns true if successful.

### setDistanceExtent(distance: ValueInput) -> boolean
Defines the depth of the hole using a specific distance.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **distance** (ValueInput): The depth of the hole. If a real is specified the value is in centimeters. If a string is specified the units are derived from the string. If no units are specified, the default units of the document are used.
- **Returns** (boolean): Returns true if setting the extent was successful.

### setOneSideToExtent(toEntity: Base, matchShape: boolean, directionHint: Vector3D) -> boolean
Sets the extent of the hole to be from the sketch plane to the specified "to" face.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **toEntity** (Base): The entity that defines the "to" extent. The valid types of entities can vary depending on the type of feature this is being used with. For a hole it can be a BRepBody, BRepFace, BRepVertex, ConstructionPlane, or ConstructionPoint.
- **matchShape** (boolean): Indicates if the hole is not contained on the face that the hole should match the shape of the entity as if it extended beyond its current boundaries.
- **directionHint** (Vector3D): Specifies the direction of the hole. This is only used in the case where there are two possible solutions and the hole can hit the toEntity in either direction.

Typically there is only a single solution and the direction is determined automatically.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if successful.

### setPositionAtCenter(planarEntity: Base, centerEdge: BRepEdge) -> boolean
Redefines the position of the hole at the center of a circular or elliptical edge of the face.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **planarEntity** (Base): The planar BRepFace or ConstructionPlane object that defines the orientation of the hole. The natural direction of the hole will be opposite the normal of the face or construction plane.
- **centerEdge** (BRepEdge): A circular or elliptical edge whose center point will be the position of the hole.
- **Returns** (boolean): Returns true if successful.

### setPositionByPlaneAndOffsets(planarEntity: Base, point: Point3D, edgeOne: BRepEdge, offsetOne: ValueInput, edgeTwo: BRepEdge, offsetTwo: ValueInput) -> boolean
Redefines the orientation of the hole using a planar face or construction plane. The position of the hole is defined by the distance from one or two edges.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **planarEntity** (Base): The planar BRepFace or ConstructionPlane object that defines the orientation of the hole. The natural direction of the hole will be opposite the normal of the face or construction plane.
- **point** (Point3D): A Point3D object that defines the approximate initial position of the hole. The point will be projected onto the plane. This point should be close to the final position of the hole and is used to determine which solution out of several possible solutions should be chosen for the hole location.
- **edgeOne** (BRepEdge): A linear BRepEdge object that the position of the hole will be measured from. The position of the hole will be measured along a perpendicular from this edge.
- **offsetOne** (ValueInput): A ValueInput object that defines the offset distance from edgeOne. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "3 in"). If no units are specified it is interpreted using the current default units for length.
- **edgeTwo** (BRepEdge): You can optionally define a second edge and offset to specify the position of the hole. If you use a second edge it has the same requirements as the edgeOne argument. If you provide a second edge you must also provide the offsetTwo argument.

This is an optional argument whose default value is null.
- **offsetTwo** (ValueInput): If edgeTwo is defined, you must provide this argument which is a ValueInput object that defines the offset from the edgeTwo. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "3 in"). If no units are specified it is interpreted using the current default units for length.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if successful.

### setPositionByPoint(planarEntity: Base, point: Base) -> boolean
Redefines the position of a the hole using a point. The point can be a vertex on the face or it can be a Point3D object to define any location on the face. If a Point3D object is provided it will be projected onto the plane along the planes normal. The orientation of the hole is defined by the planar face or construction plane. If a vertex is used, the position of the hole is associative to that vertex. If a Point3D object is used the position of the hole is not associative.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **planarEntity** (Base): The planar BRepFace or ConstructionPlane object that defines the orientation of the hole. The natural direction of the hole will be opposite the normal of the face or construction plane.
- **point** (Base): A Point3D object or vertex that defines the position of the hole. The point will be projected onto the plane along the normal of the plane.
- **Returns** (boolean): Returns true if successful.

### setPositionBySketchPoint(sketchPoint: SketchPoint) -> boolean
Redefines the position and orientation of the hole using a sketch point.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **sketchPoint** (SketchPoint): The sketch point that defines the position of the hole. The orientation is inferred from the normal of the point's parent sketch. The natural direction will be opposite the normal of the sketch.
- **Returns** (boolean): Returns true if successful.

### setPositionBySketchPoints(sketchPoints: ObjectCollection) -> boolean
Redefines the position and orientation of the hole using a set of points.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **sketchPoints** (ObjectCollection): A collection of sketch points that defines the positions of the holes. The orientation is inferred from the normal of the point's parent sketch. The natural direction will be opposite the normal of the sketch. All of the points must be in the same sketch.
- **Returns** (boolean): Returns true if successful.

### setPositionOnEdge(planarEntity: Base, edge: BRepEdge, position: HoleEdgePositions) -> boolean
Redefines the position and orientation of the hole to be on the start, end or center of an edge.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **planarEntity** (Base): The planar BRepFace or ConstructionPlane object that defines the orientation of the hole and start of the hole. The natural direction of the hole will be opposite the normal of the face or construction plane.
- **edge** (BRepEdge): The edge to position the hole on.
- **position** (HoleEdgePositions): The position along the edge to place the hole.
- **Returns** (boolean): Returns true if successful.

### setToClearanceHole(clearanceHoleInfo: ClearanceHoleInfo) -> boolean
Sets the hole to be a clearance hole of the size specified by the ClearanceHoleInfo object.
- **clearanceHoleInfo** (ClearanceHoleInfo): The ClearanceHoleInfo object that specifies the size of the clearance hole.
- **Returns** (boolean): Returns true if setting to a clearance hole was successful.

### setToCounterbore(counterboreDiameter: ValueInput, counterboreDepth: ValueInput) -> boolean
Calling this method will change the hole to a counterbore hole.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **counterboreDiameter** (ValueInput): A ValueInput object that defines the counterbore diameter. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "3 in"). If no units are specified it is interpreted using the current default units for length.
- **counterboreDepth** (ValueInput): A ValueInput object that defines the counterbore depth. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "3 in"). If no units are specified it is interpreted using the current default units for length.
- **Returns** (boolean): Returns true if changing the hole was successful.

### setToCountersink(countersinkDiameter: ValueInput, countersinkAngle: ValueInput) -> boolean
Calling this method will change the hole to a countersink hole.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **countersinkDiameter** (ValueInput): A ValueInput object that defines the countersink diameter. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "3 in"). If no units are specified it is interpreted using the current default units for length.
- **countersinkAngle** (ValueInput): A ValueInput object that defines the countersink angle. If the ValueInput uses a real then it is interpreted as radians. If it is a string then the units can be defined as part of the string (i.e. "120 deg"). If no units are specified it is interpreted using the current default units for length.
- **Returns** (boolean): Returns true if changing the hole was successful.

### setToSimple() -> boolean
Calling this method will change the hole to a simple hole.
- **Returns** (boolean): Returns true if changing the hole was successful.

### setToSimpleHole() -> boolean
This method sets the hole's tap to be "simple," which means that the hole will not have any tap and will be a simple hole.
- **Returns** (boolean): Returns true if successful.

### setToTappedHole(threadInfo: ThreadInfo) -> boolean
Sets the hole to be a straight or tapered tapped hole of the size specified by the ThreadInfo object.
- **threadInfo** (ThreadInfo): The ThreadInfo object that specifies the thread to use for the tapped hole. Whether it is straight or tapered tap is defined by the input ThreadInfo object.
- **Returns** (boolean): Returns true if setting to a tapped hole was successful.

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

### clearanceHoleInfo : ClearanceHoleInfo [read-only]
Returns the information used to define a clearance hole. This returns a ClearanceHoleInfo object when the holeTapType returns ClearanceHoleTapType. Otherwise this property returns null.

### counterboreDepth : ModelParameter [read-only]
Returns the model parameter controlling the counterbore depth. This will return null in the case the hole type is not a counterbore. The depth of the counterbore can be edited through the returned parameter.

### counterboreDiameter : ModelParameter [read-only]
Returns the model parameter controlling the counterbore diameter. This will return null in the case the hole type is not a counterbore. The diameter of the counterbore can be edited through the returned parameter.

### countersinkAngle : ModelParameter [read-only]
Returns the model parameter controlling the countersink angle. This will return null in the case the hole type is not a countersink. The angle of the countersink can be edited through the returned parameter.

### countersinkDiameter : ModelParameter [read-only]
Returns the model parameter controlling the countersink diameter. This will return null in the case the hole type is not a countersink. The diameter of the countersink can be edited through the returned parameter.

### direction : Vector3D [read-only]
Returns the direction of the hole.

### endFaces : BRepFaces [read-only]
Property that returns the faces at the bottom of the hole. This will typically be a single face but could return more than one face in the case where the bottom of the hole is uneven.

### entityToken : string [read-only]
Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### errorOrWarningMessage : string [read-only]
Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string.

### extentDefinition : ExtentDefinition [read-only]
Gets the definition object that is defining the extent of the hole. Modifying the definition object will cause the hole to recompute. The extent type of a hole is currently limited to a distance extent.

### faces : BRepFaces [read-only]
Returns the faces that were created by this feature. This works for both parametric and non-parametric features.

Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available.

### healthState : FeatureHealthStates [read-only]
Returns the current health state of the feature.

### holeDiameter : ModelParameter [read-only]
Returns the model parameter controlling the hole diameter. The diameter of the hole can be edited through the returned parameter object.

If there is a thread associated with the hole the thread definition controls the diameter of the hole. Even though there is a parameter for the diameter, its value is ignored when there is a thread.

### holePositionDefinition : HolePositionDefinition [read-only]
Returns a HolePositionDefinition object that provides access to the information used to define the position of the hole. This returns null in the case where IsParametric is false.

### holeTapType : HoleTapTypes [read-only]
This property returns the current type of tap associated with this hole. You can set the tap type by using one of the following methods: setToSimpleHole, setToClearanceHole, or setToTappedHole.

### holeType : HoleTypes [read-only]
Returns the current type of hole this feature represents.

### isDefaultDirection : boolean [read-write]
Gets and sets if the hole is in the default direction or not.

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

### nativeObject : HoleFeature [read-only]
The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentComponent : Component [read-only]
Returns the parent component that owns this feature.

### participantBodies : array [read-write]
Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.

To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### position : Point3D [read-only]
Returns the position of the hole.

### sideFaces : BRepFaces [read-only]
Property that returns all of the side faces of the hole.

### tappedHoleInfo : ThreadInfo [read-only]
This property returns the information used to define a tapped hole. Otherwise, this property returns null.

### thread : ThreadFeature [read-only]
When a tapped hole is created, a thread feature is also automatically created and controls the tapped threads. The thread feature is tied to the hole and is not displayed in the timeline and is suppressed if the hole is suppressed and deleted if the hole is deleted. This property returns the thread feature associated with this hole if it is a tapped hole. It returns null for all other hole types.

### timelineObject : TimelineObject [read-only]
Returns the timeline object associated with this feature.

### tipAngle : ModelParameter [read-only]
Returns the model parameter controlling the angle of the tip of the hole. The tip angle of the hole can be edited through the returned parameter object.

## Samples
- **Hole Feature API Sample**: Demonstrates creating a new hole feature.
