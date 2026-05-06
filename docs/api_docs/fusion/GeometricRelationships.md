# GeometricRelationships
Namespace: adsk.fusion
Inherits: Base
Since: July 2025

This object represents a set of geometry relationships. They are used when creating a new inferred joint or assembly constraint and querying an existing one.

**Accessed from:** AssemblyConstraint.geometricRelationships, AssemblyConstraintInput.geometricRelationships, InferredJointInput.geometricRelationships, Joint.geometricRelationships

## Methods

### add(entityOne: Base, entityTwo: Base, isMate: boolean, value: ValueInput, biasPointOne: Point3D, biasPointTwo: Point3D) -> GeometricRelationship
Creates a GeometricRelationship object, which defines two entities that will be used to either infer a joint or to create an assembly constraint.
- **entityOne** (Base): Specifies the entity from the first occurrence being constrained. The entity can be a BRepFace, BRepEdge, BRepVertex ,SketchLine, SketchPoint, ConstructionPlane, ConstructionAxis, or ConstructionPoint object in the component referenced by the occurrence. It must be a proxy relative to the root component of the assembly.

For an inferred joint, if multiple geometric relationships are created, the entities for entityOne must all be from the same occurrence.This is because a single joint will be inferred between the two occurrences.

For an assembly constraint, if multiple geometric relationships are created, the entities for entityOne must all be from the same occurrence. This is because all the geometric relationships constrain the occurrence this entity is from.
- **entityTwo** (Base): Specifies the entity from the second occurrence being constrained. The entity can be a BRepFace, BRepEdge, BRepVertex, SketchLine, SketchPoint, ConstructionPlane, ConstructionAxis, or ConstructionPoint object in the component referenced by the occurrence. It must be a proxy relative to the root component of the assembly.

For an inferred joint, if multiple geometric relationships are created, the entities for entityTwo must all be from the same occurrence. This is because a single joint will be inferred between the two occurrences.

For an assembly constraint, if multiple geometric relationships are created, the entities for entityTwo must all be from the same occurrence. This is because all the geometric relationships constrain the occurrence this entity is from.
- **isMate** (boolean): Specifies if this geometric relationship defines a mate or an angle between the two input entities. If true, it defines a mate; if false, it is an angle.
- **value** (ValueInput): Specifies the value associated with the geometric relationship. If isMate is true, the value is a length, and a real value in centimeters. If it is a string, it is an expression that must evaluate to a length. If the isMate argument is False, the value is an angle, and a real value in radians. If it is a string, it is an expression that must evaluate to an angle.
- **biasPointOne** (Point3D): This optional argument defines a position on the first entity that will be used when positioning the two occurrences. In the user interface, if you select two faces and create an inferred joint, the two faces will be used to mate the occurrences together. Still, there are infinite possibilities of how the occurrences can be positioned relative to one another. The location of the selection points is used to determine a single result, and the occurrences will be positioned so that the selection points are coincident. There aren't selection points in the API, but you can optionally define points that will be used, like the selection points. Fusion will calculate arbitrary points on the entities if the bias points aren't provided. The bias points are not remembered and are only used for the initial placement.

This is an optional argument whose default value is null.
- **biasPointTwo** (Point3D): See the description for biasPointOne.

This is an optional argument whose default value is null.
- **Returns** (GeometricRelationship): Returns the GeometricRelationship object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> GeometricRelationship
Function that returns the specified GeometricRelationship using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (GeometricRelationship): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns number of geometric relationships in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
