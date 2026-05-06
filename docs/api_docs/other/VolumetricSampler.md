# VolumetricSampler
Namespace: adsk.volume
Inherits: Base
Since: May 2025

The VolumetricSampler object which is used for controled sampling of the volumetric model.

**Accessed from:** VolumetricModel.createSampler

## Methods

### addSamplePoints(samplePoints: Point3D[])
Appends sample points to the existing sample points to be used for sampling the volumetric model.
- **samplePoints** (Point3D[]): The sample points to be added to the sampler.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### clearSamplePoints() -> boolean
Clears the sample points that have been set for sampling the volumetric model.
- **Returns** (boolean): True if the sample points were successfully cleared.

### evaluate(graphNode: GraphNode, isOutput: boolean, index: integer) -> VolumetricSample
Evaluates the volumetric model at the previously set sample points for the given node and returns the results.
- **graphNode** (GraphNode): The graph node to evaluate at the sample points.
- **isOutput** (boolean): Optional argument that controls the sampling. If set to true samples an output pin, if set to false samples an input pin. Default is True.

This is an optional argument whose default value is True.
- **index** (integer): Optional argument that controls the index of the pin to sample. Default is 0 which is the first pin.

This is an optional argument whose default value is 0.
- **Returns** (VolumetricSample): An array of VolumetricSample objects that contain the results of sampling the volumetric model.

### evaluateColor() -> VolumetricColorSample
Evaluates the color of the model at the previously set sample points and returns the results.
- **Returns** (VolumetricColorSample): An array of VolumetricColorSample objects that contain the results of sampling the volumetric model.

### evaluateDensity() -> VolumetricScalarSample
Evaluates the density of the model at the previously set sample points and returns the results. This value is what is used to determine the level set of the model.
- **Returns** (VolumetricScalarSample): An array of VolumetricScalarSample objects that contain the results of sampling the volumetric model.

### evaluateLevelSet() -> VolumetricScalarSample
Evaluates the level set function of the model at the previously set sample points and returns the results.
- **Returns** (VolumetricScalarSample): An array of VolumetricScalarSample objectst that contain the results of sampling the volumetric model.

### samplePointCount() -> uinteger
Gets the number of sample points that will be used for sampling the volumetric model.
- **Returns** (uinteger): The number of sample points that will be used for sampling the volumetric model.

### setBoundingBoxSampling(elementSize: double, boundingBox3d: BoundingBox3D) -> boolean
Calculates and sets the sample points to be used for sampling the volumetric model for a given resolution throughout the bounding box provided. This will override any previously set sample points.
- **elementSize** (double): The approximate spacing between sample points. The units used for the element size are centimeters.
- **boundingBox3d** (BoundingBox3D): The bounding box in which the sample points will be distributed.
- **Returns** (boolean): True if the sample points were set successfully.

### setPlaneSampling(elementSize: double, plane: Plane, primaryAxis: Vector3D, primaryAxisSize: double, secondaryAxisSize: double) -> boolean
Calculates and sets the sample points to be used for sampling the volumetric model for a given resolution, plane and primary axis. The points will be distributed in a grid pattern on the plane, starting at the plane origin and extend in the primary axis and secodary axis for the axis size arguments. The secondary axis is calculated from the cross product of the plane normal and the primary axis. This will override any previously set sample points.
- **elementSize** (double): The approximate spacing between sample points. The units used for the element size are centimeters.
- **plane** (Plane): The plane on which the points will be distributed.
- **primaryAxis** (Vector3D): The primary axis of the plane. This vector should be on the plane. The secondary axis of the plane is calculated as the cross-product of the plane normal and the primary axis
- **primaryAxisSize** (double): The size of the plane in the primary axis direction.
- **secondaryAxisSize** (double): The size of the plane in the secondary axis direction.
- **Returns** (boolean): True if the sample points were set successfully.

### setSamplePoints(samplePoints: Point3D[]) -> boolean
Sets sample points to be used for sampling the volumetric model.
- **samplePoints** (Point3D[]): The sample points to be used for sampling the volumetric model.
- **Returns** (boolean): True if the sample points were set successfully.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
