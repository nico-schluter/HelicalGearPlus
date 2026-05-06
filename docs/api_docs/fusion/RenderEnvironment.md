# RenderEnvironment
Namespace: adsk.fusion
Inherits: Base
Since: May 2023

A render environment that is used when defining the scene for rendering. You see these in the user interface in the "Environment Library" tab of the "Scene Settings" dialog. Use this with the backgroundEnvironment property of the SceneSettings object to set a render environment. For a custom render environment, use the loadCustomEnvironment method to statically create a custom environment and assign it to the backgroundEnvironment property.

**Accessed from:** RenderEnvironment.loadCustomEnvironment, RenderEnvironments.item, RenderEnvironments.itemById, RenderEnvironments.itemByName, SceneSettings.backgroundEnvironment

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### loadCustomEnvironment(fullFilename: string)
Statically creates a RenderEnvironment which can be used to set the environment for a scene using the SceneSettings.backgroundEnvironment property.

## Properties

### id : string [read-only]
The internal ID of the environment.

### isCustomEnvironment : boolean [read-only]
Returns true if this environment is a custom environment.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
The name of the environment.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
