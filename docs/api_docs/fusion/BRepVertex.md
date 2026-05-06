# BRepVertex
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

A 0-dimensional topological entity that bounds a BRepEdge.

**Accessed from:** BRepEdge.endVertex, BRepEdge.startVertex, BRepVertex.createForAssemblyContext, BRepVertex.nativeObject, BRepVertices.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> BRepVertex
Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context for the created proxy.
- **Returns** (BRepVertex): Returns the new BrepVertex proxy or null if this isn't the NativeObject.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this BRepVertex object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this face.

### body : BRepBody [read-only]
Returns the parent body.

### edges : BRepEdges [read-only]
Returns the BRepEdges bounded by this vertex

### entityToken : string [read-only]
Returns a token for the BRepVertex object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same vertex.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

This is only valid for vertices that exist in the design, (the isTemporary property is false).

### faces : BRepFaces [read-only]
Returns the BRepFaces that uses this vertex through BRepEdge

### geometry : Point3D [read-only]
Returns the underlying geometry point

### isTolerant : boolean [read-only]
Returns if the vertex is tolerant. The tolerance used is available from the tolerance property.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### nativeObject : BRepVertex [read-only]
The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### shell : BRepShell [read-only]
Returns the parent shell.

### tempId : integer [read-only]
Returns the temporary ID of this vertex. This ID is only good while the document remains open and as long as the owning BRepBody is not modified in any way. The findByTempId method of the BRepBody will return the entity in the body with the given ID.

### tolerance : double [read-only]
Returns the tolerance used by a tolerant vertex. This value is only useful when isTolerant is true.
