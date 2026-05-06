# FilletEdgeSets
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

Collection that provides access to all of the existing fillet edge sets associated with a fillet feature.

**Accessed from:** FilletFeature.edgeSets

## Methods

### addAsymmetricRadiusEdgeSet(entities: ObjectCollection, offsetOne: ValueInput, offsetTwo: ValueInput, isTangentChain: boolean) -> AsymmetricFilletEdgeSet
Adds an asymmetric fillet edge set to the fillet feature.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **entities** (ObjectCollection): An ObjectCollection containing the BRepEdge, BRepFace, and Feature objects to be filleted. If the isTangentChain argument is true additional edges or faces may also get filleted if they are tangentially connected to any of the input edges or faces.
- **offsetOne** (ValueInput): A ValueInput object that defines the offset distance of the fillet in the first direction. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **offsetTwo** (ValueInput): A ValueInput object that defines the offset distance of the fillet in the second direction. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **isTangentChain** (boolean): A boolean value for setting whether or not edges or faces that are tangentially connected to the input edges or faces will also be filleted.
- **Returns** (AsymmetricFilletEdgeSet): Returns the newly created AsymmetricFilletEdgeSet.

### addChordLengthEdgeSet(entities: ObjectCollection, chordLength: ValueInput, isTangentChain: boolean) -> ChordLengthFilletEdgeSet
Adds a set of edges with a chord length to this fillet feature.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **entities** (ObjectCollection): An ObjectCollection containing the BRepEdge, BRepFace, and Feature objects to be filleted. If the isTangentChain argument is true additional edges or faces may also get filleted if they are tangentially connected to any of the input edges or faces.
- **chordLength** (ValueInput): A ValueInput object that defines the chord length of the fillet. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **isTangentChain** (boolean): A boolean value for setting whether or not edges that are tangentially connected to the input edges (if any) will also be filleted.
- **Returns** (ChordLengthFilletEdgeSet): Returns the newly created FilletEdgeSet.

### addConstantRadiusEdgeSet(entities: ObjectCollection, radius: ValueInput, isTangentChain: boolean) -> ConstantRadiusFilletEdgeSet
Adds a set of edges with a constant radius to this fillet feature.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **entities** (ObjectCollection): An ObjectCollection containing the BRepEdge, BRepFace, and Feature objects to be filleted. If the isTangentChain argument is true additional edges or faces may also get filleted if they are tangentially connected to any of the input edges or faces.
- **radius** (ValueInput): A ValueInput object that defines the radius of the fillet. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **isTangentChain** (boolean): A boolean value for setting whether or not edges that are tangentially connected to the input edges (if any) will also be filleted.
- **Returns** (ConstantRadiusFilletEdgeSet): Returns the newly created FilletEdgeSet.

### addVariableRadiusEdgeSet(tangentEdges: ObjectCollection, startRadius: ValueInput, endRadius: ValueInput, positions: ValueInput[], radii: ValueInput[], isTangentChain: boolean) -> VariableRadiusFilletEdgeSet
Adds a single edge or set of tangent edges along with variable radius information to this fillet feature.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **tangentEdges** (ObjectCollection): An object collection containing a single edge or multiple edges. Multiple edges must be tangentially connected and added to the collection in their connected order. If a single edge is input, you can use the isTangentChain argument to automatically find any tangentially connected edges.
- **startRadius** (ValueInput): A ValueInput object that defines the starting radius of the fillet. If a single edge is being filleted, the start radius is at the start end of the edge. If multiple tangent edges are being filleted the start radius is the open end of the first edge in the collection.

If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **endRadius** (ValueInput): A ValueInput object that defines the ending radius of the fillet. If a single edge is being filleted, the end radius is at the end of the edge. If multiple tangent edges are being filleted the end radius is the open end of the last edge in the collection. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **positions** (ValueInput[]): An array of ValueInput objects that defines the positions of any additional radii along the edge(s). The value must be between 0 and 1 and defines the percentage along the curve where a radius is defined. The value is unitless. This array must have the same number of values as the array passed in for the radii argument.
- **radii** (ValueInput[]): An array of ValueInput objects that define the radii at positions along the edge(s). This array must have the same number of values as the array passed in for the positions argument. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in"). If no units are specified it will be interpreted using the current default units for length.
- **isTangentChain** (boolean): A boolean value for setting whether or not edges that are tangentially connected to the single input edge will also be filleted.
- **Returns** (VariableRadiusFilletEdgeSet): Returns the newly created FilletEdgeSet.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> FilletEdgeSet
Function that returns the specified fillet edge set using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (FilletEdgeSet): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
The number of fillet edge sets in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Fillet Feature Edit API Sample**: Demonstrates editing a fillet feature.
To successfully run this sample you can use this
