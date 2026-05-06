# Arc2D
Namespace: adsk.core
Inherits: Curve2D
Since: August 2014

Transient 2D arc. A transient arc is not displayed or saved in a document. Transient arcs are used as a wrapper to work with raw 2D arc information. They are created statically using one of the create methods supported by the Arc2D class.

**Accessed from:** Arc2D.copy, Arc2D.createByCenter, Arc2D.createByThreePoints

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Arc2D
Creates and returns an independent copy of this Arc2D object.
- **Returns** (Arc2D): Returns a new Arc2D object that is a copy of this Arc2D object.

### createByCenter(center: Point2D, radius: double, startAngle: double, endAngle: double, isClockwise: boolean) -> Arc2D
Creates a transient 2D arc object specifying the center, radius and start and end angles. A transient arc is not displayed or saved in a document. Transient arcs are used as a wrapper to work with raw 2D arc information.
- **center** (Point2D): A Point2D object that defines the center position of the arc in 2D space.
- **radius** (double): The radius of the arc.
- **startAngle** (double): The start angle in radians, where 0 is along the X-axis.
- **endAngle** (double): The end angle in radians, where 0 is along the X-axis.
- **isClockwise** (boolean): Specifies if the sweep of the arc is clockwise or counterclockwise from the start to end angle.

This is an optional argument whose default value is False.
- **Returns** (Arc2D): Returns the newly created arc or null if the creation failed.

### createByThreePoints(startPoint: Point2D, point: Point2D, endPoint: Point2D) -> Arc2D
Creates a transient 2D arc by specifying 3 points. A transient arc is not displayed or saved in a document. Transient arcs are used as a wrapper to work with raw 2D arc information.
- **startPoint** (Point2D): The start point of the arc.
- **point** (Point2D): A point along the arc.
- **endPoint** (Point2D): The end point of the arc.
- **Returns** (Arc2D): Returns the newly created arc or null if the creation failed.

### getData(center: Point2D, radius: double, startAngle: double, endAngle: double, isClockwise: boolean) -> boolean
Gets all of the data defining the arc.
- **center** (Point2D): The output center point of the arc.
- **radius** (double): The output radius of the arc.
- **startAngle** (double): The output start angle of the arc in radians, where 0 is along the x axis.
- **endAngle** (double): The output end angle of the arc in radians, where 0 is along the x axis.
- **isClockwise** (boolean): The output value that indicates if the sweep direction is clockwise or counterclockwise.
- **Returns** (boolean): Returns true if successful

### set(center: Point2D, radius: double, startAngle: double, endAngle: double, isClockwise: boolean) -> boolean
Sets all of the data defining the arc.
- **center** (Point2D): A Point2D object defining the center position of the arc.
- **radius** (double): The radius of the arc.
- **startAngle** (double): The start angle of the arc in radians, where 0 is along the x axis.
- **endAngle** (double): The end angle of the arc in radians, where 0 is along the x axis.
- **isClockwise** (boolean): Indicates if the sweep direction is clockwise or counterclockwise.
- **Returns** (boolean): Returns true if redefining the arc is successful

### transformBy(matrix: Matrix2D) -> boolean
Transforms this curve in 2D space.
- **matrix** (Matrix2D): A 2D matrix that defines the transform to apply to the curve.
- **Returns** (boolean): Return true if the transform was successful.

## Properties

### asNurbsCurve : NurbsCurve2D [read-only]
Returns a NURBS curve that is geometrically identical to the arc.

### center : Point2D [read-write]
Gets and sets the center position of the arc.

### curveType : Curve2DTypes [read-only]
Returns the type of geometry this curve represents.

### endAngle : double [read-write]
Gets and sets the end angle of the arc in radians, where 0 is along the x axis.

### endPoint : Point2D [read-only]
Gets the position of the end point of the arc.

### evaluator : CurveEvaluator2D [read-only]
Returns an evaluator object that lets you perform additional evaluations on the curve.

### isClockwise : boolean [read-only]
Gets if the sweep direction of the arc is clockwise or counterclockwise.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### radius : double [read-write]
Gets and sets the radius of the arc.

### startAngle : double [read-write]
Gets and sets the start angle of the arc in radians, where 0 is along the x axis.

### startPoint : Point2D [read-only]
Gets the position of the start point of the arc.
