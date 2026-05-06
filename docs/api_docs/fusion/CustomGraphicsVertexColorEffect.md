# CustomGraphicsVertexColorEffect
Namespace: adsk.fusion
Inherits: CustomGraphicsColorEffect
Since: September 2017

One of the types of color effects that can be applied to a custom graphics entity. With this type of effect, the graphics entity will display using the colors associated with the vertices of the mesh in the CustomGraphicsCoordinates object.

**Accessed from:** CustomGraphicsVertexColorEffect.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create() -> CustomGraphicsVertexColorEffect
Statically creates a new CustomGraphicsVertexColorEffect object.
- **Returns** (CustomGraphicsVertexColorEffect): Returns the created CustomGraphicsVertexColorEffect or null in case of a failure.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
