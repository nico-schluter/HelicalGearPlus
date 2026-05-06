# MeshBodies
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Provides access to the MeshBodies in the parent Component and supports the creation of new mesh bodies.

**Accessed from:** Component.meshBodies, FlatPatternComponent.meshBodies

## Methods

### add(fullFilename: string, units: MeshUnits, baseOrFormFeature: Base) -> MeshBodyList
Creates a new mesh body by importing an STL, OBJ or 3MF file.

Because of a current limitation, if you want to create a mesh body in a parametric model, you must first call the edit method of the base or form feature, use this method to create the mesh body, and then call the finishEdit method of the base or form feature. The base or form feature must be in an "edit" state to be able to add any additional items to it.
- **fullFilename** (string): The full filename (path and file) of a STL, OBJ or 3MF file.
- **units** (MeshUnits): The units to use when importing the file.
- **baseOrFormFeature** (Base): The BaseFeature or FormFeature object that this mesh body will be associated with. This is an optional requirement. It is required in a parametric modeling design but is ignored in a direct modeling design.

This is an optional argument whose default value is null.
- **Returns** (MeshBodyList): Returns a list of the newly created mesh bodies or null if the creation failed. Multiple bodies can be created in the case where a .obj file that contains multiple bodies was imported. STL files always contain a single body.

### addByTriangleMeshData(coordinates: double[], coordinateIndexList: integer[], normalVectors: double[], normalIndexList: integer[]) -> MeshBody
Creates a new mesh body using the mesh description provided.
- **coordinates** (double[]): Input array of doubles that defines the X, Y, Z coordinates of each node in the mesh. Each set of three numbers define the coordinates of a node.
- **coordinateIndexList** (integer[]): An array of integers that represent indices into the coordinates to define the vertices of the triangles. If an empty array is provided, then it's assumed that the first three coordinates defines the first triangle, the next three define the second triangle, and so on.
- **normalVectors** (double[]): An array of doubles that represent the x, y, z components of the normals at each coordinate. There should be a normal defined for each coordinate. If an empty array is provided for the normal vectors, Fusion will automatically calculate normal vectors that are 90 degrees to the face of the triangle, making it appear flat.
- **normalIndexList** (integer[]): An array of integers that represent indices into the normal vectors to define the which vector corresponds to which vertex. This should be the same size as the vertex index list. If an empty array is input and normal vectors are provided, it is assumed that the normals match up one-to-one to each coordinate.
- **Returns** (MeshBody): Returns the newly created MeshBody object or null in the case of a failure.

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
