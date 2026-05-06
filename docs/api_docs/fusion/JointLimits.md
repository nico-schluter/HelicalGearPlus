# JointLimits
Namespace: adsk.fusion
Inherits: Base
Since: July 2015

Used to define limits for the range of motion of a joint.

**Accessed from:** BallJointMotion.pitchLimits, BallJointMotion.rollLimits, BallJointMotion.yawLimits, CylindricalJointMotion.rotationLimits, CylindricalJointMotion.slideLimits, PinSlotJointMotion.rotationLimits, PinSlotJointMotion.slideLimits, PlanarJointMotion.primarySlideLimits, PlanarJointMotion.rotationLimits, PlanarJointMotion.secondarySlideLimits, RevoluteJointMotion.rotationLimits, SliderJointMotion.slideLimits

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isMaximumValueEnabled : boolean [read-write]
Gets and sets whether the maximum joint limit is enabled or not.

### isMinimumValueEnabled : boolean [read-write]
Gets and sets whether the minimum joint limit is enabled or not.

### isRestValueEnabled : boolean [read-write]
Gets and sets whether the resting joint value is enabled or not.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maximumValue : double [read-write]
The maximum value of the value. This is in either centimeters or radians depending on if the joint value this is associated with defines a distance or an angle.

### minimumValue : double [read-write]
The minimum value of the value. This is in either centimeters or radians depending on if the joint value this is associated with defines a distance or an angle.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### restValue : double [read-write]
The resting state value. This is in either centimeters or radians depending on if the joint value this is associated with defines a distance or an angle.

## Samples
- **BallJointMotion API Sample**: Demonstrates creating a joint with ball joint motion
- **CylindricalJointMotion API Sample**: Demonstrates creating a joint with cylindrical joint motion.
- **Pin Slot Joint Motion API Sample**: Demonstrates creating a joint with pin slot joint motion
- **Planar Joint Motion API Sample**: Demonstrates creating a joint with planar joint motion
- **RevoluteJointMotion API Sample**: Demonstrates creating a joint with revolute joint motion.
- **SliderJointMotion API Sample**: Demonstrates creating a joint with slider joint motion.
