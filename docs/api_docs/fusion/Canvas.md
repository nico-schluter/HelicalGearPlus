# Canvas
Namespace: adsk.fusion
Inherits: Base
Since: May 2023

Represents a Canvas within a component.

**Accessed from:** Canvas.createForAssemblyContext, Canvas.nativeObject, Canvases.add, Canvases.item, Canvases.itemByName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> Canvas
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (Canvas): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe()
Deletes the canvas from the component.

### flipHorizontal() -> boolean
Flips the image along the horizontal axis. This is a convenience method that flips the direction of the X axis of the transform.
- **Returns** (boolean): Returns true if the flip was successful.

### flipVertical() -> boolean
Flips the image along the vertical axis. This is a convenience method that flips the direction of the Y axis of the transform.
- **Returns** (boolean): Returns true if the flip was successful.

### saveImage(filename: string) -> boolean
Saves the image associated with the canvas to the specified file. This is useful in cases where the original image file is no longer available but you need the image for some other purpose.
- **filename** (string): The full filename of the image to save, including the file extension, which controls the format of the image file. If a file extension other than png, jpg, or tiff is specified, a png extension will be added to the filename by default.

This method will fail if a file with the specified filename already exists. If you want to overwrite the file, you'll need to delete it first before calling this method.
- **Returns** (boolean): Returns true if writing the file was successful.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### deriveFeature : DeriveFeature [read-only]
Returns the DeriveFeature if this canvas is derived from another design. This property returns null if the canvas is not derived from another design (i.e. isDerived property returns false).

### entityToken : string [read-only]
Returns a token for the Canvas object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same canvas.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### imageFilename : string [read-write]
Gets and sets the filename of the image used for the canvas. When getting this property, the filename returned is the file that was used when the canvas was initially created. it's possible the file may no longer exist.

When setting this property, it is the full filename to the image to use for the canvas. PNG, JPEG, and TIFF files are supported.

### isDerived : boolean [read-only]
Returns if this canvas is derived from another design. If true, the canvas cannot be deleted. You should not attempt to make any edits to the derived canvas. Any edits made to this derived canvas will be lost when the derive updates.

### isDisplayedThrough : boolean [read-write]
Controls if the image is visible through the model or not.

### isLightBulbOn : boolean [read-write]
Gets and sets if the light bulb of this canvas as displayed in the browser is on or off.

A canvas will only be visible if the light bulb is switched on. However, the light bulb can be on and the canvas still invisible if the visibility of a higher level occurrence has its light bulb off or if the light bulb for Canvases folder is off to turn off all canvases in a component.

### isRenderable : boolean [read-write]
Controls if the canvas will be rendered when ray tracing within the Render workspace.

### isSelectable : boolean [read-write]
Controls if the canvas is selectable or not within the graphics window.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-only]
Returns if the canvas is currently visible in the graphics window. The isLightBulbOn property of the canvas controls if the canvas should be displayed or not, but even when true, the canvas may not be visible because the occurrence that references the component may not be visible. It's also possible to turn off the visibility of all canvases for a component. This property takes all of that into account when reporting if the canvas is visible or not.

### name : string [read-write]
Gets and sets the name of the canvas. This is the name seen in the browser and timeline.

### nativeObject : Canvas [read-only]
The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### opacity : integer [read-write]
Gets and sets the opacity of the canvas where 0 is completely transparent and 100 is completely opaque. Setting this property to a value outside the range of 0-100 will result in the value being set to the closest valid value.

### planarEntity : Base [read-write]
Gets and sets the plane the canvas is associated with. This can be either a planar Face or a construction plane. In a direct modeling design or the canvas is being created in a base feature, this can be a Plane object.

### plane : Plane [read-only]
Returns a Plane object that represents the position and orientation of the canvas in model space.

### timelineObject : TimelineObject [read-only]
Returns the timeline object associated with the creation of this canvas.

### transform : Matrix2D [read-write]
Gets and sets the transform of the canvas. This allows you to control the position, rotation, scaling, and flipping. The X and Y axes defined by the matrix and must be perpendicular to one another.

This is a 3x3 matrix where the third column controls the position of the canvas and defines the position using 2D coordinates in the model space.
