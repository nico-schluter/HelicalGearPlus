# BoundingBox2D
Namespace: adsk.core
Inherits: Base
Since: August 2014

Transient object that represents a 2D bounding box. A 2D bounding box is a rectangle box that is parallel to the x and y axes. The box is defined by a minimum point (smallest x-y values) and maximum point (largest x-y values). This object is a wrapper for these points and serves as a way to pass bounding box information in and out of functions. It also provides some convenience function when working with the bounding box data. They are created statically using the create method of the BoundingBox2D class.

**Accessed from:** ArrangePlaneResultEnvelope.boundingBox, BoundingBox2D.copy, BoundingBox2D.create, ConstructionPlane.displayBounds, SurfaceEvaluator.parametricRange

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### combine(boundingBox: BoundingBox2D) -> boolean
Combines this bounding box with the input bounding box. If the input bounding box extends outside this bounding box then this bounding box will be extended to encompass both of the original bounding boxes.
- **boundingBox** (BoundingBox2D): The other bounding box. It is not edited but is used to extend the boundaries of the bounding box the method is being called on.
- **Returns** (boolean): Returns true if the combine was successful.

### contains(point: Point2D) -> boolean
Determines if the specified point lies within the bounding box.
- **point** (Point2D): The point to test containment with.
- **Returns** (boolean): Returns true if the point lies within the bounding box.

### copy() -> BoundingBox2D
Create a copy of this bounding box.
- **Returns** (BoundingBox2D): Returns the new bounding box copy.

### create(minPoint: Point2D, maxPoint: Point2D) -> BoundingBox2D
Creates a transient bounding box object.
- **minPoint** (Point2D): The minimum point of the box.
- **maxPoint** (Point2D): The maximum point of the box.
- **Returns** (BoundingBox2D): Returns the new bounding box.

### expand(point: Point2D) -> boolean
Expand this bounding box to contain the specified point.
- **point** (Point2D): The point to expand the box to.
- **Returns** (boolean): Returns true if successful.

### intersects(boundingBox: BoundingBox2D) -> boolean
Test if this bounding box intersects with the specified bounding box.
- **boundingBox** (BoundingBox2D): The bounding box to test intersection with.
- **Returns** (boolean): Returns true if the bounding boxes intersect.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maxPoint : Point2D [read-write]
Gets and sets the maximum point of the box.

### minPoint : Point2D [read-write]
Gets and sets the minimum point of the box.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
