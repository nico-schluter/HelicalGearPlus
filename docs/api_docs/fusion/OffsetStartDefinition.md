# OffsetStartDefinition
Namespace: adsk.fusion
Inherits: ExtentDefinition
Since: November 2016

A definition object that is used to define a feature whose start plane is defined as plane that is offset from the sketch plane of the profile.

**Accessed from:** OffsetStartDefinition.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(offset: ValueInput) -> OffsetStartDefinition
Statically creates a new OffsetStartDefinition object. This is used as input when create a new feature and defining the starting condition.
- **offset** (ValueInput): An input ValueInput objects that defines the offset distance. The offset can be positive or negative. A positive value indicates an offset in the same direction as the z axis of the profile plane.
- **Returns** (OffsetStartDefinition): Returns the newly created OffsetStartDefinition object or null in the case of failure.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### offset : Base [read-only]
Gets the currently defined offset value. If the ProfilePlaneWithOffsetDefinition object was created statically and is not associated with a feature, this will return a ValueInput object. if the ProfilePlaneWithOffsetDefinition is associated with an existing feature, this will return the parameter that was created when the feature was created. To edit the offset, use properties on the parameter to change the value of the parameter.

### parentFeature : Feature [read-only]
Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null.

### profilePlane : Plane [read-only]
Returns the geometric definition of the profile plane.

## Samples
- **Extrude Feature API Sample**: Demonstrates creating a new extrude feature.
- **extrudeFeatures.add using setSymmetricExtent**: Demonstrates the extrudeFeatures.add method using the setSymmetricExtent method. To use this sample have a design open that contains a sketch with a profile. When you run the script you will be prompted to select the profile that will be used to create the extrusion.
