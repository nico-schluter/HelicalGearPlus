# MoveFeaturePointToPointDefinition
Namespace: adsk.fusion
Inherits: MoveFeatureDefinition
Since: January 2023

The MoveFeaturePointToPointDefinition object defines a move feature described by the translation from one point to another.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### originPoint : Base [read-write]
Gets and sets the first point that defines the start position of the move.

To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### parentMoveFeature : MoveFeature [read-only]
Returns the parent MoveFeature object

### targetPoint : Base [read-write]
Gets and sets the second point that defines the direction and distance of the move.

To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
