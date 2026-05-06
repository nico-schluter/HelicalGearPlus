# Rendering
Namespace: adsk.fusion
Inherits: Base
Since: May 2023

Provides access to the ability to render in a background process on the local machine.

**Accessed from:** RenderManager.rendering

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### startLocalRender(filename: string, camera: Camera) -> RenderFuture
Starts a local rendering process using either the active viewport or a specified camera to define the camera information. This starts a background process on the local machine to generate the rendering. Even though this is a background process, it is tied to the running Fusion process and will be terminated if Fusion is shut down. If multiple local renders are started, they are queued and only one runs at a time.
- **filename** (string): Optional argument that is the full path and filename of the file to write the resulting rendering to. The file extension can be .png, .jpg, .jpeg, or .tiff and the file will be saved as that type. If not provided or is an empty string, the rendering will be saved to the cloud as a PNG file.

This is an optional argument whose default value is "".
- **camera** (Camera): Optional argument that specifies the camera to use for the rendering. The default value is null, which will use the camera associated with the active viewport.

This is an optional argument whose default value is null.
- **Returns** (RenderFuture): Returns a RenderFuture that allows you to check the current state of this rendering job.

## Properties

### aspectRatio : RenderAspectRatios [read-write]
Gets and sets the aspect ratio of the rendered image. This is not the resolution, but only the aspect ratio. To define a custom aspect ratio set this property to CustomAspectRatio and use the resolutionHeight and resolutionWidth properties to define the resolution and aspect ratio. The default value is the aspect ratio defined in the scene settings. The width and height must be between 108 and 4000 pixels.

### isBackgroundTransparent : boolean [read-write]
Specifies if the background of the rendering should be transparent. The default is false, which means it will not be transparent.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### renderQuality : integer [read-write]
Gets and sets the desired quality of the rendering. The quality is specified using a value between 25 and 100, where 75 is the equivalent of "Final" and 100 is the same as "Excellent" in the user interface. The default value is 75

### resolution : RenderResolutions [read-write]
Gets and sets the resolution of the rendered image. This is the final width and height of the image in pixels. To define a custom aspect ratio, use the resolutionHeight and resolutionWidth properties to define any resolution. Using those has the side effect of setting this property to CustomRenderResolution. Setting this to anything except CustomRenderResolution, will also have the side effect of setting the aspect ratio.

### resolutionHeight : integer [read-write]
Gets and sets the height of the image in pixels. If anything but CustomRenderAspectRatio is defined as the aspect ratio, the resolution width will be modified to maintain the specified aspect ratio. The height must be between 108 and 4000 pixels.

### resolutionWidth : integer [read-write]
Gets and sets the width of the image in pixels. If anything but CustomRenderAspectRatio is defined as the aspect ratio, the resolution height will be modified to maintain the specified aspect ratio. The width must be between 108 and 4000 pixels.

## Samples
- **Rendering Sample**: Demonstrates using the Rendering capabilities in the API. This starts a series of local renderings to generate a series of frames, where the camera is repositioned and a parameter is modified for each frame to create a dynamic animation. To use the sample, have a design open that contains a parameter named "Length". It can be a user or model parameter. The sample will modify this parameter from a value of 0.1 cm to 15 cm, but you can change these values by editing the values of the paramStartVal and paramEndVal variables on lines 90 and 91 of the sample. It expects a folder named "C:\Temp\RenderSample" to exist, and will fail if it doesn't. The rendered frames will be written to that folder.
An example rendering is shown below where this file was used. The parameter is modifying a move feature which results in changing the shape of an extrusion. The parameter could be driving anything and you could modify the code to edit more than one parameter. The result of this sample is a folder containing all of the rendered frames. You can process these to create an animation. The sample animation was created using GIMP.
