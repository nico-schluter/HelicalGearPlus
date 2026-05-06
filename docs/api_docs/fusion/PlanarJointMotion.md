# PlanarJointMotion
Namespace: adsk.fusion
Inherits: JointMotion
Since: July 2015

Represents the set of information specific to a planar joint.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### customNormalDirectionEntity : Base [read-write]
This property defines a custom normal direction and can be set using various types of entities that can infer a direction. For example, a linear edge, sketch line, planar face, and cylindrical face.This property is only valid in the case where the normalDirection property returns CustomJointDirection. Setting this property will automatically set the normalDirection property to CustomJointDirection.

To set this property, you need to position the timeline marker to immediately before this joint. This can be accomplished using the following code: thisJoint.timelineObject.rollTo(True)

### customPrimarySlideDirectionEntity : Base [read-write]
This property can be set using various types of entities that can infer a direction. For example, a linear edge, sketch line, planar face, and cylindrical face. When reading this property, it is only valid in the case where the primarySlideDirection property returns CustomJointDirection. Setting this property will automatically set the primarySlideDirection property to CustomJointDirection. The entity defining the custom direction by be perpendicular to the normal direction.

To set this property, you need to position the timeline marker to immediately before this joint. This can be accomplished using the following code: thisJoint.timelineObject.rollTo(True)

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### jointType : JointTypes [read-only]
Returns an enum value indicating the type of joint this joint represents.

### normalDirection : JointDirections [read-write]
Gets and sets the direction of the normal of the single degree of rotation. This can be set to XAxisJointDirection, YAxisJointDirection, or ZAxisJointDirection. It can return those three directions and CustomJointDirection. If this returns CustomJointDirection then the customNormalDirectionEntity will return an entity that defines the direction. If there is a custom direction defined and this property is set to one of the three standard axes, the custom direction will be removed and customNormalDirectionEntity will return null.

### normalDirectionVector : Vector3D [read-only]
Returns the direction of the normal direction. This property will return null in the case where the PlanarJointMotion object was obtained from a JointInput object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### primarySlideDirection : JointDirections [read-only]
Gets the direction used as the primary direction for the two translational degrees of freedom. The value of this property is automatically set when setting the normalDirection. When reading this value it can return XAxisJointDirection, YAxisJointDirection, ZAxisJointDirection, or CustomJointDirection. If it's CustomJointDirection then the direction the direction can be determined using the primarySlideDirectionVector and the entity controlling the direction can be get and set using the customPrimarySlideDirectionEntity.

### primarySlideDirectionVector : Vector3D [read-only]
Returns the direction of the primary slide direction. This property will return null in the case where the PlanarJointMotion object was obtained from a JointInput object.

### primarySlideLimits : JointLimits [read-only]
Returns a JointLimits object that defines the limits in the primary direction for this joint. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits.

### primarySlideValue : double [read-write]
Gets and sets the offset value in the primary direction. This is in centimeters. Setting this value is the equivalent of using the Drive Joints command.

### rotationLimits : JointLimits [read-only]
Returns a JointLimits object that defines the limits of rotation for this joint. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits.

### rotationValue : double [read-write]
Gets and sets the rotation value. This is in radians. Setting this value is the equivalent of using the Drive Joints command.

### secondarySlideDirectionVector : Vector3D [read-only]
Returns the direction of the secondary slide direction. This property will return null in the case where the PlanarJointMotion object was obtained from a JointInput object.

### secondarySlideLimits : JointLimits [read-only]
Returns a JointLimits object that defines the limits in the secondary direction for this joint. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits.

### secondarySlideValue : double [read-write]
Gets and sets the offset value in the secondary direction. This is in centimeters. Setting this value is the equivalent of using the Drive Joints command.

## Samples
- **Planar Joint Motion API Sample**: Demonstrates creating a joint with planar joint motion
