# BoundaryFillFeatures
Namespace: adsk.fusion
Inherits: Base
Since: June 2015

Collection that provides access to all of the existing boundary fill features in a component and supports the ability to create new boundary fill features.

**Accessed from:** Features.boundaryFillFeatures

## Methods

### add(input: BoundaryFillFeatureInput) -> BoundaryFillFeature
Creates a new boundary fill feature.
- **input** (BoundaryFillFeatureInput): A BoundaryFillFeatureInput object that defines the desired boundary fill feature. Use the createInput method to create a new BoundaryFillFeatureInput object and then use methods on it (the BoundaryFillFeatureInput object) to define the boundary fill feature.
- **Returns** (BoundaryFillFeature): Returns the newly created BoundaryFillFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(tools: ObjectCollection, operation: FeatureOperations) -> BoundaryFillFeatureInput
Creates a BoundaryFillFeatureInput object. Use properties and methods on this object to define the boundary fill you want to create and then use the Add method, passing in the BoundaryFillFeatureInput object.

To determine the possible boundaries and allow you to choose which cells to keep, the boundary fill feature does a partial compute when the input object is created. To do this it starts a boundary fill feature transaction and completes the transaction when you call the add method. If you don't call the add method to finish the transaction it leaves Fusion in a bad state and there will be undo problems and possibly a crash. If you have created a BoundFillFeatureInput object and don't want to finish the feature creation, you need to call the cancel method on the BoundaryFillFeatureInput object to safely abort the current boundary fill transaction.
- **tools** (ObjectCollection): A collection of one or more construction planes and open or closed BRepBody objects that will be used in calculating the possible closed boundaries.
- **operation** (FeatureOperations): The operation type to perform.
- **Returns** (BoundaryFillFeatureInput): Returns the newly created BoundaryFillFeatureInput object or null if the creation failed.

### item(index: uinteger) -> BoundaryFillFeature
Function that returns the specified boundary fill feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (BoundaryFillFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> BoundaryFillFeature
Function that returns the specified boundary fill feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (BoundaryFillFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of boundary fill features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Boundary Fill Feature API Sample**: Demonstrates creating a new boundary fill feature.
