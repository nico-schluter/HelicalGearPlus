# CustomGraphicsBasicMaterialColorEffect
Namespace: adsk.fusion
Inherits: CustomGraphicsColorEffect
Since: September 2017

One of the types of color effects that can be applied to a custom graphics entity. With this type of effect, basic Phong shading and lighting techniques are used so give the entity a 3-dimensional appearance.

**Accessed from:** CustomGraphicsBasicMaterialColorEffect.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(diffuseColor: Color, ambientColor: Color, specularColor: Color, emissiveColor: Color, glossiness: double, opacity: double) -> CustomGraphicsBasicMaterialColorEffect
Statically creates a new basic CustomGraphicsBasicMaterialColorEffect object. This can be used to color custom graphics entities. With this type of effect you define the basic Phong shading properties so that the entity can be rendered with basic shading and lighting effects applied so that it appears 3-dimensional.

If only the emissive color is provided, the API will automatically create values for the other colors to render the object as a single color.
- **diffuseColor** (Color): The diffuse color is the color of reflected light as it scatters off of a rough surface and is the primary color of the entity. This color is always required.
- **ambientColor** (Color): The ambient color is the color of the light anywhere there's not a specific light source. If not specified the same color as the diffuse color is used.

This is an optional argument whose default value is null.
- **specularColor** (Color): The specular color is the color of reflected light (highlights) as it is reflected off of a shiny surface. This is commonly white or a lighter shade of the diffuse color. If not specified, white is used.

This is an optional argument whose default value is null.
- **emissiveColor** (Color): The emissive color is the color of light that entity emits, such as in a light bulb. If not specified, black for no emissive light is used.

This is an optional argument whose default value is null.
- **glossiness** (double): This specifies how glossy the entity is. The glossiness determines the size of highlights, and thus the apparent shininess of the material. A value of 0.0 will result in very large highlights like you would see with a rough surface. A maximum value of 128.0 will result in very small highlight as from a smooth surface.

This is an optional argument whose default value is 5.0.
- **opacity** (double): Specifies the opacity of the entity where a value of 1.0 is completely opaque and 0.0 is completely transparent.

This is an optional argument whose default value is 1.0.
- **Returns** (CustomGraphicsBasicMaterialColorEffect): Returns the created CustomGraphicsBasicMaterialColorEffect or null in case of a failure.

## Properties

### ambientColor : Color [read-write]
Gets and sets the ambientColor associated with this CustomGraphicsBasicMaterialColorEffect object. The ambient color is the color of the light anywhere there's not a specific light source.

### diffuseColor : Color [read-write]
Gets and sets the diffuseColor associated with this CustomGraphicsBasicMaterialColorEffect object. The diffuse color is the color of reflected light as it scatters off of a rough surface.

### emissiveColor : Color [read-write]
Gets and sets the emissiveColor associated with this CustomGraphicsBasicMaterialColorEffect object. The emissive color is the primary color of the entity

### glossiness : double [read-write]
Gets and sets the glossiness associated with this CustomGraphicsBasicMaterialColorEffect object. The glossiness determines the size of highlights, and thus the apparent shininess of the material. A value of 0.0 will result in very large highlights like you would see with a rough surface. A maximum value of 128.0 will result in very small highlight as from a smooth surface.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### opacity : double [read-write]
Gets and sets the opacity associated with this CustomGraphicsBasicMaterialColorEffect object. A value of 1.0 is completely opaque and 0.0 is completely transparent.

### specularColor : Color [read-write]
Gets and sets the specularColor associated with this CustomGraphicsBasicMaterialColorEffect object. The specular color is the color of reflected light (highlights) as it is reflected off of a shiny surface. This is commonly white or a lighter shade of the emissive color.
