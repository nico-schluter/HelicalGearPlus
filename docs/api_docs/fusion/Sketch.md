# Sketch
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Represents a sketch within a component.

**Accessed from:** AutoConstrainInput.parentSketch, BaseFeature.sketches, CircularPatternConstraint.parentSketch, CoincidentConstraint.parentSketch, CoincidentToSurfaceConstraint.parentSketch, CollinearConstraint.parentSketch, ConcentricConstraint.parentSketch, EqualConstraint.parentSketch, GeometricConstraint.parentSketch, HorizontalConstraint.parentSketch, HorizontalPointsConstraint.parentSketch, LineOnPlanarSurfaceConstraint.parentSketch, LineParallelToPlanarSurfaceConstraint.parentSketch, MidPointConstraint.parentSketch, OffsetConstraint.parentSketch, ParallelConstraint.parentSketch, PerpendicularConstraint.parentSketch, PerpendicularToSurfaceConstraint.parentSketch, PolygonConstraint.parentSketch, Profile.parentSketch, ProfileCurve.parentSketch, RectangularPatternConstraint.parentSketch, Sketch.createForAssemblyContext, Sketch.nativeObject, SketchAngularDimension.parentSketch, SketchArc.parentSketch, SketchCircle.parentSketch, SketchConcentricCircleDimension.parentSketch, SketchConicCurve.parentSketch, SketchControlPointSpline.parentSketch, SketchCurve.parentSketch, SketchDiameterDimension.parentSketch, SketchDimension.parentSketch, SketchDistanceBetweenLineAndPlanarSurfaceDimension.parentSketch, SketchDistanceBetweenPointAndSurfaceDimension.parentSketch, SketchEllipse.parentSketch, SketchEllipseMajorRadiusDimension.parentSketch, SketchEllipseMinorRadiusDimension.parentSketch, SketchEllipticalArc.parentSketch, SketchEntity.parentSketch, Sketches.add, Sketches.addToBaseOrFormFeature, Sketches.addWithoutEdges, Sketches.item, Sketches.itemByName, SketchFittedSpline.parentSketch, SketchFixedSpline.parentSketch, SketchLine.parentSketch, SketchLinearDiameterDimension.parentSketch, SketchLinearDimension.parentSketch, SketchOffsetCurvesDimension.parentSketch, SketchOffsetDimension.parentSketch, SketchPoint.parentSketch, SketchRadialDimension.parentSketch, SketchTangentDistanceDimension.parentSketch, SketchText.parentSketch, SmoothConstraint.parentSketch, SymmetryConstraint.parentSketch, TangentConstraint.parentSketch, VerticalConstraint.parentSketch, VerticalPointsConstraint.parentSketch

## Methods

### addCenterPointSlot(centerPoint: Base, endPoint: Base, width: ValueInput, createWidthDimension: boolean, halfLength: ValueInput, angle: ValueInput) -> Base
Creates the geometry that represents a slot where the first point defines the center of the slot and the second point defines the direction and half-length. Geometric constraints are automatically added to the geometry to maintain the slot shape and optionally, dimensions to control the size can be added. The created geometry and constraints are returned.
- **centerPoint** (Base): The center point of the slot. It can be a SketchPoint or Point3D object. If a SketchPoint is provided a coincident constraint will be created between the center point of the slot and the provided sketch point.
- **endPoint** (Base): A point that defines the direction and half-length of the slot. It can be a SketchPoint or Point3D object. The distance from the center point to this point represents half the total length of the slot. If a SketchPoint is provided a coincident constraint is created between the end point of the slot and the provided sketch point.

If the halfLength or angle arguments are provided, the point is not the actual end point but is used to determine the direction of the slot. If both the halfLength and angle arguments are provided this endPoint will be ignored and null can be provided.
- **width** (ValueInput): A ValueInput object that defines the width of the slot. The ValueInput can define either a real value or an expression string. If it is a real value, it defines the width of the slot in centimeters.

When using a ValueInput created using a string, it's the same as creating a parameter in the user-interface. You can specify any valid expression, i.e. "5", "5 in", "5 in / 2", "5 + Length" that defines a length.
- **createWidthDimension** (boolean): Specifies if a dimension constraint and its associated parameter is created to control the width of the slot.

This is an optional argument whose default value is False.
- **halfLength** (ValueInput): Optional argument that defines half the length of the slot using a ValueInput. If this is provided, it overrides the endPoint distance and explicitly defines half the length of the slot. If the half length is specified, a dimension constraint and its associated parameter is created to control the length.

The ValueInput can define either a real value or an expression string. If it is a real value, it defines half the length of the slot in centimeters. When it is an expression string, it's the same as creating a parameter in the user-interface. You can specify any valid expression, i.e. "2.5", "2.5 in", "5 in / 4", "HalfLength" that defines a length.

This is an optional argument whose default value is null.
- **angle** (ValueInput): Optional argument that defines the angle of the slot using a ValueInput. If this is provided, it overrides the endPoint and explicitly defines the angle of the slot. If the angle is specified, a horizontal construction line, a dimension constraint, and its associated parameter is created to control the angle. The angle is measured from a horizontal line that starts at the center point and goes in the positive X direction. The angle is always less than 180 deg. and depending on the location of the direction point, the angle will be clockwise or counterclockwise from the horizontal line.

The ValueInput can define either a real value or an expression string. If it is a real value, it defines the angle of the slot in radians. When it is an expression string, it's the same as creating a parameter in the user-interface. You can specify any valid expression, i.e. "45", "45 deg", "180 / 3", "Sweep * 2" that defines an angle.

This is an optional argument whose default value is null.
- **Returns** (Base): Returns an array containing the start point arc, the end point arc, the two lines that define the slot, the construction line between the start and end point, and optionally, the construction line the angle is measured from if an angle is specified, and the dimension constraints that were created in the order of width, half length, and angle.

### addCenterToCenterSlot(startPoint: Base, endPoint: Base, width: ValueInput, createWidthDimension: boolean, length: ValueInput, angle: ValueInput) -> Base
Creates the geometry that represents a slot. Geometric constraints are automatically added to the geometry to maintain the slot shape and optionally, dimensions to control the size can be added. The created geometry and constraints are returned.
- **startPoint** (Base): The start point of the slot. It can be a SketchPoint or Point3D object. If a SketchPoint is provided a coincident constraint will be created between the start point of the slot and the provided sketch point.
- **endPoint** (Base): The end point of the slot. It can be a SketchPoint or Point3D object. This point defines the length of the slot. If a SketchPoint is provided a coincident constraint is created between the end point of the slot and the provided sketch point.

If the length or angle arguments are provided, the point is not the actual end point but is used to determine the direction of the slot. If both the length and angle arguments are provided this endPoint will be ignored and null can be provided.
- **width** (ValueInput): A ValueInput object that defines the width of the slot. The ValueInput can define either a real value or an expression string. If it is a real value, it defines the width of the slot in centimeters.

When using a ValueInput created using a string, it's the same as creating a parameter in the user-interface. You can specify any valid expression, i.e. "5", "5 in", "5 in / 2", "5 + Length" that defines a length.
- **createWidthDimension** (boolean): Specifies if a dimension constraint and its associated parameter is created to control the width of the slot.

This is an optional argument whose default value is False.
- **length** (ValueInput): Optional argument that defines the length of the slot using a ValueInput. If this is provided, it overrides the endPoint and explicitly defines the length of the slot. If the length is specified, a dimension constraint and its associated parameter is created to control the length.

The ValueInput can define either a real value or an expression string. If it is a real value, it defines the length of the slot in centimeters. When it is an expression string, it's the same as creating a parameter in the user-interface. You can specify any valid expression, i.e. "5", "5 in", "5 in / 2", "5 + Length" that defines a length.

This is an optional argument whose default value is null.
- **angle** (ValueInput): Optional argument that defines the angle of the slot using a ValueInput. If this is provided, it overrides the endPoint and explicitly defines the angle of the slot. If the angle is specified, a horizontal construction line, a dimension constraint, and its associated parameter is created to control the angle. The angle is measured from a horizontal line that starts at that start point and goes in the positive X direction. The angle is always less than 180 deg. and depending on the location of the end point, the angle will be clockwise or counterclockwise from the horizontal line.

The ValueInput can define either a real value or an expression string. If it is a real value, it defines the angle of the slot in radians. When it is an expression string, it's the same as creating a parameter in the user-interface. You can specify any valid expression, i.e. "45", "45 deg", "180 / 3", "Sweep * 2" that defines an angle.

This is an optional argument whose default value is null.
- **Returns** (Base): Returns an array containing the start point arc, the end arc, the two lines that define the slot, the construction line between the two points, and optionally, the construction line the angle is measured from if an angle is specified, and the dimension constraints that were created in the order of width, length, and angle.

### addOverallSlot(startPoint: Base, endPoint: Base, width: ValueInput, createWidthDimension: boolean, length: ValueInput, angle: ValueInput) -> Base
Creates the geometry that represents an overall slot. Geometric constraints are automatically added to the geometry to maintain the slot shape and optionally, dimensions to control the size can be added. The created geometry and constraints are returned.
- **startPoint** (Base): The start point of the slot. It can be a SketchPoint or Point3D object. If a SketchPoint is provided a coincident constraint will be created between the start point of the slot and the provided sketch point.
- **endPoint** (Base): The end point of the slot. It can be a SketchPoint or Point3D object. This point defines the length of the slot. If a SketchPoint is provided a coincident constraint is created between the end point of the slot and the provided sketch point.

If either the length or angle argument is provided, the point is not the actual end point but is used to determine the direction of the slot. If both the length and angle arguments are provided this endPoint will be ignored and null can be provided.
- **width** (ValueInput): A ValueInput object that defines the width of the slot. The ValueInput can define either a real value or an expression string. If it is a real value, it defines the width of the slot in centimeters.

When using a ValueInput created using a string, it's the same as creating a parameter in the user-interface. You can specify any valid expression, i.e. "5", "5 in", "5 in / 2", "5 + Length" that defines a length.
- **createWidthDimension** (boolean): Specifies if a dimension constraint and its associated parameter is created to control the width of the slot.

This is an optional argument whose default value is False.
- **length** (ValueInput): Optional argument that defines the overall length of the slot using a ValueInput. If this is provided, it overrides the endPoint and explicitly defines the length of the slot. If the length is specified, a dimension constraint and its associated parameter is created to control the length.

The ValueInput can define either a real value or an expression string. If it is a real value, it defines the length of the slot in centimeters. When it is an expression string, it's the same as creating a parameter in the user-interface. You can specify any valid expression, i.e. "5", "5 in", "5 in / 2", "5 + Length" that defines a length.

This is an optional argument whose default value is null.
- **angle** (ValueInput): Optional argument that defines the angle of the slot using a ValueInput. If this is provided, it overrides the endPoint and explicitly defines the angle of the slot. If the angle is specified, a horizontal construction line, a dimension constraint, and its associated parameter is created to control the angle. The angle is measured from a horizontal line that starts at the start point and goes in the positive X direction. The angle is always less than 180 deg. and depending on the location of the end point, the angle will be clockwise or counterclockwise from the horizontal line.

The ValueInput can define either a real value or an expression string. If it is a real value, it defines the angle of the slot in radians. When it is an expression string, it's the same as creating a parameter in the user-interface. You can specify any valid expression, i.e. "45", "45 deg", "180 / 3", "Sweep * 2" that defines an angle.

This is an optional argument whose default value is null.
- **Returns** (Base): Returns an array containing the start point arc, the end point arc, the two lines that define the slot, the construction line between the two points, and optionally, the construction line the angle is measured from if an angle is specified, and the dimension constraints that were created in the order of length, angle and width.

### autoConstrain(input: AutoConstrainInput) -> AutoConstrainResult
Auto constrains the sketch using the information provided by the input object. This returns a single locally computed solution.
- **input** (AutoConstrainInput): The AutoConstrainInput object that defines the various settings to use when fully constraining the sketch. The input object must be associated with this sketch (created by this sketch's createAutoConstrainInput method).
- **Returns** (AutoConstrainResult): Returns an AutoConstrainResult object where information about how the sketch was constrained can be obtained. Returns null in the case of a failure or if the input is invalid.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### copy(sketchEntities: ObjectCollection, transform: Matrix3D, targetSketch: Sketch) -> ObjectCollection
Copies the specified sketch entities, applying the specified transform. Any geometric or dimension constraints associated with the entities will automatically be copied, if possible. For example, if there is a horizontal dimension and the transform defines a rotation then it will not be included in the result. This same behavior can be seen when performing a copy/paste operation in the user interface.
- **sketchEntities** (ObjectCollection): The collection of sketch entities to copy. They must all exist in this sketch.
- **transform** (Matrix3D): The transform to apply to the copied entities.
- **targetSketch** (Sketch): Optionally specifies the sketch to copy the entities to. If not provided the entities are copied to this sketch.

This is an optional argument whose default value is null.
- **Returns** (ObjectCollection): Returns a collection of the new sketch entities that were created as a result of the copy.

### createAutoConstrainInput() -> AutoConstrainInput
Creates a new AutoConstrainInput object associated with this sketch. The input object is used to define the various options when adding dimension and geometric constraints to help constrain a sketch. The returned object has all options defined with default values and additional constraints can be applied by passing this into the autoConstrain method.
- **Returns** (AutoConstrainInput): Returns the newly created AutoConstrainInput object. Validation of sketch suitability (entity count, entitlements, fully constrained status, 3D vs 2D, etc.) is performed when the autoConstrain method is called, not during input creation.

### createForAssemblyContext(occurrence: Occurrence) -> Sketch
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (Sketch): Returns the proxy object or null if this isn't the NativeObject.

### createSpunProfile(input: SpunProfileInput) -> SketchEntity
Creates sketch geometry that represents the spun profile. The spun profile is the silhouette of the entities as if they were spinning around an axis. The created spun profile is based on the information provided by the SpunProfileInput object.
- **input** (SpunProfileInput): The SpunProfileInput object that specifies the input needed to create the spun profile.
- **Returns** (SketchEntity): An array of sketch entities that were created as a result of the spun profile.

### createSpunProfileInput(entities: Base[], axis: Base) -> SpunProfileInput
Creates a new SpunProfileInput object that is used to specify the input needed to create a spun profile.
- **entities** (Base[]): An array containing the entities (BRepBody or BRepFace) to create a spun profile.
- **axis** (Base): The axis can be a sketch line, construction axis, or linear edge. The axis must not be perpendicular to the sketch plane.
- **Returns** (SpunProfileInput): Returns the newly created SpunProfileInput object or null if the creation failed.

### deleteMe() -> boolean
Deletes the sketch.
- **Returns** (boolean): Returns true if the delete was successful.

### findConnectedCurves(curve: SketchCurve) -> ObjectCollection
Finds the sketch curves that are end connected to the input curve. This can be useful for many cases but is especially useful in gathering the input when creating an offset.
- **curve** (SketchCurve): The initial sketch curve that will be used to find the connected curves.
- **Returns** (ObjectCollection): A collection of the connected curves. They are returned in their connected order with the original input curve being one of the curves.

### importSVG(fullFilename: string, xPosition: double, yPosition: double, scale: double) -> boolean
Imports the contents of an SVG file into the active sketch.
- **fullFilename** (string): The full filename, including the path, of the SVG file.
- **xPosition** (double): The X offset in centimeters in the sketch for the origin of the SVG data relative to the sketch origin.
- **yPosition** (double): The Y offset in centimeters in the sketch for the origin of the SVG data relative to the sketch origin.
- **scale** (double): The scale value to apply to the imported SVG data.
- **Returns** (boolean): Returns true if the import was successful.

### include(entity: Base) -> ObjectCollection
Creates new sketch curves and points that represent the specified entity as sketch geometry. The sketch geometry is not projected but is created in the same location in space as the input geometry.
- **entity** (Base): The entity to include into the sketch. This can be a sketch entity from another sketch, edge, face (which results in getting all of its edges, a vertex, construction axis, or construction point.
- **Returns** (ObjectCollection): Returns a collection of the sketch entities that were created as a result of the include. When including this curves it will be a single sketch curve, but for faces, multiple sketch curves will be created; one for each edge.

### intersectWithSketchPlane(entities: Base[]) -> SketchEntity
Intersects the specified entities (BRepBody, BRepFace, BRepEdge, BRepVertex, SketchCurve, ConstructionPoint, ConstructionAxis, and ConstructionPlane) with the sketch plane and creates sketch geometry that represents the intersection.
- **entities** (Base[]): An array containing the entities to intersect with the sketch plane.
- **Returns** (SketchEntity): An array returning the sketch entities that were created as a result of the intersections. It's possible that this can come back empty in the case where the input entities don't intersect the sketch plane.

### modelToSketchSpace(modelCoordinate: Point3D) -> Point3D
A specified point in model space returns the equivalent point in sketch space. This is sensitive to the assembly context.
- **modelCoordinate** (Point3D): A coordinate in model space.
- **Returns** (Point3D): Returns the equivalent point in sketch space.

### move(sketchEntities: ObjectCollection, transform: Matrix3D) -> boolean
Moves the specified sketch entities using the specified transform. Transform respects any constraints that would normally prohibit the move.
- **sketchEntities** (ObjectCollection): A collection of sketch entities to transform.
- **transform** (Matrix3D): The transform that defines the move, rotate or scale.
- **Returns** (boolean): Returns true if the move was successful.

### offset(curves: ObjectCollection, directionPoint: Point3D, offset: double) -> ObjectCollection
This function is retired. See more information in the 'Remarks' section below.

Creates offset curves for the set of input curves. If the offset distance is not provided, the offset distance is defined by the direction point.
- **curves** (ObjectCollection): A set of end connected curves. The Sketch.FindConnectedCurves method is a convenient way to get this set of curves.
- **directionPoint** (Point3D): Defines which side of the input curves to create the offset on
- **offset** (double): The distance to offset the curves in centimeters.

This is an optional argument whose default value is 0.0.
- **Returns** (ObjectCollection): A collection of the new offset sketch curves created

### project(entity: Base) -> ObjectCollection
This function is retired. See more information in the 'Remarks' section below.

This method has been replaced by the project2 method, which supports specifying if the result will be linked or not.
- **entity** (Base): The entity to project. This can be a single entity of the following types: sketch entity, an edge, a face (which will get all of its edges), a vertex, a construction axis, a construction point, or a construction plane that is perpendicular to the sketch to create a line.

This can also be an ObjectCollection that contains multiple entities and will be projected simultaneously. The entities that can be projected must be the types and have the same restrictions as described above.
- **Returns** (ObjectCollection): Returns a collection of the sketch entities that were created as a result of the projection.

### project2(entities: Base[], isLinked: boolean) -> SketchEntity
Projects the specified entity or entities onto the X-Y plane of the sketch and returns the created sketch entity(s).
- **entities** (Base[]): An array containing the entities to project. It can be an array of one for the case where a single entity is being projected. The following types of entities are valid for projection: sketch curves and points, B-Rep bodies (which results in projecting the silhouette of the body), B-Rep edges, B-Rep faces (which results in projecting all of its edges), B-Rep vertices, construction axes, construction points, and construction planes that are perpendicular to the sketch which results in the creation of a line.
- **isLinked** (boolean): A Boolean that indicates if the resulting sketch curves will be parametrically linked to the source geometry that was projected. If true, they will be linked. If false, the resulting curves are independent.
- **Returns** (SketchEntity): Returns an array of the sketch entities that were created as a result of the projection.

### projectCutEdges(body: BRepBody) -> ObjectCollection
Intersects the specified body with the sketch plane and creates new curves representing the intersection.
- **body** (BRepBody): The body to be intersected by the sketch.
- **Returns** (ObjectCollection): Returns a collection of the sketch entities that were created a a result of the cut.

### projectToSurface(faces: BRepFace[], curves: Base[], projectType: SurfaceProjectTypes, directionEntity: Base) -> SketchEntity
Projects the specified set of curves onto the specified set of faces using the specified method of projection. if the projection type is along a vector, then the directionEntity argument must be supplied. if the projectionType is the closest point method, the directionEntity argument is ignored.
- **faces** (BRepFace[]): An array of BRepFace objects that the curves will be projected onto.
- **curves** (Base[]): An array of various curve objects that will be projected onto the faces. The curves can be sketch curves and points, BRepEdge objects, ConstructionAxis objects, and ConstructionPoint objects.
- **projectType** (SurfaceProjectTypes): Specifies which projection type to use which defines the direction of projection. If this is set to AlongVectorSurfaceProjectType the directionEntity argument must be provided.
- **directionEntity** (Base): if the projectType argument is AlongVectorSurfaceProjectType, this argument must be specified and defines the direction of projection. It can be a linear BRepEdge, a BRepFace where the normal will be used, a SketchLine, or a ConstructionLine.

This is an optional argument whose default value is null.
- **Returns** (SketchEntity): Returns an array of the sketch entities that were created as a result of projection the specified curves onto the faces.

### redefine(planarEntity: Base) -> boolean
Changes which plane the sketch is based on.
- **planarEntity** (Base): A construction plane or planar face that defines the sketch plane
- **Returns** (boolean): Returns true if the operation was successful.

### saveAsDXF(fullFilename: string) -> boolean
This function is retired. See more information in the 'Remarks' section below.

Saves the contents of the sketch to a specified DXF file.
- **fullFilename** (string): The full filename, including the path, of the DXF file.
- **Returns** (boolean): Returns true if the operation was successful.

### setCenterlineState(sketchLines: SketchLine[], centerlineState: SketchLineCenterlineStates) -> boolean
Method that sets the Centerline state for an array of sketch lines.
- **sketchLines** (SketchLine[]): An array of sketch lines to set the centerline status
- **centerlineState** (SketchLineCenterlineStates): Input enum value that specifies if the centerline state of the input lines should be toggled, set to centerline, or set to normal
- **Returns** (boolean): Returns true if successful.

### setConstructionState(sketchCurves: SketchCurve[], constructionState: SketchCurveConstructionStates) -> boolean
Method that sets the Construction state for an array of sketch curves.
- **sketchCurves** (SketchCurve[]): An array of sketch curves to set the construction status.
- **constructionState** (SketchCurveConstructionStates): Input enum value that specifies if the construction state of the input curves should be toggled, set to construction, or set to normal.
- **Returns** (boolean): Returns true if successful.

### sketchToModelSpace(sketchCoordinate: Point3D) -> Point3D
A specified point in sketch space returns the equivalent point in model space. This is sensitive to the assembly context.
- **sketchCoordinate** (Point3D): A coordinate in sketch space.
- **Returns** (Point3D): Returns the equivalent point in model space.

## Properties

### areConstraintsShown : boolean [read-write]
Indicates if the constraints of the sketch are displayed when the sketch is active.

### areDimensionsShown : boolean [read-write]
Indicates if the dimensions of the sketch are displayed when the sketch is not active (in sketch edit mode)

### arePointsShown : boolean [read-write]
Indicates if the sketch points in the sketch are displayed. Points that are not connected to any other geometry will continue to be shown.

### areProfilesShown : boolean [read-write]
Indicates if the profiles of the sketch are displayed

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this face.

### baseOrFormFeature : Base [read-only]
This property returns the base or form feature that this sketch is associated with. It returns null in the case where the sketch is parametrically defined and is not related to a base or form feature. It also returns null in a direct modeling design.

### boundingBox : BoundingBox3D [read-only]
Returns the 3D bounding box of the sketch

### deriveFeature : DeriveFeature [read-only]
Returns the DeriveFeature if this sketch is derived from another design. This property returns null if the sketch is not derived from another design (i.e. isDerived property returns false).

### entityToken : string [read-only]
Returns a token for the Sketch object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same token.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### errorOrWarningMessage : string [read-only]
Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string.

### geometricConstraints : GeometricConstraints [read-only]
Returns the sketch constraints collection associated with this sketch. This provides access to the existing sketch constraints and supports the creation of new sketch constraints.

### healthState : FeatureHealthStates [read-only]
Returns the current health state of this sketch.

### isComputeDeferred : boolean [read-write]
This property temporarily turns off sketch computing. It is used to increase the performance as sketch geometry is created and modified. Once the sketch is drawn, this property should be set to false to allow the sketch to recompute. The file does not save this setting and is always false when a file is opened.

There is a side-effect when using this property that can result in the creation of a bad model. This is only a problem when editing an existing sketch used by one or more features. When the sketch is edited with the isComputeDeferred property set to true, the compute of the profiles can sometimes create weird results in the dependent features. There are two easy ways to solve this problem. The first is not to defer the sketch compute. The second is to roll the timeline back to just after the sketch, make whatever changes you want to the sketch with the compute deferred, and then roll the timeline back to its original location. This process mimics the behavior you see in the user interface when you manually edit a sketch where Fusion automatically rolls the timeline back while you're editing the sketch.

### isConstructionGeometryShown : boolean [read-write]
Gets and sets whether construction geometry in the sketch is displayed. This provides access to the "Construction Geometries" setting in the "SKETCH PALETTE".

### isDerived : boolean [read-only]
Returns if this sketch is derived from another design. If true, the sketch cannot be deleted. You should not attempt to make any edits to the derived sketch. Any edits made to this derived sketch will be lost when the derive updates.

### isFullyConstrained : boolean [read-only]
Indicates if this sketch is fully constrained.

### isLightBulbOn : boolean [read-write]
Gets and set if the light bulb beside the sketch node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children so this property does not indicate if the body is actually visible, just that it should be visible if all of it's parent nodes are also visible. Use the isVisible property to determine if it's actually visible.

### isModelSliced : boolean [read-write]
Gets and sets whether the model is sliced along the sketch plane when this sketch is active. This provides access to the "Slice" setting in the "SKETCH PALETTE".

### isParametric : boolean [read-only]
Indicates if this sketch is parametric or not. For parametric sketches, you can also get the construction plane or face it is associative to using the ReferencePlane property.

### isProjectedGeometryShown : boolean [read-write]
Gets and sets whether projected geometry in the sketch is displayed. This provides access to the "Projected Geometries" setting in the "SKETCH PALETTE".

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-write]
Gets if this sketch is currently visible in the graphics window. Use the isLightBulbOn to change if the light bulb beside the sketch node in the browser is on or not. Parent nodes in the browser can have their light bulb off which affects all of their children. This property indicates the final result and whether this body is actually visible or not.

### name : string [read-write]
Gets and sets the name of this sketch as seen in the browser and timeline.

### nativeObject : Sketch [read-only]
The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### origin : Point3D [read-only]
Returns the origin point of the sketch in model space.

### originPoint : SketchPoint [read-only]
Returns the sketch point that was automatically created by projecting the origin construction point into the sketch.

### parentComponent : Component [read-only]
Returns the parent Component.

### profiles : Profiles [read-only]
Returns the profiles currently computed for the sketch.

### referencePlane : Base [read-write]
Gets and sets the construction plane or planar face the sketch is associated to. This is only valid when the IsParametric property is True otherwise this returns null and setting the property will fail.

Setting this property is the equivalent of the Redefine command.

### revisionId : string [read-only]
Returns the current revision ID of the sketch. This ID changes any time the sketch is modified in any way. By getting and saving the ID when you create any data that is dependent on the sketch, you can then compare the saved ID with the current ID to determine if the sketch has changed to know if you should update your data.

### sketchCurves : SketchCurves [read-only]
Returns the sketch curves collection associated with this sketch. This provides access to the existing sketch curves which is all geometry in the sketch except for sketch points. It is through this collection that new sketch geometry gets created.

### sketchDimensions : SketchDimensions [read-only]
Returns the sketch dimensions collection associated with this sketch. This provides access to the existing sketch dimensions and supports the creation of new sketch dimensions.

### sketchPoints : SketchPoints [read-only]
Returns the sketch points collection associated with this sketch. This provides access to the existing sketch points and supports the creation of new sketch points.

### sketchTexts : SketchTexts [read-only]
Returns the sketch text collection associated with this sketch. This provides access to existing text and supports the creation of new text.

### timelineObject : TimelineObject [read-only]
Returns the timeline object associated with this sketch.

### transform : Matrix3D [read-write]
Gets and sets the transform of the sketch with respect to model space. This defines the transform from the parent component space to the sketch space. For example, if you have point coordinates in the space of the parent component and apply this transform it will result in the coordinates of the equivalent position in sketch space. The transform is sensitive to the assembly context.

The position of a parametric sketch cannot be modified since its position is defined by its parametric association to other geometry. As a result this property will fail when called on a parametric sketch. Setting this property is only valid for sketches in a non-parametric design or sketches owned by a base feature.

### xDirection : Vector3D [read-only]
Returns the X direction of the sketch as defined in model space.

### yDirection : Vector3D [read-only]
Returns the Y direction of the sketch as defined in model space.

## Samples
- **API Sample that demonstrates creating sketch lines in various ways.**: Demonstrates several ways to create sketch lines, including as the result of creating a rectangle.
- **Loft Feature API Sample**: Demonstrates creating a new loft feature.
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
- **Simple Extrusion Sample**: Creates a new extrusion feature, resulting in a new component.
- **Simple Revolve Feature Sample**: Creates a new revolve feature, resulting in a new component.
