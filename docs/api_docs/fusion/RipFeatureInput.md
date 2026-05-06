# RipFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: September 2023

This class defines the methods and properties that pertain to the definition of a Rip feature.

**Accessed from:** RipFeatures.createRipFeatureInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setAlongEdge(edge: BRepEdge, gapDistance: ValueInput) -> boolean
Specifies the rip feature will be along an edge.
- **edge** (BRepEdge): The BRepEdge that defines the location of the rip.
- **gapDistance** (ValueInput): The gap distance of the rip.
- **Returns** (boolean): Returns true if the defining the rip is successful.

### setBetweenPoints(pointOneEntity: Base, pointTwoEntity: Base, gapDistance: ValueInput, pointOneOffset: ValueInput, pointTwoOffset: ValueInput) -> boolean
This input method is for creating a rip between two points. Each point can be either a BRepVertex or a BRepEdge and an associated offset along the edge.
- **pointOneEntity** (Base): The first point of the rip. This can be defined using a BrepVertex or a BRepEdge and offset to define where the point is along the edge. If an edge is specified, the pointOneOffset parameter must be specified.
- **pointTwoEntity** (Base): The second point of the rip and must lie on the same face as point 1. This can be defined using a BrepVertex or a BRepEdge and an offset to define where the point is along the edge. If an edge is specified, the pointTwoOffset parameter must be specified.
- **gapDistance** (ValueInput): The gap distance of the rip.
- **pointOneOffset** (ValueInput): If the first point lies on an edge, then this is the offset along the edge which defines the point. This is the physical distance from the topological start of the edge. If the offset is negative or exceeds the edge length, the corresponding vertex of the edge will be used.

This is an optional argument whose default value is null.
- **pointTwoOffset** (ValueInput): If the second point lies on an edge, then this is the offset along the edge which defines the point. This is the physical distance from the topological start of the edge. If the offset is negative or exceeds the edge length, the corresponding vertex of the edge will be used.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if the rip definition is successful.

### setByFace(face: BRepFace) -> boolean
Specifies the rip feature will be defined by a face..
- **face** (BRepFace): The sheet metal face that defines the rip.
- **Returns** (boolean): Returns true if the defining the rip is successful.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Rip Feature Sample**: Demonstrates creating a new sheet metal rip feature.
