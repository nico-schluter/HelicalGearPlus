# InCanvasRendering
Namespace: adsk.fusion
Inherits: Base
Since: September 2023

Provides access to the in-canvas rendering capabilities of Fusion. This uses the active viewport and the user will see the rendering as it takes place.

**Accessed from:** RenderManager.inCanvasRendering

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### saveImage(filename: string) -> boolean
Saves the image as it currently exists in the active viewport. To get the best quality, this should be called after the renderComplete event has fired.
- **filename** (string): The filename to save the image to. This must be the full path. The file extension can be .png, .jpg, .jpeg, or .tiff and the file will be saved as that type.

The size of the image is dependent on the size of the viewport and the current specified aspect ratio.
- **Returns** (boolean): Returns true if the save was successful.

### start(renderQuality: double) -> boolean
Starts the process of in-canvas rendering. There are two modes when doing in-canvas rendering; advanced and fast. This is specified in the API using the isAdvanced property. When using advanced rendering, you can specify the desired quality and the rendering will stop once that quality has been reached. When using fast rendering, the rendering never stops but continues until you stop it.

When using the API, it's generally best to use advanced rendering so you can easily control the final quality and get notified by the renderComplete event when it has finished. When using fast rendering, the renderComplete event is not fired and you have to use some other criteria like the number of iterations complete or the time taken to determine when to stop the rendering process.
- **renderQuality** (double): Specifies the desired quality of the rendering. The quality is specified using a value between 0 and 1, where 0.75 is the equivalent of "Excellent" and 1.0 is the same as "Final" in the user interface.

This is ignored when using fast rendering (the isAdvanced property is False).
- **Returns** (boolean): Returns true if the rendering was successfully started.

### stop() -> boolean
Stops the current rendering process.
- **Returns** (boolean): Returns true if successful.

## Properties

### elapsedTime : integer [read-only]
Returns the seconds spent on the current render.

### isAdvanced : boolean [read-write]
Gets and sets if "Fast" or "Advanced" rendering should be used. If false, "Fast" rendering is used, which uses simplified lighting and materials.

There are two modes when doing in-canvas rendering; advanced and fast. When using advanced rendering, you can specify the desired quality and the rendering will stop once that quality has been reached. When using fast rendering, the rendering never stops but continues until you stop it.

When using the API, it's generally best to use advanced rendering so you can easily control the final quality and get notified by the renderComplete event when it has finished. When using fast rendering, the renderComplete event is not fired, and you have to use some other criteria like the number of iterations complete, or the time taken to determine when to stop the rendering process.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### iterations : integer [read-only]
Returns the current number of iterations the renderer has completed.

### limitResolution : double [read-write]
Sets the percentage of the full resolution to render the image. Valid values are between 20 and 100 inclusive. 100 is full resolution (100%).

### lockView : boolean [read-write]
Gets and sets if the view should be locked during the in-canvas render. This prohibits the user from interacting with the view, which will cause the rendering to restart.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Events

### renderComplete
The RenderEvent event fires when the rendering has reached the quality that was specified when the rendering started. This event is only fired when using advanced rendering (the isAdvanced property is True). To save the finished rendering, use the saveImage method.

You can add or remove event handlers from the RenderEvent.
