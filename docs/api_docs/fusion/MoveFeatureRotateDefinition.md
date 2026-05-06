# MoveFeatureRotateDefinition
Namespace: adsk.fusion
Inherits: MoveFeatureDefinition
Since: January 2023

The MoveFeatureRotateDefinition object defines a move feature described by a rotation around a specified entity.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### angle : ModelParameter [read-only]
Gets the model parameter that controls the rotation angle. You can use properties on the returned ModelParameter object to edit the offset distance.

### axisEntity : Base [read-write]
Gets and sets the linear entity that defines the axis of rotation. This can be a linear BRepEdge, ConstructionAxis, or a SketchLine. The natural direction of the entity defines a right-hand rule for the rotation direction.

To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentMoveFeature : MoveFeature [read-only]
Returns the parent MoveFeature object
