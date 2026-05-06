# DeriveFeatures
Namespace: adsk.fusion
Inherits: Base
Since: January 2026

Collection that provides access to all of the existing derive features in a component and supports the ability to create new derive features.

**Accessed from:** Features.deriveFeatures

## Methods

### add(input: DeriveFeatureInput) -> DeriveFeature
Creates a new derive feature.
- **input** (DeriveFeatureInput): A DeriveFeatureInput object that defines the desired derive. Use the createInput method to create a new DeriveFeatureInput object and then use methods on it to define the derive.
- **Returns** (DeriveFeature): Returns the newly created DeriveFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(sourceDesign: Design) -> DeriveFeatureInput
Creates a DeriveFeatureInput object. Use properties and methods on this object to define the derive you want to create and then use the Add method, passing in the DeriveFeatureInput object.
- **sourceDesign** (Design): The Design that will be derived.
- **Returns** (DeriveFeatureInput): Returns a DeriveFeatureInput or null if the creation failed.

### item(index: uinteger) -> DeriveFeature
Function that returns the specified derive feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (DeriveFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> DeriveFeature
Function that returns the specified derive feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (DeriveFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of derive features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
