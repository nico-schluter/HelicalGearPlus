# SketchLines
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

The collection of lines in a sketch. This provides access to the existing lines and supports the methods to create new lines.

**Accessed from:** SketchCurves.sketchLines

## Methods

### addAngleChamfer(firstLine: SketchLine, firstLinePoint: Point3D, secondLine: SketchLine, secondLinePoint: Point3D, distance: double, angle: double) -> SketchLine
Creates a chamfer between two sketch lines. In the case where the two input lines cross each other creating an "X" shape, this results in four quadrants where the chamfer can be placed. The point arguments are used to define which of the four quadrants the chamfer should be created in. The two points define which side of the two lines should be kept and the other end will be trimmed by the chamfer. The easiest way to use this is to use the end points of the lines on the side you want to keep. In the case where the lines don't intersect or connect at the end points, there is only one valid quadrant for the chamfer so the points are ignored.
- **firstLine** (SketchLine): The first line you want to chamfer.
- **firstLinePoint** (Point3D): A point on the first line that is on the side of the intersection with the second line that you want to keep.
- **secondLine** (SketchLine): The second line you want to chamfer.
- **secondLinePoint** (Point3D): A point on the second line that is on the side of the intersection with the first line that you want to keep.
- **distance** (double): Defines the distance of the start point of the chamfer from the intersection point of the two lines along the first line. The distance is defined in centimeters.
- **angle** (double): Defines the angle of the chamfer as measured from the first line. The angle is defined in radians.
- **Returns** (SketchLine): Returns the newly created SketchLine object that represents the chamfer or null if the creation failed.

### addByMidpoint(midPoint: Base, secondPoint: Base) -> SketchLine
Creates a sketch line where the first point is the midpoint and the second point is one endpoint. The system automatically calculates the other endpoint to create a line where the first point is exactly at the midpoint.
- **midPoint** (Base): The midpoint of the line. It can be a SketchPoint or Point3D object.
- **secondPoint** (Base): One endpoint of the line. It can be a SketchPoint or Point3D object. The other endpoint will be calculated automatically.
- **Returns** (SketchLine): Returns the newly created SketchLine object or null if the creation failed.

### addByTwoPoints(startPoint: Base, endPoint: Base) -> SketchLine
Creates a sketch line between the two input points. The input points can be either existing SketchPoints or Point3D objects. If a SketchPoint is used the new line will be based on that sketch point and update if the sketch point is modified.
- **startPoint** (Base): The start point of the line. It can be a SketchPoint or Point3D object.
- **endPoint** (Base): The end point of the line. It can be a SketchPoint or Point3D object.
- **Returns** (SketchLine): Returns the newly created SketchLine object or null if the creation failed.

### addCenterPointRectangle(centerPoint: Point3D, cornerPoint: Base) -> SketchLineList
Creates four sketch lines representing a rectangle where the first point represents the center of the rectangle. The second point is the corner of the rectangle and can be either an existing SketchPoint or Point3D object. The four sketch lines are returned.
- **centerPoint** (Point3D): The center point of the rectangle
- **cornerPoint** (Base): The corner of the rectangle. It can be a SketchPoint or Point3D object.
- **Returns** (SketchLineList): Returns the four new sketch lines or null if the creation failed.

### addDistanceChamfer(firstLine: SketchLine, firstLinePoint: Point3D, secondLine: SketchLine, secondLinePoint: Point3D, distanceOne: double, distanceTwo: double) -> SketchLine
Creates a chamfer between two sketch lines. In the case where the two input lines cross each other creating an "X" shape, this results in four quadrants where the chamfer can be placed. The point arguments are used to define which of the four quadrants the chamfer should be created in. The two points define which side of the two lines should be kept and the other end will be trimmed by the chamfer. The easiest way to use this is to use the end points of the lines on the side you want to keep. In the case where the lines don't intersect or connect at the end points, there is only one valid quadrant for the chamfer so the points are ignored.
- **firstLine** (SketchLine): The first line you want to chamfer.
- **firstLinePoint** (Point3D): A point on the first line that is on the side of the intersection with the second line that you want to keep.
- **secondLine** (SketchLine): The second line you want to chamfer.
- **secondLinePoint** (Point3D): A point on the second line that is on the side of the intersection with the first line that you want to keep.
- **distanceOne** (double): Defines the distance of the start point of the chamfer line from the intersection point of the two lines along the first line. The distance is defined in centimeters.
- **distanceTwo** (double): Defines the distance of the start point of the chamfer line from the intersection point of the two lines along the second line. The distance is defined in centimeters.
- **Returns** (SketchLine): Returns the newly created SketchLine object that represents the chamfer or null if the creation failed.

### addEdgePolygon(pointOne: Base, pointTwo: Base, isRight: boolean, edgeCount: integer) -> SketchLineList
Creates a polygon where two points specify an edge of the polygon. By specifying an edge, the size and position of the polygon is also defined.
- **pointOne** (Base): The first point of the edge.
- **pointTwo** (Base): The second point of the edge.
- **isRight** (boolean): After defining points one and two, a polygon can be created on either side of the line defined by the two points. This argument specifies which side of the line the polygon will be created on. If this is true, the polygon will be created to the right of the line from the perspective of looking from point one to point two. If false, it will be to the left of the line.
- **edgeCount** (integer): The number of edges in the resulting polygon.
- **Returns** (SketchLineList): Returns a list of the sketch lines that were created to represent the polygon or null in the case of bad input.

### addScribedPolygon(centerPoint: Base, edgeCount: integer, angle: double, radius: double, isInscribed: boolean) -> SketchLineList
Creates either an inscribed or circumscribed n-sided polygon.
- **centerPoint** (Base): Either an existing SketchPoint or a Point3D object that defines the center point of the polygon. If a SketchPoint object is provided the point will continue to control the center of the polygon.
- **edgeCount** (integer): The number of edges in the resulting polygon.
- **angle** (double): Controls the rotation of the polygon around the center point. For a circumscribed polygon, this defines where the center of one of the edges will be positioned. For an inscribed polygon, this defines where one of the corners of the polygon will be positioned.
- **radius** (double): The radius of the circle in centimeters that the polygon goes to, either outside (circumscribed) or inside (inscribed) the circle.
- **isInscribed** (boolean): Specifies if a circumscribed or inscribed polygon should be created.
- **Returns** (SketchLineList): Returns a list of the sketch lines that were created to represent the polygon or null in the case of bad input.

### addThreePointRectangle(pointOne: Base, pointTwo: Base, pointThree: Point3D) -> SketchLineList
Creates four sketch lines representing a rectangle where the first two points are the base corners of the rectangle and the third point defines the height.
- **pointOne** (Base): The first corner of the rectangle. It can be a SketchPoint or Point3D object.
- **pointTwo** (Base): The first corner of the rectangle. It can be a SketchPoint or Point3D object.
- **pointThree** (Point3D): The first corner of the rectangle. a Point3D object defining the height of the rectangle.
- **Returns** (SketchLineList): Returns the four new sketch lines or null if the creation failed.

### addTwoPointRectangle(pointOne: Base, pointTwo: Base) -> SketchLineList
Creates four sketch lines representing a rectangle where the two points are the opposing corners of the rectangle. The input points can be either existing SketchPoints or Point3D objects. If a SketchPoint is used the new lines will be based on that sketch point and update if the sketch point is modified.
- **pointOne** (Base): The first corner of the rectangle. It can be a SketchPoint or Point3D object.
- **pointTwo** (Base): The second corner of the rectangle. It can be a SketchPoint or Point3D object.
- **Returns** (SketchLineList): Returns the four new sketch lines or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SketchLine
Function that returns the specified sketch line using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SketchLine): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of lines in the sketch.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **API Sample that demonstrates creating sketch lines in various ways.**: Demonstrates several ways to create sketch lines, including as the result of creating a rectangle.
- **Simple Revolve Feature Sample**: Creates a new revolve feature, resulting in a new component.
- **SketchLines.addAngleChamfer**: Demonstrates the SketchLines.addAngleChamfer method.
- **SketchLines.addByTwoPoints**: Demonstrates the SketchLines.addByTwoPoints method.
- **SketchLines.addCenterPointRectangle**: Demonstrates the SketchLines.addCenterPointRectangle method.
- **SketchLines.addDistanceChamfer**: Demonstrates the SketchLines.addDistanceChamfer method.
- **SketchLines.addThreePointRectangle**: Demonstrates the SketchLines.addThreePointRectangle method.
- **SketchLines.addTwoPointRectangle**: Demonstrates the SketchLines.addTwoPointRectangle method.
