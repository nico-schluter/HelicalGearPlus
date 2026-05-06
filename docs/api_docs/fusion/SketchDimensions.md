# SketchDimensions
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

A collection of the dimensions in a sketch. This object also supports the methods to add new sketch dimensions.

**Accessed from:** Sketch.sketchDimensions

## Methods

### addAngularDimension(lineOne: SketchLine, lineTwo: SketchLine, textPoint: Point3D, isDriving: boolean) -> SketchAngularDimension
Creates a new angular dimension constraint between the two input lines. The position of the text controls which of the four quadrants will be dimensioned.
- **lineOne** (SketchLine): The first SketchLine to dimension to.
- **lineTwo** (SketchLine): The second SketchLine to dimension to.
- **textPoint** (Point3D): A Point3D object that defines the position of the dimension text. The position of the text also defines which quadrant will be dimensioned.
- **isDriving** (boolean): Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.

This is an optional argument whose default value is True.
- **Returns** (SketchAngularDimension): Returns the newly created dimension or null if the creation failed.

### addConcentricCircleDimension(circleOne: SketchCurve, circleTwo: SketchCurve, textPoint: Point3D, isDriving: boolean) -> SketchConcentricCircleDimension
Creates a new dimension constraint between to concentric circles or arcs.
- **circleOne** (SketchCurve): The first SketchCircle or SketchArc to dimension.
- **circleTwo** (SketchCurve): The second SketchCircle or SketchArc to dimension.
- **textPoint** (Point3D): A Point3D object that defines the position of the dimension text.
- **isDriving** (boolean): Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.

This is an optional argument whose default value is True.
- **Returns** (SketchConcentricCircleDimension): Returns the newly created dimension or null if the creation failed.

### addDiameterDimension(entity: SketchCurve, textPoint: Point3D, isDriving: boolean) -> SketchDiameterDimension
Creates a new diameter dimension constraint on the arc or circle.
- **entity** (SketchCurve): The SketchCircle or SketchArc to dimension.
- **textPoint** (Point3D): A Point3D object that defines the position of the dimension text.
- **isDriving** (boolean): Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.

This is an optional argument whose default value is True.
- **Returns** (SketchDiameterDimension): Returns the newly created dimension or null if the creation failed.

### addDistanceBetweenLineAndPlanarSurfaceDimension(line: SketchLine, planarSurface: Base, isDriving: boolean) -> SketchDistanceBetweenLineAndPlanarSurfaceDimension
Creates a new linear dimension controlling the distance between a sketch line and the specified planar face or construction plane. The sketch line must lie on a plane that is parallel to the planar surface. The text position is automatically chosen and is positioned so it is midway between the line and surface and the extension lines are a minimum length. You can modify the position by using functionality on the returned SketchDistanceBetweenLineAndPlanarSurfaceDimension object.
- **line** (SketchLine): The SketchLine being constrained by the dimension.
- **planarSurface** (Base): The planar BRepFace or ConstructionPlane that the dimension will anchor to.
- **isDriving** (boolean): Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.

This is an optional argument whose default value is True.
- **Returns** (SketchDistanceBetweenLineAndPlanarSurfaceDimension): Returns the newly created dimension or null if the creation failed.

### addDistanceBetweenPointAndSurfaceDimension(point: SketchPoint, surface: Base, isDriving: boolean) -> SketchDistanceBetweenPointAndSurfaceDimension
Creates a new linear dimension controlling the distance between a sketch point and the specified surface or point. The text position is automatically chosen and is positioned so it is midway between the point and surface and the extension lines are a minimum length. You can modify the position by using functionality on the returned SketchDistanceBetweenPointAndSurfaceDimension object.
- **point** (SketchPoint): The SketchPoint being constrained by the dimension.
- **surface** (Base): The BRepFace or ConstructionPlane to which the dimension will anchor. Planar, cylindrical, spherical and conical faces are supported. If a cylindrical, spherical or conical face is used, the dimension is from the point to the nearest point on the surface.
- **isDriving** (boolean): Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.

This is an optional argument whose default value is True.
- **Returns** (SketchDistanceBetweenPointAndSurfaceDimension): Returns the newly created dimension or null if the creation failed.

### addDistanceDimension(pointOne: SketchPoint, pointTwo: SketchPoint, orientation: DimensionOrientations, textPoint: Point3D, isDriving: boolean) -> SketchLinearDimension
Creates a new linear dimension constraint between the two input entities.
- **pointOne** (SketchPoint): The first SketchPoint to dimension to.
- **pointTwo** (SketchPoint): The second SketchPoint to dimension to..
- **orientation** (DimensionOrientations): The orientation of the dimension.
- **textPoint** (Point3D): A Point3D object that defines the position of the dimension text.
- **isDriving** (boolean): Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.

This is an optional argument whose default value is True.
- **Returns** (SketchLinearDimension): Returns the newly created dimension or null if the creation failed.

### addEllipseMajorRadiusDimension(ellipse: SketchCurve, textPoint: Point3D, isDriving: boolean) -> SketchEllipseMajorRadiusDimension
Creates a new dimension constraint on the major radius of an ellipse.
- **ellipse** (SketchCurve): The SketchEllipse to dimension.
- **textPoint** (Point3D): A Point3D object that defines the position of the dimension text.
- **isDriving** (boolean): Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.

This is an optional argument whose default value is True.
- **Returns** (SketchEllipseMajorRadiusDimension): Returns the newly created dimension or null if the creation failed.

### addEllipseMinorRadiusDimension(ellipse: SketchCurve, textPoint: Point3D, isDriving: boolean) -> SketchEllipseMinorRadiusDimension
Creates a new dimension constraint on the minor radius of an ellipse.
- **ellipse** (SketchCurve): The SketchEllipse to dimension.
- **textPoint** (Point3D): A Point3D object that defines the position of the dimension text.
- **isDriving** (boolean): Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.

This is an optional argument whose default value is True.
- **Returns** (SketchEllipseMinorRadiusDimension): Returns the newly created dimension or null if the creation failed.

### addLinearDiameterDimension(centerLine: SketchLine, entityTwo: SketchEntity, textPoint: Point3D, isDriving: boolean) -> SketchLinearDiameterDimension
Creates a new linear dimension showing the diameter where the first line acts as the center line and the second entity defines the size. The first input entity must be a sketch line. The second entity can be a point or a line that is parallel to the first. The dimension controls the distance as measured perpendicular to the first input line.
- **centerLine** (SketchLine): The SketchLine to dimension to which acts as the center line.
- **entityTwo** (SketchEntity): The parallel SketchLine or SketchPoint to dimension to. If a SketchLine is used it must be parallel to the first line.
- **textPoint** (Point3D): A Point3D object that defines the position of the dimension text.
- **isDriving** (boolean): Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.

This is an optional argument whose default value is True.
- **Returns** (SketchLinearDiameterDimension): Returns the newly created dimension or null if the creation failed.

### addOffsetDimension(line: SketchLine, entityTwo: SketchEntity, textPoint: Point3D, isDriving: boolean) -> SketchOffsetDimension
Creates a new linear dimension constraint between the two input entities. The first input entity must be a sketch line. The second entity can be a point or a line that is parallel to the first. The dimension controls the distance as measured perpendicular to the first input line.
- **line** (SketchLine): The SketchLine to dimension to.
- **entityTwo** (SketchEntity): The parallel SketchLine or SketchPoint to dimension to. If a SketchLine is used it must be parallel to the first line.
- **textPoint** (Point3D): A Point3D object that defines the position of the dimension text.
- **isDriving** (boolean): Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.

This is an optional argument whose default value is True.
- **Returns** (SketchOffsetDimension): Returns the newly created dimension or null if the creation failed.

### addRadialDimension(entity: SketchCurve, textPoint: Point3D, isDriving: boolean) -> SketchRadialDimension
Creates a new radial dimension constraint on the arc or circle.
- **entity** (SketchCurve): The SketchCircle or SketchArc to dimension.
- **textPoint** (Point3D): A Point3D object that defines the position of the dimension text.
- **isDriving** (boolean): Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.

This is an optional argument whose default value is True.
- **Returns** (SketchRadialDimension): Returns the newly created dimension or null if the creation failed.

### addTangentDistanceDimension(entityOne: SketchEntity, isCloseToEnityTwo: boolean, entityTwo: SketchCurve, isCloseToEnityOne: boolean, textPoint: Point3D, isDriving: boolean) -> SketchTangentDistanceDimension
Creates a new linear dimension from between a line and circle or arc and a second circle or arc where the dimension is to the tangent on the edge of the circle or arc.
- **entityOne** (SketchEntity): The first entity to dimension to. This can be a SketchPoint, SketchLine, SketchCircle or SketchArc. If a circle or arc is provided then the tangentSideOne argument must be specified.
- **isCloseToEnityTwo** (boolean): If entityOne is a circle or arc this specifies which side of the circle or arc the dimension will be tangent to. If true, it will be on the side that is closer to entityTwo. If a SketchLine or SketchPoint was input for the entityOne argument this argument is ignored and any value can be used.
- **entityTwo** (SketchCurve): A SketchCircle or SketchArc entity that you will dimension to.
- **isCloseToEnityOne** (boolean): Specifies which side of the circle or arc input as the entityTwo argument the dimension will be tangent to. If true, it will be on the side that is closer to entityOne.
- **textPoint** (Point3D): A Point3D object that defines the position of the dimension text.
- **isDriving** (boolean): Optional argument that specifies if a driving (the dimension controls the geometry) or a driven (the geometry controls the dimension) dimension is created. If not provided a driving dimension will be created.

This is an optional argument whose default value is True.
- **Returns** (SketchTangentDistanceDimension): Returns the newly created dimension or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> SketchDimension
Function that returns the specified sketch dimension using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SketchDimension): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of sketch dimensions in the sketch.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **API Sample that demonstrates creating sketch lines in various ways.**: Demonstrates several ways to create sketch lines, including as the result of creating a rectangle.
- **SketchDimensions.addAngularDimension**: Demonstrates the SketchDimension.addAngularDimension method.
- **SketchDimensions.addConcentricCicleDimension**: Demonstrates the SketchDimension.addConcentricCircleDimension method.
- **SketchDimensions.addDiameterDimension**: Demonstrates the SketchDimension.addDiameterDimension method.
- **SketchDimensions.addDistanceDimension**: Demonstrates the SketchDimension.addDistanceDimension method.
- **SketchDimensions.AddEllipseMajorRadiusDimension**: Demonstrates the SketchDimension.addEllipseMajorRadiusDimension method.
- **SketchDimensions.AddEllipseMinorRadiusDimension**: Demonstrates the SketchDimension.addEllipseMinorRadiusDimension method.
- **SketchDimensions.addOffsetDimension**: Demonstrates the SketchDimension.addOffsetDimension method.
