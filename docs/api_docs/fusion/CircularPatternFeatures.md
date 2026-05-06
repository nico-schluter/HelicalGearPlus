# CircularPatternFeatures
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

Collection that provides access to all of the existing circular pattern features in a component and supports the ability to create new circular pattern features.

**Accessed from:** Features.circularPatternFeatures

## Methods

### add(input: CircularPatternFeatureInput) -> CircularPatternFeature
Creates a new circular pattern feature.
- **input** (CircularPatternFeatureInput): A CircularPatternFeatureInput object that defines the desired circular pattern. Use the createInput method to create a new CircularPatternFeatureInput object and then use methods on it (the CircularPatternFeatureInput object) to define the circular pattern.
- **Returns** (CircularPatternFeature): Returns the newly created CircularPatternFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(inputEntities: ObjectCollection, axis: Base) -> CircularPatternFeatureInput
Creates a CircularPatternFeatureInput object. Use properties and methods on this object to define the circular pattern you want to create and then use the Add method, passing in the CircularPatternFeatureInput object.
- **inputEntities** (ObjectCollection): The collection can contain faces, features, bodies or occurrences. All of the entities must be of a single type. For example, it can't contain features and occurrences but only features or occurrences.
- **axis** (Base): Input linear entity or the entity has axis that defines axis of circular pattern. This can be a sketch line, linear edge, construction axis, an edge/sketch curve that defines an axis (circle, etc.) or a face that defines an axis (cylinder, cone, torus, etc.).
- **Returns** (CircularPatternFeatureInput): Returns the newly created CircularPatternFeatureInput object or null if the creation failed.

### item(index: uinteger) -> CircularPatternFeature
Function that returns the specified circular pattern feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (CircularPatternFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> CircularPatternFeature
Function that returns the specified circular pattern feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (CircularPatternFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of circular pattern features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **CircularPattern Feature API Sample**: Demonstrates creating a new circular pattern feature.
