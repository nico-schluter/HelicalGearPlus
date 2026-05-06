# DraftFeatures
Namespace: adsk.fusion
Inherits: Base
Since: January 2015

Collection that provides access to all of the existing draft features in a component and supports the ability to create new draft features.

**Accessed from:** Features.draftFeatures

## Methods

### add(input: DraftFeatureInput) -> DraftFeature
Creates a new draft feature.
- **input** (DraftFeatureInput): A DraftFeatureInput object that defines the desired draft. Use the createInput method to create a new DraftFeatureInput object and then use methods on it (the DraftFeatureInput object) to define the draft.
- **Returns** (DraftFeature): Returns the newly created DraftFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(inputFaces: BRepFace[], plane: Base, isTangentChain: boolean) -> DraftFeatureInput
Creates a DraftFeatureInput object. Use properties and methods on this object to define the draft you want to create and then use the Add method, passing in the DraftFeatureInput object.
- **inputFaces** (BRepFace[]): BRepFace array that contains the faces to which draft will be applied. The picked point on face is always the point returned from pointOnFace property of the first BRepFace in this collection.
- **plane** (Base): Input object that defines the direction in which the draft is applied. This can be a planar BrepFace, or a ConstructionPlane.
- **isTangentChain** (boolean): A boolean value for setting whether or not faces that are tangentially connected to any of the input faces (if any) will also be included. It defaults to true.

This is an optional argument whose default value is True.
- **Returns** (DraftFeatureInput): Returns the newly created DraftFeatureInput object or null if the creation failed.

### item(index: uinteger) -> DraftFeature
Function that returns the specified draft feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (DraftFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> DraftFeature
Function that returns the specified draft feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (DraftFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of draft features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Draft Feature API Sample**: Demonstrates creating a new draft feature.
