# SceneSettings
Namespace: adsk.fusion
Inherits: Base
Since: May 2023

Provides access to all the settings that control how the scene is rendered.

**Accessed from:** RenderManager.sceneSettings

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### restoreDefaults() -> boolean
Changes all of the scene settings to the default values.
- **Returns** (boolean): Returns true if setting to the default settings was successful.

### saveAsDefaults() -> boolean
Saves all of the scene settings as the default settings for this Design.
- **Returns** (boolean): Returns true if saving the defaults was successful.

## Properties

### aspectRatio : RenderAspectRatios [read-write]
Gets and sets the aspect ratio of the rendered image. This is not the resolution, but only the aspect ratio. To define a custom aspect ratio set this property to CustomRenderAspectRatio and use the aspectRatioHeight and aspectRatioWidth properties to define any aspect ratio.

This is used for in-canvas render to allow you to use a different aspect ratio than what is implicitly defined by the size of the active viewport.

If this is set to CustomRenderAspectRatio, use the aspectRatioHeight and aspectRatioWidth to define the aspect ratio.

### aspectRatioHeight : integer [read-write]
Gets and sets the height of the aspect ratio of the rendered image. This is not the resolution, but only the aspect ratio. For example specifying the width and height of 4:3 is equivalent to setting 20:15. It's only the ratio of the numbers that matters.

The resolution is determined by the screen resolution when rendering in-canvas or is specified when rendering locally or using the cloud. When setting this property the aspectRatio property is automatically set to CustomRenderAspectRatio.

### aspectRatioWidth : integer [read-write]
Gets and sets the width of the aspect ratio of the rendered image. This is not the resolution, but only the aspect ratio. For example specifying the width and height of 4:3 is equivalent to setting 20:15. It's only the ratio of the numbers that matters.

The resolution is determined by the screen resolution when rendering in-canvas or is specified when rendering locally or using the cloud. When setting this property the aspectRatio property is automatically set to CustomRenderAspectRatio.

### backgroundEnvironment : RenderEnvironment [read-write]
Gets and sets the environment to use for the background. The available environments can be accessed through the RenderManager.renderEnvironments property.

Getting this property is only valid when the backgroundType property returns EnvironmentRenderSceneBackgroundType. Setting this property will automatically set the background type to EnvironmentRenderSceneBackgroundType.

### backgroundSolidColor : Color [read-write]
Gets and sets the background color. When this property is set, it defines the background to be a solid color. The opacity component of the color is ignored.

Getting this property is only valid when the backgroundType property returns SolidColorRenderSceneBackgroundType. Setting this property will automatically set the background type to SolidColorRenderSceneBackgroundType.

### backgroundType : RenderSceneBackgroundTypes [read-only]
Specifies the current type of background being used to render the scene. To change the background type use either the backgroundEnvironment or the backgroundSolidColor to set the environment or color.

### brightness : double [read-write]
Gets and sets the brightness or luminance of the scene. This must be a value between 0 and 100,000 and is in lux units.

### cameraExposure : double [read-write]
Gets and sets if the exposure of the camera as specified using the "Exposure Value" (EV). Valid values are between -15.0 and 25.0, inclusive.

### cameraFocalLength : double [read-write]
Gets and sets the focal length of the camera, specified in millimeters. Changing the perspective angle of the camera associated with the active viewport will also change the focal length. Focal length and perspective angle are two different ways to control the same setting.

### cameraType : CameraTypes [read-write]
Gets and sets the type of camera to use when rendering the scene.

### centerOfFocus : Point3D [read-write]
When the isDepthofFieldEnabled property is true, this point is used as the center of focus. All objects that are the same distance from the camera as this point will be in focus. Any geometry that is closer or further away from the camera than this point will appear more out of focus.

Setting this property has the side effect of setting the isDepthOfField property to true. If the isDepthOfFieldEnabled property is false, the value of this property is ignored.

### depthOfFieldBlur : double [read-write]
Specify the amount of blur to apply to objects outside the center of focus. This must be a value between 0.001 and 2.000 inclusive. The depth of field is defined by using the centerOfFocus property to set the depth where the model is in focus.

Setting this property has the side effect of setting the isDepthOfField property to true. If the isDepthOfFieldEnabled property is false, the value of this property is ignored.

### groundOffset : double [read-write]
Gets and sets the distance of the ground from the bottom of the model. A value of 0 is at the bottom of the model and a positive value moves the plane up and negative down. The value is in centimeters.

If the isGroundFlattened property is true, and a texture is being applied to the ground, the groundPosition property can be used to change both the offset and location of the texture on the ground. The lightAngle property controls the orientation of the texture.

### groundPosition : Point3D [read-write]
Gets and sets the origin of the projection of the environment onto the textured ground plane. This lets you position the environment relative to the model. This is only used when the isGroundFlattened property is true.

If the isGroundFlattened property is true, and a texture is being applied to the ground, the groundPosition property can be used to change both the offset and location of the texture on the ground. The lightAngle property controls the orientation of the texture.

### groundRoughness : double [read-write]
Gets and sets the roughness of the ground which controls the sharpness of the reflection. This is only used when the isGroundReflections property is true. This is a value between 0 and 1, where 0 is smooth and 1 is rough.

### isDepthOfFieldEnabled : boolean [read-write]
Gets and sets if the depth of field option is enabled. When setting this to true, use the centerOfFocus and depthOfFieldBlur properties to specify how the depth of field is defined.

### isGroundDisplayed : boolean [read-write]
Gets and sets if the ground plane is displayed. The plane allows shadows on the ground and reflections if the isGroundReflections property is true.

### isGroundFlattened : boolean [read-write]
Gets and sets if the ground plane is "textured" where the environment image is mapped as a texture.

### isGroundReflections : boolean [read-write]
Gets and sets if objects are reflected on the ground plane.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### lightAngle : double [read-write]
Specifies the rotation of the lighting. The angle is specified in Radians.

When the isGroundFlattened property is true, this also controls the angle of the texture that is applied to the ground. When the background is an environment, this controls the rotation of the environment relative to the model.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
