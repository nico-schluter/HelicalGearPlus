# RipFeatures
Namespace: adsk.fusion
Inherits: Base
Since: September 2023

Collection that provides access to all of the existing Rip features in a design.

**Accessed from:** Features.ripFeatures

## Methods

### add(input: RipFeatureInput) -> RipFeature
Creates a new Rip feature.
- **input** (RipFeatureInput): A RipFeatureInput object that defines the desired rip. Use the createInput method to create a new RipFeatureInput object and then use methods on it (the RipFeatureInput object) to define the rip.
- **Returns** (RipFeature): Returns the newly created RipFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createRipFeatureInput() -> RipFeatureInput
Creates a RipFeatureInput object. Use methods on this object to define the rip you want to create and then use the add method, passing in the RipFeatureInput object.
- **Returns** (RipFeatureInput): Returns the newly created RipFeatureInput object or null if the creation failed.

### item(index: uinteger) -> RipFeature
Function that returns the specified Rip feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (RipFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> RipFeature
Function that returns the specified Rip feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (RipFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of Rip features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Rip Feature Sample**: Demonstrates creating a new sheet metal rip feature.
