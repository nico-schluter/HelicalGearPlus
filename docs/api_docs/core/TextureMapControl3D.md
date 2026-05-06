# TextureMapControl3D
Namespace: adsk.core
Inherits: TextureMapControl
Since: March 2022

Provides access to the various settings that control how a 3D texture is applied to a body.

## Methods

### bestFit() -> boolean
Reorients the transform to best fit the geometry of the body.
- **Returns** (boolean): Returns true if the best fit was successful.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### reset() -> boolean
Resets the texture map back to its original default settings.
- **Returns** (boolean): Returns true if the reset was successful.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### transform : Matrix3D [read-write]
Gets and sets the transform that defines the position and orientation of how the texture is applied to the body. For wood grain, the Z direction of the defined coordinate system is the direction of the grain.
