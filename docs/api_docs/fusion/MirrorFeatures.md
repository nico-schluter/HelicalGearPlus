# MirrorFeatures
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

Collection that provides access to all of the existing mirror features in a component and supports the ability to create new mirror features.

**Accessed from:** Features.mirrorFeatures

## Methods

### add(input: MirrorFeatureInput) -> MirrorFeature
Creates a new mirror feature.
- **input** (MirrorFeatureInput): A MirrorFeatureInput object that defines the desired mirror. Use the createInput method to create a new MirrorFeatureInput object and then use methods on it (the MirrorFeatureInput object) to define the mirror.
- **Returns** (MirrorFeature): Returns the newly created MirrorFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(inputEntities: ObjectCollection, mirrorPlane: Base) -> MirrorFeatureInput
Creates a MirrorFeatureInput object. Use properties and methods on this object to define the mirror you want to create and then use the Add method, passing in the MirrorFeatureInput object.
- **inputEntities** (ObjectCollection): A collection of the entities to mirror. It can contain faces, features, bodies, or components. The input must all be of a single type. For example, you can't provide a body and a component but the collection must be either all bodies or all components.
- **mirrorPlane** (Base): Input planar entity that defines the mirror plane. This can be either a planar face or a construction plane.
- **Returns** (MirrorFeatureInput): Returns the newly created MirrorFeatureInput object or null if the creation failed.

### item(index: uinteger) -> MirrorFeature
Function that returns the specified mirror feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (MirrorFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> MirrorFeature
Function that returns the specified mirror feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (MirrorFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of mirror features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Mirror Feature API Sample**: Demonstrates creating a new mirror feature
