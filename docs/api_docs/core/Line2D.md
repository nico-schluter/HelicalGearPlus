# Line2D
Namespace: adsk.core
Inherits: Curve2D
Since: August 2014

Transient 2D line. A transient line is not displayed or saved in a document. Transient 2D lines are used as a wrapper to work with raw 2D line information. They are created statically using the create method of the Line2D class.

**Accessed from:** Line2D.copy, Line2D.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Line2D
Creates and returns a copy of this line object.
- **Returns** (Line2D): Returns an independent copy of this line object.

### create(startPoint: Point2D, endPoint: Point2D) -> Line2D
Creates a transient line.
- **startPoint** (Point2D): The start point of the line
- **endPoint** (Point2D): The end point of the line
- **Returns** (Line2D): Returns the new Line2D object or null if the creation failed.

### getData(startPoint: Point2D, endPoint: Point2D) -> boolean
Gets all of the data defining the line segment.
- **startPoint** (Point2D): The output start point of the line.
- **endPoint** (Point2D): The output end point of the line.
- **Returns** (boolean): Returns true if successful.

### set(startPoint: Point2D, endPoint: Point2D) -> boolean
Sets all of the data defining the line segment.
- **startPoint** (Point2D): The start point of the line
- **endPoint** (Point2D): The end point of the line
- **Returns** (boolean): Returns true if redefining the line is successful

### transformBy(matrix: Matrix2D) -> boolean
Transforms this curve in 2D space.
- **matrix** (Matrix2D): A 2D matrix that defines the transform to apply to the curve.
- **Returns** (boolean): Return true if the transform was successful.

## Properties

### asNurbsCurve : NurbsCurve2D [read-only]
Returns a NURBS curve that is geometrically identical to the line.

### curveType : Curve2DTypes [read-only]
Returns the type of geometry this curve represents.

### endPoint : Point2D [read-write]
Gets and sets the end point of the line.

### evaluator : CurveEvaluator2D [read-only]
Returns an evaluator object that lets you perform additional evaluations on the curve.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### startPoint : Point2D [read-write]
Gets and sets the start point of the line.
