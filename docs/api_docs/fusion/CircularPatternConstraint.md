# CircularPatternConstraint
Namespace: adsk.fusion
Inherits: GeometricConstraint
Since: March 2016

A circular pattern constraint in a sketch.

**Accessed from:** CircularPatternConstraint.createForAssemblyContext, CircularPatternConstraint.nativeObject, GeometricConstraints.addCircularPattern

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> CircularPatternConstraint
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (CircularPatternConstraint): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes this constraint. The IsDeletable property can be used to determine if this constraint can be deleted.
- **Returns** (boolean): Returns true if the delete was successful.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this geometric constraint.

### centerPoint : SketchPoint [read-write]
Gets and sets the sketch point that defines the center of the pattern.

### createdEntities : array [read-only]
Returns an array that contains all of the sketch entities that were created as a result of the pattern. This does not contain the original entities that were used as input to the pattern. The input entities can be obtained by using the entities property.

### entities : array [read-write]
Gets and sets the entities to pattern. Sketch points and curves are valid entities to pattern.

### entityToken : string [read-only]
Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### isDeletable : boolean [read-only]
Indicates if this constraint is deletable.

### isSuppressed : array [read-write]
Specifies which, if any, instances of the pattern are suppressed. This returns an array of Boolean values that indicates if a particular instance in the pattern is suppressed or not. A value of true will result in the associated instance being suppressed.

### isSymmetric : boolean [read-write]
Gets and sets if the angle extent is in one direction or is symmetric.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### nativeObject : CircularPatternConstraint [read-only]
The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentSketch : Sketch [read-only]
Returns the parent sketch object.

### quantity : ModelParameter [read-only]
Returns the parameter that controls the number of instances in the pattern. To change the value, use the properties on the returned ModelParameter object.

### totalAngle : ModelParameter [read-only]
Returns the parameter that controls the number of instances in the pattern. A positive angle is a counter-clockwise direction and a negative angle can be used to reverse the direction. An angle of 360 degrees or 2 pi radians will create a full circular pattern.
