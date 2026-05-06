# ThroughAllExtentDefinition
Namespace: adsk.fusion
Inherits: ExtentDefinition
Since: November 2016

A definition object that is used to define the extents of a feature to be through all.

**Accessed from:** ThroughAllExtentDefinition.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create() -> ThroughAllExtentDefinition
Statically creates a new ThroughAllExtentDefinition object. This is used as input when defining the extents of a feature to be through all.
- **Returns** (ThroughAllExtentDefinition): Returns the newly created ThroughAllExtentDefinition or null in the case of a failure.

## Properties

### isPositiveDirection : boolean [read-write]
Gets and sets if the direction is positive or negative. A value of true indicates it is in the same direction as the z direction of the profile's sketch plane.

This is only used when the extrusion is only defined in a single direction from the profile plane. If it's a two sided extrusion, this value is ignored.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentFeature : Feature [read-only]
Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null.

## Samples
- **Extrude Feature API Sample**: Demonstrates creating a new extrude feature.
