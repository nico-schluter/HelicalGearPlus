# FromEntityStartDefinition
Namespace: adsk.fusion
Inherits: ExtentDefinition
Since: November 2016

A definition object that is used to define a feature whose start is defined by a specified construction plane or face. If a face is specified it must be large enough to completely contain the projected profile.

**Accessed from:** FromEntityStartDefinition.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(entity: Base, offset: ValueInput) -> FromEntityStartDefinition
Statically creates a new FromEntityStartDefinition object. This is used as input when create a new feature and defining the starting condition.
- **entity** (Base): An input construction plane or face that defines the start of the feature. If a face is specified it must be large enough to completely contain the projected profile.
- **offset** (ValueInput): An input ValueInput objects that defines the offset distance from the specified entity. The offset can be positive or negative. A positive value indicates an offset in the same direction as the positive normal direction of the face.
- **Returns** (FromEntityStartDefinition): Returns the newly created FromEntityStartDefinition or null in the case of a failure.

## Properties

### entity : Base [read-write]
Gets and sets the entity defining the start of the feature.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### offset : Base [read-only]
Gets the currently defined offset value. If the FromEntityStartDefinition object was created statically and is not associated with a feature, this will return a ValueInput object. if the FromEntityStartDefinition is associated with an existing feature, this will return the parameter that was created when the feature was created. To edit the offset, use properties on the parameter to change the value of the parameter.

### parentFeature : Feature [read-only]
Returns the parent feature that this definition is associated with. If this definition has been created statically and is not associated with a feature this property will return null.

## Samples
- **Extrude Feature API Sample**: Demonstrates creating a new extrude feature.
