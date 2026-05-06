# CustomGraphicsViewPlacement
Namespace: adsk.fusion
Inherits: Base
Since: September 2017

Positions custom graphics relative to one of the four corners of the view. Graphics positioned this way will always appear on top of the model graphics. This is typically used to display legends are small interactive tools.

**Accessed from:** CustomGraphicsBRepBody.viewPlacement, CustomGraphicsCurve.viewPlacement, CustomGraphicsEntity.viewPlacement, CustomGraphicsGroup.viewPlacement, CustomGraphicsLines.viewPlacement, CustomGraphicsMesh.viewPlacement, CustomGraphicsPointSet.viewPlacement, CustomGraphicsText.viewPlacement, CustomGraphicsViewPlacement.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(anchorPoint: Point3D, viewCorner: ViewCorners, viewPoint: Point2D) -> CustomGraphicsViewPlacement
Creates a new CustomGraphicsViewPlacement object that can be used when setting the viewPlacement property of a custom graphics entity to specify the billboarding behavior.
- **anchorPoint** (Point3D): The position within the defined graphics that will serve as the anchor. This is the location on the graphics that will be positioned at the specified view point.
- **viewCorner** (ViewCorners): Defines which of the four corners of the view the graphics are drawn relative to.
- **viewPoint** (Point2D): A 2D point in the view that defines the position of the graphics. This is relative to the corner and is in pixels. The x and y directions vary for each of the corners. These directions are only used to position the 2D point and do not affect the standard coordinate system the graphics were drawn in.

upperLeftViewCorner - The x direction is to the right and y is down.

upperRightViewCorner - The x direction is to the left and y is down.

lowerLeftViewCorner - The x direction is to the right and y is up.

lowerRightViewCorner - The x direction is to the left and y is up.
- **Returns** (CustomGraphicsViewPlacement): Returns the newly created CustomGraphicsViewPlacement object or null in the case of failure. This can then be assigned to any custom graphics entity using its viewPlacement property.

## Properties

### anchorPoint : Point3D [read-write]
Gets and sets the position within the defined graphics that serves as the anchor. This is the location on the graphics that is positioned at the specified view point.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### viewCorner : ViewCorners [read-write]
Gets and sets which corner the graphics are positioned relative to.

### viewPoint : Point2D [read-write]
A 2D point in the view that defines the position of the graphics. This is relative to the corner and is in pixels. The x and y directions vary for each of the corners. These directions are only used to position the 2D point and do not affect the standard coordinate system the graphics were drawn in.

upperLeftViewCorner - The x direction is to the right and y is down.

upperRightViewCorner - The x direction is to the left and y is down.

lowerLeftViewCorner - The x direction is to the right and y is up.

lowerRightViewCorner - The x direction is to the left and y is up.
