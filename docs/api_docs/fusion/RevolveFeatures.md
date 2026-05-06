# RevolveFeatures
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Collection that provides access to all of the existing revolve features in a design and supports the ability to create new revolve features.

**Accessed from:** Features.revolveFeatures

## Methods

### add(input: RevolveFeatureInput) -> RevolveFeature
Creates a new revolve feature based on the information provided by the provided RevolveFeatureInput object. To create a new revolve, use the createInput function to create a new input object and then use the methods and properties on that object to define the required input for a revolve. Once the information is defined on the input object you can pass it to the Add method to create the revolve.
- **input** (RevolveFeatureInput): The RevolveFeatureInput object that specifies the input needed to create a new extrude
- **Returns** (RevolveFeature): Returns the newly created RevolveFeature or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(profile: Base, axis: Base, operation: FeatureOperations) -> RevolveFeatureInput
Creates a new RevolveFeatureInput object that is used to specify the input needed to create a new revolve feature.
- **profile** (Base): The profile argument can be a single Profile, a single planar face, or an ObjectCollection consisting of multiple profiles and planar faces. When an ObjectCollection is used all of the profiles and faces must be co-planar.

To create a surface (non-solid) revolution, you can use the createOpenProfile and createBRepEdgeProfile methods of the Component object to create an open profile. You also need to set the isSolid property of the returned RevolveFeatureInput property to False.
- **axis** (Base): The axis can be a sketch line, construction axis, linear edge or a face that defines an axis (cylinder, cone, torus, etc.). If it is not in the same plane as the profile, it is projected onto the profile plane.
- **operation** (FeatureOperations): The operation type to perform.
- **Returns** (RevolveFeatureInput): Returns the newly created RevolveFeatureInput object or null if the creation failed.

### item(index: uinteger) -> RevolveFeature
Function that returns the specified revolve feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (RevolveFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> RevolveFeature
Function that returns the specified revolve feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (RevolveFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of revolve features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Simple Revolve Feature Sample**: Creates a new revolve feature, resulting in a new component.
