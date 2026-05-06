# MeshRemoveFeatures
Namespace: adsk.fusion
Inherits: Base
Since: November 2025

Collection that provides access to all of the existing mesh remove features in a component and supports the ability to create new mesh remove features.

**Accessed from:** Features.meshRemoveFeatures

## Methods

### add(input: MeshRemoveFeatureInput) -> MeshRemoveFeature
Creates a mesh remove feature. Works only in parametric mode.
- **input** (MeshRemoveFeatureInput): A MeshRemoveFeatureInput object that defines the desired mesh remove feature. Use the createInput method to create a new MeshRemoveFeatureInput object and then use methods on it (the MeshRemoveFeatureInput object) to define the removal.
- **Returns** (MeshRemoveFeature): When successfull, a MeshRemoveFeature is created for each MeshBody that was input. An array of the created MeshRemoveFeature objects is returned.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(inputBodies: MeshBody[]) -> MeshRemoveFeatureInput
Creates a MeshRemoveFeatureInput object. Use properties and methods on this object to define the mesh remove feature you want to create and then use the add method, passing in the MeshRemoveFeatureInput object.
- **inputBodies** (MeshBody[]): A array with mesh bodies in a parametric design.
- **Returns** (MeshRemoveFeatureInput): Returns the newly created MeshRemoveFeatureInput object or null if the creation failed.

### item(index: uinteger) -> MeshRemoveFeature
Function that returns the specified mesh remove feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (MeshRemoveFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> MeshRemoveFeature
Function that returns the specified mesh remove feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (MeshRemoveFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of mesh remove features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
