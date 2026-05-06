# CanvasInput
Namespace: adsk.fusion
Inherits: Base
Since: May 2023

The CanvasInput object is used to define the various options when creating a new canvas. It's created using the Canvases.createInput method and is used by the Canvases.add method to create a Canvas.

**Accessed from:** Canvases.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### flipHorizontal() -> boolean
Flips the image along the horizontal axis. This is a convenience method that flips the direction of the X axis of the transform.
- **Returns** (boolean): Returns true if the flip was successful.

### flipVertical() -> boolean
Flips the image along the vertical axis. This is a convenience method that flips the direction of the Y axis of the transform.
- **Returns** (boolean): Returns true if the flip was successful.

## Properties

### imageFilename : string [read-write]
Gets and sets the filename of the image used for the canvas.

When setting this property, it is the full filename to the image to use for the canvas. PNG, JPEG, and TIFF files are supported.

### isDisplayedThrough : boolean [read-write]
Controls if the image is visible through the model or not.

Defaults to true when the input is created.

### isRenderable : boolean [read-write]
Controls if the canvas will be rendered when ray tracing within the Render workspace.

Defaults to false when the input is created.

### isSelectable : boolean [read-write]
Controls if the canvas is selectable or not within the graphics window.

Defaults to false when the input is created.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### opacity : integer [read-write]
Gets and sets the opacity of the canvas where 0 is completely transparent and 100 is completely opaque. Setting this property to a value outside the range of 0-100 will result in the value being set to the closest valid value.

Defaults to 50 when the input is created.

### planarEntity : Base [read-write]
Gets and sets the plane the canvas is associated with. This can be either a planar Face or a construction plane. In a direct modeling design or the canvas is being created in a base feature, this can be a Plane object.

### plane : Plane [read-only]
Returns a Plane object that is obtained from the planar face or construction plane and defines the parameter space the canvas is positioned relative to.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

### transform : Matrix2D [read-write]
Gets and sets the transform of the canvas. This allows you to control the position, rotation, scaling, and flipping. The X and Y axes defined by the matrix, must be perpendicular to one another. The directions of the X and Y axes defines the orientation of the image.

This is a 3x3 matrix where the third column controls the position of the canvas and is relative to the parameter space of the plane defined by the specified planar face or construction plane.
