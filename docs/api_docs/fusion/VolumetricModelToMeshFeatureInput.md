# VolumetricModelToMeshFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: May 2025

An input object for creating a volumetric model to mesh feature.

**Accessed from:** VolumetricModelToMeshFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### elementSize : ValueInput [read-write]
Gets and sets the element size to be used when creating the mesh. This value is only used when the RefinementType is set to Custom. The value must be greater than 0. The default is equivalent to the Low refinement type and is dependent on the size of the model.

### isComputeSuspended : boolean [read-write]
Gets and sets if the feature compute should be suspended if a dependent entity changes. Default is false. If true, the feature will need to be recomputed manually if a dependent entity changes. The default is false.

### isSmallShellsRemoved : boolean [read-write]
Gets and sets if small mesh shells should be removed after creating the mesh. The default is false.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVolumetricModelRemoved : boolean [read-write]
Gets and sets if the volumetric model should be removed after creating the mesh. the default is true.

### meshingApproach : VolumetricMeshingApproachTypes [read-write]
Gets and sets the meshing approach to be used when creating the mesh. The default is VolumetricMeshingAdvancedType.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### refinementType : VolumetricMeshRefinementTypes [read-write]
Gets and sets the refinement type to be used when creating the mesh. The default is Low.

### smallShellThreshold : ValueInput [read-write]
Gets and Sets the small mesh threshold used to determine if a mesh shell is considered small. The value is a fraction of the total mesh area and must be between 0 and 1. The default is 0.02.

### volumetricModel : Base [read-write]
Gets and sets the volumetric model to be converted to a mesh. The volumetric model must have the same parent component as the VolumetricModelToMeshFeature.This property is typed as core.Base because the adsk.fusion library does not reference the volume library where the VolumetricModel object is defined. At runtime, this property will return a VolumetricModel object.

## Samples
- **Volumetric Custom Feature API Sample**: Demonstrates how to create a Volumetric Custom Feature using the API for graph creation.


To run the sample script, have a document open in Fusion’s DESIGN workspace. This script will create a component with a box by sketching then extruding that sketch. It will then use that box as a boundary body and create a Volumetric Custom Feature.


The script will the create a gyroid lattice using the Volumetric Model API with the appropriate Graphs, Nodes and Connections for a minimal example. Finally, the script will convert that Volumetric Model to Mesh using the API and the VolumetricModelToMeshFeature.
