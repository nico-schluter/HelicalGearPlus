# RenderFuture
Namespace: adsk.fusion
Inherits: Base
Since: May 2023

Used to check the state of a local or in canvas rendering.

**Accessed from:** Rendering.startLocalRender

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### filename : string [read-only]
The filename that the finished rendering will be saved to. If being saved to the cloud, this is the name Fusion will use for the completed rendering.

### imageHeight : integer [read-only]
Returns the height of the image. The height was specified when the rendering was started.

### imageWidth : integer [read-only]
Returns the width of the image. The width was specified when the rendering was started.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### progress : double [read-only]
Returns the progress of this rendering expressed as a percentage where 0.0 is no progress and 1.0 is complete.

### renderState : LocalRenderStates [read-only]
Returns the current state of the rendering.

## Samples
- **Rendering Sample**: Demonstrates using the Rendering capabilities in the API. This starts a series of local renderings to generate a series of frames, where the camera is repositioned and a parameter is modified for each frame to create a dynamic animation. To use the sample, have a design open that contains a parameter named "Length". It can be a user or model parameter. The sample will modify this parameter from a value of 0.1 cm to 15 cm, but you can change these values by editing the values of the paramStartVal and paramEndVal variables on lines 90 and 91 of the sample. It expects a folder named "C:\Temp\RenderSample" to exist, and will fail if it doesn't. The rendered frames will be written to that folder.
An example rendering is shown below where this file was used. The parameter is modifying a move feature which results in changing the shape of an extrusion. The parameter could be driving anything and you could modify the code to edit more than one parameter. The result of this sample is a folder containing all of the rendered frames. You can process these to create an animation. The sample animation was created using GIMP.
