# AsBuiltJoint
Namespace: adsk.fusion
Inherits: Base
Since: September 2015

Represent an as-built joint.

**Accessed from:** AsBuiltJoint.createForAssemblyContext, AsBuiltJoint.nativeObject, AsBuiltJointList.item, AsBuiltJointList.itemByName, AsBuiltJoints.add, AsBuiltJoints.item, AsBuiltJoints.itemByName, Component.allAsBuiltJoints, FlatPatternComponent.allAsBuiltJoints

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> AsBuiltJoint
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (AsBuiltJoint): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes this as-built joint.
- **Returns** (boolean): Returns true if the delete was successful.

### setAsBallJointMotion(pitchDirection: JointDirections, yawDirection: JointDirections, geometry: JointGeometry, customPitchDirection: Base, customYawDirection: Base) -> boolean
Redefines the relationship between the two joint geometries as a ball joint.

To use this method, you need to position the timeline marker to immediately before this as-built joint. This can be accomplished using the following code: thisAsBuiltJoint.timelineObject.rollTo(True)
- **pitchDirection** (JointDirections): Defines the direction the pitch angle is measured from. This can be ZAxisJointDirection or CustomJointDirection. If CustomJointDirection is specified then you must also provide a value for the customPitchDirection argument.
- **yawDirection** (JointDirections): Defines the direction the yaw is measured from. This can be XAxisJointDirection or CustomJointDirection. If CustomJointDirection is specified then you must also provide a value for the customYawDirection argument.
- **geometry** (JointGeometry): Redefines the joint geometry. If not provided, the existing geometry is used. This argument is required if the current joint motion is rigid.

This is an optional argument whose default value is null.
- **customPitchDirection** (Base): If the pitchDirection argument is customPitchDirection this argument is used to define the direction the pitch angel is measured from. This can be several types of entities that can define a direction.

This is an optional argument whose default value is null.
- **customYawDirection** (Base): If the yawDirection argument is customPitchDirection this argument is used to define the direction the yaw angel is measured from. This can be several types of entities that can define a direction.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if the operation was successful.

### setAsCylindricalJointMotion(rotationAxis: JointDirections, geometry: JointGeometry, customRotationAxisEntity: Base) -> boolean
Redefines the relationship between the two joint geometries as a cylindrical joint.

To use this method, you need to position the timeline marker to immediately before this as-built joint. This can be accomplished using the following code: thisAsBuiltJoint.timelineObject.rollTo(True)
- **rotationAxis** (JointDirections): Specifies which axis the rotation is around. If this is set to CustomJointDirection then the customRotationAxisEntity argument must also be provided.
- **geometry** (JointGeometry): Redefines the joint geometry. If not provided, the existing geometry is used. This argument is required if the current joint motion is rigid.

This is an optional argument whose default value is null.
- **customRotationAxisEntity** (Base): If the rotationAxis is customAxisEntity this argument is used to specify the entity that defines the custom axis of rotation. This can be several types of entities that an axis can be derived from.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if the operation was successful.

### setAsPinSlotJointMotion(rotationAxis: JointDirections, slideDirection: JointDirections, geometry: JointGeometry, customRotationAxisEntity: Base, customSlideDirectionEntity: Base) -> boolean
Redefines the relationship between the two joint geometries as a pin-slot joint.

To use this method, you need to position the timeline marker to immediately before this as-built joint. This can be accomplished using the following code: thisAsBuiltJoint.timelineObject.rollTo(True)
- **rotationAxis** (JointDirections): Specifies which axis the rotation is around. If this is set to CustomJointDirection then the customRotationAxisEntity argument must also be provided.
- **slideDirection** (JointDirections): Specifies which axis the slide direction is along. If this is set to CustomJointDirection then the customSlideDirectionEntity argument must also be provided.
- **geometry** (JointGeometry): Redefines the joint geometry. If not provided, the existing geometry is used. This argument is required if the current joint motion is rigid.

This is an optional argument whose default value is null.
- **customRotationAxisEntity** (Base): If the rotationAxis is customAxisEntity this argument is used to specify the entity that defines the custom axis of rotation. This can be several types of entities that an axis can be derived

This is an optional argument whose default value is null.
- **customSlideDirectionEntity** (Base): If the slideDirection is CustomJointDirection this argument is used to specify the entity that defines the custom slide direction. This can be several types of entities that can define a direction.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if the operation was successful.

### setAsPlanarJointMotion(normalDirection: JointDirections, geometry: JointGeometry, customNormalDirectionEntity: Base, customPrimarySlideDirection: Base) -> boolean
Redefines the relationship between the two joint geometries as a planar joint.

To use this method, you need to position the timeline marker to immediately before this as-built joint. This can be accomplished using the following code: thisAsBuiltJoint.timelineObject.rollTo(True)
- **normalDirection** (JointDirections): Defines the direction of the normal of the single degree of rotation. This can be set to XAxisJointDirection, YAxisJointDirection, ZAxisJointDirection, or CustomJointDirection. If set to CustomJointDirection then the customNormalDirectionEntity argument must also be provided.
- **geometry** (JointGeometry): Redefines the joint geometry. If not provided, the existing geometry is used. This argument is required if the current joint motion is rigid.

This is an optional argument whose default value is null.
- **customNormalDirectionEntity** (Base): If the normalDirection is CustomJointDirection this argument is used to specify the entity that defines the direction of the normal. This can be several types of entities that can define a direction.

This is an optional argument whose default value is null.
- **customPrimarySlideDirection** (Base): This arguments defines the direction of the primary slide direction. A default primary slide direction is automatically chosen and will be used if this argument is not provided or is null. The secondary slide direction is automatically inferred from the normal and primary slide directions.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if the operation was successful.

### setAsRevoluteJointMotion(rotationAxis: JointDirections, geometry: JointGeometry, customRotationAxisEntity: Base) -> boolean
Redefines the relationship between the two joint geometries as a revolute joint.

To use this method, you need to position the timeline marker to immediately before this as-built joint. This can be accomplished using the following code: thisAsBuiltJoint.timelineObject.rollTo(True)
- **rotationAxis** (JointDirections): Specifies which axis the rotation is around. If this is set to CustomJointDirection then the customRotationAxisEntity argument must also be provided.
- **geometry** (JointGeometry): Redefines the joint geometry. If not provided, the existing geometry is used. This argument is required if the current joint motion is rigid.

This is an optional argument whose default value is null.
- **customRotationAxisEntity** (Base): If the rotationAxis is customAxisEntity this argument is used to specify the entity that defines the custom axis of rotation. This can be several types of entities that an axis can be derived from.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if the operation was successful.

### setAsRigidJointMotion() -> boolean
Redefines the relationship between the two joint geometries as a rigid joint.

To use this method, you need to position the timeline marker to immediately before this as-built joint. This can be accomplished using the following code: thisAsBuiltJoint.timelineObject.rollTo(True)
- **Returns** (boolean): Returns true if successful.

### setAsSliderJointMotion(sliderDirection: JointDirections, geometry: JointGeometry, customSliderDirectionEntity: Base) -> boolean
Redefines the relationship between the two joint geometries as a slider joint.

To use this method, you need to position the timeline marker to immediately before this as-built joint. This can be accomplished using the following code: thisAsBuiltJoint.timelineObject.rollTo(True)
- **sliderDirection** (JointDirections): Specifies which axis the slide direction is along. If this is set to CustomJointDirection then the customSliderDirectionEntity argument must also be provided.
- **geometry** (JointGeometry): Redefines the joint geometry. If not provided, the existing geometry is used. This argument is required if the current joint motion is rigid.

This is an optional argument whose default value is null.
- **customSliderDirectionEntity** (Base): If the sliderDirection is CustomJointDirection this argument is used to specify the entity that defines the custom slider direction. This can be several types of entities that can define a direction.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if the operation was successful.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this as-built joint.

### entityToken : string [read-only]
Returns a token for the AsBuiltJoint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same as-built joint.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### geometry : JointGeometry [read-write]
Specifies the position of the joint. Getting this property will return null and setting it will be ignored in the case where the joint motion is rigid.

To set this property, you need to position the timeline marker to immediately before this as-built joint. This can be accomplished using the following code: thisAsBuiltJoint.timelineObject.rollTo(True)

### isLightBulbOn : boolean [read-write]
Gets and sets if the light bulb of this as-built joint as displayed in the browser is on or off. A joint will only be visible if the light bulb is switched on. However, the light bulb can be on and the joint still invisible if a higher level occurrence in the assembly context is not visible because its light bulb is off or the joints folder is light bulb is off.

### isSuppressed : boolean [read-write]
Gets and sets if this as-built joint is suppressed.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-only]
Gets whether the as-built joint is visible. To change the visibility see the isLightBulbOn property. This property is affected by the assembly context.

### jointMotion : JointMotion [read-only]
Returns a JointMotion object that defines the motion relationship between the two geometries.

### motionLinks : array [read-only]
Returns the MotionLink objects that this joint is involved in.

### name : string [read-write]
The name of the as-built joint as it is displayed in the timeline and the browser. The name can be changed.

### nativeObject : AsBuiltJoint [read-only]
The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### occurrenceOne : Occurrence [read-only]
Specifies the first of two occurrences the joint is between.

### occurrenceTwo : Occurrence [read-only]
Specifies the second of two occurrences the joint is between.

### parentComponent : Component [read-only]
Returns the parent component that owns this AsBuiltJoint.

### timelineObject : TimelineObject [read-only]
Returns the timeline object associated with this as-built joint.

### transform : Matrix3D [read-only]
Returns the position and orientation of the joint geometry associated with this as-built joint. This is returned as a 3D matrix which provides the origin and the X, Y, and Z axis vectors of the coordinate system.

This property is especially useful in cases where the JointGeometry cannot be obtained. This can happen when the model has been modified in a way where the geometry used to create the joint is no longer available.

## Samples
- **As-Built Joint Sample**: Demonstrates creating a new As-Built Joint.
