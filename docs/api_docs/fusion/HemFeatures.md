# HemFeatures
Namespace: adsk.fusion
Inherits: Base
Since: September 2025

Collection that provides access to all of the existing hem features in a design and supports the ability to create new hem features.

**Accessed from:** Features.hemFeatures

## Methods

### add(input: HemFeatureInput) -> HemFeature
Creates a new Hem feature.
- **input** (HemFeatureInput): A HemFeatureInput object that defines the desired hem. Use the createInput method to create a new HemFeatureInput object and then use methods on it (the HemFeatureInput object) to define the hem.
- **Returns** (HemFeature): Returns the newly created HemFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createHemFeatureInput() -> HemFeatureInput
Creates a HemFeatureInput object. Use methods on this object to define the hem you want to create and then use the add method, passing in the HemFeatureInput object.
- **Returns** (HemFeatureInput): Returns the newly created HemFeatureInput object or null if the creation failed.

### item(index: uinteger) -> HemFeature
Function that returns the specified hem feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (HemFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> HemFeature
Function that returns the specified hem feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (HemFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of hem features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Hem Feature Sample**: Demonstrates creating a new sheet metal hem feature.
