# TessellateFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: January 2025

This class defines the methods and properties that pertain to the definition of a tessellate feature.

**Accessed from:** TessellateFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### aspectRatio : ValueInput [read-write]
Specify ratio between the height and width of each face on the mesh body. Only valid if tessellateRefinementType is CustomTessellateRefinementType.

### createQuads : boolean [read-write]
Creates quad faces on the mesh body where possible.

### inputBodies : array [read-write]
Gets and sets the input list of BReb bodies.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maximumEdgeLength : ValueInput [read-write]
Specify maximum length of any face edge on the mesh body. Only valid if tessellateRefinementType is CustomTessellateRefinementType.

### normalDeviation : ValueInput [read-write]
Specify maximum angle between the normal vectors of each face on the mesh body. Only valid if tessellateRefinementType is CustomTessellateRefinementType.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### surfaceDeviation : ValueInput [read-write]
Specify maximum distance between the surface of the original body and the surface of the mesh body. Only valid if tessellateRefinementType is CustomTessellateRefinementType.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

### tessellateRefinementType : TessellateRefinementTypes [read-write]
Gets and sets the type of refinement, default value is MediumTessellateRefinementType.
