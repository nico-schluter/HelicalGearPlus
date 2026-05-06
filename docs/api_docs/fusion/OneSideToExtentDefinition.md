# OneSideToExtentDefinition
Namespace: adsk.fusion
Inherits: ExtentDefinition
Since: August 2014

This object is retired. See more information in the 'Remarks' section below.

Defines the inputs for a OneSideToExtentDefinition object. This defines a feature extent that goes up to a face or construction plane in one direction.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### matchShape : boolean [read-write]
Specifies if the face should be extended or use adjacent faces if necessary to define the termination of the extrusion. When used for a revolve feature this is ignored and is always treated as true.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentFeature : Feature [read-only]
Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null.

### toEntity : Base [read-write]
Gets and sets the entity that defines the extent. The valid types of entities can vary depending on the type of feature this is being used with.
