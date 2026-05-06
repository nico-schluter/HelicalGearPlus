# JointOrigins
Namespace: adsk.fusion
Inherits: Base
Since: September 2015

The collection of joint origins in this component. This provides access to all existing joint origins and supports the ability to create new joint origins.

**Accessed from:** Component.jointOrigins, FlatPatternComponent.jointOrigins

## Methods

### add(input: JointOriginInput) -> JointOrigin
Create a new joint origin.
- **input** (JointOriginInput): A JointOriginInput object that full defines all of the information needed to create a joint origin. You create a JointOriginInput by using the createInput method of the JointOrigins object.
- **Returns** (JointOrigin): Returns a JointOrigin object if successfully created and null if it fails.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(geometry: JointGeometry) -> JointOriginInput
Creates a JointOriginInput object which is used to collect all of the information needed to create a simple joint origin. The creation of the input object takes the required input as the geometry argument and you can optionally use methods and properties on the created JointOriginInput to set other optional settings. The JointOrigin is created by calling the add method of the JointOrigins object and passing it the JointOriginInput object.
- **geometry** (JointGeometry): A JointGeometry object that defines the geometry the joint origin will be created on.
- **Returns** (JointOriginInput): Returns a JointOriginInput object if successfully created and null if it fails.

### item(index: uinteger) -> JointOrigin
Function that returns the specified joint origin using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (JointOrigin): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> JointOrigin
Function that returns the specified joint origin using a name.
- **name** (string): The name of the item within the collection to return.
- **Returns** (JointOrigin): Returns the specified item or null if an invalid name was specified.

## Properties

### count : uinteger [read-only]
Returns number of joint origins in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Joint Origin Between Two Faces Sample**: Demonstrates creating a new Joint Origin between two planes.
- **Joint Origin Sample**: Demonstrates creating a new Joint Origin.
