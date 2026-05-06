# PathEntity
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

The PathEntity object represents a curve within a path

**Accessed from:** Path.item, PathEntity.createForAssemblyContext, PathEntity.nativeObject

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> PathEntity
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **Returns** (PathEntity): Returns the proxy object or null if this isn't the NativeObject.

## Properties

### assemblyContext : Occurrence [read-only]
This property is not supported for a PathEntity object.

### curve : Curve3D [read-only]
Property that returns the geometry of the entity. This is different from the original path curve if the true start point is not the same as the start point of the original path curve.

### curveType : Curve3DTypes [read-only]
Property that returns the type of the curve referenced by the path entity. This property allows you to determine what type of object will be returned by the Curve property.

### entity : Base [read-only]
Property that gets the sketch curve or edge this entity was derived from.

### isOpposedToEntity : boolean [read-only]
Indicates if the orientation of this PathEntity is in the same direction or opposed to the natural direction of the SketchCurve or BRepEdge object it is derived from.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### nativeObject : PathEntity [read-only]
This property is not supported for a PathEntity object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentPath : Path [read-only]
Property that returns the parent Path of the entity.
