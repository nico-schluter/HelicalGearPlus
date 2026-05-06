# ThickenFeatures
Namespace: adsk.fusion
Inherits: Base
Since: June 2015

Collection that provides access to all of the existing Thicken features in a component and supports the ability to create new Thicken features.

**Accessed from:** Features.thickenFeatures

## Methods

### add(input: ThickenFeatureInput) -> ThickenFeature
Creates a new Thicken feature.
- **input** (ThickenFeatureInput): A FeatureInput object that defines the desired Thicken feature. Use the createInput method to create a new ThickenFeatureInput object and then use methods on it (the ThickenFeatureInput object) to define the Thicken feature.
- **Returns** (ThickenFeature): Returns the newly created ThickenFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(inputFaces: ObjectCollection, thickness: ValueInput, isSymmetric: boolean, operation: FeatureOperations, isChainSelection: boolean) -> ThickenFeatureInput
Creates a ThickenFeatureInput object. Use properties and methods on this object to define the Thicken feature you want to create and then use the Add method, passing in the ThickenFeatureInput object to create the feature.
- **inputFaces** (ObjectCollection): The faces or patch bodies to thicken. Faces need not be from the same component or body, nor do they need to be connected or touching one another.
- **thickness** (ValueInput): ValueInput object that defines the thickness.
- **isSymmetric** (boolean): A boolean value for setting whether to add thickness symmetrically or only on one side of the face/s to thicken
- **operation** (FeatureOperations): The feature operation to perform.
- **isChainSelection** (boolean): A boolean value for setting whether or not faces that are tangentially connected to the input faces (if any) will be included in the thicken. The default value is true.

This is an optional argument whose default value is True.
- **Returns** (ThickenFeatureInput): Returns the newly created ThickenFeatureInput object or null if the creation failed.

### item(index: uinteger) -> ThickenFeature
Function that returns the specified Thicken feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ThickenFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> ThickenFeature
Function that returns the specified thicken feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (ThickenFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of Thicken features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Thicken Feature API Sample**: Demonstrates creating a new thiken feature.
