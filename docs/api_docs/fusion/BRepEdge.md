# BRepEdge
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Represents a one-dimensional topological element that can be used to bound a BRepFace A BRepEdge uses a single, connected and bounded subset of a curve for it geometry.

**Accessed from:** AlongEdgeRipFeatureDefinition.ripEdge, AtCenterHolePositionDefinition.centerEdge, BRepCoEdge.edge, BRepEdge.createForAssemblyContext, BRepEdge.nativeObject, BRepEdges.item, CornerClosureFeatureDefinition.dominantEdge, CornerClosureFeatureDefinition.submissiveEdge, CornerClosureFeatureInput.dominantEdge, CornerClosureFeatureInput.submissiveEdge, DoubleHemFeatureDefinition.hemEdge, FlatHemFeatureDefinition.hemEdge, HemFeatureDefinition.hemEdge, OnEdgeHolePositionDefinition.edge, OpenHemFeatureDefinition.hemEdge, PlaneAndOffsetsHolePositionDefinition.edgeOne, PlaneAndOffsetsHolePositionDefinition.edgeTwo, RolledHemFeatureDefinition.hemEdge, RopeHemFeatureDefinition.hemEdge, TeardropHemFeatureDefinition.hemEdge, ThreeBendCornerClosureFeatureDefinition.dominantEdge, ThreeBendCornerClosureFeatureDefinition.submissiveEdge, TwoBendCornerClosureFeatureDefinition.dominantEdge, TwoBendCornerClosureFeatureDefinition.submissiveEdge

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> BRepEdge
Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context for the created proxy.
- **Returns** (BRepEdge): Returns the new BrepEdge proxy or null if this isn't the NativeObject.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this BRepEdge object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this face.

### body : BRepBody [read-only]
Returns the parent body of the edge.

### boundingBox : BoundingBox3D [read-only]
Returns the bounding box of this edge.

### coEdges : BRepCoEdges [read-only]
Returns the BRepCoEdges on the edge.

### endVertex : BRepVertex [read-only]
Returns the BRepVertex that bounds its high parameter end.

### entityToken : string [read-only]
Returns a token for the BRepEdge object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same edge.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

This is only valid for edges that exist in the design, (the isTemporary property is false).

### evaluator : CurveEvaluator3D [read-only]
Returns CurveEvaluator3D for evaluation.

### faces : BRepFaces [read-only]
Returns the BRepFaces that are associated with this edge through its BRepCoEdges.

### geometry : Curve3D [read-only]
Returns the underlying curve geometry of the edge.

### isDegenerate : boolean [read-only]
Returns if the edge's geometry is degenerate. For example, the apex of a cone is a degenerate edge.

### isParamReversed : boolean [read-only]
Returns if the parametric direction of this edge is reversed from the parametric direction of the underlying curve obtained from the geometry property. An edge's parametric direction is from the start vertex to the end vertex. But the underlying curve geometry may have the opposite parameterization. This property indicates if the parameterization order of the evaluator obtained from this edge is reversed from the order of the geometry curve's evaluator.

### isTolerant : boolean [read-only]
Returns if the edge is tolerant. The tolerance used is available from the tolerance property.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### length : double [read-only]
Returns the length of the edge in centimeters.

### nativeObject : BRepEdge [read-only]
The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### pointOnEdge : Point3D [read-only]
Returns a sample point guaranteed to lie on the edge's curve, within its boundaries, and not on a vertex (unless this is a degenerate edge).

### shell : BRepShell [read-only]
Returns the parent shell of the edge.

### startVertex : BRepVertex [read-only]
Returns the BRepVertex that bounds its low parameter end.

### tangentiallyConnectedEdges : ObjectCollection [read-only]
Returns a collection of edges that includes all of the edges tangentially connected to this edge. The result includes this edge. The edges are in the collection in their connected order.

### tempId : integer [read-only]
Returns the temporary ID of this edge. This ID is only good while the document remains open and as long as the owning BRepBody is not modified in any way. The findByTempId method of the BRepBody will return the entity in the body with the given ID.

### tolerance : double [read-only]
Returns the tolerance used by a tolerant edge. This value is only useful when isTolerant is true.

## Samples
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
