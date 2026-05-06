# Path
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

The Path object represents a single set of connected curves. The order of the objects within the collection is the same as the connection order of the entities. When using a Path to create a feature, the Path serves as a way to pass in the set of sketch entities and edges. When getting the Path of an existing feature it returns the actual path used to define the feature geometry. In cases like a sweep feature, this can result in using portions of the original input sketch curves or edges and the returned path will provide these "partial" curves as the PathEntity objects.

**Accessed from:** Features.createPath, Path.create, Path.createForAssemblyContext, Path.nativeObject, PathEntity.parentPath, PathPatternFeature.path, PathPatternFeatureInput.path, PipeFeature.path, PipeFeatureInput.path, SweepFeature.guideRail, SweepFeature.path, SweepFeatureInput.guideRail, SweepFeatureInput.path

## Methods

### addCurves(curves: Base, chainOptions: ChainedCurveOptions) -> boolean
Adds additional curves to the existing path. This can be useful when creating a complex path for a sweep and you want to include sets of curves from multiple sketches and edges from multiple bodies.
- **curves** (Base): A SketchCurve, BRepEdge, or an ObjectCollection containing multiple sketch entities and/or BRepEdges. If a single sketch curve or BRepEdge is input the chainCurves argument is used to determine if connected curves or edges (they do not need to be tangent) should be automatically found. Searching for connected curves is only performed within the same sketch or open edges on the same body. If multiple curves are provided the chainCurves argument is treated as false so only the specified input curves are used. The input curves need to geometrically connect for a path to be created.
- **chainOptions** (ChainedCurveOptions): If a single SketchCurve or BRepEdge is input, this argument is used to specify the rules in how chained entities should be found. If an ObjectCollection is input, this argument is ignored.
- **Returns** (boolean): Returns a bool indicating if the process was successful or not.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(curves: Base, chainOptions: ChainedCurveOptions) -> Path
Creates a new Path that can be used as input to various features. For example, it is used to create an open set of curves to create surfaces using extrude, revolve, and sweep. It is also used to create the path for a sweep and sections and profiles and rails for lofts. And it is used to define the boundary of a patch feature.

Although the creation of a path is very flexible as far as the types of entities and whether they are planar or not, each of the features have specific requirements and the path must meet those requirements. For example, a path for an extrusion can only contain sketch curves and must be planar, whereas the path for a sweep can contain a mix of sketch curves and edges and can be in three dimensions.
- **curves** (Base): A SketchCurve, BRepEdge, or an ObjectCollection containing multiple sketch entities and/or BRepEdges. If a single sketch curve or BRepEdge is input the chainCurves argument is used to determine if connected curves or edges (they do not need to be tangent) should be automatically found. Searching for connected curves is only performed within the same sketch or open edges on the same body. If multiple curves are provided the chainCurves argument is treated as false so only the specified input curves are used. The input curves need to geometrically connect for a path to be created.
- **chainOptions** (ChainedCurveOptions): If a single SketchCurve or BRepEdge is input, this argument is used to specify the rules in how chained entities should be found. If an ObjectCollection is input, this argument is ignored.
- **Returns** (Path): Returns the new Path object or null in the case of a failure.

### createForAssemblyContext(occurrence: Occurrence) -> Path
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **Returns** (Path): Returns the proxy object or null if this isn't the NativeObject.

### item(index: uinteger) -> PathEntity
Function that returns the specified PathEntity using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (PathEntity): Returns the specified item or null if an invalid index was specified.

## Properties

### assemblyContext : Occurrence [read-only]
This property is not supported for the Path object.

### count : uinteger [read-only]
The number of curves in the path.

### isClosed : boolean [read-only]
Indicates if the path is closed or not. Returns True in the case of a closed path.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### nativeObject : Path [read-only]
This property is not supported for the Path object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
