# TriangleMeshList
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Provides access to a set of triangle meshes.

**Accessed from:** MeshManager.displayMeshes

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> TriangleMesh
Returns the specified triangle meshes.
- **index** (uinteger): The index of the mesh to return where the first item has an index of 0.
- **Returns** (TriangleMesh): Returns the specified mesh or null in the case of invalid index.

## Properties

### bestMesh : TriangleMesh [read-only]
Returns the mesh with the tightest surface tolerance. This can return null in the case the list is empty, i.e. Count is 0.

### count : uinteger [read-only]
Returns the number of meshes in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
