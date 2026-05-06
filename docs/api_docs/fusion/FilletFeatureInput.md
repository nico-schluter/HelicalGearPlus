# FilletFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

This class defines the methods and properties that pertain to the definition of a fillet feature.

**Accessed from:** FilletFeatures.createInput

## Methods

### addChordLengthEdgeSet(edges: ObjectCollection, chordLength: ValueInput, isTangentChain: boolean) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Adds a set of edges with a chord length to this input.
- **edges** (ObjectCollection): An ObjectCollection containing the edges to be filleted. If the isTangentChain argument is true additional edges may also get filleted if they are tangentially connected to any of the input edges.
- **chordLength** (ValueInput): A ValueInput object that defines the chord length of the fillet. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **isTangentChain** (boolean): A boolean value for setting whether or not edges that are tangentially connected to the input edges or faces will also be filleted.
- **Returns** (boolean): Returns true if the set of edges was successfully added to the FilletFeatureInput.

### addConstantRadiusEdgeSet(edges: ObjectCollection, radius: ValueInput, isTangentChain: boolean) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Adds a set of edges with a constant radius to this input.
- **edges** (ObjectCollection): An ObjectCollection containing the edges to be filleted. If the isTangentChain argument is true additional edges may also get filleted if they are tangentially connected to any of the input edges.
- **radius** (ValueInput): A ValueInput object that defines the radius of the fillet. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **isTangentChain** (boolean): A boolean value for setting whether or not edges that are tangentially connected to the input edges will also be filleted.
- **Returns** (boolean): Returns true if the set of edges was successfully added to the FilletFeatureInput.

### addVariableRadiusEdgeSet(tangentEdges: ObjectCollection, startRadius: ValueInput, endRadius: ValueInput, positions: ValueInput[], radii: ValueInput[]) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Adds a single edge or set of tangent edges along with variable radius information to this input.
- **tangentEdges** (ObjectCollection): An object collection containing a single edge or multiple edges. Multiple edges must be tangentially connected and added to the collection in order.
- **startRadius** (ValueInput): A ValueInput object that defines the starting radius of the fillet. If a single edge is being filleted, the start radius is at the start end of the edge. If multiple tangent edges are being filleted the start radius is the open end of the first edge in the collection.

If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **endRadius** (ValueInput): A ValueInput object that defines the ending radius of the fillet. If a single edge is being filleted, the end radius is at the end of the edge. If multiple tangent edges are being filleted the end radius is the open end of the last edge in the collection. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **positions** (ValueInput[]): An array of ValueInput objects that defines the positions of any additional radii along the edge(s). The value must be between 0 and 1 and defines the percentage along the curve where a radius is defined. The value is unitless. This array must have the same number of values as the array passed in for the radii argument.
- **radii** (ValueInput[]): An array of ValueInput objects that define the radii at positions along the edge(s). This array must have the same number of values as the array passed in for the positions argument. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in"). If no units are specified it will be interpreted using the current default units for length.
- **Returns** (boolean): Returns true if the edge set was successfully added to the FilletFeatureInput.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### edgeSetInputs : FilletEdgeSetInputs [read-only]
Gets the FilletEdgeSetInputs object that provides support to create the various types of edge sets that will be used to create the fillet.

### isG2 : boolean [read-write]
This function is retired. See more information in the 'Remarks' section below.

Gets and sets if the fillet uses the G2 (curvature-continuity) surface quality option.

### isRollingBallCorner : boolean [read-write]
Gets and sets if a rolling ball or setback solution is to be used in any corners. For an asymmetric fillet only a setback solution is supported, so any asymmetric edge sets will ignore this setting and will always be a setback corner.

### isTangentChain : boolean [read-write]
This function is retired. See more information in the 'Remarks' section below.

Gets and sets if any edges that are tangentially connected to any of filleted edges will also be included in the fillet.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

## Samples
- **Fillet Feature API Sample**: Demonstrates creating fillets using the various types of fillets. Create a new design and add a box that is at least 2 cm on each side. The script creates a constant radius, variable radius and chord length fillets. After creating each one, it deletes it and then creates the next. To see any of the fillets that were deleted, undo to get the fillet back.
