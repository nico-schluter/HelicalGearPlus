# UntrimFeatures
Namespace: adsk.fusion
Inherits: Base
Since: January 2021

Collection that provides access to all of the existing Untrim features in a component and supports the ability to create new Untrim features.

**Accessed from:** Features.untrimFeatures

## Methods

### add(input: UntrimFeatureInput) -> UntrimFeature
Creates a new Untrim feature.
- **input** (UntrimFeatureInput): An UntrimFeatureInput object that defines the desired Untrim feature. Use the createInput method to create a new UntrimFeatureInput object and then use methods on it (the UntrimFeatureInput object) to define the desired options for the Untrim feature.
- **Returns** (UntrimFeature): Returns the newly created UntrimFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInputFromFaces(faces: BRepFace[], untrimLoopType: UntrimLoopTypes, extensionDistance: ValueInput) -> UntrimFeatureInput
Creates an UntrimFeatureInput object that defines the input needed to create an untrim feature. Use the input object to define the input to create the desired feature and then use the Add method, passing in the UntrimFeatureInput object.
- **faces** (BRepFace[]): An array of BRepFace objects that will have the loops of the specified type removed. Only loops that do not have a connected face can be removed (the edges in the loop have a single face). The array can only contain faces from surface bodies, (the isSolid property of the BRepBody returns false).
- **untrimLoopType** (UntrimLoopTypes): The loop type to be untrimmed (AllLoopUntrimType, InternalLoopUntrimType, or ExternalLoopUntrimType).
- **extensionDistance** (ValueInput): If the untrim loop type is AllLoopUntrimType or ExternalLoopUntrimType the untrimmed faces can be extended by a specified distance.

This is an optional argument whose default value is null.
- **Returns** (UntrimFeatureInput): Returns the newly created UntrimFeatureInput object or null if the creation failed.

### createInputFromLoops(loops: BRepLoop[], extensionDistance: ValueInput) -> UntrimFeatureInput
Creates an UntrimFeatureInput object that defines the input needed to create an untrim feature. Use the input object to define the input to create the desired feature and then use the Add method, passing in the UntrimFeatureInput object.
- **loops** (BRepLoop[]): Input the entities that define loops to remove. Only loops that do not have a connected face can be removed (the edges in the loop have a single face) The array can only contain loops from surface bodies, (the isSolid property of the BRepBody returns false).
- **extensionDistance** (ValueInput): If an external boundary is removed the untrimmed face can be extended by a specified distance.

This is an optional argument whose default value is null.
- **Returns** (UntrimFeatureInput): Returns the newly created UntrimFeatureInput object or null if the creation failed.

### item(index: uinteger) -> UntrimFeature
Function that returns the specified Untrim feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (UntrimFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> UntrimFeature
Function that returns the specified Untrim feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (UntrimFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of Untrim features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Untrim Feature API Sample**: Demonstrates creating a new untrim feature.
