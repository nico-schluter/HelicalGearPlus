# PipeFeatures
Namespace: adsk.fusion
Inherits: Base
Since: September 2015

Collection that provides access to all of the existing Pipe features in a design.

**Accessed from:** Features.pipeFeatures

## Methods

### add(input: PipeFeatureInput) -> PipeFeature
Creates a new Pipe feature.
- **input** (PipeFeatureInput): A PipeFeatureInput object that defines the desired Pipe. Use the createInput method to create a new PipeFeatureInput object and then use methods on it (the PipeFeatureInput object) to define the Pipe.
- **Returns** (PipeFeature): Returns the newly created PipeFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(path: Path, operation: FeatureOperations) -> PipeFeatureInput
Creates a PipeFeatureInput object for defining a simple Pipe feature with only a path. Use properties and methods on this object to define the Pipe you want to create and then use the Add method, passing in the PipeFeatureInput object.
- **path** (Path): The path to create the Pipe.
- **operation** (FeatureOperations): The feature operation to perform.
- **Returns** (PipeFeatureInput): Returns the newly created PipeFeatureInput object or null if the creation failed.

### item(index: uinteger) -> PipeFeature
Function that returns the specified Pipe feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (PipeFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> PipeFeature
Function that returns the specified Pipe feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (PipeFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of Pipe features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
