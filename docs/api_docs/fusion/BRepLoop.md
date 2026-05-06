# BRepLoop
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Represents a connected portion of a BRepFace boundary. It consists of a chain of BRepCoEdges.

**Accessed from:** BRepCoEdge.loop, BRepLoop.createForAssemblyContext, BRepLoop.nativeObject, BRepLoops.item, UntrimFeature.loopsToUntrim, UntrimFeatureInput.loopsToUntrim

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> BRepLoop
Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context for the created proxy.
- **Returns** (BRepLoop): Returns the new BrepLoop proxy or null if this isn't the NativeObject.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this BRepLoop object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object.

### body : BRepBody [read-only]
Returns the parent body of the loop.

### boundingBox : BoundingBox3D [read-only]
Returns the bounding box of this loop

### coEdges : BRepCoEdges [read-only]
Returns the BRepCoEdges consisting this loop

### edges : BRepEdges [read-only]
Returns the BRepEdges used by this loop

### entityToken : string [read-only]
Returns a token for the BRepLoop object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same loop.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

This is only valid for loops that exist in the design, (the isTemporary property is false).

### face : BRepFace [read-only]
Returns the parent face of the loop.

### isOuter : boolean [read-only]
Returns true of this loop is an outer loop of a face

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### nativeObject : BRepLoop [read-only]
The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
