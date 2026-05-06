# SaveImageFileOptions
Namespace: adsk.core
Inherits: Base
Since: May 2022

Class that defines the various options that can be used when saving a viewport as an image. This object is created by using the static create method on the class and is then used as input to the Viewport.saveAsImageFileWithOptions method.

**Accessed from:** SaveImageFileOptions.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(filename: string) -> SaveImageFileOptions
Creates a new SaveImageFileOptions object. The returned object can be used to define the various options to use when saving a viewport as an image. The object is passed into the ViewPort.saveAsImageFileWithOptions method to create an image of the viewport.
- **filename** (string): The full filename, including the path, of the image file. The type of image file to be created is inferred from the extension of the filename.
- **Returns** (SaveImageFileOptions): Returns a SaveImageFileOptions object.

## Properties

### filename : string [read-write]
Gets and sets the full filename, including the path, of the image file. The type of image file to be created is inferred from the extension of the filename.

### height : integer [read-write]
Gets and set the height of the image to be created in pixels. A value of zero is valid and indicates the current height of the viewport is to be used. When the SaveImageFileOptions object is initially created, this is initialized to 0.

### isAntiAliased : boolean [read-write]
Gets and sets if the rendered image should be anti-aliased or not. If false, there is no anti-aliasing.

When the SaveImageFileOptions object is initially created, this is initialized to true.

### isBackgroundTransparent : boolean [read-write]
Gets and sets if the background should be rendered as transparent. If false, the background will be the same as seen in Fusion.

When the SaveImageFileOptions object is initially created, this is initialized to false.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### width : integer [read-write]
Gets and set the width of the image to be created in pixels. A value of zero is valid and indicates the current width of the viewport is to be used. When the SaveImageFileOptions object is initially created, this is initialized to 0.
