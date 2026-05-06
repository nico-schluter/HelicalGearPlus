# InterferenceResult
Namespace: adsk.fusion
Inherits: Base
Since: November 2015

Represents the interference between bodies and/or occurrences in an interference analysis.

**Accessed from:** InterferenceResults.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### entityOne : Base [read-only]
Returns the first entity involved in the interference

### entityTwo : Base [read-only]
Returns the second entity involved in the interference

### interferenceBody : BRepBody [read-only]
Returns a transient BRepBody that represents the volume of interference.

### isCreateBody : boolean [read-write]
Gets and sets if this interference volume should be created as a model body. Setting this to true doesn't create the body just indicates that a body is desired. Calling the createBodies method on the interferenceResults object will result in the creation of the model body if this property is true.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
