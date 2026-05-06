# BoundingBox3D
Namespace: adsk.core
Inherits: Base
Since: August 2014

Transient object that represents a 3D bounding box. It defines a rectangular box whose sides are parallel to the model space x, y, and z planes. Because of the fixed orientation of the box it can be fully defined by two points at opposing corners; the min and max points. This object is usually used to provide a rough approximation of the volume in space that an entity occupies. It also provides some convenience function when working with the bounding box data. They are created statically using the create method of the BoundingBox3D class.

**Accessed from:** Arrange3DResultEnvelope.boundingBox, BoundingBox3D.copy, BoundingBox3D.create, BRepBody.boundingBox, BRepBody.preciseBoundingBox, BRepEdge.boundingBox, BRepFace.boundingBox, BRepLoop.boundingBox, BRepLump.boundingBox, BRepShell.boundingBox, Component.boundingBox, Component.boundingBox2, Component.preciseBoundingBox, CustomGraphicsBRepBody.boundingBox, CustomGraphicsCurve.boundingBox, CustomGraphicsEntity.boundingBox, CustomGraphicsGroup.boundingBox, CustomGraphicsLines.boundingBox, CustomGraphicsMesh.boundingBox, CustomGraphicsPointSet.boundingBox, CustomGraphicsText.boundingBox, FaceGroup.boundingBox, FlatPatternComponent.boundingBox, FlatPatternComponent.boundingBox2, FlatPatternComponent.preciseBoundingBox, MeshBody.boundingBox, Occurrence.boundingBox, Occurrence.boundingBox2, Occurrence.preciseBoundingBox, Profile.boundingBox, ProfileCurve.boundingBox, Sketch.boundingBox, SketchArc.boundingBox, SketchCircle.boundingBox, SketchConicCurve.boundingBox, SketchControlPointSpline.boundingBox, SketchCurve.boundingBox, SketchEllipse.boundingBox, SketchEllipticalArc.boundingBox, SketchEntity.boundingBox, SketchFittedSpline.boundingBox, SketchFixedSpline.boundingBox, SketchLine.boundingBox, SketchPoint.boundingBox, SketchText.boundingBox

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### combine(boundingBox: BoundingBox3D) -> boolean
Combines this bounding box with the input bounding box. If the input bounding box extends outside this bounding box then this bounding box will be extended to encompass both of the original bounding boxes.
- **boundingBox** (BoundingBox3D): The other bounding box. It is not edited but is used to extend the boundaries of the bounding box the method is being called on.
- **Returns** (boolean): Returns true if the combine was successful.

### contains(point: Point3D) -> boolean
Determines if the specified point is within the bound box.
- **point** (Point3D): The point you want to check to see if it's in the bounding box.
- **Returns** (boolean): Returns true if the point is within the bounding box.

### copy() -> BoundingBox3D
Creates an independent copy of this bounding box.
- **Returns** (BoundingBox3D): Returns the new bounding box or null if the copy failed.

### create(minPoint: Point3D, maxPoint: Point3D) -> BoundingBox3D
Creates a transient bounding box object. This object is created statically using the BoundingBox3D.create method.
- **minPoint** (Point3D): The point that defines the minimum corner of the bounding box.
- **maxPoint** (Point3D): The point that defines the maximum corner of the bounding box.
- **Returns** (BoundingBox3D): Returns the newly created bounding box or null if the creation failed.

### expand(point: Point3D) -> boolean
Expands the size of bounding box to include the specified point.
- **point** (Point3D): The point to include within the bounding box.
- **Returns** (boolean): Returns true if the expansion was successful.

### intersects(boundingBox: BoundingBox3D) -> boolean
Determines if the two bounding boxes intersect.
- **boundingBox** (BoundingBox3D): The other bounding box to check for intersection with.
- **Returns** (boolean): Returns true if the two boxes intersect.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maxPoint : Point3D [read-write]
Gets and sets the maximum point corner of the box.

### minPoint : Point3D [read-write]
Gets and sets the minimum point corner of the box.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Rendering Sample**: Demonstrates using the Rendering capabilities in the API. This starts a series of local renderings to generate a series of frames, where the camera is repositioned and a parameter is modified for each frame to create a dynamic animation. To use the sample, have a design open that contains a parameter named "Length". It can be a user or model parameter. The sample will modify this parameter from a value of 0.1 cm to 15 cm, but you can change these values by editing the values of the paramStartVal and paramEndVal variables on lines 90 and 91 of the sample. It expects a folder named "C:\Temp\RenderSample" to exist, and will fail if it doesn't. The rendered frames will be written to that folder.
An example rendering is shown below where this file was used. The parameter is modifying a move feature which results in changing the shape of an extrusion. The parameter could be driving anything and you could modify the code to edit more than one parameter. The result of this sample is a folder containing all of the rendered frames. You can process these to create an animation. The sample animation was created using GIMP.
