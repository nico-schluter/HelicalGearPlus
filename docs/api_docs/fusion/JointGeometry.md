# JointGeometry
Namespace: adsk.fusion
Inherits: Base
Since: July 2015

A transient object used to define and query the geometric input of a joint and the resulting coordinate system it defines. New JointGeometry objects are created using its various static create methods and are then used as input to the Joints.createInput method.

**Accessed from:** AsBuiltJoint.geometry, AsBuiltJointInput.geometry, JointGeometry.createByBetweenTwoPlanes, JointGeometry.createByCurve, JointGeometry.createByCylinderOrConeFace, JointGeometry.createByNonPlanarFace, JointGeometry.createByPlanarFace, JointGeometry.createByPoint, JointGeometry.createByProfile, JointGeometry.createBySphereFace, JointGeometry.createBySplineFace, JointGeometry.createByTangentFaceEdge, JointGeometry.createByTorusFace, JointGeometry.createByTwoEdgeIntersection, JointOrigin.geometry, JointOriginInput.geometry

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createByBetweenTwoPlanes(planeOne: Base, planeTwo: Base, entityOne: Base, entityTwo: Base, keyPointType: JointKeyPointTypes) -> JointGeometry
Creates a new transient JointGeometry object based on a plane bisecting the two input planes.
- **planeOne** (Base): The first planar entity that the joint origin will be created between. This can be a planar BRepFace or a ConstructionPlane object.
- **planeTwo** (Base): The second planar entity that the joint origin will be created between. This can be a planar BRepFace or a ConstructionPlane object.
- **entityOne** (Base): Specifies the entity that is used to define the keypoint. This can be many types of geometry including edges, planar and non-planar faces, profiles, and sketch geometry.
- **entityTwo** (Base): If the entityOne argument is a planar BRepFace or a Profile, then this argument specifies either an edge on the face or a sketch curve on the profile. For a planar face this argument is optional in the case where the keyPointType argument is CenterKeyPoint indicating the center of area of the face is to be used.
- **keyPointType** (JointKeyPointTypes): Specifies the position on the keyPointGeometry where the keypoint will be defined. This keypoint is then projected onto the plane to define the position of the joint geometry.

The values that are valid for this argument depend on the type of geometry specified for the geometry and edgeOrCurve arguments.

If the geometry argument is a planar face and the edgeOrCurve argument is an open BRepEdge object then this can be StartKeyPoint, MiddleKeyPoint, or EndKeyPoint. If the geometry argument is a planar face and the edgeOrCurve argument is a closed BRepEdge object (i.e. circles), it must be CenterKeyPoint. If the geometry argument is a planar face and the edgeOrCurve argument is null, then this must be CenterKeyPoint indicating the center of area of the face.

If the geometry argument is a non-planar face (cylinder, cone, sphere, or torus) this can be StartKeyPoint, MiddleKeyPoint, or EndKeyPoint for cylinders and cones but must be CenterKeyPoint for spheres and tori. The edgeOrCurve argument is ignored in this case.

If the geometry argument is a profile and the edgeOrCurve argument is null this can be CenterKeyPoint indicating the center of area of the profile. If the geometry argument is a profile and the edgeOrCurve argument is an open sketch curve on the profile then this can be StartKeyPoint, MiddleKeyPoint, or EndKeyPoint. If the geometry argument is a profile and the edgeOrCurve argument is a closed sketch curve (i.e. circles), it must be CenterKeyPoint.
- **Returns** (JointGeometry): Returns the transient JointGeometry object that can be used to create a joint or joint origin or null in case of a failure.

### createByCurve(curve: Base, keyPointType: JointKeyPointTypes) -> JointGeometry
Creates a new transient JointGeometry object using a BRepEdge or SketchCurve as input. A JointGeometry object can be used to create a joint or joint origin.
- **curve** (Base): Input BRepEdge or SketchCurve.
- **keyPointType** (JointKeyPointTypes): The position on the curve where to position the joint coordinate system. For any open curves the valid types are StartKeyPoint, MiddleKeyPoint, CenterKeyPoint and EndKeyPoint. For circular and elliptical shaped curves the option is CenterKeyPoint. For closed spline curves either StartKeyPoint or EndKeyPoint can be used and the result is the same.
- **Returns** (JointGeometry): Returns the transient JointGeometry object that can be used to create a joint or joint origin or null in case of a failure.

### createByCylinderOrConeFace(face: BRepFace, angle: JointQuadrantAngleTypes, height: JointKeyPointTypes) -> JointGeometry
Creates a new transient JointGeometry object based on a cylinder or cone BRepFace object.
- **face** (BRepFace): The cylindrical or conical BRepFace object.
- **angle** (JointQuadrantAngleTypes): Specifies the angle relative to the parameterization of the input face. The zero, or start angle, is where the v parameter of the cylinder is zero. This can be determined by using the getPointAtParameter method of the SurfaceEvaluator object obtained from the evaluator property of the BRepFace object. The possible values can be StartJointQuadrantAngleType, QuarterJointQuadrantAngleType, MiddleJointQuadrantAngleType or ThirdQuarterJointQuadrantAngleType.
- **height** (JointKeyPointTypes): Specifies the vertical position relative to the bottom of the cylinder at the given angle. The possible values can be StartKeyPoint, MiddleKeyPoint or EndKeyPoint.
- **Returns** (JointGeometry): Returns the transient JointGeometry object that can be used to create a joint or joint origin or null in the case of a failure.

### createByNonPlanarFace(face: BRepFace, keyPointType: JointKeyPointTypes) -> JointGeometry
Creates a new transient JointGeometry object based on a non-planar analytical BRepFace object. This is limited to cylinders, cones, spheres, and tori. A JointGeometry object can be used to create a joint or joint origin.
- **face** (BRepFace): The cylindrical, conical, spherical, or toroidal BRepFace object.
- **keyPointType** (JointKeyPointTypes): Specifies the position relative to the input face where the joint keypoint will be located. For cylinders and cones this can be StartKeyPoint, MiddleKeyPoint, or EndKeyPoint. For spheres and tori this must be CenterKeyPoint.
- **Returns** (JointGeometry): Returns the transient JointGeometry object that can be used to create a joint or joint origin or null in case of a failure.

### createByPlanarFace(face: BRepFace, edge: BRepEdge, keyPointType: JointKeyPointTypes) -> JointGeometry
Creates a new transient JointGeometry object based on a planar BRepFace object. A JointGeometry object can be used to create a joint or joint origin.
- **face** (BRepFace): The planar BRepFace object
- **edge** (BRepEdge): A BRepEdge edge object that is one of the edges of the specified face. This argument can be null in the case where the keyPointType is CenterKeypoint indicating the center of the face is to be used. When an edge is used, the keyPointType specifies the position along the edge for the keypoint.
- **keyPointType** (JointKeyPointTypes): Specifies the position along the edge where the joint keypoint will be located. For open edges this can be StartKeyPoint, MiddleKeyPoint, or EndKeyPoint. For closed edges (i.e. circles), it must be CenterKeyPoint. When no edge is specified, it must be CenterKeyPoint indicating the center of area of the face is to be used.
- **Returns** (JointGeometry): Returns the transient JointGeometry object that can be used to create a joint or joint origin or null in case of a failure.

### createByPoint(point: Base) -> JointGeometry
Creates a new transient JointGeometry object using a ConstructionPoint, SketchPoint or BRepVertex as input. A JointGeometry object can be used to create a joint or joint origin.
- **point** (Base): The ConstructionPoint, SketchPoint or BRepVertex object.
- **Returns** (JointGeometry): Returns the transient JointGeometry object that can be used to create a joint or joint origin or null in case of a failure.

### createByProfile(profile: Profile, sketchCurve: SketchCurve, keyPointType: JointKeyPointTypes) -> JointGeometry
Creates a new transient JointGeometry object based on a planar BRepFace object. A JointGeometry object can be used to create a joint or joint origin.
- **profile** (Profile): The Profile object.
- **sketchCurve** (SketchCurve): A sketch curve that is part of the input profile. This argument can be null in the case where the keyPointType is CenterKeypoint indicating the center of the profile is to be used. When a curve is used, the keyPointType specifies the position along the curve for the keypoint.
- **keyPointType** (JointKeyPointTypes): Specifies the position along the curve where the joint keypoint will be located. For open curves (lines, arcs, elliptical arcs, and open splines) this can be StartKeyPoint, MiddleKeyPoint, or EndKeyPoint. For closed analytic (circles and ellipses), it must be CenterKeyPoint. When no curve is specified, it must be CenterKeyPoint indicating the center of area of the profile is to be used.
- **Returns** (JointGeometry): Returns the transient JointGeometry object that can be used to create a joint or joint origin or null in case of a failure.

### createBySphereFace(face: BRepFace, azimuthAngle: JointQuadrantAngleTypes, polarAngle: JointKeyPointTypes) -> JointGeometry
Creates a new transient JointGeometry object based on a sphere BRepFace object.
- **face** (BRepFace): The sphere BRepFace object.
- **azimuthAngle** (JointQuadrantAngleTypes): Specifies the azimuth angle relative to the v parameterization of the input face. The zero, or start angle, is where the v parameter of the sphere is zero. This can be determined by using the getPointAtParameter method of the SurfaceEvaluator object obtained from the evaluator property of the BRepFace object. The possible values can be StartJointQuadrantAngleType, QuarterJointQuadrantAngleType, MiddleJointQuadrantAngleType or ThirdQuarterJointQuadrantAngleType.
- **polarAngle** (JointKeyPointTypes): Specifies the polar angle relative to the u parameterization of the input face. The zero, or start angle, is where the u parameter of the sphere is zero. This can be determined by using the getPointAtParameter method of the SurfaceEvaluator object obtained from the evaluator property of the BRepFace object. The possible values can be StartKeyPoint for the north pole, MiddleKeyPoint for points on the equator, or EndKeyPoint for the south pole.
- **Returns** (JointGeometry): Returns the transient JointGeometry object that can be used to create a joint or joint origin or null in the case of a failure.

### createBySplineFace(face: BRepFace, paramU: JointKeyPointTypes, paramV: JointKeyPointTypes) -> JointGeometry
Creates a new transient JointGeometry object based on a spline BRepFace object.
- **face** (BRepFace): The spline BRepFace object.
- **paramU** (JointKeyPointTypes): Specifies the u parameter of the input spline face where the joint keypoint will be located. The possible values can be StartKeyPoint, MiddleKeyPoint or EndKeyPoint.
- **paramV** (JointKeyPointTypes): Specifies the v parameter of the input spline face where the joint keypoint will be located. The possible values can be StartKeyPoint, MiddleKeyPoint or EndKeyPoint.
- **Returns** (JointGeometry): Returns the transient JointGeometry object that can be used to create a joint or joint origin or null in the case of a failure.

### createByTangentFaceEdge(face: BRepFace, edge: BRepEdge, edgePointType: JointTangentFaceEdgePointTypes) -> JointGeometry
Creates a new transient JointGeometry object based on a BRepFace object as well as a BRepEdge object which is on the BRepFace.
- **face** (BRepFace): The cylindrical, conical, spherical, toroidal or spline BRepFace object.
- **edge** (BRepEdge): A BRepEdge object that is one of the edges on the selected face.
- **edgePointType** (JointTangentFaceEdgePointTypes): Specifies the position along the edge where the joint keypoint will be located. The possible values depend on whether the edge is closed or not. For closed edge, the possible values can be StartJointTangentFaceEdgePointType, QuarterJointTangentFaceEdgePointType, MiddleJointTangentFaceEdgePointType or ThirdQuarterJointTangentFaceEdgePointType. For open edge, the possible values can be StartJointTangentFaceEdgePointType, MiddleJointTangentFaceEdgePointType, or EndJointTangentFaceEdgePointType.
- **Returns** (JointGeometry): Returns the transient JointGeometry object that can be used to create a joint or joint origin or null in the case of a failure.

### createByTorusFace(face: BRepFace, azimuthAngle: JointQuadrantAngleTypes, sectionAngle: JointQuadrantAngleTypes) -> JointGeometry
Creates a new transient JointGeometry object based on a torus BRepFace object.
- **face** (BRepFace): The torus BRepFace object.
- **azimuthAngle** (JointQuadrantAngleTypes): Specifies the azimuth angle relative to the v parameterization of the input face. The zero, or start angle, is where the v parameter of the sphere is zero. This can be determined by using the getPointAtParameter method of the SurfaceEvaluator object obtained from the evaluator property of the BRepFace object. The possible values can be StartJointQuadrantAngleType, QuarterJointQuadrantAngleType, MiddleJointQuadrantAngleType or ThirdQuarterJointQuadrantAngleType.
- **sectionAngle** (JointQuadrantAngleTypes): Specifies the angle relative to the start point of the section circle at give azimuth angle. The possible values can be StartJointQuadrantAngleType, QuarterJointQuadrantAngleType, MiddleJointQuadrantAngleType or ThirdQuarterJointQuadrantAngleType.
- **Returns** (JointGeometry): Returns the transient JointGeometry object that can be used to create a joint or joint origin or null in the case of a failure.

### createByTwoEdgeIntersection(edgeOne: BRepEdge, edgeTwo: BRepEdge) -> JointGeometry
Creates a new transient JointGeometry object that is positioned at the intersection of the two input linear BRepEdge objects.
- **edgeOne** (BRepEdge): The first linear BRepEdge object.
- **edgeTwo** (BRepEdge): The second linear BRepEdge object. This edge must exist either on the same body as edgeOne or on a body in the same component as edgeOne. edgeOne and edgeTwo must also both lie on the same plane and must intersect, they cannot be parallel.
- **Returns** (JointGeometry): Returns the transient JointGeometry object that can be used to create a joint or joint origin or null in case of a failure.

## Properties

### entityOne : Base [read-only]
The first entity that's defining this joint geometry. This can be various types of geometry depending on how this joint geometry is defined. The geometryType property indicates how this joint geometry is defined a provides a clue about the type of geometry to expect back from this property.

### entityTwo : Base [read-only]
This is the second entity that defines this joint geometry. This isn't used for all joint geometry types and will return null in the cases where it's not used. A second geometry is used in the case where the geometryType property returns JointProfileGeometry, JointPlanarBRepFaceGeometry, JointBetweenTwoFacesGeometry or JointByTwoEdgeIntersectionGeometry.

### geometryType : JointGeometryTypes [read-only]
Returns the type of geometry this JointGeometry object represents.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### keyPointType : JointKeyPointTypes [read-only]
Returns the keypoint type this JointGeometry is using.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### origin : Point3D [read-only]
Returns the origin point that's been calculated for this joint geometry.

### planeOne : Base [read-only]
Returns the first plane for joint geometry that is defined between two planes. Returns null in all other cases.

### planeTwo : Base [read-only]
Returns the second plane for joint geometry that is defined between two planes. Returns null in all other cases.

### primaryAxisVector : Vector3D [read-only]
Returns the direction of the primary axis that's been calculated for this joint geometry. Conceptually, this is the Z-axis of the computed coordinate system.

### secondaryAxisVector : Vector3D [read-only]
Returns the direction of the secondary axis that's been calculated for this joint geometry. Conceptually, this is the X-axis of the computed coordinate system.

### tangentFaceParamOne : double [read-only]
Returns the first tangent face parameter.

### tangentFaceParamTwo : double [read-only]
Returns the second tangent face parameter.

### tangentFaceType : JointTangentFaceTypes [read-only]
Returns the tangent face type this JointGeometry is using.

### thirdAxisVector : Vector3D [read-only]
Returns the direction of the third axis that's been calculated for this joint geometry. Conceptually, this is the Y-axis of the computed coordinate system.

## Samples
- **BallJointMotion API Sample**: Demonstrates creating a joint with ball joint motion
- **CylindricalJointMotion API Sample**: Demonstrates creating a joint with cylindrical joint motion.
- **Joint Origin Between Two Faces Sample**: Demonstrates creating a new Joint Origin between two planes.
- **Joint Origin Sample**: Demonstrates creating a new Joint Origin.
- **Joint API Sample**: Demonstrates creating a new joint.
- **Pin Slot Joint Motion API Sample**: Demonstrates creating a joint with pin slot joint motion
- **Planar Joint Motion API Sample**: Demonstrates creating a joint with planar joint motion
- **RevoluteJointMotion API Sample**: Demonstrates creating a joint with revolute joint motion.
- **SliderJointMotion API Sample**: Demonstrates creating a joint with slider joint motion.
