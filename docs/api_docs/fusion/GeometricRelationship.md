# GeometricRelationship
Namespace: adsk.fusion
Inherits: Base
Since: July 2025

This object represents a pair of entity inputs that are used when inferring a joint from geometry or for an assembly constraint.

**Accessed from:** GeometricRelationships.add, GeometricRelationships.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
This method deletes this geometric relationship.

If the isTemporary property is True, it removes it from the input object.

If the GeometricRelationship is associated with an existing joint or assembly constraint (the isTemporary property is false), you need to position the timeline marker immediately before the joint or assembly constraint. This can be accomplished using the following code: thisJointOrConstraint.timelineObject.rollTo(True).
- **Returns** (boolean): Returns true if the delete was successful.

### redefineOffsetOrAngle(isMate: boolean, offsetOrAngleValue: ValueInput) -> boolean
This method redefines an existing geometric relationship by defining if it is a mate or angle and specifying a new value.

If the GeometricRelationship is associated with an existing joint or assembly constraint (the isTemporary property is false), you need to position the timeline marker immediately before the joint or assembly constraint. This can be accomplished using the following code: thisJointOrConstraint.timelineObject.rollTo(True).
- **isMate** (boolean): This argument indicates if the geometric relationship defines a mate or an angle. A value of true indicates a mate relationship.
- **offsetOrAngleValue** (ValueInput): This argument specifies the value associated with the geometric relationship. If isMate is true, the value is a length, and if it is a real value, then it is centimeters. If it is a string, it is an expression that must evaluate to a length. If isMate is False, the value is an angle, and if it is a real value, then it is radians. If it is a string, it is an expression that must evaluate to an angle.
- **Returns** (boolean): Returns true if the redefinition was successful.

## Properties

### angleReferenceEntity : Base [read-write]
This property is used to define a third vector when an angle constraint is being defined. This property is ignored for mate constraints.

In some cases, when specifying entityOne and entityTwo for an angle constraint there is more than one solution. When the constraint is solved, entityOne and entityTwo each define a vector. When the reference entity is provided, the vectors need to follow the "right hand rule" with respect to the reference entity. This means the angle between the reference entity and the cross product of entityOne and entityTwo should be between 0 and 90 deg.

The reference entity can be a planar BRepFace or a linear or circular BRepedge.

This property can return and be set to null to indicate there is no reference entity.

### entityOne : Base [read-write]
Gets and sets the first entity in the relationship. The entity can be a BRepFace, BRepedge, BRepVertex, SketchPoint, SketchCurve, ConstructionPlane, ConstructionAxis, or ConstructionPoint object.

If the GeometricRelationship is associated with an existing joint or assembly constraint (the isTemporary property is false), you need to position the timeline marker immediately before the joint or assembly constraint. This can be accomplished using the following code: thisJointOrConstraint.timelineObject.rollTo(True).

### entityTwo : Base [read-write]
Gets and sets the second entity in the relationship. The entity can be a BRepFace, BRepedge, BRepVertex, SketchPoint, SketchCurve, ConstructionPlane, ConstructionAxis, or ConstructionPoint object.

If the GeometricRelationship is associated with an existing joint or assembly constraint (the isTemporary property is false), you need to position the timeline marker immediately before the joint or assembly constraint. This can be accomplished using the following code: thisJointOrConstraint.timelineObject.rollTo(True).

### isFlipped : boolean [read-write]
Gets and sets if the directions of the entities are aligned or opposed. The natural direction is for them to be opposed, and flipping them will align them.

If the GeometricRelationship is associated with an existing joint or assembly constraint (the isTemporary property is false), you need to position the timeline marker immediately before the joint or assembly constraint. This can be accomplished using the following code: thisJointOrConstraint.timelineObject.rollTo(True).

### isMate : boolean [read-only]
Gets and sets if this geometric relationships defines a mate or angle relationship between the two input entities. If true, it is a mate relationship.

### isSuppressed : boolean [read-write]
Gets and sets if this relationship is suppressed. This property is only valid when this geometric relationship is associated with an existing AssemblyConstraint. Otherwise, getting the value of this property will always return false, and setting it will be ignored.

### isTemporary : boolean [read-only]
Specifies if this GeometricRelationship is a child of an input object is being used to create a new Joint or AssemblyConstraint or is being used by an existing Joint or AssemblyConstraint.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
Returns the name of the constraint as seen in the browser. This property will only return a name when the geometric relationship is associated with an existing AssemblyConstraint or inferred Joint (the isTemporary property is false). Otherwise, it will return an empty string.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### offsetOrAngle : ModelParameter [read-only]
This property is used when the geometric relationship is associated with an existing joint or assembly constraint (the isTemporary property is false). It returns the parameter that controls the offset or angle of this geometric relationship. You can change the value by editing properties on the returned ModelParameter object.

If this geometric relationship is associated with a JointInput object (the isTemporary property is true), this property returns null, and you should use the offsetOrAngleValue property to get and set the value.

### offsetOrAngleValue : ValueInput [read-write]
This property is used when creating a new joint or assembly constraint and defines the offset or angle associated with this geometric relationship. The value defaults to 0, but can be set with a ValueInput defining a length or angle. It can be either a real value, which will be in centimeters or radians, or a string, which is an expression whose units are length or angle.

If the GeometricRelationship is associated with an existing joint or assembly constraint (the isTemporary property is false), this property will return null and fail if set. To get and set the value in this case you should use the offsetOrAngle property to access the controlling parameter.

### parent : Base [read-only]
Returns the parent AssemblyConstraint, Joint, InferredJointInput, or AssemblyConstraintInput object with which this geometric relationship is associated.
