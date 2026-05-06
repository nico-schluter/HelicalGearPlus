# LoftCenterLineOrRail
Namespace: adsk.fusion
Inherits: Base
Since: August 2016

Represent a centerline or a single rail used by a loft feature.

**Accessed from:** LoftCenterLineOrRails.addCenterLine, LoftCenterLineOrRails.addRail, LoftCenterLineOrRails.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes the centerline or rail.

If this LoftCenterLineOrRail object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **Returns** (boolean): Returns true if the operation was successful.

## Properties

### edgeCondition : LoftRailEdgeConditions [read-write]
Gets and sets the edge condition for this rail. This value is only applicable when a BRepEdge is used as the rail entity. If sketch geometry is used, this value is ignored. The property defaults to G0LoftRailEdgeCondition.

If this LoftCenterLineOrRail object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### entity : Base [read-write]
Gets and sets the entity that defines the centerline or rail. This can be a single sketch entity, a single BRepEdge, a Path, or a Profile.

If this LoftCenterLineOrRail object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### isCenterLine : boolean [read-only]
Indicates if this object is a loft centerline (true) or a rail (false).

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
