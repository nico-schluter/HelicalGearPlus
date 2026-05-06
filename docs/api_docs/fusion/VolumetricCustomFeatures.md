# VolumetricCustomFeatures
Namespace: adsk.fusion
Inherits: Base
Since: May 2025

Collection that provides access to all of the existing volumetric custom features in a component and supports the ability to create new Volumetric Custom features.

**Accessed from:** Features.volumetricCustomFeatures

## Methods

### add(input: VolumetricCustomFeatureInput) -> VolumetricCustomFeature
Add a new volumetric custom feature. To create a new volumetric custom feature use the createInput method to create a new input object and use the methods and properties on that object to define the required input for a volumetric custom feature. Once the information is defined on the input object you can pass it to the add method to create the feature.
- **input** (VolumetricCustomFeatureInput): The input object for creating a volumetric custom feature.
- **Returns** (VolumetricCustomFeature): The newly added volumetric custom feature object or null if one cannot be added. Only one volumetric model can be added to each body.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(boundaryBody: Base) -> VolumetricCustomFeatureInput
Create a new VolumetricCustomFeatureInput object.
- **boundaryBody** (Base): The boundary body for the volumetric model. Must be a BRepBody or MeshBody. Must have the same parent component as the VolumetricCustomFeatures.
- **Returns** (VolumetricCustomFeatureInput): Returns the newly created VolumetricCustomFeatureInput object or null if the creation failed.

### item(index: uinteger) -> VolumetricCustomFeature
Function that returns the specified item using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (VolumetricCustomFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> VolumetricCustomFeature
Returns the item with the specified internal name.
- **name** (string): The name of the item.
- **Returns** (VolumetricCustomFeature): Returns the specified item or null in the case where there is no item with the specified name.

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
