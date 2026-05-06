# MeshSmoothFeatures
Namespace: adsk.fusion
Inherits: Base
Since: March 2024

Collection that provides access to all of the existing MeshSmooth features in a component and supports the ability to create new MeshSmooth features.

**Accessed from:** Features.meshSmoothFeatures

## Methods

### add(input: MeshSmoothFeatureInput) -> MeshSmoothFeature
Creates a mesh smooth feature.
- **input** (MeshSmoothFeatureInput): A MeshSmoothFeatureInput object that defines the desired MeshSmooth feature. Use the createInput method to create a new MeshSmoothFeatureInput object and then use methods on it (the MeshSmoothFeatureInput object) to define the smoothing.
- **Returns** (MeshSmoothFeature): Returns the newly created MeshSmoothFeature object or null if the creation failed. Returns nothing in the case where the feature is non-parametric.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(mesh: Base) -> MeshSmoothFeatureInput
Creates a MeshSmoothFeatureInput object. Use properties and methods on this object to define the mesh smooth you want to create and then use the add method, passing in the MeshSmoothFeatureInput object.
- **mesh** (Base): A MeshBody in either a parametric or direct modeling design.
- **Returns** (MeshSmoothFeatureInput): Returns the newly created MeshSmoothFeatureInput object or null if the creation failed.

### item(index: uinteger) -> MeshSmoothFeature
Function that returns the specified mesh smooth feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (MeshSmoothFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> MeshSmoothFeature
Function that returns the specified MeshSmooth feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (MeshSmoothFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of mesh smooth features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
