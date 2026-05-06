# MeshReverseNormalFeatures
Namespace: adsk.fusion
Inherits: Base
Since: July 2025

Collection that provides access to all of the existing MeshReverseNormal features in a component and supports the ability to create new MeshReverseNormal features.

**Accessed from:** Features.meshReverseNormalFeatures

## Methods

### add(input: MeshReverseNormalFeatureInput) -> MeshReverseNormalFeature
Creates a mesh reverse normal feature.
- **input** (MeshReverseNormalFeatureInput): A MeshReverseNormalFeatureInput object that defines the desired MeshReverseNormal feature. Use the createInput method to create a new MeshReverseNormalFeatureInput object and then use methods on it (the MeshReverseNormalFeatureInput object) to define the normal reversion.
- **Returns** (MeshReverseNormalFeature): Returns the newly created MeshReverseNormalFeature object or null if the creation failed. Returns nothing in the case where the feature is non-parametric.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(mesh: Base) -> MeshReverseNormalFeatureInput
Creates a MeshReverseNormalFeatureInput object. Use properties and methods on this object to define the mesh reverse normal you want to create and then use the add method, passing in the MeshReverseNormalFeatureInput object.
- **mesh** (Base): A mesh body or an object collection with face groups in either a parametric or direct modeling design.
- **Returns** (MeshReverseNormalFeatureInput): Returns the newly created MeshReverseNormalFeatureInput object or null if the creation failed.

### item(index: uinteger) -> MeshReverseNormalFeature
Function that returns the specified mesh reverse normal feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (MeshReverseNormalFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> MeshReverseNormalFeature
Function that returns the specified MeshReverseNormal feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (MeshReverseNormalFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of mesh reverse normal features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
