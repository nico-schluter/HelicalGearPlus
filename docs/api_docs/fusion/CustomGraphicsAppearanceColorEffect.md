# CustomGraphicsAppearanceColorEffect
Namespace: adsk.fusion
Inherits: CustomGraphicsColorEffect
Since: September 2017

One of the types of color effects that can be applied to a custom graphics entity. With this type of effect, the graphics entity will display using a Fusion appearance.

**Accessed from:** CustomGraphicsAppearanceColorEffect.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(appearance: Appearance) -> CustomGraphicsAppearanceColorEffect
Statically creates a new CustomGraphicsAppearanceColorEffect object. This can be used when setting the color property of the various custom graphics objects. With this coloring effect, an existing appearance is used. The appearance must be available in the design where the graphics will be drawn.
- **appearance** (Appearance): The appearance to use. The appearance must be available in the design where the graphics will be drawn.
- **Returns** (CustomGraphicsAppearanceColorEffect): Returns the created CustomGraphicsAppearanceColorEffect or null in case of a failure.

## Properties

### appearance : Appearance [read-write]
Gets and sets the appearance to use. The appearance assigned must be available in the design where the graphics will be drawn.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
