# FilletEdgeSetInputs
Namespace: adsk.fusion
Inherits: Base
Since: November 2022

Collection of edge sets associated with the input object that will be used to create the new fillet feature. Use the various add methods on this object to add new edge sets to the input object.

**Accessed from:** FilletFeatureInput.edgeSetInputs

## Methods

### addAsymmetricRadiusEdgeSet(entities: ObjectCollection, offsetOne: ValueInput, offsetTwo: ValueInput, isTangentChain: boolean) -> AsymmetricFilletEdgeSetInput
Adds an asymmetric fillet edge set to the fillet feature input. Some settings are initialized with a default value and can be set by modifying properties on the returned AsymmetricFilletEdgeSetInput object.
- **entities** (ObjectCollection): An ObjectCollection containing the BRepEdge, BRepFace, and Feature objects to be filleted. If the isTangentChain argument is true additional edges or faces may also get filleted if they are tangentially connected to any of the input edges or faces.
- **offsetOne** (ValueInput): A ValueInput object that defines the offset of the fillet in the first direction. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **offsetTwo** (ValueInput): A ValueInput object that defines the offset of the fillet in the second direction. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **isTangentChain** (boolean): A boolean value for setting whether or not edges or faces that are tangentially connected to the input edges or faces will also be filleted.
- **Returns** (AsymmetricFilletEdgeSetInput): Returns the newly created AsymmetricFilletEdgeSetInput. This object provides access to additional settings.

### addChordLengthEdgeSet(entities: ObjectCollection, chordLength: ValueInput, isTangentChain: boolean) -> ChordLengthFilletEdgeSetInput
Adds a set of edges to be filleted with a chord length fillet to the fillet feature input. Some settings are initialized with a default value and can be set by modifying properties on the returned ChordLengthFilletEdgeSetInput object.
- **entities** (ObjectCollection): An ObjectCollection containing the BRepEdge, BRepFace, and Feature objects to be filleted. If the isTangentChain argument is true additional edges or faces may also get filleted if they are tangentially connected to any of the input edges or faces.
- **chordLength** (ValueInput): A ValueInput object that defines the chord length of the fillet. If the ValueInput uses a real value then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current document units for length.
- **isTangentChain** (boolean): A boolean value for setting whether or not edges or faces that are tangentially connected to the input edges or faces (if any) will also be filleted.
- **Returns** (ChordLengthFilletEdgeSetInput): Returns the newly created ChordLengthFilletEdgeSetInput. This object provides access to additional settings.

### addConstantRadiusEdgeSet(entities: ObjectCollection, radius: ValueInput, isTangentChain: boolean) -> ConstantRadiusFilletEdgeSetInput
Adds a constant radius fillet edge set to the fillet feature input. Some settings are initialized with a default value and can be set by modifying properties on the returned ConstantRadiusFilletEdgeSetInput object.
- **entities** (ObjectCollection): An ObjectCollection containing the BRepEdge, BRepFace, and Feature objects to be filleted. If the isTangentChain argument is true additional edges or faces may also get filleted if they are tangentially connected to any of the input edges or faces.
- **radius** (ValueInput): A ValueInput object that defines the radius of the fillet. If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **isTangentChain** (boolean): A boolean value for setting whether or not edges that are tangentially connected to the input edges (if any) will also be filleted.
- **Returns** (ConstantRadiusFilletEdgeSetInput): Returns the newly created ConstantRadiusFilletEdgeSetInput. This object provides access to additional settings.

### addVariableRadiusEdgeSet(tangentEdges: ObjectCollection, startRadius: ValueInput, endRadius: ValueInput, isTangentChain: boolean) -> VariableRadiusFilletEdgeSetInput
Adds a single edge or set of tangent edges to the fillet feature input. Some settings are initialized with a default value and can be set by modifying properties on the returned VariableRadiusFilletEdgeSetInput object.
- **tangentEdges** (ObjectCollection): An object collection containing a single edge or multiple edges. Multiple edges must be tangentially connected and added to the collection in their connected order. If a single edge is input, you can use the isTangentChain argument to automatically find any tangentially connected edges.
- **startRadius** (ValueInput): A ValueInput object that defines the starting radius of the fillet. If a single edge is being filleted, the start radius is at the start end of the edge. If multiple tangent edges are being filleted the start radius is the start end of the first edge in the collection.

If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **endRadius** (ValueInput): A ValueInput object that defines the ending radius of the fillet. If a single edge is being filleted, the end radius is at the end of the edge. If multiple tangent edges are being filleted the end radius is the open end of the last edge in the collection.

If the ValueInput uses a real then it is interpreted as centimeters. If it is a string then the units can be defined as part of the string (i.e. "2 in") or if no units are specified it is interpreted using the current default units for length.
- **isTangentChain** (boolean): A boolean value for setting whether or not edges that are tangentially connected to the single input edge will also be filleted.
- **Returns** (VariableRadiusFilletEdgeSetInput): Returns the newly created VariableRadiusFilletEdgeSetInput. This object provides access to additional settings.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> FilletEdgeSetInput
Function that returns the specified fillet edge set input using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0. The edge sets are returned in the same order they were created in.
- **Returns** (FilletEdgeSetInput): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
The number of fillet edge set input objects in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **filletFeatures.add**: Demonstrates the filletFeatures.add method.
- **Fillet Feature API Sample**: Demonstrates creating fillets using the various types of fillets. Create a new design and add a box that is at least 2 cm on each side. The script creates a constant radius, variable radius and chord length fillets. After creating each one, it deletes it and then creates the next. To see any of the fillets that were deleted, undo to get the fillet back.
