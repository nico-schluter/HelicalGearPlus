# SliderJointMotion
Namespace: adsk.fusion
Inherits: JointMotion
Since: July 2015

Represents the set of information specific to a slider joint.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### customSlideDirectionEntity : Base [read-write]
This property can be set using various types of entities that can infer a direction. For example, a linear edge, sketch line, planar face, and cylindrical face. This property is only valid in the case where the slideDirection property returns CustomJointDirection. Setting this property will automatically set the slideDirection property to CustomJointDirection.

To set this property, you need to position the timeline marker to immediately before this joint. This can be accomplished using the following code: thisJoint.timelineObject.rollTo(True)

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### jointType : JointTypes [read-only]
Returns an enum value indicating the type of joint this joint represents.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### slideDirection : JointDirections [read-write]
Gets and sets the direction of the slide. This can be set to XAxisJointDirection, YAxisJointDirection, or ZAxisJointDirection. It can return those three directions and CustomJointDirection. If this returns CustomJointDirection then the customSlideDirectionEntity will return an entity that defines the direction. If there is a custom direction defined and this property is set to one of the three standard axes, the custom direction will be removed and customSlideDirectionEntity will return null.

### slideDirectionVector : Vector3D [read-only]
Returns the direction of the slide. This property will return null in the case where the SliderJointMotion object was obtained from a JointInput object.

### slideLimits : JointLimits [read-only]
Returns a JointLimits object that defines the slide limits for this joint. Use the functionality of the returned JointLimits object to get, set, and modify the joint limits.

### slideValue : double [read-write]
Gets and sets the slide value. This is in centimeters. Setting this value is the equivalent of using the Drive Joints command.

## Samples
- **SliderJointMotion API Sample**: Demonstrates creating a joint with slider joint motion.
