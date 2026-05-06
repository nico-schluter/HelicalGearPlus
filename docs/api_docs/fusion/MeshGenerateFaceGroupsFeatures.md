# MeshGenerateFaceGroupsFeatures
Namespace: adsk.fusion
Inherits: Base
Since: January 2025

Collection that provides access to all of the existing mesh generate face groups features in a component and supports the ability to create new mesh generate face groups features.

**Accessed from:** Features.meshGenerateFaceGroupsFeatures

## Methods

### add(input: MeshGenerateFaceGroupsFeatureInput) -> MeshGenerateFaceGroupsFeature
Creates a mesh generate face groups feature.
- **input** (MeshGenerateFaceGroupsFeatureInput): A MeshGenerateFaceGroupsFeatureInput object that defines the desired generate face groups feature. Use the createInput method to create a new MeshGenerateFaceGroupsFeatureInput object and then use methods on it (the MeshGenerateFaceGroupsFeatureInput object) to define the generate face groups feature.
- **Returns** (MeshGenerateFaceGroupsFeature): Returns the newly created MeshGenerateFaceGroupsFeatureInput object or null if the creation failed. Returns nothing in the case where the feature is non-parametric.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(mesh: Base) -> MeshGenerateFaceGroupsFeatureInput
Creates a MeshGenerateFaceGroupsFeatureInput object. Use properties and methods on this object to define the mesh generate face groups feature you want to create and then use the add method, passing in the MeshGenerateFaceGroupsFeatureInput object.
- **mesh** (Base): A MeshBody in either a parametric or direct modeling design.
- **Returns** (MeshGenerateFaceGroupsFeatureInput): Returns the newly created MeshGenerateFaceGroupsFeatureInput object or null if the creation failed.

### item(index: uinteger) -> MeshGenerateFaceGroupsFeature
Function that returns the specified mesh generate face groups feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (MeshGenerateFaceGroupsFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> MeshGenerateFaceGroupsFeature
Function that returns the specified MeshGenerateFaceGroups feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (MeshGenerateFaceGroupsFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of mesh generate face groups features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
