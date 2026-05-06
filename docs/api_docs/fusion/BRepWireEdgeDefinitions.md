# BRepWireEdgeDefinitions
Namespace: adsk.fusion
Inherits: Base
Since: September 2020

A collection of BRepWireEdgeDefinition objects. Using this collection you can create new BRepWireDefinition objects to full define a wire body.

**Accessed from:** BRepWireDefinition.wireEdgeDefinitions

## Methods

### add(startVertex: BRepVertexDefinition, endVertex: BRepVertexDefinition, modelSpaceCurve: Curve3D) -> BRepWireEdgeDefinition
Creates a new BRepWireEdgeDefinition object associated with the parent BRepWireDefinition object.
- **startVertex** (BRepVertexDefinition): Vertex definition that defines the start of the edge. For a closed curve, like a circle, you still need to provide a vertex on the curve but should use the same BRepVertexDefinition for both the start and end vertices.
- **endVertex** (BRepVertexDefinition): Vertex definition that defines the end of the edge. For a closed curve, like a circle, this should be the same vertex as used for the start vertex.
- **modelSpaceCurve** (Curve3D): A Curve3D object that defines the shape of the edge using 3D geometry in model space. Valid input is an Arc3D, NurbsCurve3D, Circle3D, Ellipse3D, EllipticalArc3D, or Line3D.
- **Returns** (BRepWireEdgeDefinition): Returns the newly created BRepWireEdgeDefinition object or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> BRepWireEdgeDefinition
Function that returns the specified BRepWireEdgeDefinition object using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (BRepWireEdgeDefinition): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
The number of B-Rep wire edge definition objects in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **BRep Body definition Sample**: Demonstrates creating BRep bodies by BRepBodyDefinition.
