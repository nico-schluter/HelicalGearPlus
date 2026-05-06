# ReplaceFaceFeatures
Namespace: adsk.fusion
Inherits: Base
Since: March 2015

Collection that provides access to all of the existing replace face features in a component and supports the ability to create new replace face features.

**Accessed from:** Features.replaceFaceFeatures

## Methods

### add(input: ReplaceFaceFeatureInput) -> ReplaceFaceFeature
Creates a new replace face feature.
- **input** (ReplaceFaceFeatureInput): A ReplaceFaceFeatureInput object that defines the desired replace face. Use the createInput method to create a new ReplaceFaceFeatureInput object and then use methods on it (the ReplaceFaceFeatureInput object) to define the replace face.
- **Returns** (ReplaceFaceFeature): Returns the newly created ReplaceFaceFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(sourceFaces: ObjectCollection, isTangentChain: boolean, targetFaces: Base) -> ReplaceFaceFeatureInput
Creates a ReplaceFaceFeatureInput object. Use properties and methods on this object to define the replace face you want to create and then use the Add method, passing in the ReplaceFaceFeatureInput object.
- **sourceFaces** (ObjectCollection): Input the entities that define the source faces (the faces to be replaced). The collection can contain the faces from a solid and/or features. All the faces must be on the same body.
- **isTangentChain** (boolean): A boolean value for setting whether or not faces that are tangentially connected to the input faces (if any) will also be included. A value of true indicates that tangent faces will be included.
- **targetFaces** (Base): Input the entities that define the target faces. The new faces must completely intersect the part. The collection can contain the surface faces, surface bodies and construction planes.
- **Returns** (ReplaceFaceFeatureInput): Returns the newly created ReplaceFaceFeatureInput object or null if the creation failed.

### item(index: uinteger) -> ReplaceFaceFeature
Function that returns the specified replace face feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ReplaceFaceFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> ReplaceFaceFeature
Function that returns the specified replace face feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (ReplaceFaceFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of replace face features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **ReplaceFace Feature**: Demonstrates creating a new replaceface feature.
