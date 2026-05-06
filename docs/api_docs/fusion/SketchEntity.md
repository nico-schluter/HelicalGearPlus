# SketchEntity
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

This object represents all geometry in a sketch, including all the various curves, points, and text.

**Accessed from:** CircularPatternConstraint.createdEntities, CircularPatternConstraint.entities, CircularPatternConstraintInput.entities, CoincidentConstraint.entity, ProfileCurve.sketchEntity, RectangularPatternConstraint.createdEntities, RectangularPatternConstraint.entities, RectangularPatternConstraintInput.entities, Sketch.createSpunProfile, Sketch.intersectWithSketchPlane, Sketch.project2, Sketch.projectToSurface, SketchEntityList.item, SketchLinearDiameterDimension.entityTwo, SketchLinearDimension.entityOne, SketchLinearDimension.entityTwo, SketchOffsetDimension.entityTwo, SketchTangentDistanceDimension.entityOne, SymmetryConstraint.entityOne, SymmetryConstraint.entityTwo

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes the entity from the sketch.
- **Returns** (boolean): Returns true is the delete was successful.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this face.

### boundingBox : BoundingBox3D [read-only]
Returns the bounding box of the entity in sketch space.

### entityToken : string [read-only]
Returns a token for the SketchEntity object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same sketch entity.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### geometricConstraints : GeometricConstraintList [read-only]
Returns the sketch constraints that are attached to this curve.

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

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentSketch : Sketch [read-only]
Returns the parent sketch.

### referencedEntity : Base [read-only]
Returns the referenced entity in the case where IsReference is true. However, this property can also return null when IsReference is true in the case where the reference is not parametric.

### sketchDimensions : SketchDimensionList [read-only]
Returns the sketch dimensions that are attached to this curve.
