# MeshConvertFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: July 2025

This class defines the methods and properties that pertain to the definition of a mesh convert feature.

**Accessed from:** MeshConvertFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### inputBodies : array [read-write]
Gets and sets the input meshes.

### isPreprocessHoles : boolean [read-write]
Smooths the boundaries of open holes in the mesh body. Improves the chance of successful conversion by refining the shape of holes that will remain open. Default value is false. Only valid if meshConvertMethodType is OrganicMeshConvertType.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### meshConvertAccuracyType : MeshConvertAccuracyTypes [read-write]
Gets and sets the accuracy of organic mesh convert, default value is MediumMeshConvertResolutionType. Only valid if meshConvertResolutionType is ByAccuracyMeshConvertResolutionType.

### meshConvertMethodType : MeshConvertMethodTypes [read-write]
Gets and sets the convert type of mesh convert, default value is FacetedMeshConvertMethodType.

### meshConvertOperationType : MeshConvertOperationTypes [read-write]
Gets and sets the operation type of mesh convert, default value is ParametricFeatureMeshConvertOperationType.

### meshConvertResolutionType : MeshConvertResolutionTypes [read-write]
Gets and sets the resolution method of mesh convert, default value is ByAccuracyMeshConvertResolutionType. Only valid if meshConvertMethodType is OrganicMeshConvertMethodType.

### numberOfFaces : ValueInput [read-write]
Specify the number of faces to generate for the converted body. Only valid if meshConvertResolutionType is ByFacetNumberMeshConvertResolutionType.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.
