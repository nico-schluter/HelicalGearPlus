# Vector3D
Namespace: adsk.core
Inherits: Base
Since: August 2014

Transient 3D vector. This object is a wrapper over 3D vector data and is used as way to pass vector data in and out of the API and as a convenience when operating on vector data. They are created statically using the create method of the Vector3D class.

**Accessed from:** AngleValueCommandInput.manipulatorXDirection, AngleValueCommandInput.manipulatorYDirection, Arc3D.getData, Arc3D.normal, Arc3D.referenceVector, AreaProperties.getPrincipalAxes, ArrangeComponent.upDirection, ArrangeComponent.zeroDirection, BallJointMotion.pitchDirectionVector, BallJointMotion.rollDirectionVector, BallJointMotion.yawDirectionVector, BossFeature.direction, Camera.upVector, Circle3D.getData, Circle3D.normal, Cone.axis, Cone.getData, CurveEvaluator3D.getCurvature, CurveEvaluator3D.getFirstDerivative, CurveEvaluator3D.getSecondDerivative, CurveEvaluator3D.getTangent, CurveEvaluator3D.getThirdDerivative, CustomGraphicsBillBoard.axis, Cylinder.axis, Cylinder.getData, CylindricalJointMotion.rotationAxisVector, DirectionCommandInput.manipulatorDirection, DistanceValueCommandInput.manipulatorDirection, Ellipse3D.getData, Ellipse3D.majorAxis, Ellipse3D.normal, EllipticalArc3D.getData, EllipticalArc3D.majorAxis, EllipticalArc3D.normal, EllipticalCone.getAxes, EllipticalCone.getData, EllipticalCylinder.axis, EllipticalCylinder.getData, EllipticalCylinder.majorAxis, ExtruderMachineElement.offset, HoleFeature.direction, InfiniteLine3D.direction, InfiniteLine3D.getData, JointGeometry.primaryAxisVector, JointGeometry.secondaryAxisVector, JointGeometry.thirdAxisVector, JointOrigin.primaryAxisVector, JointOrigin.secondaryAxisVector, JointOrigin.thirdAxisVector, JointOriginInput.primaryAxisVector, JointOriginInput.secondaryAxisVector, JointOriginInput.thirdAxisVector, LinearMachineAxis.direction, LinearMachineAxisInput.direction, Matrix3D.getAsCoordinateSystem, Matrix3D.translation, MultiAxisRetractAndReconfigureSettings.stockExpansion, OrientedBoundingBox3D.heightDirection, OrientedBoundingBox3D.lengthDirection, OrientedBoundingBox3D.widthDirection, PhysicalProperties.getPrincipalAxes, PinSlotJointMotion.rotationAxisVector, PinSlotJointMotion.slideDirectionVector, PlanarJointMotion.normalDirectionVector, PlanarJointMotion.primarySlideDirectionVector, PlanarJointMotion.secondarySlideDirectionVector, Plane.normal, Plane.uDirection, Plane.vDirection, Point3D.asVector, Point3D.vectorTo, PolygonMesh.normalVectors, RecognizedHole.axis, RecognizedHoleSegment.axis, RectangularPatternFeature.directionOne, RectangularPatternFeature.directionTwo, RectangularPatternFeatureInput.directionOne, RectangularPatternFeatureInput.directionTwo, RevoluteJointMotion.rotationAxisVector, Sketch.xDirection, Sketch.yDirection, SketchEllipse.majorAxis, SketchEllipticalArc.majorAxis, SliderJointMotion.slideDirectionVector, SurfaceEvaluator.getCurvature, SurfaceEvaluator.getFirstDerivative, SurfaceEvaluator.getNormalAtParameter, SurfaceEvaluator.getNormalAtPoint, SurfaceEvaluator.getSecondDerivative, SurfaceEvaluator.getThirdDerivative, ToEntityExtentDefinition.directionHint, Torus.axis, Torus.getData, TriangleMesh.normalVectors, Vector3D.copy, Vector3D.create, Vector3D.crossProduct, Vector3DGraphNodeProperty.value, Viewport.frontEyeDirection, Viewport.frontUpDirection, VolumetricVectorSample.value

## Methods

### add(vector: Vector3D) -> boolean
Adds a vector to this vector.
- **vector** (Vector3D): The vector to add to this vector.
- **Returns** (boolean): Returns true if successful.

### angleTo(vector: Vector3D) -> double
Determines the angle between this vector and the specified vector.
- **vector** (Vector3D): The vector to measure the angle to.
- **Returns** (double): The angle in radians between this vector and the specified vector.

### asArray() -> double[]
Returns the vector coordinates as an array [x, y, z].
- **Returns** (double[]): Returns the array of vector coordinates [x, y, z].

### asPoint() -> Point3D
Returns a new point with the same coordinate values as this vector.
- **Returns** (Point3D): Return the new point.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Vector3D
Creates a copy of this vector.
- **Returns** (Vector3D): Returns the new vector copy.

### create(x: double, y: double, z: double) -> Vector3D
Creates a 3D vector object. This object is created statically using the Vector3D.create method.
- **x** (double): The optional x value.

This is an optional argument whose default value is 0.0.
- **y** (double): The optional y value.

This is an optional argument whose default value is 0.0.
- **z** (double): The optional z value.

This is an optional argument whose default value is 0.0.
- **Returns** (Vector3D): Returns the new vector.

### crossProduct(vector: Vector3D) -> Vector3D
Returns the cross product between this vector and the specified vector.
- **vector** (Vector3D): The vector to take the cross product to.
- **Returns** (Vector3D): Returns the vector cross product.

### dotProduct(vector: Vector3D) -> double
Returns the dot product between this vector and the specified vector.
- **vector** (Vector3D): The vector to take the dot product to.
- **Returns** (double): Returns the dot product value.

### isEqualTo(vector: Vector3D) -> boolean
Determines if this vector is equal to the specified vector.
- **vector** (Vector3D): The vector to test equality to.
- **Returns** (boolean): Returns true if the vectors are equal.

### isParallelTo(vector: Vector3D) -> boolean
Determines if the input vector is parallel with this vector.
- **vector** (Vector3D): The vector to test parallelism to.
- **Returns** (boolean): Returns true if the vectors are parallel.

### isPerpendicularTo(vector: Vector3D) -> boolean
Determines if the input vector is perpendicular to this vector.
- **vector** (Vector3D): The vector to test perpendicularity to.
- **Returns** (boolean): Returns true if the vectors are perpendicular.

### normalize() -> boolean
Makes this vector of unit length. This vector should not be zero length.
- **Returns** (boolean): Returns true if successful.

### scaleBy(scale: double) -> boolean
Scale this vector by the specified product.
- **scale** (double): The scale value.
- **Returns** (boolean): Returns true if successful.

### setWithArray(coordinates: double[]) -> boolean
Reset this vector with the coordinate values in an array [x, y, z].
- **coordinates** (double[]): The array of coordinate values.
- **Returns** (boolean): Returns true if successful.

### subtract(vector: Vector3D) -> boolean
Subtract a vector from this vector.
- **vector** (Vector3D): The vector to subtract.
- **Returns** (boolean): Returns true if successful.

### transformBy(matrix: Matrix3D) -> boolean
Transform this vector by the specified matrix.
- **matrix** (Matrix3D): The transformation matrix.
- **Returns** (boolean): Returns true if successful.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### length : double [read-only]
Get the length of this vector.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### x : double [read-write]
The x value.

### y : double [read-write]
The y value.

### z : double [read-write]
The z value.

## Samples
- **Create Setups From Hole Recognition API Sample**: This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.
The Fusion Manufacturing Extension is required for Hole Recognition.
The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector.
- **moveFeatures.add**: Demonstrates the moveFeatures.add method.
