# MultiAxisSingularityLinearizationSettings
Namespace: adsk.cam
Inherits: Base
Since: September 2025

The class for the multi-axis singularity linearization settings.

**Accessed from:** MultiAxisSingularitySettings.createLinearizationSettings, MultiAxisSingularitySettings.linearizationSettings

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### linearizationTolerance : double [read-write]
The linearization tolerance for the multi-axis singularity settings.

### linearizeMethod : MultiAxisSingularityLinearizeMethod [read-write]
The linearization method to use for the multi-axis singularity settings.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
