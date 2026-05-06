# AllExtentDefinition
Namespace: adsk.fusion
Inherits: ExtentDefinition
Since: August 2014

This object is retired. See more information in the 'Remarks' section below.

Defines the inputs for an AllExtentDefinition object. This is used when defining the extent for a hole feature. Some other features, like extrude, support defining the extents independently in both directions. In that case you need to create a ThroughAllExtentDefinition and apply it for the extent direction you want a through all type.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### direction : ExtentDirections [read-write]
Gets and sets the direction of the extent.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentFeature : Feature [read-only]
Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null.
