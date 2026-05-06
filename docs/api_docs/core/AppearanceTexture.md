# AppearanceTexture
Namespace: adsk.core
Inherits: Base
Since: August 2014

Provides access to a list of properties that define a texture.

**Accessed from:** AppearanceTextureProperty.value, ColorProperty.connectedTexture, FloatProperty.connectedTexture

## Methods

### changeTextureImage(imageFilename: string) -> boolean
Changes the image of this texture.
- **imageFilename** (string): Input String specifying the full filename of the texture file to use.
- **Returns** (boolean): Returns true if the change was successful.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### properties : Properties [read-only]
Returns a collection of the properties associated with this texture.

### textureType : TextureTypes [read-only]
Gets the type of texture this appearance currently is.
