# CustomGraphicsShowThroughColorEffect
Namespace: adsk.fusion
Inherits: CustomGraphicsColorEffect
Since: August 2020

One of the types of color effects that can be applied to a custom graphics entity. With this type of effect, the graphics entity will display using the specified color and will show through other graphics that are in front of it.

**Accessed from:** CustomGraphicsShowThroughColorEffect.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(color: Color, opacity: double) -> CustomGraphicsShowThroughColorEffect
Creates a new CustomGraphicsShowThroughColorEffect object that can be assigned to a custom graphics entity using its showThrough property.
- **color** (Color): The color that will be used to render the custom graphics object.
- **opacity** (double): The level of opacity that will be applied when rendering the custom graphics object. A value of 0 is fully translucent and will have the effect of the object being completely covered by objects in front of it. A value of 1 is fully opaque which will have the effect of the object completely covering all objects. Values in between will make objects in front of the graphics object appear translucent to varying degrees so you can see the custom graphics object through it.
- **Returns** (CustomGraphicsShowThroughColorEffect): Returns the newly created CustomGraphicsShowThroughColorEffect object or null in the case of failure. This can be assigned to a custom graphics entity using its showThrough property.

## Properties

### color : Color [read-write]
Gets and sets the color associated with this CustomGraphicsShowThroughColorEffect object. The color that will be used to render the portion of the entity that is covered by other objects in the scene.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### opacity : double [read-write]
Gets and sets the opacity value associated with this CustomGraphicsShowThroughColorEffect object. The opacity is used when rendering the portion of the entity that is covered by other objects in the scene. This can be a value between 0 and 1, where 1 is fully opaque and will completely cover any other entities.
