# DistanceExtentDefinition
Namespace: adsk.fusion
Inherits: ExtentDefinition
Since: August 2014

Defines the inputs for a distance ExtentDefinition object. This feature extent type defines the distance as well as whether the extent is symmetric or in only one direction. If the extent is not symmetric, a positive or negative distance can be used to control the direction. For a hole, the IsSymmetric property value will always be false.

**Accessed from:** DistanceExtentDefinition.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(distance: ValueInput) -> DistanceExtentDefinition
Statically creates a new DistanceExtentDefinition object. This is used as input when defining the extents of a feature to be a specified distance.
- **distance** (ValueInput): A ValueInput that defines the distance of the extrusion.
- **Returns** (DistanceExtentDefinition): Returns the newly created DistanceExtentDefinition or null in the case of failure.

## Properties

### distance : ModelParameter [read-only]
Returns the parameter controlling the distance. You can edit the distance by editing the value of the parameter object.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentFeature : Feature [read-only]
Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null.

## Samples
- **Extrude Feature API Sample**: Demonstrates creating a new extrude feature.
- **Manage Participant Bodies API Sample**: Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also.
