# Matrix2D
Namespace: adsk.core
Inherits: Base
Since: August 2014

Transient 2D 3x3 matrix. This object is a wrapper over 2D matrix data and is used as way to pass matrix data in and out of the API and as a convenience when operating on matrix data. They are created statically using the create method of the Matrix2D class.

**Accessed from:** Canvas.transform, CanvasInput.transform, Matrix2D.copy, Matrix2D.create

## Methods

### asArray() -> double[]
Returns the contents of the matrix as a 9 element array.
- **Returns** (double[]): Returns the array of matrix values.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Matrix2D
Creates an independent copy of this matrix.
- **Returns** (Matrix2D): Returns the new matrix copy.

### create() -> Matrix2D
Creates a transient 2D matrix (3x3) object. It is initialized as an identity matrix.
- **Returns** (Matrix2D): Returns the new matrix.

### getAsCoordinateSystem(origin: Point2D, xAxis: Vector2D, yAxis: Vector2D)
Gets the matrix data as the components that define a coordinate system.
- **origin** (Point2D): The output origin point of the coordinate system.
- **xAxis** (Vector2D): The output x axis direction of the coordinate system.
- **yAxis** (Vector2D): The output y axis direction of the coordinate system.

### getCell(row: integer, column: integer) -> double
Gets the value of the specified cell in the 3x3 matrix.
- **row** (integer): The index of the row. The first row has in index of 0
- **column** (integer): The index of the column. The first column has an index of 0
- **Returns** (double): Returns the value at [row][column].

### invert() -> boolean
Invert this matrix.
- **Returns** (boolean): Returns true if successful.

### isEqualTo(matrix: Matrix2D) -> boolean
Compares this matrix with another matrix and returns True if they're identical.
- **matrix** (Matrix2D): The matrix to compare to.
- **Returns** (boolean): Returns true if the matrix is equal to this matrix.

### setCell(row: integer, column: integer, value: double) -> boolean
Sets the specified cell in the 3x3 matrix to the specified value.
- **row** (integer): The index of the row. The first row has in index of 0
- **column** (integer): The index of the column. The first column has an index of 0
- **value** (double): The new value of the cell.
- **Returns** (boolean): Returns true if successful.

### setToAlignCoordinateSystems(fromOrigin: Point2D, fromXAxis: Vector2D, fromYAxis: Vector2D, toOrigin: Point2D, toXAxis: Vector2D, toYAxis: Vector2D) -> boolean
Sets this matrix to be the matrix that maps from the 'from' coordinate system to the 'to' coordinate system.
- **fromOrigin** (Point2D): The origin point of the from coordinate system.
- **fromXAxis** (Vector2D): The x axis direction of the from coordinate system.
- **fromYAxis** (Vector2D): The y axis direction of the from coordinate system.
- **toOrigin** (Point2D): The origin point of the to coordinate system.
- **toXAxis** (Vector2D): The x axis direction of the to coordinate system.
- **toYAxis** (Vector2D): The y axis direction of the to coordinate system.
- **Returns** (boolean): Returns true if successful.

### setToIdentity() -> boolean
Resets this matrix to be an identity matrix.
- **Returns** (boolean): Returns true if successful.

### setToRotateTo(from: Vector2D, to: Vector2D) -> boolean
Sets to the matrix of rotation that would align the 'from' vector with the 'to' vector.
- **from** (Vector2D): The from vector.
- **to** (Vector2D): The to vector.
- **Returns** (boolean): Returns true if successful.

### setToRotation(angle: double, origin: Point2D) -> boolean
Sets this matrix to the matrix of rotation by the specified angle, through the specified origin.
- **angle** (double): The rotation angle in radians.
- **origin** (Point2D): The origin point of the rotation.
- **Returns** (boolean): Returns true if successful.

### setWithArray(cells: double[]) -> boolean
Sets the contents of the array using a 9 element array.
- **cells** (double[]): The array of cell values.
- **Returns** (boolean): Returns true if successful.

### setWithCoordinateSystem(origin: Point2D, xAxis: Vector2D, yAxis: Vector2D) -> boolean
Reset this matrix to align with a specific coordinate system.
- **origin** (Point2D): The origin point of the coordinate system.
- **xAxis** (Vector2D): The x axis direction of the coordinate system.
- **yAxis** (Vector2D): The y axis direction of the coordinate system.
- **Returns** (boolean): Returns true if successful.

### transformBy(matrix: Matrix2D) -> boolean
Transforms this matrix using the input matrix.
- **matrix** (Matrix2D): The transformation matrix.
- **Returns** (boolean): Returns true if successful.

## Properties

### determinant : double [read-only]
Returns the determinant of the matrix.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
