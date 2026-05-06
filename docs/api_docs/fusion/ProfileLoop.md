# ProfileLoop
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

A loop within a profile.

**Accessed from:** ProfileCurve.parentProfileLoop, ProfileLoop.createForAssemblyContext, ProfileLoop.nativeObject, ProfileLoops.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> ProfileLoop
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. Returns null if this isn't the NativeObject.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (ProfileLoop): Returns the proxy object or null if this isn't the NativeObject.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### isOuter : boolean [read-only]
Indicates if this is an outer or inner loop. Profiles always have one outer loop and have an zero to many inner loops defining voids.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### nativeObject : ProfileLoop [read-only]
The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentProfile : Profile [read-only]
Returns the parent Profile object.

### profileCurves : ProfileCurves [read-only]
Returns a collection of the curves making up this loop.
