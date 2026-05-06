# BRepLump
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Represents an entirely connected set of entities. A BRepBody consists of BRepLumps.

**Accessed from:** BRepLump.createForAssemblyContext, BRepLump.nativeObject, BRepLumps.item, BRepShell.lump

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> BRepLump
Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context for the created proxy.
- **Returns** (BRepLump): Returns the new BrepLump proxy or null if this isn't the NativeObject.

### pointContainment(point: Point3D) -> PointContainment
Determines the relationship of the input point with respect to this lump.
- **point** (Point3D): The point to do the containment check for.
- **Returns** (PointContainment): Returns a value from the PointContainment enum indicating the relationship of the input point to the lump.

## Properties

### area : double [read-only]
Returns the area in cm ^ 2.

### assemblyContext : Occurrence [read-only]
Returns the assembly context that is directly referencing this object in an assembly. This is only valid in the case where this BRepLump object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object.

### body : BRepBody [read-only]
Returns the immediate owner BRepBody of the lump

### boundingBox : BoundingBox3D [read-only]
Returns the bounding box of the lump

### edges : BRepEdges [read-only]
Returns the BRepEdges owned by the lump

### entityToken : string [read-only]
Returns a token for the BRepLump object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same lump.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

This is only valid for lump that exist in the design, (the isTemporary property is false).

### faces : BRepFaces [read-only]
Returns the BRepFaces owned by the lump

### isClosed : boolean [read-only]
Returns true of the lump is closed

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### meshManager : MeshManager [read-only]
Returns the mesh manager object for this lump.

### nativeObject : BRepLump [read-only]
The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### shells : BRepShells [read-only]
Returns the BRepShells owned by the lump

### vertices : BRepVertices [read-only]
Returns the BRepVertices owned by the lump

### volume : double [read-only]
Returns the volume in cm ^ 3. Returns 0 in the case the lump is not solid.
