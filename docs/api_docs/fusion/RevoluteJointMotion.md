# RevoluteJointMotion
Namespace: adsk.fusion
Inherits: JointMotion
Since: July 2015

Represents the set of information specific to a revolute joint.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### customRotationAxisEntity : Base [read-write]
This property can be set using various types of entities that can infer an axis. For example, a linear edge, sketch line, planar face, and cylindrical face. This property is only valid in the case where the rotationAxis property returns CustomJointDirection. Setting this property will automatically set the rotationAxis property to CustomJointDirection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### jointType : JointTypes [read-only]
Returns an enum value indicating the type of joint this joint represents.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### rotationAxis : JointDirections [read-write]
Gets and sets the direction of the axis of rotation. This can be set to XAxisJointDirection, YAxisJointDirection, or ZAxisJointDirection. It can return those three directions and CustomJointDirection. If this returns CustomJointDirection then the customRotationAxisEntity will return an entity that defines the axis. If there is a custom rotation axis defined and this property is set to one of the three standard axes, the custom rotation will be removed and customRotationAxisEntity will return null.

### rotationAxisVector : Vector3D [read-only]
Returns the direction of the rotation axis. This property will return null in the case where the RevolutionJointMotion object was obtained from a JointInput object.

### rotationLimits : JointLimits [read-only]
Returns a JointLimits object that defines the rotation limits for this joint. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits.

### rotationValue : double [read-write]
Gets and sets the rotation value. This is in radians. Setting this value is the equivalent of using the Drive Joints command.

## Samples
- **RevoluteJointMotion API Sample**: Demonstrates creating a joint with revolute joint motion.
