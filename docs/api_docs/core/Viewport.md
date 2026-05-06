# Viewport
Namespace: adsk.core
Inherits: Base
Since: August 2014

A viewport within Fusion. A viewport is the window where the model is displayed.

**Accessed from:** Application.activeViewport, CameraEventArgs.viewport, MouseEventArgs.viewport, RenderEventArgs.viewport

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### fit() -> boolean
Forces a camera change so that all of the graphics are visible in the viewport.
- **Returns** (boolean): Returns true if the fit was successful.

### goHome(transition: boolean) -> boolean
Sets the camera of the viewport to the defined "home" position.
- **transition** (boolean): If this is true it will do a smooth transition from the current camera position to the home position. If false, the view will jump to the home position with no intermediate steps.

This is an optional argument whose default value is True.
- **Returns** (boolean): Returns true if setting the view orientation was successful.

### modelToViewSpace(modelCoordinate: Point3D) -> Point2D
A specified point in model space returns the equivalent point in view space.
- **modelCoordinate** (Point3D): A coordinate in model space.
- **Returns** (Point2D): Returns the equivalent point in view space.

### refresh() -> boolean
Forces the view to refresh. It is sometimes useful to force a refresh to be able to see edits that have been made using the API.
- **Returns** (boolean): Returns true if the operation was successful.

### resetFront() -> boolean
Resets the front view to be the default front view orientation.
- **Returns** (boolean): Returns true if resetting to front was successful.

### saveAsImageFile(filename: string, width: integer, height: integer) -> boolean
Saves the current view to the specified image file. The view is re-rendered to the specified size and not just scaled from the existing view. This allows you to generate higher resolution images than you could do with just a screen capture.
- **filename** (string): The full filename, including the path, of the image file. The type of image file to be created is inferred from the extension of the filename.
- **width** (integer): The width in pixels of the output image. A value of zero indicates that the current width of the viewport is to be used.
- **height** (integer): The height in pixels of the output image. A value of zero indicates that the current height of the viewport is to be used.
- **Returns** (boolean): Returns true if the operation was successful.

### saveAsImageFileWithOptions(options: SaveImageFileOptions) -> boolean
Saves the current view to the specified image file. The view is re-rendered to the specified size and not just scaled from the existing view. This allows you to generate higher resolution images than you could do with just a screen capture.
- **options** (SaveImageFileOptions): A SaveImageFileOptions object that defines the various options that define how the image should be created. The SaveImageFileOptions can be created by using the static create method on the SaveImageFileOptions class.
- **Returns** (boolean): Returns true if the operation was successful.

### screenToView(screenCoordinate: Point2D) -> Point2D
Converts a 2D screen point into the equivalent viewport coordinate.
- **screenCoordinate** (Point2D): A 2D coordinate in screen space. (0,0) indicates the upper-left corner of the entire screen.
- **Returns** (Point2D): Returns the equivalent point in the viewport. This can return null in the case where the input screen point does not lie within the viewport.

### setCurrentAsFront() -> boolean
Sets the "front" view to be the current view orientation.
- **Returns** (boolean): Returns true if setting the view orientation was successful.

### setCurrentAsHome(isFitToView: boolean) -> boolean
Sets the "home" view to be the current view orientation.
- **isFitToView** (boolean): Specifies if when the view goes "home" if the view should be fit to the model or not. True indicates the view will be fit to the model.
- **Returns** (boolean): Returns true if setting the view orientation was successful.

### setCurrentAsTop() -> boolean
Sets the "top" view to be the current view orientation.
- **Returns** (boolean): Returns true if setting the view orientation was successful.

### viewToModelSpace(viewCoordinate: Point2D) -> Point3D
A specified point in view space returns the equivalent point in model space. Because view space is 2D and model space is 3D, the depth of the point is returned is somewhat arbitrary along the eye to target point direction.
- **viewCoordinate** (Point2D): A coordinate in view space.
- **Returns** (Point3D): Returns the equivalent point in model space.

### viewToScreen(viewCoordinate: Point2D) -> Point2D
Converts a 2D viewPort point into the equivalent screen coordinate.
- **viewCoordinate** (Point2D): A 2D coordinate in the viewport. (0,0) indicates the upper-left corner of the viewport.
- **Returns** (Point2D): Returns the equivalent point in the screen. This can return null in the case where the input point is outside the bounds of the screen, which also means it's outside any viewport.

## Properties

### camera : Camera [read-write]
Gets and sets the camera associated with the view. The camera returned is a copy of the current camera settings of the view. Editing the properties of the camera will have no affect on the viewport until the camera is assigned back to the viewport.

### frontEyeDirection : Vector3D [read-only]
Returns the direction of the front view as defined by the view cube. This vector defines the direction from the eye to the target for the front view.

### frontUpDirection : Vector3D [read-only]
Returns the up direction of the front view as defined by the view cube.

### height : integer [read-only]
Returns the height of the viewport in pixels.

### isFullScreen : boolean [read-write]
Gets and sets if the view is in full screen mode.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### modelToViewSpaceTransform : Matrix3D [read-only]
Returns a transformation matrix that defines the transform from model to viewport space.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentDocument : Document [read-only]
Returns the parent document of this viewport.

### visualStyle : VisualStyles [read-write]
Gets and sets the current visual style being used.

### width : integer [read-only]
Returns the width of the viewport in pixels.

## Samples
- **As-Built Joint Sample**: Demonstrates creating a new As-Built Joint.
- **Create Animation API Sample**: Creates a series of images of a design where a parameter is being changed. The series of images can be used to create an animation using other software. To run this sample, have a part open that contains a parameter named "Length". The parameter should be able to be successfully modified from 10 to 15 centimeters. Run the sample and choose or create a directory for the output. After running you should have a folder full of images that are snapshots of each parameter value.
- **Joint Origin Sample**: Demonstrates creating a new Joint Origin.
- **Rigid Group API Sample**: Demonstrates creating a new Rigid Group.
