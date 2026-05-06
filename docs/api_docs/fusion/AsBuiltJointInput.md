# AsBuiltJointInput
Namespace: adsk.fusion
Inherits: Base
Since: September 2015

Defines all of the information needed to create an as-built joint.

**Accessed from:** AsBuiltJoints.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setAsBallJointMotion(pitchDirection: JointDirections, yawDirection: JointDirections, customPitchDirection: Base, customYawDirection: Base) -> boolean
Defines the relationship between the two joint geometries as a ball joint.
- **pitchDirection** (JointDirections): Defines the direction the pitch angle is measured from. This can be ZAxisJointDirection or CustomJointDirection. If CustomJointDirection is specified then you must also provide a value for the customPitchDirection argument.
- **yawDirection** (JointDirections): Defines the direction the yaw is measured from. This can be XAxisJointDirection or CustomJointDirection. If CustomJointDirection is specified then you must also provide a value for the customYawDirection argument.
- **customPitchDirection** (Base): If the pitchDirection argument is customPitchDirection this argument is used to define the direction the pitch angel is measured from. This can be several types of entities that can define a direction.

This is an optional argument whose default value is null.
- **customYawDirection** (Base): If the yawDirection argument is customPitchDirection this argument is used to define the direction the yaw angel is measured from. This can be several types of entities that can define a direction.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if the operation was successful.

### setAsCylindricalJointMotion(rotationAxis: JointDirections, customRotationAxisEntity: Base) -> boolean
Defines the relationship between the two joint geometries as a cylindrical joint.
- **rotationAxis** (JointDirections): Specifies which axis the rotation is around. If this is set to CustomJointDirection then the customRotationAxisEntity argument must also be provided.
- **customRotationAxisEntity** (Base): If the rotationAxis is customAxisEntity this argument is used to specify the entity that defines the custom axis of rotation. This can be several types of entities that an axis can be derived from.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if the operation was successful.

### setAsPinSlotJointMotion(rotationAxis: JointDirections, slideDirection: JointDirections, customRotationAxisEntity: Base, customSlideDirectionEntity: Base) -> boolean
Defines the relationship between the two joint geometries as a pin-slot joint.
- **rotationAxis** (JointDirections): Specifies which axis the rotation is around. If this is set to CustomJointDirection then the customRotationAxisEntity argument must also be provided.
- **slideDirection** (JointDirections): Specifies which axis the slide direction is along. If this is set to CustomJointDirection then the customSlideDirectionEntity argument must also be provided.
- **customRotationAxisEntity** (Base): If the rotationAxis is customAxisEntity this argument is used to specify the entity that defines the custom axis of rotation. This can be several types of entities that an axis can be derived

This is an optional argument whose default value is null.
- **customSlideDirectionEntity** (Base): If the slideDirection is CustomJointDirection this argument is used to specify the entity that defines the custom slide direction. This can be several types of entities that can define a direction.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if the operation was successful.

### setAsPlanarJointMotion(normalDirection: JointDirections, customNormalDirectionEntity: Base, customPrimarySlideDirection: Base) -> boolean
Defines the relationship between the two joint geometries as a planar joint.
- **normalDirection** (JointDirections): Defines the direction of the normal of the single degree of rotation. This can be set to XAxisJointDirection, YAxisJointDirection, ZAxisJointDirection, or CustomJointDirection. If set to CustomJointDirection then the customNormalDirectionEntity argument must also be provided.
- **customNormalDirectionEntity** (Base): If the normalDirection is CustomJointDirection this argument is used to specify the entity that defines the direction of the normal. This can be several types of entities that can define a direction.

This is an optional argument whose default value is null.
- **customPrimarySlideDirection** (Base): This arguments defines the direction of the primary slide direction. A default primary slide direction is automatically chosen and will be used if this argument is not provided or is null. The secondary slide direction is automatically inferred from the normal and primary slide directions.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if the operation was successful.

### setAsRevoluteJointMotion(rotationAxis: JointDirections, customRotationAxisEntity: Base) -> boolean
Defines the relationship between the two joint geometries as a revolute joint.
- **rotationAxis** (JointDirections): Specifies which axis the rotation is around. If this is set to CustomJointDirection then the customRotationAxisEntity argument must also be provided.
- **customRotationAxisEntity** (Base): If the rotationAxis is customAxisEntity this argument is used to specify the entity that defines the custom axis of rotation. This can be several types of entities that an axis can be derived from.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if the operation was successful.

### setAsRigidJointMotion() -> boolean
Defines the relationship between the two joint geometries as a rigid joint.
- **Returns** (boolean): Returns true if successful.

### setAsSliderJointMotion(sliderDirection: JointDirections, customSliderDirectionEntity: Base) -> boolean
Defines the relationship between the two joint geometries as a slider joint.
- **sliderDirection** (JointDirections): Specifies which axis the slide direction is along. If this is set to CustomJointDirection then the customSliderDirectionEntity argument must also be provided.
- **customSliderDirectionEntity** (Base): If the sliderDirection is CustomJointDirection this argument is used to specify the entity that defines the custom slider direction. This can be several types of entities that can define a direction.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if the operation was successful.

## Properties

### geometry : JointGeometry [read-write]
Specifies the position of the joint.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### jointMotion : JointMotion [read-only]
Returns one of the objects derived from JointMotion that defines how the motion between the two joint geometries is defined. Can be null if the motion hasn't yet been defined.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### occurrenceOne : Occurrence [read-write]
Specifies the first of two occurrences the joint is between.

### occurrenceTwo : Occurrence [read-write]
Specifies the second of two occurrences the joint is between.

## Samples
- **As-Built Joint Sample**: Demonstrates creating a new As-Built Joint.
