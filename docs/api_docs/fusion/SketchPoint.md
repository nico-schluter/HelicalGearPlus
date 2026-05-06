# SketchPoint
Namespace: adsk.fusion
Inherits: SketchEntity
Since: August 2014

A point within a sketch.

**Accessed from:** AutoConstrainInput.datumPoint, CircularPatternConstraint.centerPoint, CircularPatternConstraintInput.centerPoint, CoincidentConstraint.point, CoincidentToSurfaceConstraint.point, HorizontalPointsConstraint.pointOne, HorizontalPointsConstraint.pointTwo, MidPointConstraint.point, PolygonConstraint.centerPoint, PolygonConstraint.points, SharedPointCoincident.point, Sketch.originPoint, SketchArc.centerSketchPoint, SketchArc.endSketchPoint, SketchArc.startSketchPoint, SketchCircle.centerSketchPoint, SketchConicCurve.apexSketchPoint, SketchConicCurve.endSketchPoint, SketchConicCurve.startSketchPoint, SketchControlPointSpline.controlPoints, SketchControlPointSpline.endSketchPoint, SketchControlPointSpline.startSketchPoint, SketchDistanceBetweenPointAndSurfaceDimension.point, SketchEllipse.centerSketchPoint, SketchEllipticalArc.centerSketchPoint, SketchEllipticalArc.endSketchPoint, SketchEllipticalArc.startSketchPoint, SketchFittedSpline.addFitPoint, SketchFittedSpline.endSketchPoint, SketchFittedSpline.startSketchPoint, SketchFixedSpline.endSketchPoint, SketchFixedSpline.startSketchPoint, SketchLine.endSketchPoint, SketchLine.startSketchPoint, SketchPoint.createForAssemblyContext, SketchPoint.detach, SketchPoint.nativeObject, SketchPointHolePositionDefinition.sketchPoint, SketchPointList.item, SketchPoints.add, SketchPoints.item, VerticalPointsConstraint.pointOne, VerticalPointsConstraint.pointTwo

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> SketchPoint
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (SketchPoint): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes the entity from the sketch.
- **Returns** (boolean): Returns true is the delete was successful.

### detach(curve: SketchCurve) -> SketchPoint
This method disconnects the specified curve from the sketch point. The specified curve must use this point as one of its endpoints, and at least one other sketch curve must also use the point as its endpoint. Detaching the curve creates a new sketch point, which becomes the curve's end point. All other curves using the original sketch point will remain unaffected.
- **curve** (SketchCurve): The sketch curve to detach from the sketch point. One of its end points must be the sketch point.
- **Returns** (SketchPoint): If successful, the newly created sketch point that the curve was moved to is returned. Null is returned in the case of failure. Typical failure cases are if the specified curve is the only curve connected to the point or if the curve is not connected to the point.

### merge(point: SketchPoint) -> boolean
Merges the input sketch point into this sketch point. This effectively deletes the other sketch point and changes all entities that referenced that sketch point to reference this sketch point.

This is the equivalent of dragging a sketch point on top of another sketch point in the user interface.
- **point** (SketchPoint): The point to merge with this point.
- **Returns** (boolean): Returns true if the merge was successful.

### move(translation: Vector3D) -> boolean
Moves the sketch geometry using the specified transform. Move respects any constraints that would normally prohibit the move. This will fail in the case where the IsReference property is true.
- **translation** (Vector3D): The vector that defines the distance and direction to move.
- **Returns** (boolean): Returns true if moving the sketch point was successful.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this face.

### boundingBox : BoundingBox3D [read-only]
Returns the bounding box of the entity in sketch space.

### connectedEntities : SketchEntityList [read-only]
Returns the set of sketch entities that are directly connected to this point. For example any entities that use this point as their start point or end point will be returned and any circle, arc or ellipse who have this point as a center point will be returned. This does not include entities that are related to the point through a constraint.

### entityToken : string [read-only]
Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### geometricConstraints : GeometricConstraintList [read-only]
Returns the sketch constraints that are attached to this curve.

### geometry : Point3D [read-only]
Returns a Point3D object which provides the position of the sketch point. The returned geometry is always in sketch space.

### is2D : boolean [read-only]
Indicates if this curve lies entirely on the sketch x-y plane.

### isDeletable : boolean [read-only]
Indicates if this sketch entity can be deleted. There are cases, especially with sketch points where another entity is dependent on an entity so deleting it is not allowed. For example, you can't delete the center point of circle by itself but deleting the circle will delete the point. The same is true for the end points of a line.

### isFixed : boolean [read-write]
Indicates if this geometry is "fixed".

### isFullyConstrained : boolean [read-only]
Indicates if this sketch entity is fully constrained.

### isLinked : boolean [read-only]
Indicates if this sketch entity was created by a projection, inclusion, or driven by an API script. If this returns true, then the entity is presented to the user as not editable and with a 'break link' command available.

### isReference : boolean [read-write]
Indicates if this geometry is a reference. Changing this property from true to false removes the reference. This property can not be set to true if it is already false.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-only]
When a sketch is created, geometry is sometimes automatically added to the sketch. For example a sketch point that references the origin point is always included and if a face was selected to create the sketch on, geometry from the face is also included. This automatically created geometry behaves in a special way in that it is invisible but is available for selection and it also participates in profile calculations. It's not possible to make them visible but they can be deleted and they can be used for any other standard sketch operation.

### nativeObject : SketchPoint [read-only]
The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentSketch : Sketch [read-only]
Returns the parent sketch.

### referencedEntity : Base [read-only]
Returns the referenced entity in the case where IsReference is true. However, this property can also return null when IsReference is true in the case where the reference is not parametric.

### sketchDimensions : SketchDimensionList [read-only]
Returns the sketch dimensions that are attached to this curve.

### worldGeometry : Point3D [read-only]
Returns a Point3D object which provides the position of the sketch point in world space. The returned coordinate takes into account the assembly context and the position of the sketch in it's parent component, which means the coordinate will be returned in the root component space.

## Samples
- **Sketch Point API Sample**: Demonstrates creating a new sketch point.
