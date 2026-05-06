# BRepEdgeDefinition
Namespace: adsk.fusion
Inherits: Base
Since: September 2020

Represents the definition of a B-Rep edge that can be used as input to create a BRepBody.

**Accessed from:** BRepBodyDefinition.createEdgeDefinitionByCurve, BRepCoEdgeDefinition.edgeDefinition

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### associativeID : integer [read-write]
Gets and sets the associate ID of this edge definition. This ID will be copied to the corresponding edge when the BRepBodyDefinition is used to create a BrepBody. It is used internally by Fusion as the identifier for the edge and is used for tracking this geometry for parametric recomputes.

### endVertex : BRepVertexDefinition [read-write]
Gets and sets the end vertex of the edge definition.

### isMergeable : boolean [read-write]
Gets and sets if the two faces that share this edge can be merged along this edge. This property defaults to true so that merging is always done but this can be set to false in cases where you want to preserve the edge.

An example where merging is typically done is when you have multiple planar faces that all lie on the same plane and are connected. When merging is allowed these faces can be replaced by a single face and the edges connecting the faces (the merged edges) are no longer part of the body.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### modelSpaceCurve : Curve3D [read-write]
Gets and sets the curve that defines the shape of the edge.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### startVertex : BRepVertexDefinition [read-write]
Gets and sets the start vertex of the edge definition.

## Samples
- **BRep Body definition Sample**: Demonstrates creating BRep bodies by BRepBodyDefinition.
