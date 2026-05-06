# LoftFeatures
Namespace: adsk.fusion
Inherits: Base
Since: September 2015

Collection that provides access to all of the existing loft features in a design.

**Accessed from:** Features.loftFeatures

## Methods

### add(input: LoftFeatureInput) -> LoftFeature
Creates a new loft feature.
- **input** (LoftFeatureInput): A LoftFeatureInput object that defines the desired loft feature. Use the createInput method to create a new LoftFeatureInput object and then use methods on it (the LoftFeatureInput object) to define the required input.
- **Returns** (LoftFeature): Returns the newly created LoftFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(operation: FeatureOperations) -> LoftFeatureInput
Creates a LoftFeatureInput object. Use properties and methods on the returned LoftFeatureInput object to provide the required input to create a loft feature. The LoftFeatureInput object can then be used as input to the add method to create the loft feature.
- **operation** (FeatureOperations): The feature operation to perform.
- **Returns** (LoftFeatureInput): Returns the newly created LoftFeatureInput object or null if the creation failed.

### item(index: uinteger) -> LoftFeature
Function that returns the specified loft feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (LoftFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> LoftFeature
Function that returns the specified loft feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (LoftFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of loft features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Loft Feature API Sample**: Demonstrates creating a new loft feature.
