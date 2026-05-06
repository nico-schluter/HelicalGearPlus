# BossFeatures
Namespace: adsk.fusion
Inherits: Base
Since: October 2022

Collection that provides access to all of the existing boss features in a design.

**Accessed from:** Features.bossFeatures

## Methods

### add(input: BossFeatureInput) -> BossFeature
Creates a new boss feature (or more boss features) based on the information provided by a BossFeatureInput object. To create a new boss or boss connection, use createInput function to define a new input object for the type of boss feature you want to create. Use the methods and properties on the input object to define any additional inputs. Once the information is defined on the input object, you can pass it to the Add method to create the boss feature or boss connection.
- **input** (BossFeatureInput): The BossFeatureInput object that defines the boss or boss connection you want to create.
- **Returns** (BossFeature): Returns the newly created BossFeature objects or empty vector/list if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput() -> BossFeatureInput
Creates a new BossFeatureInput object that is used to specify the input needed to create a new boss feature(s).
- **Returns** (BossFeatureInput): Returns the newly created BossFeatureInput object or null if the creation failed.

### item(index: uinteger) -> BossFeature
Function that returns the specified boss feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (BossFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> BossFeature
Function that returns the specified boss feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (BossFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of boss features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Boss Feature Sample**: Demonstrates creating a new boss feature
