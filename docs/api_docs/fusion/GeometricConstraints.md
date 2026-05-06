# GeometricConstraints
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

A collection of all of the geometric constraints in a sketch. This object also supports the methods to create new geometric constraints.

**Accessed from:** Sketch.geometricConstraints

## Methods

### addCircularPattern(input: CircularPatternConstraintInput) -> CircularPatternConstraint
Creates a new circular pattern in the sketch.
- **input** (CircularPatternConstraintInput): A CircularPatternConstraintInput object that defines the desired circular pattern. Use the createCircularPatternInput method to create a new CircularPatternConstraintInput object and then use methods on it to define the circular pattern.
- **Returns** (CircularPatternConstraint): Returns the newly created CircularPatternConstraint object or null if the creation failed.

### addCoincident(point: SketchPoint, entity: SketchEntity) -> CoincidentConstraint
Creates a new coincident constraint between two entities. The first argument is a sketch point. The second argument is a sketch curve or point.
- **point** (SketchPoint): The SketchPoint that will be made coincident.
- **entity** (SketchEntity): The SketchPoint or sketch curve that the point will be made coincident to.
- **Returns** (CoincidentConstraint): Returns the newly created CoincidentConstraint object or null if the creation failed.

### addCoincidentToSurface(point: SketchPoint, surface: Base) -> CoincidentToSurfaceConstraint
Creates a new coincident constraint between the sketch point and surface. This forces the point to lie on the surface.
- **point** (SketchPoint): The SketchPoint to constrain to the surface.
- **surface** (Base): The BRepFace or ConstructionPlane the point will be coincident to.
- **Returns** (CoincidentToSurfaceConstraint): Returns the newly created CoincidentToSurfaceConstraint object or null if the creation failed.

### addCollinear(lineOne: SketchLine, lineTwo: SketchLine) -> CollinearConstraint
Creates a new collinear constraint between two lines.
- **lineOne** (SketchLine): The first line to create the constraint on.
- **lineTwo** (SketchLine): The second line to create the constraint on.
- **Returns** (CollinearConstraint): Returns the newly created CollinearConstraint object or null if the creation failed.

### addConcentric(entityOne: SketchCurve, entityTwo: SketchCurve) -> ConcentricConstraint
Creates a new concentric constraint between two circles, arcs, ellipses, or elliptical arcs.
- **entityOne** (SketchCurve): The first circle, arc, ellipse or elliptical arc.
- **entityTwo** (SketchCurve): The second circle, arc, ellipse or elliptical arc.
- **Returns** (ConcentricConstraint): Returns the newly created ConcentricConstraint object or null if the creation failed.

### addEqual(curveOne: SketchCurve, curveTwo: SketchCurve) -> EqualConstraint
Creates a new equal constraint between two lines, or between arcs and circles.
- **curveOne** (SketchCurve): The first line, arc, or circle.
- **curveTwo** (SketchCurve): The second line, arc, or circle.
- **Returns** (EqualConstraint): Returns the newly created EqualConstraint object or null if the creation failed.

### addHorizontal(line: SketchLine) -> HorizontalConstraint
Creates a new horizontal constraint on a line.
- **line** (SketchLine): The line to constrain horizontally.
- **Returns** (HorizontalConstraint): Returns the newly created HorizontalConstraint object or null if the creation failed.

### addHorizontalPoints(pointOne: SketchPoint, pointTwo: SketchPoint) -> HorizontalPointsConstraint
Creates a new horizontal constraint between two points.
- **pointOne** (SketchPoint): The first SketchPoint to constrain horizontally.
- **pointTwo** (SketchPoint): The second SketchPoint to constrain horizontally.
- **Returns** (HorizontalPointsConstraint): Returns the newly created HorizontalPointsConstraint object or null if the creation failed.

### addLineOnPlanarSurface(line: SketchLine, planarSurface: Base) -> LineOnPlanarSurfaceConstraint
Creates a new constraint that forces the sketch line to lie on a planar surface.
- **line** (SketchLine): The SketchLine to constrain to the surface.
- **planarSurface** (Base): The planar BRepFace or CosntructionPlane the sketch line will lie on.
- **Returns** (LineOnPlanarSurfaceConstraint): Returns the newly created LineOnPlanarSurfaceConstraint object or null if the creation failed.

### addLineParallelToPlanarSurface(line: SketchLine, planarSurface: Base) -> LineParallelToPlanarSurfaceConstraint
Creates a new parallel constraint between a sketch line and a planar surface that will constrain the line to lie on a plane parallel to the specified surface.
- **line** (SketchLine): The SketchLine to constrain to the surface.
- **planarSurface** (Base): The planar BRepFace or CosntructionPlane the sketch line will be parallel to.
- **Returns** (LineParallelToPlanarSurfaceConstraint): Returns the newly created LineParallelToPlanarSurfaceConstraint object or null if the creation failed.

### addMidPoint(point: SketchPoint, midPointCurve: SketchCurve) -> MidPointConstraint
Creates a new midpoint constraint between a point and a curve.
- **point** (SketchPoint): The point to constrain to the midpoint of a curve.
- **midPointCurve** (SketchCurve): The curve that defines the midpoint to constraint to.
- **Returns** (MidPointConstraint): Returns the newly created MidPointConstraint object or null if the creation failed.

### addOffset(curves: SketchCurve[], offset: ValueInput, basePoint: Point3D) -> OffsetConstraint
This function is retired. See more information in the 'Remarks' section below.

Creates an offset constraint, which results in creating a new set of curves that are an offset of the input curves. The returned offset constraint provides access to the created curves and the parameter controlling the offset.

The offset direction is implied by the flow direction of the provided curves. For example, if two connected lines are offset, the flow direction is from line 1 to line 2. A positive offset value creates the offset curve to the "right" of the lines and a negative offset goes to the "left". Left and right are evaluated with respect to the geometry. If you are standing on line 1 looking towards line 2 your left and right are the offset left and right. For closed single curves like circles and ellipses their flow direction is always counterclockwise so a positive offset is always to the outsides.
- **curves** (SketchCurve[]): A set of end connected curves. The Sketch.FindConnectedCurves method is a convenient way to get this set of curves.
- **offset** (ValueInput): The value that defines the offset. This is a ValueInput object so it can be a float value to define the offset in centimeters or it can be a string defining an expression that will be used by the dimension that controls the offset.
- **basePoint** (Point3D): The location on one of the curves where the offset dimension will be created.
- **Returns** (OffsetConstraint): The created OffsetConstraint. You can use properties on the constraint to get information about the offset.

### addOffset2(input: OffsetConstraintInput) -> OffsetConstraint
Creates an offset constraint, which results in creating a new set of curves that are an offset of the input curves. The returned offset constraint object provides access to the created curves and the parameter controlling the offset.
- **input** (OffsetConstraintInput): The OffsetConstraintInput object that defines the offset to create.
- **Returns** (OffsetConstraint): Returns the newly created OffsetConstraint object or null if the creation failed.

### addParallel(lineOne: SketchLine, lineTwo: SketchLine) -> ParallelConstraint
Creates a new parallel constraint between two lines.
- **lineOne** (SketchLine): The first SketchLine.
- **lineTwo** (SketchLine): The second SketchLine.
- **Returns** (ParallelConstraint): Returns the newly created ParallelConstraint object or null if the creation failed.

### addPerpendicular(lineOne: SketchLine, lineTwo: SketchLine) -> PerpendicularConstraint
Creates a new perpendicular constraint between two lines.
- **lineOne** (SketchLine): The first SketchLine.
- **lineTwo** (SketchLine): The second SketchLine.
- **Returns** (PerpendicularConstraint): Returns the newly created PerpendicularConstraint object or null if the creation failed.

### addPerpendicularToSurface(curve: SketchCurve, surface: Base) -> PerpendicularToSurfaceConstraint
Creates a new perpendicular constraint that forces the sketch curve to be perpendicular to the specified surface. Line and spline curves are supported.
- **curve** (SketchCurve): The SketchCurve to constrain to the surface.
- **surface** (Base): The BRepFace or ConstructionPlane the line will be perpendicular to.
- **Returns** (PerpendicularToSurfaceConstraint): Returns the newly created PerpendicularToSurfaceConstraint object or null if the creation failed.

### addPolygon(lines: SketchLine[]) -> PolygonConstraint
Creates a polygon constraint on existing lines in the sketch.
- **lines** (SketchLine[]): An array of existing SketchLine objects in this sketch that define a valid polygon. They must be the same length, connect at their endpoints, have the same angle between them, and define a closed shape. The order of the lines within the array does not matter.
- **Returns** (PolygonConstraint): Returns the created PolygonConstraint or null if the creation failed.

### addRectangularPattern(input: RectangularPatternConstraintInput)
Creates a new rectangular pattern in the sketch.
- **input** (RectangularPatternConstraintInput): A RectangularPatternConstraintInput object that defines all of inputs required to create the desired rectangular pattern. Use the createRectangularPatternInput method to create the input object.

### addSmooth(curveOne: SketchCurve, curveTwo: SketchCurve) -> SmoothConstraint
Creates a new smooth constraint between two curves. One of the curves must be a spline. The other curve can be a spline or any other type of curve.
- **curveOne** (SketchCurve): The first curve to be constrained to be smooth to the second curve.
- **curveTwo** (SketchCurve): The second curve to be constrained to be smooth to the first curve.
- **Returns** (SmoothConstraint): Returns the newly created SmoothConstraint object or null if the creation failed.

### addSymmetry(entityOne: SketchEntity, entityTwo: SketchEntity, symmetryLine: SketchLine) -> SymmetryConstraint
Creates a new symmetry constraint.
- **entityOne** (SketchEntity): The first sketch entity to be symmetric.
- **entityTwo** (SketchEntity): The second sketch entity to be symmetric. It must be the same type as the first entity.
- **symmetryLine** (SketchLine): The SketchLine that defines the axis of symmetry.
- **Returns** (SymmetryConstraint): Returns the newly created SymmetryConstraint object or null if the creation failed.

### addTangent(curveOne: SketchCurve, curveTwo: SketchCurve) -> TangentConstraint
Creates a new tangent constraint between two curves.
- **curveOne** (SketchCurve): The first curve to be tangent.
- **curveTwo** (SketchCurve): The second curve to be tangent.
- **Returns** (TangentConstraint): Returns the newly created TangentConstraint object or null if the creation failed.

### addTwoSidesOffset(input: OffsetConstraintInput, linkOffsets: boolean) -> OffsetConstraint
Creates two offset constraints, which results in creating two new sets of curves that are an offset of the input curves on each side of the original set of curves. The returned offset constraint objects provide access to the created curves and the parameters controlling the offsets.
- **input** (OffsetConstraintInput): The OffsetConstraintInput object that defines the offset to create. The same definition applies to both offsets that are created.
- **linkOffsets** (boolean): Defines if the parameter driving the offset of the second side should reference the parameter of the first side. This sets up the parameters so if the first side is edited, the second side will automatically update using the same value. A value of true will create the linked parameter.
- **Returns** (OffsetConstraint): Returns an array containing the two OffsetConstraint objects or errors if the creation failed.

### addVertical(line: SketchLine) -> VerticalConstraint
Creates a new vertical constraint on a line.
- **line** (SketchLine): The line to constrain vertically.
- **Returns** (VerticalConstraint): Returns the newly created VerticalConstraint object or null if the creation failed.

### addVerticalPoints(pointOne: SketchPoint, pointTwo: SketchPoint) -> VerticalPointsConstraint
Creates a new vertical constraint between two points.
- **pointOne** (SketchPoint): The first SketchPoint to constrain vertically.
- **pointTwo** (SketchPoint): The second SketchPoint to constrain vertically.
- **Returns** (VerticalPointsConstraint): Returns the newly created VerticalPointsConstraint object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createCircularPatternInput(inputEntities: SketchEntity[], centerPoint: SketchPoint) -> CircularPatternConstraintInput
Creates a CircularPatternConstraintInput object. Use properties and methods on this object to define the circular pattern you want to create and then use the Add method, passing in the CircularPatternConstraintInput object.
- **inputEntities** (SketchEntity[]): An array of sketch entities to be patterned. All of the entities must be from the current sketch.
- **centerPoint** (SketchPoint): A SketchPoint from the same sketch that defines the center of the pattern.
- **Returns** (CircularPatternConstraintInput): Returns the newly created CircularPatternConstraintInput object or null if the creation failed.

### createOffsetInput(curves: SketchCurve[], offset: ValueInput) -> OffsetConstraintInput
Creates an OffsetConstraintInput object. Use properties and methods on this object to define the offset you want to create and then use the addOffset2 method, passing in the OffsetConstraintInput object, to create the offset.
- **curves** (SketchCurve[]): A set of end connected curves. The Sketch.FindConnectedCurves method is a convenient way to get this set of curves.
- **offset** (ValueInput): The value that defines the offset. This is a ValueInput object so it can be a float value to define the offset in centimeters or it can be a string defining an expression that will be used by the parameter controlling the offset. A positive offset value creates the offset curve to the "right" and a negative offset value goes to the "left".

The flow direction of the provided curves implies the offset direction. For example, if two connected lines are offset, the flow direction is from line 1 to line 2. Left and right are evaluated relative to the input geometry. If you are standing on line 1 and looking towards line 2, the offset's left side is on your left, and the right side is to your right. Closed single curves like circles and ellipses always have a counterclockwise flow, so a positive offset is always to the outside. For closed splines, the positive direction is based on the spline's parameterization.
- **Returns** (OffsetConstraintInput): Returns an OffsetConstraintInput object or null in the case of invalid input.

### createRectangularPatternInput(entities: SketchEntity[], distanceType: PatternDistanceType) -> RectangularPatternConstraintInput
Creates a new RectangularPatternConstraintInput object. Use this object to define the various settings associated with a rectangular pattern in a sketch. Once the pattern is defined you can call the addRectangularPattern method and pass in the input object to create the sketch rectangular pattern.
- **entities** (SketchEntity[]): An array of sketch entities to pattern. These can be sketch points and curves.
- **distanceType** (PatternDistanceType): Specifies if the distances defined for the pattern define the overall size of the pattern or the distance between the rows and columns.
- **Returns** (RectangularPatternConstraintInput): Returns the created RectangularPatternsConstraintInput object or null in the case of failure.

### item(index: uinteger) -> GeometricConstraint
Function that returns the specified sketch constraint using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (GeometricConstraint): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of constraints in the sketch.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **API Sample that demonstrates creating sketch lines in various ways.**: Demonstrates several ways to create sketch lines, including as the result of creating a rectangle.
- **GeometricConstraints.addConcentric**: Demonstrates the GeometricConstraints.addConcentric method.
