# SymmetryConstraint
Namespace: adsk.fusion
Inherits: GeometricConstraint
Since: August 2014

A symmetry constraint in a sketch.

**Accessed from:** GeometricConstraints.addSymmetry, SymmetryConstraint.createForAssemblyContext, SymmetryConstraint.nativeObject

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> SymmetryConstraint
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (SymmetryConstraint): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes this constraint. The IsDeletable property can be used to determine if this constraint can be deleted.
- **Returns** (boolean): Returns true if the delete was successful.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this geometric constraint.

### entityOne : SketchEntity [read-only]
Returns the first curve.

### entityToken : string [read-only]
Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### entityTwo : SketchEntity [read-only]
Returns the second curve.

### isDeletable : boolean [read-only]
Indicates if this constraint is deletable.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### nativeObject : SymmetryConstraint [read-only]
The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentSketch : Sketch [read-only]
Returns the parent sketch object.

### symmetryLine : SketchLine [read-only]
Returns the axis (SketchLine) that defines the symmetry.
