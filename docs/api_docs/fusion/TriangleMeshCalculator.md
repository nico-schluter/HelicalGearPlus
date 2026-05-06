# TriangleMeshCalculator
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Used to calculate new meshes for a B-Rep or T-Spline using defined criteria.

**Accessed from:** MeshManager.createMeshCalculator

## Methods

### calculate() -> TriangleMesh
Calculates a new triangle mesh based on the current settings.
- **Returns** (TriangleMesh): Returns the new TriangleMesh object or null in the case where the calculation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setQuality(triangleMeshQuality: TriangleMeshQualityOptions) -> boolean
This is a simplified way to set the various settings that control the resulting mesh. When used it automatically adjusts all of the property values appropriately. It does this for the given geometry by computing its bounding box diameter. Then the surface tolerance is calculated as shown below where the meshLOD is the "Level of Detail" and is described in more detail below. The diameter is the bounding box diameter.

double nodeApproximateSize = std::pow(2.0, meshLOD); double fracTol = 1.0 / nodeApproximateSize; surfaceTolerance = fracTol * diameter;
- **triangleMeshQuality** (TriangleMeshQualityOptions): The mesh quality is specified by using an item from the enum list where the following items result in a corresponding mesh LOD that's used in the equation above.

LowQualityTriangleMesh: 8 NormalQualityTriangleMesh: 11 HighQualityTriangleMesh: 13 VeryHighQualityTriangleMesh: 15
- **Returns** (boolean): Returns true if setting the quality was successful.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maxAspectRatio : double [read-write]
Specifies the maximum length to height ratio that a triangle can have. This helps to avoid long skinny triangles. A value of 0 (the default) indicates that no maximum aspect ratio is specified.

### maxNormalDeviation : double [read-write]
Specifies the maximum deviation between adjacent vertex normals. This value is the maximum angle allowed between normals and is specified in radians. A value of 0 (the default) indicates that no normal deviation is specified.

### maxSideLength : double [read-write]
Specifies the maximum side of any triangle in the mesh. A value of 0 (the default) indicates that no maximum length is specified. The value is specified in centimeters.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentMeshManager : MeshManager [read-only]
Returns the parent MeshManager object.

### surfaceTolerance : double [read-write]
Specifies the maximum distance that the mesh can deviate from the smooth surface. The value is in centimeters. Smaller values can result in a much greater number of facets being returned and will require more processing time to calculate.
