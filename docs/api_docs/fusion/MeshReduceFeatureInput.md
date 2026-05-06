# MeshReduceFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: March 2024

This class defines the methods and properties that pertain to the definition of a mesh reduce feature.

**Accessed from:** MeshReduceFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### facecount : ValueInput [read-write]
Gets and sets the target face count for the reduced mesh as a target for the reduction. Only valid if meshReduceTargetType is FaceCountMeshReduceTargetType.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maximumDeviation : ValueInput [read-write]
Controls the maximum deviation of the reduced mesh to the original mesh. The default value is 0. Only valid if meshReduceTargetType is MaximumDeviationMeshReduceTargetType.

### mesh : Base [read-write]
Gets and sets the input mesh body.

### meshReduceMethodType : MeshReduceMethodTypes [read-write]
Gets and sets the type of mesh reduce, default value is AdaptiveReduceType.

### meshReduceTargetType : MeshReduceTargetTypes [read-write]
Gets and sets the target criteria for the reduction, default value is MaximumDeviationMeshReduceTargetType.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### proportion : ValueInput [read-write]
Gets and sets the proportion of number of faces of the reduced mesh to the number of faces of original mesh as a target for the reduction. The value can range between 0 and 100 percent. Only valid if meshReduceTargetType is ProportionMeshReduceTargetType.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.
