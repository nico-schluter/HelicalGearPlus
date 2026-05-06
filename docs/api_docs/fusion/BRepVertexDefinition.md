# BRepVertexDefinition
Namespace: adsk.fusion
Inherits: Base
Since: September 2020

Represents the definition of a B-Rep vertex that can be used as input to create a BRepBody that includes this vertex.

**Accessed from:** BRepBodyDefinition.createVertexDefinition, BRepEdgeDefinition.endVertex, BRepEdgeDefinition.startVertex, BRepWireEdgeDefinition.endVertex, BRepWireEdgeDefinition.startVertex

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

### position : Point3D [read-write]
Gets and sets the position of the vertex in model space.

## Samples
- **BRep Body definition Sample**: Demonstrates creating BRep bodies by BRepBodyDefinition.
