# GraphNode
Namespace: adsk.volume
Inherits: Base
Since: May 2025

An individual node within a graph.

**Accessed from:** Graph.addNode, Graph.allNodes, Graph.getNode, Graph.getOutputNode, GraphConnector.sourceGraphNode, GraphConnector.targetGraphNode

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes the graphNode and all of its connections.
- **Returns** (boolean): Returns true in the case where the deletion was successful. All properties and proery objects of this node will become invalid after this call. Output nodes cannot be deleted.

### getInputPinCount() -> uinteger
How many input pins does this node have.
- **Returns** (uinteger): Pin count.

### getInputPinName(pinIndex: uinteger)
The name of this graph node input pin describing its function.
- **pinIndex** (uinteger): Zero based index of the pin to get. Should be less than the pin count.

### getInputPinType(pinIndex: uinteger) -> NodePinTypes
Get the type of the node input pin.
- **pinIndex** (uinteger): Zero based index of the pin to get. Should be less than the pin count.
- **Returns** (NodePinTypes): The pin type enum.

### getOutputPinCount() -> uinteger
How many output pins does this node have.
- **Returns** (uinteger): Pin count.

### getOutputPinName(pinIndex: uinteger)
The name of this graph node input pin describing its function.
- **pinIndex** (uinteger): Zero based index of the pin to get. Should be less than the pin count.

### getOutputPinType(pinIndex: uinteger) -> NodePinTypes
Get the type of the node output pin.
- **pinIndex** (uinteger): Zero based index of the pin to get. Should be less than the pin count.
- **Returns** (NodePinTypes): The pin type enum.

### hasValidProperties() -> boolean
Check if the graph node properties are valid.
- **Returns** (boolean): True if the node has good inputs for its properties, false otherwise.

### isInputPinOptional(pinIndex: uinteger) -> boolean
Some input pins can be optional, so they do not need to be connected for the node to work.
- **pinIndex** (uinteger): Zero based index of the pin to get. Should be less than the pin count.
- **Returns** (boolean): True if pin is optional, false if it is required.

## Properties

### description : string [read-only]
A user readable description that explains the function of this node type.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
The name of this graph node as give on creation. Node names for each graph should be unique.

### nodeType : string [read-only]
Get the string node type that is was created with.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### properties : GraphNodeProperties [read-only]
Get a collection of all node properties supported by this node.

## Samples
- **Volumetric Custom Feature API Sample**: Demonstrates how to create a Volumetric Custom Feature using the API for graph creation.


To run the sample script, have a document open in Fusion’s DESIGN workspace. This script will create a component with a box by sketching then extruding that sketch. It will then use that box as a boundary body and create a Volumetric Custom Feature.


The script will the create a gyroid lattice using the Volumetric Model API with the appropriate Graphs, Nodes and Connections for a minimal example. Finally, the script will convert that Volumetric Model to Mesh using the API and the VolumetricModelToMeshFeature.
