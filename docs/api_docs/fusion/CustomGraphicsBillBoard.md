# CustomGraphicsBillBoard
Namespace: adsk.fusion
Inherits: Base
Since: September 2017

Used to specify if the orientation of custom graphics are defined relative to the screen instead of model space. This is commonly used for legends and symbols that you want to always face the user, even as the camera is rotated.

**Accessed from:** CustomGraphicsBillBoard.create, CustomGraphicsBRepBody.billBoarding, CustomGraphicsCurve.billBoarding, CustomGraphicsEntity.billBoarding, CustomGraphicsGroup.billBoarding, CustomGraphicsLines.billBoarding, CustomGraphicsMesh.billBoarding, CustomGraphicsPointSet.billBoarding, CustomGraphicsText.billBoarding

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(anchorPoint: Point3D) -> CustomGraphicsBillBoard
Creates a new CustomGraphicsBillBoard object that can be used when calling the billBoarding property of the CustomGraphicsEntity object to specify the billboarding behavior of some custom graphics. Once created you can assign it to a custom graphics entity using its billBoarding property.
- **anchorPoint** (Point3D): The parameter must be input and can be null but the value is ignored. Use of the anchor point has been retired and it is no longer used.
- **Returns** (CustomGraphicsBillBoard): Returns the newly created CustomGraphicsBillBoard object or null in the case of failure. This can be assigned to a custom graphics entity using its billBoarding property.

## Properties

### anchorPoint : Point3D [read-write]
RETIRED - This property has been retired. It is not needed since the matrix defined for the CustomGraphicsText object defines the position and anchor for the billboarded text. Getting the value of this property will return a point at the origin. Setting this property will be ignored.
Specifies the coordinate in model or view space that the graphics will anchor to. For graphics that represent a label, this will typically be the point where the label attaches to the model. A CustomGraphicsAnchorPoint can be created using the static create method on the CustomGraphicsAnchorPoint object.

### axis : Vector3D [read-write]
When the billBoardStyle property is set to AxialBillBoardStyle, this is used to control the direction of the graphics. Otherwise it uses the x axis of the view.

### billBoardStyle : CustomGraphicsBillBoardStyles [read-write]
Specifies the type of billboarding to use. When a new CustomGraphicsBillBoard object is created this defaults to ScreenBillBoardStyle so the graphics will all be facing the view plane. It can also be set to an arbitrary plane by setting this to AxialBillBoardStyle and can be defined so that it never appear backwards by setting it to RightReadingBillBoardStyle.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
