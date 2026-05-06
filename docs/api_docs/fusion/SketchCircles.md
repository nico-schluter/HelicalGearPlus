# SketchCircles
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

The collection of circles in a sketch. This provides access to the existing circles and supports the methods to create new circles.

**Accessed from:** SketchCurves.sketchCircles

## Methods

### addByCenterRadius(centerPoint: Base, radius: double) -> SketchCircle
Creates a sketch circle that is always parallel to the x-y plane of the sketch and is centered at the specified point.
- **centerPoint** (Base): The center point of the circle. It can be an existing SketchPoint or a Point3D object.
- **radius** (double): The radius of the circle in centimeters.
- **Returns** (SketchCircle): Returns the newly created SketchCircle object or null if the creation failed.

### addByThreePoints(pointOne: Point3D, pointTwo: Point3D, pointThree: Point3D) -> SketchCircle
Creates a sketch circle that passes through the three points. The three points must lie on the x-y plane of the sketch.
- **pointOne** (Point3D): The first point that the circle will pass through. The z component must be zero.
- **pointTwo** (Point3D): The second point that the circle will pass through. The z component must be zero.
- **pointThree** (Point3D): The third point that the circle will pass through. The z component must be zero.
- **Returns** (SketchCircle): Returns the newly created SketchCircle object or null if the creation failed.

### addByThreeTangents(tangentOne: SketchLine, tangentTwo: SketchLine, tangentThree: SketchLine, hintPoint: Point3D) -> SketchCircle
Creates a sketch circle that is tangent to the three input lines. The three lines must lie on the x-y plane of the sketch.
- **tangentOne** (SketchLine): The first line that the circle will be tangent to. The line must lie on the x-y plane of the sketch and cannot be parallel to the second or third line.
- **tangentTwo** (SketchLine): The second line that the circle will be tangent to. The line must lie on the x-y plane of the sketch and cannot be parallel to the first or third line.
- **tangentThree** (SketchLine): The third line that the circle will be tangent to. The line must lie on the x-y plane of the sketch and cannot be parallel to the first or second line.
- **hintPoint** (Point3D): A point that specifies which of the possible multiple solutions to use when creating the circle. If you consider the three input lines to be infinite there are many possible solutions when creating a circle that is tangent to all three lines. The hint point is a point anywhere within the area defined by the three lines where the circle is to be created.
- **Returns** (SketchCircle): Returns the newly created SketchCircle object or null if the creation failed.

### addByTwoPoints(pointOne: Point3D, pointTwo: Point3D) -> SketchCircle
Creates a sketch circle where the circle passes through the two points and the distance between the two points is the diameter of the circle.
- **pointOne** (Point3D): A Point3D object that defines a point is sketch space and lies on the x-y plane of the sketch.
- **pointTwo** (Point3D): A Point3D object that defines a point is sketch space and lies on the x-y plane of the sketch.
- **Returns** (SketchCircle): Returns the newly created SketchCircle object or null if the creation failed.

### addByTwoTangents(tangentOne: SketchLine, tangentTwo: SketchLine, radius: double, hintPoint: Point3D) -> SketchCircle
Creates a sketch circle that is tangent to the two input lines. The two lines must lie on the x-y plane of the sketch.
- **tangentOne** (SketchLine): The first line that the circle will be tangent to. The line must lie on the x-y plane of the sketch.
- **tangentTwo** (SketchLine): The second line that the circle will be tangent to. The line must lie on the x-y plane of the sketch and cannot be parallel to the first line.
- **radius** (double): The radius of the circle in centimeters.
- **hintPoint** (Point3D): A point that specifies which of the possible four solutions to use when creating the circle. If you consider the two input lines to be infinite they create four quadrants which results in four possible solutions for the creation of the circle. The hint point is a point anywhere within the quadrant where you want the circle created.
- **Returns** (SketchCircle): Returns the newly created SketchCircle object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SketchCircle
Function that returns the specified sketch circle using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SketchCircle): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of circles in the sketch.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Create circle by center and radius API Sample**: Demonstrates creating a sketch circle by the center and radius.
- **Create Circle By 3 Tangents API Sample**: Creates three lines and then draws a circle that is tangent to the lines. It then creates tangent constraints to maintain that relationship.
- **Loft Feature API Sample**: Demonstrates creating a new loft feature.
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
- **Simple Extrusion Sample**: Creates a new extrusion feature, resulting in a new component.
- **Simple Revolve Feature Sample**: Creates a new revolve feature, resulting in a new component.
- **SketchCircles.addByCenterRadius**: Demonstrates the SketchCircles.addByCenterRadius method.
- **SketchCircles.addByThreePoints**: Demonstrates the SketchCircles.addByThreePoints method.
- **SketchCircles.addByThreeTangents**: Demonstrates the SketchCircles.addByThreeTangets method.
- **SketchCircles.addByTwoPoints**: Demonstrates the SketchCircles.addByTwoPoints method.
- **SketchCircles.addByTwoTangents**: Demonstrates the SketchCircles.addByTwoTangets method.
