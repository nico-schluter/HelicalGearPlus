# SketchCircle
Namespace: adsk.fusion
Inherits: SketchCurve
Since: August 2014

A circle in a sketch.

**Accessed from:** SketchCircle.createForAssemblyContext, SketchCircle.nativeObject, SketchCircles.addByCenterRadius, SketchCircles.addByThreePoints, SketchCircles.addByThreeTangents, SketchCircles.addByTwoPoints, SketchCircles.addByTwoTangents, SketchCircles.item

## Methods

### breakCurve(segmentPoint: Point3D, createConstraints: boolean) -> ObjectCollection
Breaks a curve into two or three pieces by finding intersections of this curve with all other curves in the sketch and splitting this curve at the nearest intersections to a specified point on the curve.
- **segmentPoint** (Point3D): A point that specifies the segment of the curve that is to be split from the rest of the curve. The nearest intersection(s) to this point define the break location(s).
- **createConstraints** (boolean): Optional argument that specifies if constraints should be created between the new curve segments. A value of true indicates constraints will be created.

This is an optional argument whose default value is True.
- **Returns** (ObjectCollection): All of the curves resulting from the break are returned in an ObjectCollection. In the case where no intersections are found and as a result the curve is not broken, an empty ObjectCollection is returned.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> SketchCircle
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (SketchCircle): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes the entity from the sketch.
- **Returns** (boolean): Returns true is the delete was successful.

### extend(endPoint: Point3D, createConstraints: boolean) -> ObjectCollection
Extend a curve by specifying a point that determines the end of the curve to extend
- **endPoint** (Point3D): A point (transient Point3D) on or closest to the end of the curve to extend. (start or end) The end of the curve closest to the endPoint gets extended
- **createConstraints** (boolean): Constraints are created by default. Specify false to not create constraints.

This is an optional argument whose default value is True.
- **Returns** (ObjectCollection): Returns the modified original curve if the start or end of the curve is extended If the extend joins a curve to another, the two original curves are deleted and a new curve is returned If an arc is extended so as to become a circle, the original arc is deleted and a new circle is returned

### intersections(sketchCurves: ObjectCollection, intersectingCurves: ObjectCollection, intersectionPoints: ObjectCollection) -> boolean
Get the curves that intersect this curve along with the intersection points (Point3D)
- **sketchCurves** (ObjectCollection): A collection of curves to attempt to find intersections with. Set the value of this parameter to null to use all curves in the sketch for the calculation.
- **intersectingCurves** (ObjectCollection): A collection of the actual intersecting curves
- **intersectionPoints** (ObjectCollection): A collection of intersection points (Point3D) Item numbers in this collection correspond to the item numbers in the intersectingCurves collection.
- **Returns** (boolean): Returns true if the method was successful. It can be successful regardless of whether intersections were found or not.

### split(splitPoint: Point3D, createConstraints: boolean) -> ObjectCollection
Split a curve at a position specified along the curve
- **splitPoint** (Point3D): A position (transient Point3D) on the curve that defines the point at which to split the curve
- **createConstraints** (boolean): Constraints are created by default. Specify false to create no constraints.

This is an optional argument whose default value is True.
- **Returns** (ObjectCollection): Returns the resulting 2 curves; the original curve + the newly created curve When split spline the original is deleted and two new curves returned. Empty collection returned if curve is closed.

### trim(segmentPoint: Point3D, createConstraints: boolean) -> ObjectCollection
Trim a curve by specifying a point that determines the segment of the curve to trim away
- **segmentPoint** (Point3D): A point (transient Point3D) on or closest to the segment of the curve to remove. (start, end or middle) The segment of the curve closest to the segmentPoint gets removed
- **createConstraints** (boolean): Constraints are created by default. Specify false to not create constraints.

This is an optional argument whose default value is True.
- **Returns** (ObjectCollection): When trimming the start or end side of a line, unclosed circular or elliptical arc, the original entity is modified and returned When trimming the middle of a line, unclosed circular or elliptical arc the original entity is deleted and two new entities are returned When trimming the start or end of any type of closed curve, the original is deleted and a new curve is returned Any trimming of a spline (open or closed) deletes the original and new spline/s are returned Trimming a curve having no intersections deletes the original and returns an empty collection

## Properties

### area : double [read-only]
Returns the area of the circle in square centimeters.

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this face.

### boundingBox : BoundingBox3D [read-only]
Returns the bounding box of the entity in sketch space.

### centerSketchPoint : SketchPoint [read-only]
Returns the sketch point at the center of the circle.

### entityToken : string [read-only]
Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### geometricConstraints : GeometricConstraintList [read-only]
Returns the sketch constraints that are attached to this curve.

### geometry : Circle3D [read-only]
Returns the transient geometry of the circle which provides geometric information about the circle. The returned geometry is always in sketch space.

### is2D : boolean [read-only]
Indicates if this curve lies entirely on the sketch x-y plane.

### isConstruction : boolean [read-write]
Gets and sets whether this curve is construction geometry.

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

### length : double [read-only]
Returns the length of the curve in centimeters.

### nativeObject : SketchCircle [read-only]
The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentSketch : Sketch [read-only]
Returns the parent sketch.

### radius : double [read-write]
Gets and sets the radius of the circle. Changing the radius is limited by any constraints that might exist on the circle.

### referencedEntity : Base [read-only]
Returns the referenced entity in the case where IsReference is true. However, this property can also return null when IsReference is true in the case where the reference is not parametric.

### sketchDimensions : SketchDimensionList [read-only]
Returns the sketch dimensions that are attached to this curve.

### worldGeometry : Circle3D [read-only]
Returns a Point3D object which provides the position of the sketch point in world space. The returned coordinate takes into account the assembly context and the position of the sketch in it's parent component, which means the coordinate will be returned in the root component space.
