# ConstructionPlaneDistanceOnPathDefinition
Namespace: adsk.fusion
Inherits: ConstructionPlaneDefinition
Since: August 2014

ConstructionDistanceOnPathDefinition defines a ConstructionPlane normal to an edge or sketch profile at a specified position along the path defined by the edge or sketch profile.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### redefine(pathEntity: Base, distance: ValueInput) -> boolean
Redefines the input defining the construction plane.
- **pathEntity** (Base): The sketch curve, edge, or a profile object
- **distance** (ValueInput): The ValueInput object that defines the distance along the path
- **Returns** (boolean): Returns true if the redefinition of the plane is successful.

## Properties

### distance : Parameter [read-only]
Gets the distance along the path.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentConstructionPlane : ConstructionPlane [read-only]
Returns the ConstructionPlane object

### pathEntity : Base [read-only]
Gets the sketch curve, edge, or a profile object.
