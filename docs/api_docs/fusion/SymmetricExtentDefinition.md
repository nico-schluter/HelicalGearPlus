# SymmetricExtentDefinition
Namespace: adsk.fusion
Inherits: ExtentDefinition
Since: November 2016

A definition object that is used to define the extents of a feature to be symmetric.

**Accessed from:** ExtrudeFeature.symmetricExtent, SymmetricExtentDefinition.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(distance: ValueInput, isFullLength: boolean) -> SymmetricExtentDefinition
Statically creates a new SymmetricExtentDefinition object. This is used as input when create a new feature and defining the starting condition.
- **distance** (ValueInput): An input ValueInput objects that defines either half the extent of the extrude or the full extent, depending on the value of the isFullLength argument.
- **isFullLength** (boolean): An input boolean that specifies if the distance specified defines the full or half length of the extrusion.
- **Returns** (SymmetricExtentDefinition): Returns the newly created SymmetricExtentDefinition or null in the case of a failure.

## Properties

### distance : Base [read-only]
Returns the current extent distance. If the SymmetricExtentDefinition object has been created statically and isn't associated with a feature this will return a ValueInput object. If the SymmetricExtentDefinition object is obtained from a feature this will return a ModelParameter object. You can use properties of the parameter to edit its value which will result in the feature updating.

### isFullLength : boolean [read-write]
Gets and sets if the distance defines the full extent length or half the length. A value of True indicates if defines the full length.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentFeature : Feature [read-only]
Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null.

### taperAngle : Base [read-only]
Returns the current taper angle. If the SymmetricExtentDefinition object has been created statically and isn't associated with a feature this will return a ValueInput object. If the SymmetricExtentDefinition object is obtained from a feature this will return a ModelParameter object. You can use properties of the parameter to edit its value which will result in the feature updating.

## Samples
- **Extrude Feature API Sample**: Demonstrates creating a new extrude feature.
