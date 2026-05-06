# BRepWireEdgeDefinition
Namespace: adsk.fusion
Inherits: Base
Since: September 2020

Represents the definition of an edge in B-Rep wire that can be used as input to create a BRepBody that includes this wire edge.

**Accessed from:** BRepWireEdgeDefinitions.add, BRepWireEdgeDefinitions.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### associativeID : integer [read-write]
Gets and sets the associate ID of this B-Rep wire definition. This ID will be copied to the corresponding edge when the BRepBodyDefinition is used to create a BrepBody. It is used by Fusion as the identifier for the edge and is used for tracking this geometry for parametric recomputes.

### endVertex : BRepVertexDefinition [read-write]
Gets and sets the end vertex of the wire edge definition.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### modelSpaceCurve : Curve3D [read-write]
Gets and sets the Curve3D object that defines the shape of the edge using 3D geometry in model space. Valid objects are an Arc3D, NurbsCurve3D, Circle3D, Ellipse3D, EllipticalArc3D, or Line3D.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### startVertex : BRepVertexDefinition [read-write]
Gets and sets the start vertex of the wire edge definition.

## Samples
- **BRep Body definition Sample**: Demonstrates creating BRep bodies by BRepBodyDefinition.
