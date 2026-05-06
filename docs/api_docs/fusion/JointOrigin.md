# JointOrigin
Namespace: adsk.fusion
Inherits: Base
Since: September 2015

Represents an existing joint origin in a design.

**Accessed from:** Component.allJointOrigins, FlatPatternComponent.allJointOrigins, JointOrigin.createForAssemblyContext, JointOrigin.nativeObject, JointOriginList.item, JointOriginList.itemByName, JointOrigins.add, JointOrigins.item, JointOrigins.itemByName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> JointOrigin
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (JointOrigin): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes this joint origin.
- **Returns** (boolean): Returns true if successful.

## Properties

### angle : ModelParameter [read-only]
Gets the parameter that controls the angle. The value can be changed using the functionality of the returned ModelParameter object.

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this joint origin.

### entityToken : string [read-only]
Returns a token for the JointOrigin object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same joint origin.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### geometry : JointGeometry [read-write]
Gets and sets the joint geometry for this joint origin input. This defines the location of the joint origin.

To set this property, you need to position the timeline marker to immediately before this joint. This can be accomplished using the following code: joint.timelineObject.rollTo(True)

### isFlipped : boolean [read-write]
Gets and sets if the joint origin direction is flipped or not.

To set this property, you need to position the timeline marker to immediately before this joint. This can be accomplished using the following code: joint.timelineObject.rollTo(True)

### isLightBulbOn : boolean [read-write]
Gets and sets if the light bulb of this jointOrigin as displayed in the browser is on or off. A joint origin will only be visible if the light bulb is switched on. However, the light bulb can be on and the joint origin still invisible if a higher level occurrence in the assembly context is not visible because its light bulb is off or the joint origins folder light bulb is off.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets and sets the name of this joint origin. This is the name seen by the user in the timeline.

### nativeObject : JointOrigin [read-only]
The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### offsetX : ModelParameter [read-only]
Gets the parameter that controls the X offset direction. The value can be changed using the functionality of the returned ModelParameter object.

### offsetY : ModelParameter [read-only]
Gets the parameter that controls the Y offset direction. The value can be changed using the functionality of the returned ModelParameter object.

### offsetZ : ModelParameter [read-only]
Gets the parameter that controls the Z offset direction. The value can be changed using the functionality of the returned ModelParameter object.

### parentComponent : Component [read-only]
Returns the parent component that owns this joint origin.

### primaryAxisVector : Vector3D [read-only]
Returns the direction of the primary axis that's been calculated for this joint origin. This is conceptually the Z axis as shown by the triad representing the joint origin.

### secondaryAxisVector : Vector3D [read-only]
Returns the direction of the secondary axis that's been calculated for this joint origin. This is conceptually the X axis as shown by the triad representing the joint origin.

### thirdAxisVector : Vector3D [read-only]
Returns the direction of the third axis that's been calculated for this joint origin. This is conceptually the Y axis as shown by the triad representing the joint origin.

### timelineObject : TimelineObject [read-only]
Returns the timeline object associated with this joint origin.

### transform : Matrix3D [read-only]
Returns the position and orientation of the joint geometry associated with this joint origin. This is returned as a 3D matrix which provides the origin and the X, Y, and Z axis vectors of the coordinate system.

This property is especially useful in cases where the JointGeometry cannot be obtained. This can happen when the model has been modified in a way where the geometry used to create the joint is no longer available.

### xAxisEntity : Base [read-write]
Gets and sets the entity that defines the X axis direction. This defaults to null meaning the X axis is inferred from the input geometry.

To set this property, you need to position the timeline marker to immediately before this joint. This can be accomplished using the following code: joint.timelineObject.rollTo(True)

### zAxisEntity : Base [read-write]
Gets and sets the entity that defines the Z axis direction. This defaults to null meaning the Z axis is inferred from the input geometry.

To set this property, you need to position the timeline marker to immediately before this joint. This can be accomplished using the following code: joint.timelineObject.rollTo(True)

## Samples
- **Joint Origin Between Two Faces Sample**: Demonstrates creating a new Joint Origin between two planes.
- **Joint Origin Sample**: Demonstrates creating a new Joint Origin.
