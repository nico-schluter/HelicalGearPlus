# MeshSeparateFeatures
Namespace: adsk.fusion
Inherits: Base
Since: July 2025

Collection that provides access to all of the existing MeshSeparate features in a component and supports the ability to create new MeshSeparate features.

**Accessed from:** Features.meshSeparateFeatures

## Methods

### add(input: MeshSeparateFeatureInput) -> MeshSeparateFeature
Creates a mesh separate feature.
- **input** (MeshSeparateFeatureInput): A MeshSeparateFeatureInput object that defines the desired MeshSeparate feature. Use the createInput method to create a new MeshSeparateFeatureInput object and then use methods on it (the MeshSeparateFeatureInput object) to define the separation.
- **Returns** (MeshSeparateFeature): Returns the newly created MeshSeparateFeature object or null if the creation failed. Returns nothing in the case where the feature is non-parametric.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(mesh: Base) -> MeshSeparateFeatureInput
Creates a MeshSeparateFeatureInput object. Use properties and methods on this object to define the mesh separate you want to create and then use the add method, passing in the MeshSeparateFeatureInput object.
- **mesh** (Base): A mesh body or an object collection with face groups in either a parametric or direct modeling design.
- **Returns** (MeshSeparateFeatureInput): Returns the newly created MeshSeparateFeatureInput object or null if the creation failed.

### item(index: uinteger) -> MeshSeparateFeature
Function that returns the specified mesh separate feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (MeshSeparateFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> MeshSeparateFeature
Function that returns the specified MeshSeparate feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (MeshSeparateFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of mesh separate features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
