# OrientedBoundingBox3D
Namespace: adsk.core
Inherits: Base
Since: December 2017

Transient object that represents an oriented 3D bounding box. An oriented 3D bounding box is a rectangular box that can be in any orientation in model space. They are created statically using the create method of the OrientedBoundingBox3D class and are used by some functions to return oriented box information.

**Accessed from:** BRepBody.orientedMinimumBoundingBox, Component.orientedMinimumBoundingBox, FlatPatternComponent.orientedMinimumBoundingBox, MeasureManager.getOrientedBoundingBox, MeshBody.orientedMinimumBoundingBox, Occurrence.orientedMinimumBoundingBox, OrientedBoundingBox3D.copy, OrientedBoundingBox3D.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### contains(point: Point3D) -> boolean
Determines if the specified point lies within the oriented bounding box.
- **point** (Point3D): The point to test containment with.
- **Returns** (boolean): Returns true if the point lies within the bounding box.

### copy() -> OrientedBoundingBox3D
Create a copy of this oriented bounding box.
- **Returns** (OrientedBoundingBox3D): Returns the new oriented bounding box copy.

### create(centerPoint: Point3D, lengthDirection: Vector3D, widthDirection: Vector3D, length: double, width: double, height: double) -> OrientedBoundingBox3D
Creates a transient oriented bounding box object.
- **centerPoint** (Point3D): The center point of the oriented box.
- **lengthDirection** (Vector3D): A Vector3D object that defines the direction of the length of the oriented bounding box. The magnitude of the vector is ignored and just the direction is used.
- **widthDirection** (Vector3D): A Vector3D object that defines the direction of the width of the oriented bounding box. The magnitude of the vector is ignored and just the direction is used. The width direction must be perpendicular to the length direction.
- **length** (double): The length of the oriented bounding box in centimeters.
- **width** (double): The width of the oriented bounding box in centimeters. The width of the box is always perpendicular to the length.
- **height** (double): The height of the oriented bounding box in centimeters. The height of the box is perpendicular to the length-width plane using the right-hand rule where you cross the length into the width.
- **Returns** (OrientedBoundingBox3D): Returns the new oriented bounding box.

### setOrientation(lengthDirection: Vector3D, widthDirection: Vector3D)
Sets the orientation of the oriented bounding box.
- **lengthDirection** (Vector3D): A Vector3D object that defines the direction of the length of the oriented bounding box. The magnitude of the vector is ignored and just the direction is used.
- **widthDirection** (Vector3D): A Vector3D object that defines the direction of the width of the oriented bounding box. The magnitude of the vector is ignored and just the direction is used. The width direction must be perpendicular to the length direction.

## Properties

### centerPoint : Point3D [read-write]
Gets and sets the centerPoint point of the oriented box.

### height : double [read-write]
Gets and sets the height of the oriented bounding box in centimeters.

### heightDirection : Vector3D [read-only]
Gets the direction of the height of the oriented bounding box. A unit vector is always returned.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### length : double [read-write]
Gets and sets the length of the oriented bounding box in centimeters.

### lengthDirection : Vector3D [read-only]
Gets the direction of the length of the oriented bounding box. A unit vector is always returned.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### width : double [read-write]
Gets and sets the width of the oriented bounding box in centimeters.

### widthDirection : Vector3D [read-only]
Gets the direction of the width of the oriented bounding box. A unit vector is always returned.

## Samples
- **Measure Sample**: Measure related functions
