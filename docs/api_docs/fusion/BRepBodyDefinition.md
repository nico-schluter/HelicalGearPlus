# BRepBodyDefinition
Namespace: adsk.fusion
Inherits: Base
Since: September 2020

This object is used to define a temporary B-Rep body. This includes solid, surface, and wire bodies. The class supports the ability to define the geometry and topology of the B-Rep and once the definition is complete, it supports the creation of a temporary BRepBody object.

**Accessed from:** BRepBodyDefinition.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create() -> BRepBodyDefinition
Static function that creates a new BRepBodyDefinition object. It's initially empty but you can use the functionality it provides to define the geometry and topology of the B-Rep object you want to create.
- **Returns** (BRepBodyDefinition): Returns the newly created BRepBodyDefinition object.

### createBody() -> BRepBody
Attempts to create a temporary BRepBody object using the definition provided by this BRepBodyDefinition object. Properties on this BRepBodyDefinition are used to define some of the criteria that control how the body is created.
- **Returns** (BRepBody): Returns the newly created BRepBody object if successful, otherwise null is returned. Information about the body creation can be obtained by using the outcomeInfo property. The outcom info is especially useful when initially writing and debugging your code to understand why the creation of the body is failing.

### createEdgeDefinitionByCurve(startVertex: BRepVertexDefinition, endVertex: BRepVertexDefinition, modelSpaceCurve: Curve3D) -> BRepEdgeDefinition
Using a curve in model space it creates a new BRepEdgeDefinition object that's associated with the body.
- **startVertex** (BRepVertexDefinition): Vertex definition that defines the start of the edge. For a closed curve, like a circle, you still need to provide a vertex on the curve but you should use the same BRepVertexDefinition for both the start and end vertices.
- **endVertex** (BRepVertexDefinition): Vertex definition that defines the end of the edge. For a closed curve, like a circle, this should be the same vertex as used for the start vertex.
- **modelSpaceCurve** (Curve3D): A Curve3D object that defines the shape of the edge using 3D geometry in model space. Valid input is an Arc3D, NurbsCurve3D, Circle3D, Ellipse3D, EllipticalArc3D, or Line3D.
- **Returns** (BRepEdgeDefinition): Returns the created BRepEdgeDefinition object or null in the case of failure.

### createVertexDefinition(position: Point3D) -> BRepVertexDefinition
Creates a new BRepVertexDefinition object that's associated with the body.
- **position** (Point3D): Specifies the position of the vertex in model space.
- **Returns** (BRepVertexDefinition): Returns the created BRepVertexDefinition object or null in the case of failure.

## Properties

### doFullHealing : boolean [read-write]
Specifies if full healing is done when creating the body. This defaults to true and it's highly recommended that you do full healing because it can find and correct problems with the input. If you're sure that the B-Rep definition that you've constructed is correct then you can set this to false to skip the full healing process.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### lumpDefinitions : BRepLumpDefinitions [read-only]
Provides access to the BRepLumpDefinitions object associated with this BRepBodyDefinition. It's through the returned collection that you can create new BRepLumpDefinition objects.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### outcomeInfo : array [read-only]
Returns an array of strings that contain information about the outcome of the previous call of the createBody method. This is especially useful when the createBody method fails, (returns null), because it provides information about why the failure occurred. It can also sometimes provide some information even when createBody succeeds.

Each string that's returned represents a single set of information and is packaged as JSON such as '{"description":"vertex data is null or inconsistent with edge geometry","associativeID":"unknown","code":37}'

The description is an English description of the error or warning. The associativeID maps back to the entity provided that is the cause of the problem. The ID is the associative ID you can optionally assign to the entity definition. The code is an internal code for the error or warning.

An empty array is returned if createBody succeeded and there's no additional information.

## Samples
- **BRep Body definition Sample**: Demonstrates creating BRep bodies by BRepBodyDefinition.
