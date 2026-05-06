# AsBuiltJoints
Namespace: adsk.fusion
Inherits: Base
Since: September 2015

The collection of as-built joints in this component. This provides access to all existing as-built joints and supports the ability to create new as-built joints.

**Accessed from:** Component.asBuiltJoints, FlatPatternComponent.asBuiltJoints

## Methods

### add(input: AsBuiltJointInput) -> AsBuiltJoint
Creates a new as-built joint.
- **input** (AsBuiltJointInput): An AsBuiltJointInput object that was created using the AsBuiltJoints.createInput method and then fully defined using the properties and methods on the AsBuiltJointInput object.
- **Returns** (AsBuiltJoint): Returns the new AsBuiltJoint object or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(occurrenceOne: Occurrence, occurrenceTwo: Occurrence, geometry: JointGeometry) -> AsBuiltJointInput
Creates an AsBuiltJointInput object which is used to collect all of the information needed to create an as-built joint. This object is equivalent to the as-built joint dialog in the user-interface in that it doesn't represent an actual joint but just the information needed to create an as-built joint. Once this is fully defined the add method can be called, passing this object in to create the actual joint.
- **occurrenceOne** (Occurrence): Specifies the first of two occurrences the joint is between.
- **occurrenceTwo** (Occurrence): Specifies the second of two occurrences the joint is between.
- **geometry** (JointGeometry): Specifies the geometry of where the joint will be positioned. If the as-built joint is a rigid joint, this argument should be null because no geometry is needed.
- **Returns** (AsBuiltJointInput): Returns the new AsBuiltJointInput object or null in the case of failure.

### item(index: uinteger) -> AsBuiltJoint
Function that returns the specified as-built joint using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (AsBuiltJoint): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> AsBuiltJoint
Function that returns the specified as-built joint using a name.
- **name** (string): The name of the item within the collection to return.
- **Returns** (AsBuiltJoint): Returns the specified item or null if an invalid name was specified.

## Properties

### count : uinteger [read-only]
Returns number of joint origins in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **As-Built Joint Sample**: Demonstrates creating a new As-Built Joint.
