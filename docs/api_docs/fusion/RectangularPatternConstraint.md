# RectangularPatternConstraint
Namespace: adsk.fusion
Inherits: GeometricConstraint
Since: March 2016

A rectangular pattern constraint in a sketch.

**Accessed from:** GeometricConstraints.addRectangularPattern, RectangularPatternConstraint.createForAssemblyContext, RectangularPatternConstraint.nativeObject

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createForAssemblyContext(occurrence: Occurrence) -> RectangularPatternConstraint
Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence.
- **occurrence** (Occurrence): The occurrence that defines the context to create the proxy in.
- **Returns** (RectangularPatternConstraint): Returns the proxy object or null if this isn't the NativeObject.

### deleteMe() -> boolean
Deletes this constraint. The IsDeletable property can be used to determine if this constraint can be deleted.
- **Returns** (boolean): Returns true if the delete was successful.

### setDirectionOne(directionOneEntity: SketchLine, quantityOne: ValueInput, distanceOne: ValueInput) -> boolean
Sets all of the input required to define the pattern in the first direction.
- **directionOneEntity** (SketchLine): Specifies the SketchLine object used to define the first direction entity.

This argument can be null to indicate that the default first direction is to be used, which is along the X axis of the sketch.
- **quantityOne** (ValueInput): Specifies the number of instances in the first direction.
- **distanceOne** (ValueInput): Specifies the distance in the first direction. How this value is used depends on the value of the PatternDistanceType property. If the value is ExtentPatternDistanceType then it defines the total distance of the pattern. If the value is SpacingPatternDistanceType then it defines the distance between each element.
- **Returns** (boolean): Returns true if it was successful.

### setDirectionTwo(directionTwoEntity: SketchLine, quantityTwo: ValueInput, distanceTwo: ValueInput) -> boolean
Sets all of the input required to define the pattern in the second direction.
- **directionTwoEntity** (SketchLine): Specifies the SketchLine object used to define the second direction entity.

This argument can be null to indicate that the default second direction is to be used, which is 90 degrees to the first direction.
- **quantityTwo** (ValueInput): Specifies the number of instances in the second direction.
- **distanceTwo** (ValueInput): Specifies the distance in the second direction. How this value is used depends on the value of the PatternDistanceType property. If the value is ExtentPatternDistanceType then it defines the total distance of the pattern. If the value is SpacingPatternDistanceType then it defines the distance between each element.
- **Returns** (boolean): Returns true if it was successful.

## Properties

### assemblyContext : Occurrence [read-only]
Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object.

### attributes : Attributes [read-only]
Returns the collection of attributes associated with this geometric constraint.

### createdEntities : array [read-only]
Returns an array that contains all of the sketch entities that were created as a result of the pattern. This does not contain the original entities that were used as input to the pattern. The input entities can be obtained by using the entities property.

### directionOneEntity : SketchLine [read-write]
Gets and sets the entity that defined the first direction of the pattern. This can be null which indicates to use the default which is the X-axis of the sketch. Setting this property to null will automatically clear directionTwoEntity, if it has been set.

### directionTwoEntity : SketchLine [read-write]
Gets and sets the entity that defines the second direction of the pattern. This can be null which indicates to use the default direction, which is perpendicular to direction one. The directionOneEntity property must be set before setting this property.

### distanceOne : ModelParameter [read-only]
Returns the parameter that controls the distance in first direction. To change the value, use the properties on the returned ModelParameter object.

### distanceTwo : ModelParameter [read-only]
Returns the parameter that controls the distance in second direction. To change the value, use the properties on the returned ModelParameter object.

### distanceType : PatternDistanceType [read-write]
Gets and sets how the distance between elements is computed.

### entities : array [read-write]
Gets and sets the entities that are patterned. Sketch points and curves are valid entities to pattern.

### entityToken : string [read-only]
Returns a token for the GeometricConstraint object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same geometric constraint.

When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them.

### isDeletable : boolean [read-only]
Indicates if this constraint is deletable.

### isSuppressed : array [read-write]
Specifies which, if any, instances of the pattern are suppressed. This returns an array of Boolean values that indicates if a particular instance in the pattern is suppressed or not. A value of true will result in the associated instance being suppressed.

The indices represent the pattern instances in a row-column order, with the initial geometry not counting. For example, if you have a 4x4 pattern, the array will have 15 elements rather than 16 because the original geometry cannot be suppressed as part of the pattern. The first element in the array is the one next to the original in the first direction. The second element is the next one on the first row, and the third is the next one. The fourth element will be the first element in the row next to the first row that contains the original geometry.

### isSymmetricInDirectionOne : boolean [read-write]
Gets and sets if the pattern in direction one is in one direction or is symmetric.

### isSymmetricInDirectionTwo : boolean [read-write]
Gets and sets if the pattern in direction two is in one direction or is symmetric.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### nativeObject : RectangularPatternConstraint [read-only]
The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentSketch : Sketch [read-only]
Returns the parent sketch object.

### quantityOne : ModelParameter [read-only]
Returns the parameter that controls the number of instances in the first direction. To change the value, use the properties on the returned ModelParameter.

### quantityTwo : ModelParameter [read-only]
Returns the parameter that controls the number of instances in the second direction. To change the value, use the properties on the returned ModelParameter object.
