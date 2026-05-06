# Joints
Namespace: adsk.fusion
Inherits: Base
Since: July 2015

The collection of joints in this component. This provides access to all existing joints and supports the ability to create new joints.

**Accessed from:** Component.joints, FlatPatternComponent.joints

## Methods

### add(input: JointInput) -> Joint
Creates a new joint.
- **input** (JointInput): The JointInput object that defines the geometry and various inputs that fully define a joint. A JointInput object is created using the Joints.createInput method.
- **Returns** (Joint): Returns the newly created Joint or null in the case of failure.

### addInferredJoint(input: InferredJointInput) -> Joint
Creates a new inferred joint.
- **input** (InferredJointInput): The InferredJointInput object that defines the pairs of geometry and other settings that Fusion will use to infer a joint from. An InferredJointInput object is created using the Joints.createInferredJointInput method.
- **Returns** (Joint): Returns the newly created Joint or fails if there is bad input.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInferredJointInput() -> InferredJointInput
Creates a joint input to define an inferred joint. Use functionality on the returned InferredJointInput to define the input needed to infer a joint.
- **Returns** (InferredJointInput): Returns an InferredJointInput.

### createInput(geometryOrOriginOne: Base, geometryOrOriginTwo: Base) -> JointInput
Creates a JointInput object, which is the API equivalent to the Joint command dialog. You you use methods and properties on the returned class to set the desired options, similar to providing input and setting options in the Joint command dialog. Once the settings are defined you call the Joints.add method passing in the JointInput object to create the actual joint.
- **geometryOrOriginOne** (Base): A JointGeometry or JointOrigin object that defines the first set of geometry of the joint. JointGeometry objects are created by using the various static methods on the JointGeometry class and JointOrigin objects are created through the JointOrigins object.
- **geometryOrOriginTwo** (Base): A JointGeometry or JointOrigin object that defines the second set of geometry of the joint. JointGeometry objects are created by using the various static methods on the JointGeometry class and JointOrigin objects are created through the JointOrigins object.
- **Returns** (JointInput): Returns the JointInput object or null if the creation failed.

### item(index: uinteger) -> Joint
Function that returns the specified joint using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Joint): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> Joint
Function that returns the specified joint using a name.
- **name** (string): The name of the item within the collection to return.
- **Returns** (Joint): Returns the specified item or null if an invalid name was specified.

## Properties

### count : uinteger [read-only]
Returns number of joints in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **BallJointMotion API Sample**: Demonstrates creating a joint with ball joint motion
- **CylindricalJointMotion API Sample**: Demonstrates creating a joint with cylindrical joint motion.
- **Joint API Sample**: Demonstrates creating a new joint.
- **Pin Slot Joint Motion API Sample**: Demonstrates creating a joint with pin slot joint motion
- **Planar Joint Motion API Sample**: Demonstrates creating a joint with planar joint motion
- **RevoluteJointMotion API Sample**: Demonstrates creating a joint with revolute joint motion.
- **SliderJointMotion API Sample**: Demonstrates creating a joint with slider joint motion.
