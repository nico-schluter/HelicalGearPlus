# BallJointMotion
Namespace: adsk.fusion
Inherits: JointMotion
Since: July 2015

Represents the set of information specific to a ball joint.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### customPitchDirectionEntity : Base [read-write]
This property defines a custom pitch direction and can be set using various types of entities that can infer a direction. For example, a linear edge, sketch line, planar face, and cylindrical face.This property is only valid in the case where the pitchDirection property returns CustomJointDirection. Setting this property will automatically set the pitchDirection property to CustomJointDirection.

To set this property, you need to position the timeline marker to immediately before this joint. This can be accomplished using the following code: thisJoint.timelineObject.rollTo(True)

### customYawDirectionEntity : Base [read-write]
This property defines a custom yaw direction and can be set using various types of entities that can infer a direction. For example, a linear edge, sketch line, planar face, and cylindrical face.This property is only valid in the case where the yawDirection property returns CustomJointDirection. Setting this property will automatically set the yawDirection property to CustomJointDirection.

To set this property, you need to position the timeline marker to immediately before this joint. This can be accomplished using the following code: thisJoint.timelineObject.rollTo(True)

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### jointType : JointTypes [read-only]
Returns an enum value indicating the type of joint this joint represents.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### pitchDirection : JointDirections [read-write]
Gets and sets the direction that the pitch is measured from. This can only be set to ZAxisJointDirection and can return ZAxisJointDirection or CustomJointDirection. If this returns CustomJointDirection then the customNormalDirectionEntity will return an entity that defines the direction. If there is a custom direction defined and this property is set to ZAxisJointDirection, the custom direction will be removed and customNormalDirectionEntity will return null.

### pitchDirectionVector : Vector3D [read-only]
Returns the direction that the pitch angle is measured from. This property will return null in the case where the BallJointMotion object was obtained from a JointInput object.

### pitchLimits : JointLimits [read-only]
Returns a JointLimits object that defines the limits of rotation for the pitch. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits.

### pitchValue : double [read-write]
Gets and sets the pitch value. This is in radians. Setting this value is the equivalent of using the Drive Joints command.

### rollDirectionVector : Vector3D [read-only]
Returns the direction that the roll angle is measured from. This property will return null in the case where the BallJointMotion object was obtained from a JointInput object.

### rollLimits : JointLimits [read-only]
Returns a JointLimits object that defines the limits of rotation for the roll. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits.

### rollValue : double [read-write]
Gets and sets the roll value. This is in radians. Setting this value is the equivalent of using the Drive Joints command.

### yawDirection : JointDirections [read-write]
Gets and sets the direction that the pitch is measured from. This can only be set to XAxisJointDirection and can return XAxisJointDirection or CustomJointDirection. If this returns CustomJointDirection then the customYawDirectionEntity will return an entity that defines the direction. If there is a custom direction defined and this property is set to XAxisJointDirection, the custom direction will be removed and customYawDirectionEntity will return null.

### yawDirectionVector : Vector3D [read-only]
Returns the direction that the yaw angle is measured from. This property will return null in the case where the BallJointMotion object was obtained from a JointInput object.

### yawLimits : JointLimits [read-only]
Returns a JointLimits object that defines the limits of rotation for the yaw. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits.

### yawValue : double [read-write]
Gets and sets the yaw value. This is in radians. Setting this value is the equivalent of using the Drive Joints command.

## Samples
- **BallJointMotion API Sample**: Demonstrates creating a joint with ball joint motion
