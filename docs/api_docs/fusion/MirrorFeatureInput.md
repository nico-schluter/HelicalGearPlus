# MirrorFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

This class defines the methods and properties that pertain to the definition of a mirror feature.

**Accessed from:** MirrorFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### inputEntities : ObjectCollection [read-write]
Gets and sets the entities that are mirrored. It can contain faces, features, bodies, or components. The input must all be of a single type. For example, you can't provide a body and a component but the collection must be either all bodies or all components.

### isCombine : boolean [read-write]
Gets and sets whether the mirrored bodies should be combined with the original bodies. When true, the mirrored geometry will be Boolean unioned with the original solid or surface body(s) when they connect within the stitch tolerance defined with the stitchTolerance property. If the bodies cannot be unioned or stitched the result will be separate bodies. If any input object is not a body, then this setting is ignored. Default is false.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### mirrorPlane : Base [read-write]
Gets and sets the mirror plane. This can be either a planar face or construction plane.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### patternComputeOption : PatternComputeOptions [read-write]
Gets and sets the compute option when mirroring features. The default value for this is AdjustPatternCompute. This property only applies when mirroring features and is ignored in the direct modeling environment.

### stitchTolerance : ValueInput [read-write]
Gets and sets the ValueInput object that defines the Stitching Tolerance (length) to use when doing a mirror and combine for surface bodies.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

## Samples
- **Mirror Feature API Sample**: Demonstrates creating a new mirror feature
