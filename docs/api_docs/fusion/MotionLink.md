# MotionLink
Namespace: adsk.fusion
Inherits: Base
Since: November 2025

A MotionLink in a design.

**Accessed from:** AsBuiltJoint.motionLinks, Joint.motionLinks, MotionLink.createForAssemblyContext, MotionLink.nativeObject, MotionLinks.add, MotionLinks.item, MotionLinks.itemByName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> MotionLink
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (MotionLink): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes this MotionLink.
- **Returns** (boolean): Returns true if the delete is successful.

### setMotionData(motionOne: JointMotionTypes, valueOne: ValueInput, motionTwo: JointMotionTypes, valueTwo: ValueInput, isReversed: boolean) -> boolean
Method that sets the motion data.
- **motionOne** (JointMotionTypes): Specifies the first motion to link.
- **valueOne** (ValueInput): Specifies the first motion link value. If the ValueInput uses a real then it is interpreted as centimeters for length and radians for angle. If it is a string then the units can be defined as part of the string (i.e. "2 in" or "60 deg") or if no units are specified it is interpreted using the current default units for length or angle.
- **motionTwo** (JointMotionTypes): Specifies the second motion to link.
- **valueTwo** (ValueInput): Specifies the second motion link value. If the ValueInput uses a real then it is interpreted as centimeters for length and radians for angle. If it is a string then the units can be defined as part of the string (i.e. "2 in" or "60 deg") or if no units are specified it is interpreted using the current default units for length or angle.
- **isReversed** (boolean): Optional argument that specifies whether to reverse the direction of the motion.

This is an optional argument whose default value is False.
- **Returns** (boolean): Returns true if successful.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this MotionLink.

### entityToken : string [read-only]
Returns a token for the MotionLink object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same MotionLink.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### errorOrWarningMessage : string [read-only]
Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string.

### healthState : FeatureHealthStates [read-only]
Returns the current health state of the MotionLink.

### isReversed : boolean [read-write]
Gets and sets whether the motion is reversed or not.

### isSuppressed : boolean [read-write]
Gets and sets if this MotionLink is suppressed.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### jointOne : Base [read-only]
Gets the first joint for this MotionLink.

### jointTwo : Base [read-only]
Gets the second joint for this MotionLink. This can return null if the linked motions are from the same joint.

### motionOne : JointMotionTypes [read-only]
Gets the first motion type.

### motionTwo : JointMotionTypes [read-only]
Gets the second motion type.

### name : string [read-write]
Gets and sets the name of the MotionLink.

### nativeObject : MotionLink [read-only]
The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentComponent : Component [read-only]
Returns the parent component that owns this MotionLink.

### timelineObject : TimelineObject [read-only]
Returns the timeline object associated with this MotionLink.

### valueOne : ModelParameter [read-only]
Returns the ModelParameter for the first motion link value.

### valueTwo : ModelParameter [read-only]
Returns the ModelParameter for the second motion link value.
