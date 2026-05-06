# SweepFeatures
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

Collection that provides access to all of the existing sweep features in a component and supports the ability to create new sweep features.

**Accessed from:** Features.sweepFeatures

## Methods

### add(input: SweepFeatureInput) -> SweepFeature
Creates a new sweep feature.
- **input** (SweepFeatureInput): A SweepFeatureInput object that defines the desired sweep. Use the createInput method to create a new SweepFeatureInput object and then use methods on it (the SweepFeatureInput object) to define the sweep.
- **Returns** (SweepFeature): Returns the newly created SweepFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(profile: Base, path: Path, operation: FeatureOperations) -> SweepFeatureInput
Creates a SweepFeatureInput object for defining a simple sweep feature with only a path and no guide rail or surface. Use properties and methods on this object to define the sweep you want to create and then use the Add method, passing in the SweepFeatureInput object.
- **profile** (Base): The profile argument can be a single Profile, a single planar face, or an ObjectCollection consisting of multiple profiles and planar faces. When an ObjectCollection is used all of the profiles and faces must be co-planar.
- **path** (Path): The path to create the sweep.
- **operation** (FeatureOperations): The feature operation to perform
- **Returns** (SweepFeatureInput): Returns the newly created SweepFeatureInput object or null if the creation failed.

### createInputForSolid(solidBody: BRepBody, path: Path, operation: FeatureOperations) -> SweepFeatureInput
Creates a SweepFeatureInput object for defining a simple sweep feature from a B-Rep solid with a path. Use properties and methods on this object to define the sweep you want to create, and then use the Add method, passing in the SweepFeatureInput object.
- **solidBody** (BRepBody): The BRepBody object to sweep. It must be a solid body.
- **path** (Path): The Path object that defines the path the body will be swept along.
- **operation** (FeatureOperations): The type of feature operation to perform.
- **Returns** (SweepFeatureInput): Returns the newly created SweepFeatureInput object or null if the creation fails.

### item(index: uinteger) -> SweepFeature
Function that returns the specified sweep feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SweepFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> SweepFeature
Function that returns the specified sweep feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (SweepFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of sweep features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Sweep Feature API Sample**: Demonstrates creating a new sweep feature.
- **Sweep with guide rail Feature API Sample**: Demonstrates creating a new Sweep feature that uses a guide rail along with a profile.
- **Two Rail Sweep Feature API Sample**: Demonstrates creating new two rail sweep feature.
