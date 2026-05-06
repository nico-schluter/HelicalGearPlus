# MotionLinks
Namespace: adsk.fusion
Inherits: Base
Since: November 2025

The collection of MotionLinks in this component. This provides access to all existing MotionLinks and supports the ability to create new MotionLinks.

**Accessed from:** Component.motionLinks, FlatPatternComponent.motionLinks

## Methods

### add(input: MotionLinkInput) -> MotionLink
Creates a new MotionLink.
- **input** (MotionLinkInput): The MotionLinkInput object that defines various inputs that fully define a MotionLink. A MotionLinkInput object is created using the MotionLinks.createInput method.
- **Returns** (MotionLink): Returns the newly created MotionLink or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(jointOne: Base, jointTwo: Base) -> MotionLinkInput
Creates a MotionLinkInput object, which is the API equivalent to the Motion Link command dialog. You can use methods and properties on the returned object to set the desired options, similar to providing input and setting options in the MotionLink command dialog. Once the settings are defined you call the MotionLinks.add method passing in the MotionLinkInput object to create the actual MotionLink.
- **jointOne** (Base): Inputs the first Joint or AsBuiltJoint to link its motion(s). If the jointTwo is set to null, then two motions from the jointOne will be linked, and in this case a valid Joint or AsBuiltJoint for jointOne should have its joint motion type of BallJointType, CylindricalJointType, PinSlotJointType or PlanarJointType. A Joint or AsBuiltJoint whose joint motion is a RigidJointMotion type is never valid as the first joint.
- **jointTwo** (Base): Inputs the second Joint or AsBuiltJoint to link its motion. If this is set to null, then the two motions from the jointOne will be linked. A Joint or AsBuiltJoint whose joint motion is a RigidJointMotion type is never valid as the second joint.

This is an optional argument whose default value is null.
- **Returns** (MotionLinkInput): Returns the MotionLinkInput object or null if the creation failed.

### item(index: uinteger) -> MotionLink
Function that returns the specified MotionLink using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (MotionLink): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> MotionLink
Function that returns the specified MotionLink using a name.
- **name** (string): The name of the item within the collection to return.
- **Returns** (MotionLink): Returns the specified item or null if an invalid name was specified.

## Properties

### count : uinteger [read-only]
Returns number of MotionLinks in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
