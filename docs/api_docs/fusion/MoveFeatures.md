# MoveFeatures
Namespace: adsk.fusion
Inherits: Base
Since: March 2015

Collection that provides access to all of the existing move features in a component and supports the ability to create new move features.

**Accessed from:** Features.moveFeatures

## Methods

### add(input: MoveFeatureInput) -> MoveFeature
Creates a new move feature.
- **input** (MoveFeatureInput): A MoveFeatureInput object that defines the desired move feature. Use the createInput2 method to create a new MoveFeatureInput object and then use methods on the MoveFeatureInput object to define the move feature.
- **Returns** (MoveFeature): Returns the newly created MoveFeature object or null if the creation failed. Returns nothing in the case where the feature is non-parametric.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(inputEntities: ObjectCollection, transform: Matrix3D) -> MoveFeatureInput
This function is retired. See more information in the 'Remarks' section below.

Creates a MoveFeatureInput object. Use properties and methods on this object to define the move feature you want to create and then use the Add method, passing in the MoveFeatureInput object.
- **inputEntities** (ObjectCollection): An ObjectCollection containing the entities to move. This collection can only contain BRepBody objects in parametric modeling. It can be BRep bodies, T-Spline bodies, mesh bodies mixed or faces and features mixed in non-parametric modeling.
- **transform** (Matrix3D): The transform to apply to the input entities. This can describe a move (translation) or a rotation. The matrix must define an orthogonal transform. That is the axes must be perpendicular to each other and there can't be any scaling or mirroring defined.
- **Returns** (MoveFeatureInput): Returns the newly created MoveFeatureInput object or null if the creation failed.

### createInput2(inputEntities: ObjectCollection) -> MoveFeatureInput
Creates a MoveFeatureInput object. Use properties and methods on this object to define how the move is defined and then use the MoveFeatues.add method, passing in the MoveFeatureInput object to create a move feature.
- **inputEntities** (ObjectCollection): An ObjectCollection containing the objects to move. For a parametric model, the collection can contain BRepBody or BRepFace objects but not a combination of both.
- **Returns** (MoveFeatureInput): Returns the newly created MoveFeatureInput object or null if the creation failed.

### item(index: uinteger) -> MoveFeature
Function that returns the specified move feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (MoveFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> MoveFeature
Function that returns the specified move feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (MoveFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of move features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Move Feature API Sample**: Demonstrates creating a new move feature.
