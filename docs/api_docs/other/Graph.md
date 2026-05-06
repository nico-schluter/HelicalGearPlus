# Graph
Namespace: adsk.volume
Inherits: Base
Since: May 2025

The graph that describes the volumetric model. Possible node types: "BoxSDF", "CylinderSDF", "SphereSDF", "TorusSDF", "PlaneSDF", "ReferencedGeometrySDF", "ReferencedCurveLength", "ReferencedCurveCoords", "ReferencedFaceCoords", "GradientVector", "InvertDensity", "PerlinNoiseScalar", "VoronoiNoiseScalar", "Shell", "ConstantScalar", "ConstantColor", "ImageSamplerScalar", "ImageSamplerVector", "ImageSamplerColor", "3DImageSamplerScalar", "SphereCoords", "TorusCoords", "CylinderCoords", "HomogenousTransformCoords", "TransformCoords", "AxisBasedDeformCoords ", "TwistCoords", "ControlPointMapScalarToScalar", "ControlPointMapScalarToColor", "FalloffMapping", "VectorToColor", "CombineScalarsToVector", "CombineScalarsToColor", "SplitVectorToScalars", "SplitColorToScalars", "LengthOfVector", "NormalizeVector", "ExternalColor", "FunctionScalarToScalar", "FunctionVectorToColor", "FunctionVectorToVector", "FunctionVectorToScalar", "BinaryOperatorColor", "BinaryOperatorVector", "BinaryOperatorScalar", "MultiplyColor", "MultiplyVector", "MultiplyScalar"

**Accessed from:** VolumetricModel.getGraph

## Methods

### addNode(name: string, nodeType: string) -> GraphNode
Add a new node to the graph. Node names are unique, attempting to add two nodes with the same name produces an error.
- **name** (string): Name of the new node.
- **nodeType** (string): The node type string, one of the types listed in the documentation.
- **Returns** (GraphNode): The new node if it could be added, null otherwise.

### canEvaluateGraph() -> boolean
Check if all the channels in the graph can be evaluated and in a good state.
- **Returns** (boolean): True if this graph can be evaluated, false otherwise.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### connect(outputNode: GraphNode, outputPinIndex: uinteger, inputNode: GraphNode, inputPinIndex: uinteger)
Create a connection between nodes.
- **outputNode** (GraphNode): The node where the connection starts.
- **outputPinIndex** (uinteger): The index of the output pin on the start node.
- **inputNode** (GraphNode): The node where the connection ends.
- **inputPinIndex** (uinteger): The index of the input pin on the end node.

### disconnect(outputNode: GraphNode, outputPinIndex: uinteger, inputNode: GraphNode, inputPinIndex: uinteger)
Delete a connection between nodes.
- **outputNode** (GraphNode): The node where the connection starts.
- **outputPinIndex** (uinteger): The index of the output pin on the start node.
- **inputNode** (GraphNode): The node where the connection ends.
- **inputPinIndex** (uinteger): The index of the input pin on the end node.

### getNode(name: string) -> GraphNode
Get node with the given name.
- **name** (string): Name to search for.
- **Returns** (GraphNode): The node if found, null otherwise.

### getNodeInputPinConnector(node: GraphNode, inputPinIndex: uinteger) -> GraphConnector
Get an upstream connection to the node's input pin.
- **node** (GraphNode): The node in question.
- **inputPinIndex** (uinteger): The index of the input pin of the node.
- **Returns** (GraphConnector): An array of GraphConnector objects, one for each connection to another node.

### getNodeOutputPinConnectors(node: GraphNode, outputPinIndex: uinteger) -> GraphConnector
Get an array of downstream connections from the node's output pin.
- **node** (GraphNode): The node in question.
- **outputPinIndex** (uinteger): The index of the output pin of the node.
- **Returns** (GraphConnector): An array of GraphConnector objects, one for each connection to another node.

### getOutputNode(outputNodeType: GraphOutputNodeTypes) -> GraphNode
Get one of the special graph output nodes. Every graph has one or more, the cannot be created or added. The final output pins of the graph nodes should be connected to these to make a useful graph.
- **outputNodeType** (GraphOutputNodeTypes): The type of the output graph node. Not every graph has every type; the primary graph has all four ouput node types, the cell graph only has OutputDensity.
- **Returns** (GraphNode): The output node if present in the graph, null otherwise.

## Properties

### allGraphConnectors : array [read-only]
Get all the connectors in the graph.

### allNodes : array [read-only]
Get all the nodes in the graph, including the output nodes.

### allPossibleNodeTypes : array [read-only]
Get all the possible node types that can be used as the nodeType parameter for addNode.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Volumetric Custom Feature API Sample**: Demonstrates how to create a Volumetric Custom Feature using the API for graph creation.


To run the sample script, have a document open in Fusion’s DESIGN workspace. This script will create a component with a box by sketching then extruding that sketch. It will then use that box as a boundary body and create a Volumetric Custom Feature.


The script will the create a gyroid lattice using the Volumetric Model API with the appropriate Graphs, Nodes and Connections for a minimal example. Finally, the script will convert that Volumetric Model to Mesh using the API and the VolumetricModelToMeshFeature.
