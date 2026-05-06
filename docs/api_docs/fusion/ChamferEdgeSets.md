# ChamferEdgeSets
Namespace: adsk.fusion
Inherits: Base
Since: December 2020

Collection that provides access to all of the existing chamfer edge sets associated with a chamfer feature.

**Accessed from:** ChamferFeature.edgeSets, ChamferFeatureInput.chamferEdgeSets

## Methods

### addDistanceAndAngleChamferEdgeSet(edges: ObjectCollection, distance: ValueInput, angle: ValueInput, isFlipped: boolean, isTangentChain: boolean) -> boolean
Adds a set of edges an equal distance offset to this chamfer feature.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **edges** (ObjectCollection): An ObjectCollection containing the edges to be chamfered. Edges can be defined by passing in BrepEdge, BRepFace, or Feature objects. If BRepFace or Feature objects are passed in all of the edges associated with those objects will be chamfered. If BRepEdge objects are provided and the isTangentChain argument is true additional edges may also get chamfered if they are tangentially connected to any of the input edges.
- **distance** (ValueInput): A ValueInput object that defines the distance offset of the chamfer. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **angle** (ValueInput): A ValueInput object that defines the angle of the chamfer. If the ValueInput uses a real then it is interpreted as radians. If it is a string then the units can be defined as part of the string (i.e. "2 rad") or if no units are specified it is interpreted as degrees.
- **isFlipped** (boolean): Swaps the directions for distance one and two.
- **isTangentChain** (boolean): A boolean value for setting whether or not edges that are tangentially connected to the input edges (if any) will also be chamfered.
- **Returns** (boolean): Returns true if the set of edges was successfully added to the ChamferFeatureInput.

### addEqualDistanceChamferEdgeSet(edges: ObjectCollection, distance: ValueInput, isTangentChain: boolean) -> boolean
Adds a set of edges an equal distance offset to this chamfer feature.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **edges** (ObjectCollection): An ObjectCollection containing the edges to be chamfered. Edges can be defined by passing in BrepEdge, BRepFace, or Feature objects. If BRepFace or Feature objects are passed in all of the edges associated with those objects will be chamfered. If BRepEdge objects are provided and the isTangentChain argument is true additional edges may also get chamfered if they are tangentially connected to any of the input edges.
- **distance** (ValueInput): A ValueInput object that defines the distance offset of the chamfer. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **isTangentChain** (boolean): A boolean value for setting whether or not edges that are tangentially connected to the input edges (if any) will also be chamfered.
- **Returns** (boolean): Returns true if the set of edges was successfully added to the ChamferFeatureInput.

### addTwoDistancesChamferEdgeSet(edges: ObjectCollection, distanceOne: ValueInput, distanceTwo: ValueInput, isFlipped: boolean, isTangentChain: boolean) -> boolean
Adds a set of edges an equal distance offset to this chamfer feature.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **edges** (ObjectCollection): An ObjectCollection containing the edges to be chamfered. Edges can be defined by passing in BrepEdge, BRepFace, or Feature objects. If BRepFace or Feature objects are passed in all of the edges associated with those objects will be chamfered. If BRepEdge objects are provided and the isTangentChain argument is true additional edges may also get chamfered if they are tangentially connected to any of the input edges.
- **distanceOne** (ValueInput): A ValueInput object that defines the first distance offset of the chamfer. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **distanceTwo** (ValueInput): A ValueInput object that defines the second distance offset of the chamfer. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **isFlipped** (boolean): Swaps the directions for distance one and two.
- **isTangentChain** (boolean): A boolean value for setting whether or not edges that are tangentially connected to the input edges (if any) will also be chamfered.
- **Returns** (boolean): Returns true if the set of edges was successfully added to the ChamferFeatureInput.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ChamferEdgeSet
Function that returns the specified chamfer edge set using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ChamferEdgeSet): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
The number of chamfer edge sets in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Equal Distance Chamfer Feature API Sample**: Creates an equal distance chamfer on the selected edge. If there are tangent contiguous edges that will also be included in the chamfer.
