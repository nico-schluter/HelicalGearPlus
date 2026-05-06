# CanvasEffects
Namespace: adsk.core
Inherits: Base
Since: May 2025

Provides access to the settings that control the canvas effects.

**Accessed from:** GraphicsPreferences.canvasEffects

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isAmbientOcclusionEnabled : boolean [read-write]
Gets and sets if ambient occlusion is enabled. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.

Application.preferences.graphicsPreferences.graphicsPreset

### isAntiAliasingEnabled : boolean [read-write]
Gets and sets if antialiasing is enabled. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.

Application.preferences.graphicsPreferences.graphicsPreset

### isEnvironmentDomeEnabled : boolean [read-write]
Gets and sets if the environment dome is enabled. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.

Application.preferences.graphicsPreferences.graphicsPreset

### isGroundPlaneEnabled : boolean [read-write]
Gets and sets if the ground plane is enabled. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.

Application.preferences.graphicsPreferences.graphicsPreset

### isGroundReflectionEnabled : boolean [read-write]
Gets and sets if ground reflection is enabled. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.

Application.preferences.graphicsPreferences.graphicsPreset

### isGroundShadowEnabled : boolean [read-write]
Gets and sets if the ground shadow is enabled. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.

Application.preferences.graphicsPreferences.graphicsPreset

### isObjectShadowEnabled : boolean [read-write]
Gets and sets if object shadows is enabled. Setting this property is only valid when the graphics preset is set to "custom" and will fail if it is set to "quality" or "performance". The graphics preset can be determined by using the graphicsPreset property, as shown below.

Application.preferences.graphicsPreferences.graphicsPreset

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
