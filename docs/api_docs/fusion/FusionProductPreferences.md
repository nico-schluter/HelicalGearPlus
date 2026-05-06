# FusionProductPreferences
Namespace: adsk.fusion
Inherits: ProductPreferences
Since: August 2014

Fusion General Design Preferences

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### defaultDesignType : DefaultDesignTypeOptions [read-write]
Gets and sets the default modeling type setting

### defaultWorkspace : DefaultWorkspaces [read-write]
Gets and sets the Default workspace setting. (Model, Sculpt or Patch)

### is3DSketchingAllowed : boolean [read-write]
Gets and sets the Allow 3D sketching of lines and splines option which controls if 3D sketching is allowed or if sketching is forced to be on the x-y plane of the sketch.

### isActiveComponentVisibilityUsed : boolean [read-write]
Gets and sets the Active Component Visibility option

### isAllowReferencesDuringEditInPlace : boolean [read-write]
Gets and sets if you can create associative references while editing external components in context.

### isAutoHideSketchOnFeatureCreation : boolean [read-write]
Gets and sets if the sketch should be automatically hidden whenever a feature is created from it.

### isAutoLookAtSketch : boolean [read-write]
This function is retired. See more information in the 'Remarks' section below.

Gets and sets if the view is re-oriented to view the newly created sketch. This property has been replaced by the isAutoLookAtSketch2 property, which provides the full capabilities.

### isAutoLookAtSketch2 : AutoLookAtSketchSettings [read-write]
Gets and sets if the view is re-oriented to view the newly created sketch, and if it is re-oriented, if the camera uses the current camera settings or is orthographic.

### isAutoProjectEdgesOnReference : boolean [read-write]
Gets and sets if model edges should be automatically projected when creating constraints and dimensions in the active sketch when the orientation is normal to the active sketch plane.

### isAutoProjectGeometry : boolean [read-write]
Gets and Sets if geometry, not in the active sketch plane, is to be automatically projected.

### isDimensionEditedWhenCreated : boolean [read-write]
Gets and sets if dimension value is edited when the dimension is created.

### isEnableArrangeAndSimplifyTools : boolean [read-write]
Gets and sets if the Arrange, Remove Features, Remove Faces, and Replace with Primitives commands should be added to the Modify menu in the Design workspace.

### isFirstComponentGroundToParent : boolean [read-write]

### isGhostedResultBodyShown : boolean [read-write]
Gets and sets the Show ghosted result body option

### isJointPreviewAnimated : boolean [read-write]
Gets and sets the Animate joint preview option

### isSketchScaledWithFirstDimension : boolean [read-write]
Gets and sets if the sketch geometry is automatically scaled when the first dimension is added.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
Returns the name of this ProductPreferences object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
