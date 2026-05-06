# Camera
Namespace: adsk.core
Inherits: Base
Since: August 2014

The Camera class represents the information that specifies how a model is displayed within a viewport. It's analogous to a real camera, which has a position in space, is pointed towards a specific point, is oriented in a particular way, and has a specific type of lens.

Whether a camera is created statically using the Camera.create() method or obtained from a Viewport, a Camera object is always temporary and not associated with anything. This means when you get it from a Viewport, the Camera object captures the current state of the Viewport and stores it but doesn't save where it came from, so it is completely independent.

To update the camera settings associated with a Viewport, get a Camera object from a Viewport or create a new Camera using Camera.create(), modify the Camera object to define the view you want, and assign it to the Viewport.

**Accessed from:** Camera.create, NamedView.camera, Viewport.camera

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create() -> Camera
Creates a new Camera object that is independent of any viewport. This can be used to construct a camera to be used as input to modify a viewport, and create or update a named view.
- **Returns** (Camera): Returns the created camera.

### getExtents(width: double, height: double) -> boolean
Gets the extents of the camera. This is only used for orthographic cameras. The extents of a perspective camera is defined by a combination of the position of the eye point (how close the eye is to the model) and the perspective angle.
- **width** (double): The width of the extent in centimeters.
- **height** (double): The height of the extent in centimeters.
- **Returns** (boolean): Returns true if successful. This will fail in the case it is used for a perspective camera.

### setExtents(width: double, height: double) -> boolean
Sets the extents of the camera. This is only used for orthographic cameras. The extents of a perspective camera is defined by a combination of the position of the eye point (how close the eye is to the model) and the perspective angle.

When the camera is assigned to a viewport, typically only the width or the height is used depending on the aspect ratio of the viewport. For example, if the width and height are both 10, but the viewport is twice as wide as it is tall (2:1 aspect ratio). The height extent will be 10 and the width extent will be recomputed to be 20 to match the viewport.
- **width** (double): The width of the extent in centimeters.
- **height** (double): The height of the extent in centimeters.
- **Returns** (boolean): Returns true if successful. This will fail in the case it is used for a perspective camera.

## Properties

### cameraType : CameraTypes [read-write]
Gets and sets the current camera type.

### eye : Point3D [read-write]
Gets and sets the position of the eye in world space.

### isFitView : boolean [read-write]
If this property is true, when this camera is applied to a viewport it will modify the camera such that the entire model is displayed in the viewport. When getting a camera from a viewport or creating a camera using Camera.create(), this property defaults to false.

### isSmoothTransition : boolean [read-write]
This property controls if Fusion will perform a smooth transition animation from the current camera position to the new position. If this property is set to true, it will smoothly transition. If false, the camera will jump to the position defined by the camera without any animated transition.

When a camera is obtained from a Viewport or created using the Camera.create() method, this property defaults to false.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### perspectiveAngle : double [read-write]
Gets and sets the perspective angle of the camera. This property is only valid when the CameraType property is either Perspective or PerspectiveWithOrthoFaces.

### target : Point3D [read-write]
Gets and sets the camera target point in world space.

### upVector : Vector3D [read-write]
Defines the "up" direction for the camera which controls the orientation of the camera around the line defined between the eye and target points.

### viewExtents : double [read-write]
This function is retired. See more information in the 'Remarks' section below.

Defines the area that's visible by the camera. This value is the radius of a sphere centered at the target point. The camera will display everything within that sphere and everything in front of and behind the sphere. Additional geometry outside of the sphere will also be visible depending on the shape of the window. Setting this value can cause the eye and/or perspective angle to be modified when the camera type is perspective.

### viewOrientation : ViewOrientations [read-write]
Sets the camera to a standard orientation. If this is set, it will result in resetting all the camera values except the camera type. The orientation is based on the current orientation defined by the ViewCube. This means, that the view orientations cannot be expected to be consistent from one view to another.

## Samples
- **As-Built Joint Sample**: Demonstrates creating a new As-Built Joint.
- **Joint Origin Sample**: Demonstrates creating a new Joint Origin.
- **Rigid Group API Sample**: Demonstrates creating a new Rigid Group.
