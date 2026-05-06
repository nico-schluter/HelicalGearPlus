# ShellFeatures
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

Collection that provides access to all of the existing shell features in a component and supports the ability to create new shell features.

**Accessed from:** Features.shellFeatures

## Methods

### add(input: ShellFeatureInput) -> ShellFeature
Creates a new shell feature.
- **input** (ShellFeatureInput): A ShellFeatureInput object that defines the desired shell. Use the createInput method to create a new ShellFeatureInput object and then use methods on it (the ShellFeatureInput object) to define the shell.
- **Returns** (ShellFeature): Returns the newly created ShellFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(inputEntities: ObjectCollection, isTangentChain: boolean) -> ShellFeatureInput
Creates a ShellFeatureInput object. Use properties and methods on this object to define the shell you want to create and then use the Add method, passing in the ShellFeatureInput object.
- **inputEntities** (ObjectCollection): The collection contains the faces to remove and the bodies to perform shell. Fails if any faces are input, and the owning bodies of the faces are also input.
- **isTangentChain** (boolean): A boolean value for setting whether or not faces that are tangentially connected to the input faces (if any) will also be included. It defaults to true.

This is an optional argument whose default value is True.
- **Returns** (ShellFeatureInput): Returns the newly created ShellFeatureInput object or null if the creation failed.

### item(index: uinteger) -> ShellFeature
Function that returns the specified shell feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ShellFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> ShellFeature
Function that returns the specified shell feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (ShellFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of shell features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Shell Feature API Sample**: Demonstrates creating a new shell feature.
