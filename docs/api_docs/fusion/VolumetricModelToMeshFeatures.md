# VolumetricModelToMeshFeatures
Namespace: adsk.fusion
Inherits: Base
Since: May 2025

Collection that provides access to all of the existing volumetric model to mesh features in a component and supports the ability to create new Volumetric Model To Mesh features.

**Accessed from:** Features.volumetricModelToMeshFeatures

## Methods

### add(input: VolumetricModelToMeshFeatureInput) -> VolumetricModelToMeshFeature
Add a new volumetric model to mesh feature. To create a new volumetric model to mesh feature use the createInput function to create a new input object and use the methods and proprties on that object to define the required input for an volumetric model to mesh feature. Once the information is defined on the input object you can pass it to the Add method to create the Volumetric Model to Mesh.
- **input** (VolumetricModelToMeshFeatureInput): The input object for creating a volumetric model to mesh feature.
- **Returns** (VolumetricModelToMeshFeature): The newly added volumetric model to mesh feature.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(volumetricModel: Base) -> VolumetricModelToMeshFeatureInput
Create a new VolumetricModelToMeshFeatureInput object.
- **volumetricModel** (Base): The volumetric model to be converted to a mesh. Must have the same parent component as the VolumetricModelToMeshFeatures. This property is typed as core.Base because the adsk.fusion library does not reference the volume library where the VolumetricModel object is defined. At runtime, this property will return a VolumetricModel object.
- **Returns** (VolumetricModelToMeshFeatureInput): Returns the newly created VolumetricModelToMeshFeatureInput object or null if the creation failed.

### item(index: uinteger) -> VolumetricModelToMeshFeature
Function that returns the specified item using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (VolumetricModelToMeshFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> VolumetricModelToMeshFeature
Returns the item with the specified name.
- **name** (string): The name of the item.
- **Returns** (VolumetricModelToMeshFeature): Returns the specified item or null in the case where there is no item with the specified name.

## Properties

### count : uinteger [read-only]
The number of features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Volumetric Custom Feature API Sample**: Demonstrates how to create a Volumetric Custom Feature using the API for graph creation.


To run the sample script, have a document open in Fusion’s DESIGN workspace. This script will create a component with a box by sketching then extruding that sketch. It will then use that box as a boundary body and create a Volumetric Custom Feature.


The script will the create a gyroid lattice using the Volumetric Model API with the appropriate Graphs, Nodes and Connections for a minimal example. Finally, the script will convert that Volumetric Model to Mesh using the API and the VolumetricModelToMeshFeature.
