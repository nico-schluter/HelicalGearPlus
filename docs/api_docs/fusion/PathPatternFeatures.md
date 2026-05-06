# PathPatternFeatures
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

Collection that provides access to all of the existing path pattern features in a component and supports the ability to create new path pattern features.

**Accessed from:** Features.pathPatternFeatures

## Methods

### add(input: PathPatternFeatureInput) -> PathPatternFeature
Creates a new path pattern feature.
- **input** (PathPatternFeatureInput): A PathPatternFeatureInput object that defines the desired path pattern. Use the createInput method to create a new PathPatternFeatureInput object and then use methods on it (the PathPatternFeatureInput object) to define the path pattern.
- **Returns** (PathPatternFeature): Returns the newly created PathPatternFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(inputEntities: ObjectCollection, path: Path, quantity: ValueInput, distance: ValueInput, patternDistanceType: PatternDistanceType) -> PathPatternFeatureInput
Creates a PathPatternFeatureInput object. Use properties and methods on this object to define the path pattern you want to create and then use the Add method, passing in the PathPatternFeatureInput object.
- **inputEntities** (ObjectCollection): The collection can contain faces, features, bodies or occurrences. All of the entities must be of a single type. For example, it can't contain features and occurrences but only features or occurrences.
- **path** (Path): The Path object that represents a single set of connected curves along which to drive the pattern.
- **quantity** (ValueInput): Specifies the number of instances in the first direction.
- **distance** (ValueInput): Specifies the distance. How this value is used depends on the value of the PatternDistanceType property. A negative value can be used to change the direction. If the value is ExtentPatternDistanceType then it defines the total distance of the pattern. If the value is SpacingPatternDistanceType then it defines the distance between each element.
- **patternDistanceType** (PatternDistanceType): Specifies how the distance between elements is computed.
- **Returns** (PathPatternFeatureInput): Returns the newly created PathPatternFeatureInput object or null if the creation failed.

### item(index: uinteger) -> PathPatternFeature
Function that returns the specified path pattern feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (PathPatternFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> PathPatternFeature
Function that returns the specified path pattern feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (PathPatternFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of path pattern features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Path Pattern Feature API Sample**: Demonstrates creating a new path pattern feature.
