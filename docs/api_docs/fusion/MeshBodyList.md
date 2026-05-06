# MeshBodyList
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Provides access to a list of MeshBody objects.

**Accessed from:** MeshBodies.add

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> MeshBody
Provides access to a mesh body within the collection.
- **index** (uinteger): The index of the mesh body to return, where an index of 0 is the first mesh body in the collection.
- **Returns** (MeshBody): Returns the specified mesh body or null in the case of a invalid index.

## Properties

### count : uinteger [read-only]
Returns the number of mesh bodies in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
