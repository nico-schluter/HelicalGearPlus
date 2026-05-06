# GraphConnector
Namespace: adsk.volume
Inherits: Base
Since: May 2025

A simple read-only structure that represents a connection beween two nodes' pins in the graph.

**Accessed from:** Graph.allGraphConnectors, Graph.getNodeInputPinConnector, Graph.getNodeOutputPinConnectors

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### sourceGraphNode : GraphNode [read-only]
The node on the output of which this connector starts.

### sourcePinIndex : uinteger [read-only]
The output pin index of the start node.

### targetGraphNode : GraphNode [read-only]
The node on the input of which this connector ends.

### targetPinIndex : uinteger [read-only]
The intput pin index of the end node.
