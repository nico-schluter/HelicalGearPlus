# HoleFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

This class defines the methods and properties that pertain to the definition of a hole feature.

**Accessed from:** HoleFeatures.createCounterboreInput, HoleFeatures.createCountersinkInput, HoleFeatures.createSimpleInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setAllExtent(direction: ExtentDirections) -> boolean
Defines the extent of the hole to be through-all. The direction can be either positive, negative.
- **direction** (ExtentDirections): The direction of the hole relative to the normal of the sketch plane.
- **Returns** (boolean): Returns true if successful.

### setDistanceExtent(distance: ValueInput) -> boolean
Defines the depth of the hole using a specified distance.
- **distance** (ValueInput): The depth of the hole. If a real is specified the value is in centimeters. If a string is specified the units are derived from the string. If no units are specified, the default units of the document are used.
- **Returns** (boolean): Returns true if setting the extent was successful.

### setLengthAndOffset(length: ValueInput, offset: ValueInput)
Sets the length and offset of the thread of a tapped hole.

This method is only used when creating a tapped hole, which means the setToTappedHole method has been called. Otherwise calling this method will fail.

By default the isFullLength property is true which means the thread is the full length of the hole and there is no offset. Calling this method will have the side effect of setting the isFullLength property to false.
- **length** (ValueInput): Sets the length of the thread.
- **offset** (ValueInput): Sets the offset of the thread from the start of the hole. A value of zero is valid for no offset.

### setOneSideToExtent(toEntity: Base, matchShape: boolean, directionHint: Vector3D) -> boolean
Sets the extent of the hole to be from the sketch plane to the specified "to" face.
- **toEntity** (Base): The entity that defines the "to" extent. The valid types of entities can vary depending on the type of feature this is being used with. For a hole it can be a BRepBody, BRepFace, BRepVertex, ConstructionPlane, or ConstructionPoint.
- **matchShape** (boolean): Indicates if the hole is not contained on the face that the hole should match the shape of the entity as if it extended beyond its current boundaries.
- **directionHint** (Vector3D): Specifies the direction of the hole. This is only used in the case where there are two possible solutions and the hole can hit the toEntity in either direction.

Typically there is only a single solution and the direction is determined automatically.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if successful.

### setPositionAtCenter(planarEntity: Base, centerEdge: BRepEdge) -> boolean
Defines the position of the hole at the center of a circular or elliptical edge of the face.
- **planarEntity** (Base): The planar BRepFace or ConstructionPlane object that defines the orientation of the hole. The natural direction of the hole will be opposite the normal of the face or construction plane.
- **centerEdge** (BRepEdge): A circular or elliptical edge whose center point will be the position of the hole.
- **Returns** (boolean): Returns true if successful.

### setPositionByPlaneAndOffsets(planarEntity: Base, point: Point3D, edgeOne: BRepEdge, offsetOne: ValueInput, edgeTwo: BRepEdge, offsetTwo: ValueInput) -> boolean
Defines the orientation of the hole using a planar face or construction plane. The position of the hole is defined by the distance from one or two edges.
- **planarEntity** (Base): The planar BRepFace or ConstructionPlane object that defines the orientation of the hole. The natural direction of the hole will be opposite the normal of the face or construction plane.
- **point** (Point3D): A Point3D object that defines the approximate initial position of the hole. The point will be projected onto the plane. This point should be close to the final position of the hole and is used to determine which solution out of several possible solutions should be chosen for the hole location.

This point is defined in the coordinate system of the native entity used for the planarEntity argument. For example, if the planarEntity argument is a proxy to a BRepFace, the point argument must be in the coordinate system of the component of the native face, not the proxy.
- **edgeOne** (BRepEdge): A linear BRepEdge object that the position of the hole will be measured from. The position of the hole will be measured along a perpendicular from this edge.
- **offsetOne** (ValueInput): A ValueInput object that defines the offset distance from edgeOne. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "3 in"). If no units are specified it is interpreted using the current default units for length.
- **edgeTwo** (BRepEdge): You can optionally define a second edge and offset to specify the position of the hole. If you use a second edge it has the same requirements as the edgeOne argument. If you provide a second edge you must also provide the offsetTwo argument.

This is an optional argument whose default value is null.
- **offsetTwo** (ValueInput): If edgeTwo is defined, you must provide this argument which is a ValueInput object that defines the offset from the edgeTwo. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "3 in"). If no units are specified it is interpreted using the current default units for length.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if successful.

### setPositionByPoint(planarEntity: Base, point: Base) -> boolean
Defines the position of a the hole using a point. The point can be a vertex on the face or it can be a Point3D object to define any location on the face. If a Point3D object is provided it will be projected onto the plane along the planes normal. The orientation of the hole is defined by the planar face or construction plane. If a vertex is used, the position of the hole is associative to that vertex. If a Point3D object is used the position of the hole is not associative.
- **planarEntity** (Base): The planar BRepFace or ConstructionPlane object that defines the orientation of the hole. The natural direction of the hole will be opposite the normal of the face or construction plane.
- **point** (Base): A Point3D object or vertex that defines the position of the hole. The point will be projected onto the plane along the normal of the plane.
- **Returns** (boolean): Returns true if successful.

### setPositionBySketchPoint(sketchPoint: SketchPoint) -> boolean
Defines the position and orientation of the hole using a sketch point.
- **sketchPoint** (SketchPoint): The sketch point that defines the position of the hole. The orientation is inferred from the normal of the point's parent sketch. The natural direction will be opposite the normal of the sketch.
- **Returns** (boolean): Returns true if successful.

### setPositionBySketchPoints(sketchPoints: ObjectCollection) -> boolean
Defines the position and orientation of the hole using a set of sketch points.
- **sketchPoints** (ObjectCollection): A collection of sketch points that defines the positions of the holes. The orientation is inferred from the normal of the point's parent sketch. The natural direction will be opposite the normal of the sketch. The points can be from multiple sketches but they must all be co-planar.
- **Returns** (boolean): Returns true if successful.

### setPositionOnEdge(planarEntity: Base, edge: BRepEdge, position: HoleEdgePositions) -> boolean
Defines the position and orientation of the hole to be on the start, end or center of an edge.
- **planarEntity** (Base): The planar BRepFace or ConstructionPlane object that defines the orientation of the hole and start of the hole. The natural direction of the hole will be opposite the normal of the face or construction plane.
- **edge** (BRepEdge): The edge to position the hole on.
- **position** (HoleEdgePositions): The position along the edge to place the hole.
- **Returns** (boolean): Returns true if successful.

### setToClearanceHole(clearanceHoleInfo: ClearanceHoleInfo) -> boolean
Sets the hole to be a clearance hole of the size specified by the ClearanceHoleInfo object.
- **clearanceHoleInfo** (ClearanceHoleInfo): The ClearanceHoleInfo object that specifies the size of the clearance hole.
- **Returns** (boolean): Returns true if setting to a clearance hole was successful.

### setToSimpleHole() -> boolean
This property sets the hole's tap to be "simple", which means that it will not have any tap and will be a simple hole. When a new input is created, it defaults to being a simple hole.
- **Returns** (boolean): Returns true if successful.

### setToTappedHole(threadInfo: ThreadInfo) -> boolean
Sets the hole to be a straight or tapered tapped hole of the size specified by the ThreadInfo object.
- **threadInfo** (ThreadInfo): The ThreadInfo object that specifies the thread to use for the tapped hole. Whether it is straight or tapered tap is defined by the input ThreadInfo object.
- **Returns** (boolean): Returns true if setting to a tapped hole was successful.

## Properties

### creationOccurrence : Occurrence [read-write]
In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the Hole is created based on geometry (e.g. a face or point) in another component AND (the Hole) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI A value of null indicates that everything is in the context of a single component.

### holeTapType : HoleTapTypes [read-only]
Returns the current type of tap associated with this hole. When a new HoleFeatureInput is created, this will default to SimpleHoleTapType, which means the hole will not have any tap and will be a simple hole. You can set the tap type by using one of the methods to define the specific tap desired.

### isDefaultDirection : boolean [read-write]
Gets or sets if the hole goes in the default direction or is reversed.

### isFullLength : boolean [read-write]
Gets and sets if this thread is the full length of the hole. It defaults to true.

This property is only used when creating a tapped hole, which means the setToTappedHole method has been called. Otherwise this property is ignored.

The property can only be set to True, which will cause the feature to ignore the values of the threadLength and threadOffset properties. Using the setLengthAndOffset method will have the side effect of setting this property to false.

### isModeled : boolean [read-write]
Gets and sets if the thread is physical or cosmetic thread. A value of true indicates a physical thread. It defaults to false.

This property is only used when creating a tapped hole, which means the setToTappedHole method has been called. Otherwise this property is ignored.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### participantBodies : array [read-write]
Gets and sets the list of bodies that will participate in the hole.

If this property has not been set, the default behavior is that all bodies that are intersected by the hole will participate.

This property can return null in the case where the feature has not been fully defined so that possible intersecting bodies can be computed.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

### threadLength : ValueInput [read-only]
Gets the thread length when the isFullLength property is False. Returns null when the isFullLength property is true.

### threadOffset : ValueInput [read-only]
Gets the thread offset when the isFullLength property is False. Returns null when the isFullLength property is true.

### tipAngle : ValueInput [read-write]
Gets the ValueInput object that defines the angle of the tip of the hole. The default is "118.0 deg" but can be modified by setting it using another Value object.

## Samples
- **Hole Feature API Sample**: Demonstrates creating a new hole feature.
