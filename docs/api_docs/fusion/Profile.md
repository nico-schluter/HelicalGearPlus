# Profile
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Represents a profile in a sketch. Profiles are automatically computed by Fusion and represent closed areas within the sketch.

**Accessed from:** Component.createBRepEdgeProfile, Component.createOpenProfile, FlatPatternComponent.createBRepEdgeProfile, FlatPatternComponent.createOpenProfile, Profile.createForAssemblyContext, Profile.nativeObject, ProfileCurve.parentProfile, ProfileLoop.parentProfile, Profiles.item

## Methods

### areaProperties(accuracy: CalculationAccuracy) -> AreaProperties
Calculates the area properties for the profile.
- **accuracy** (CalculationAccuracy): Specifies the desired level of computational accuracy of the property calculations. The default value of 'LowCalculationAccuracy' returns results within a +/- 1% error margin.

This is an optional argument whose default value is CalculationAccuracy.LowCalculationAccuracy.
- **Returns** (AreaProperties): Returns the AreaProperties object that has properties for getting the area, perimeter, centroid, etc of this profile.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> Profile
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. Returns null if this isn't the NativeObject.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (Profile): Returns the proxy object or null if this isn't the NativeObject.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object.

### boundingBox : BoundingBox3D [read-only]
Returns the 3D bounding box of the profile in sketch space.

### entityToken : string [read-only]
Returns a token for the Profile object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same profile.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### face : BRepFace [read-only]
Returns a temporary BRepFace object that is the same shape as the profile. The geometry of the returned face is defined in the 3D space of the parent sketch of the profile.

This can be useful when wanting to use a profile in conjunction with the TemporaryBRepManager object to create B-Rep objects.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### nativeObject : Profile [read-only]
The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentSketch : Sketch [read-only]
Returns the parent sketch of the profile.

### plane : Plane [read-only]
Returns the plane the profile is defined in. Profiles are always planar and exist within a single plane.

### profileLoops : ProfileLoops [read-only]
The loops or closed areas within this profile. There is always a single outer loop but there can be zero to many inner loops defining voids in the profile.

## Samples
- **Loft Feature API Sample**: Demonstrates creating a new loft feature.
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
