# MeshReduceFeatures
Namespace: adsk.fusion
Inherits: Base
Since: March 2024

Collection that provides access to all of the existing mesh reduce features in a component and supports the ability to create new mesh reduce features.

**Accessed from:** Features.meshReduceFeatures

## Methods

### add(input: MeshReduceFeatureInput) -> MeshReduceFeature
Creates a mesh reduce feature.
- **input** (MeshReduceFeatureInput): A MeshReduceFeatureInput object that defines the desired reduce feature. Use the createInput method to create a new MeshReduceFeatureInput object and then use methods on it (the MeshReduceFeatureInput object) to define the reduce.
- **Returns** (MeshReduceFeature): Returns the newly created MeshReduceFeatureInput object or null if the creation failed. Returns nothing in the case where the feature is non-parametric.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(mesh: Base) -> MeshReduceFeatureInput
Creates a MeshReduceFeatureInput object. Use properties and methods on this object to define the mesh reduce you want to create and then use the add method, passing in the MeshReduceFeatureInput object.
- **mesh** (Base): A MeshBody in either a parametric or direct modeling design.
- **Returns** (MeshReduceFeatureInput): Returns the newly created MeshReduceFeatureInput object or null if the creation failed.

### item(index: uinteger) -> MeshReduceFeature
Function that returns the specified mesh reduce feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (MeshReduceFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> MeshReduceFeature
Function that returns the specified MeshReduce feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (MeshReduceFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of mesh reduce features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
