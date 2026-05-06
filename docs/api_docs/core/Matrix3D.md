# Matrix3D
Namespace: adsk.core
Inherits: Base
Since: August 2014

Transient 3D 4x4 matrix. This object is a wrapper over 3D matrix data and is used as way to pass matrix data in and out of the API and as a convenience when operating on matrix data. They are created statically using the create method of the Matrix3D class.

**Accessed from:** AsBuiltJoint.transform, ConstructionPlane.transform, CustomGraphicsBRepBody.transform, CustomGraphicsCurve.transform, CustomGraphicsEntity.transform, CustomGraphicsGroup.transform, CustomGraphicsLines.transform, CustomGraphicsMesh.transform, CustomGraphicsPointSet.transform, CustomGraphicsText.transform, Decal.transform, DecalInput.transform, Joint.geometryOneTransform, Joint.geometryTwoTransform, JointOrigin.transform, Matrix3D.copy, Matrix3D.create, Matrix3DGraphNodeProperty.value, MoveFeature.transform, MoveFeatureFreeMoveDefinition.transform, MoveFeatureInput.transform, Occurrence.initialTransform, Occurrence.transform, Occurrence.transform2, OptimizedOrientationResult.transformation, PatternElement.transform, ProjectedTextureMapControl.transform, SectionAnalysis.initialPosition, SectionAnalysis.transform, SectionAnalysisInput.initialPosition, SectionAnalysisInput.transform, Setup.workCoordinateSystem, Sketch.transform, SVGImportOptions.transform, TextureMapControl3D.transform, TriadCommandInput.lastTransform, TriadCommandInput.positionTransform, TriadCommandInput.transform, Viewport.modelToViewSpaceTransform

## Methods

### asArray() -> double[]
Returns the contents of the matrix as a 16 element array.
- **Returns** (double[]): Returns the array of cell values.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy() -> Matrix3D
Creates an independent copy of this matrix.
- **Returns** (Matrix3D): Returns the new matrix copy.

### create() -> Matrix3D
Creates a transient 3d matrix object. It is initialized as an identity matrix and is created statically using the Matrix3D.create method.
- **Returns** (Matrix3D): Returns the new matrix.

### getAsCoordinateSystem(origin: Point3D, xAxis: Vector3D, yAxis: Vector3D, zAxis: Vector3D)
Gets the matrix data as the components that define a coordinate system.
- **origin** (Point3D): The output origin point of the coordinate system.
- **xAxis** (Vector3D): The output x axis direction of the coordinate system.
- **yAxis** (Vector3D): The output y axis direction of the coordinate system.
- **zAxis** (Vector3D): The output z axis direction of the coordinate system.

### getCell(row: integer, column: integer) -> double
Gets the value of the specified cell in the 4x4 matrix.
- **row** (integer): The index of the row. The first row has in index of 0
- **column** (integer): The index of the column. The first column has an index of 0
- **Returns** (double): The cell value at [row][column].

### invert() -> boolean
Inverts this matrix.
- **Returns** (boolean): Returns true if successful.

### isEqualTo(matrix: Matrix3D) -> boolean
Compares this matrix with another matrix and returns True if they're identical.
- **matrix** (Matrix3D): The matrix to compare this matrix to.
- **Returns** (boolean): Returns true if the matrices are equal.

### setCell(row: integer, column: integer, value: double) -> boolean
Sets the specified cell in the 4x4 matrix to the specified value.
- **row** (integer): The index of the row. The first row has in index of 0
- **column** (integer): The index of the column. The first column has an index of 0
- **value** (double): The new cell value.
- **Returns** (boolean): Returns true if successful.

### setToAlignCoordinateSystems(fromOrigin: Point3D, fromXAxis: Vector3D, fromYAxis: Vector3D, fromZAxis: Vector3D, toOrigin: Point3D, toXAxis: Vector3D, toYAxis: Vector3D, toZAxis: Vector3D) -> boolean
Sets this matrix to be the matrix that maps from the 'from' coordinate system to the 'to' coordinate system.
- **fromOrigin** (Point3D): The origin point of the from coordinate system.
- **fromXAxis** (Vector3D): The x axis direction of the from coordinate system.
- **fromYAxis** (Vector3D): The y axis direction of the from coordinate system.
- **fromZAxis** (Vector3D): The z axis direction of the from coordinate system.
- **toOrigin** (Point3D): The origin point of the to coordinate system.
- **toXAxis** (Vector3D): The x axis direction of the to coordinate system.
- **toYAxis** (Vector3D): The y axis direction of the to coordinate system.
- **toZAxis** (Vector3D): The z axis direction of the to coordinate system.
- **Returns** (boolean): Returns true if successful.

### setToIdentity() -> boolean
Resets this matrix to an identify matrix.
- **Returns** (boolean): Returns true if successful.

### setToRotateTo(from: Vector3D, to: Vector3D, axis: Vector3D) -> boolean
Sets to the matrix of rotation that would align the 'from' vector with the 'to' vector. The optional axis argument may be used when the two vectors are perpendicular and in opposite directions to specify a specific solution, but is otherwise ignored
- **from** (Vector3D): The vector to rotate from.
- **to** (Vector3D): The vector to rotate to.
- **axis** (Vector3D): The optional axis vector to disambiguate the rotation axis.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true if successful.

### setToRotation(angle: double, axis: Vector3D, origin: Point3D) -> boolean
Sets this matrix to the matrix of rotation by the specified angle, through the specified origin, around the specified axis
- **angle** (double): The rotation angle in radians.
- **axis** (Vector3D): The axis of rotation.
- **origin** (Point3D): The origin point of the axis of rotation.
- **Returns** (boolean): Returns true if successful.

### setWithArray(cells: double[]) -> boolean
Sets the contents of the array using a 16 element array.
- **cells** (double[]): The array of cell values.
- **Returns** (boolean): Returns true if successful.

### setWithCoordinateSystem(origin: Point3D, xAxis: Vector3D, yAxis: Vector3D, zAxis: Vector3D) -> boolean
Sets the matrix based on the components of a coordinate system.
- **origin** (Point3D): The origin point of the coordinate system.
- **xAxis** (Vector3D): The x axis direction of the coordinate system.
- **yAxis** (Vector3D): The y axis direction of the coordinate system.
- **zAxis** (Vector3D): The z axis direction of the coordinate system.
- **Returns** (boolean): Returns true if successful.

### transformBy(matrix: Matrix3D) -> boolean
Transforms this matrix using the input matrix.
- **matrix** (Matrix3D): The transformation matrix.
- **Returns** (boolean): Returns true if successful.

## Properties

### determinant : double [read-only]
Returns the determinant of the matrix.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### translation : Vector3D [read-write]
Gets and sets the translation component of the matrix.

## Samples
- **moveFeatures.add**: Demonstrates the moveFeatures.add method.
