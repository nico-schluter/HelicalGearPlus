# LoftCenterLineOrRails
Namespace: adsk.fusion
Inherits: Base
Since: August 2016

Defines a single centerline or one or more rails for a loft feature.

**Accessed from:** LoftFeature.centerLineOrRails, LoftFeatureInput.centerLineOrRails

## Methods

### addCenterLine(entity: Base) -> LoftCenterLineOrRail
Adds a centerline. A single centerline can be defined for a loft. If a centerline or rails have already been defined, they will be removed and the input will become the new single centerline.

If this LoftCenterLineOrRails object is associated with a created feature,
- **entity** (Base): The entity that defines the center line. This can be a single sketch curve, a single BRepEdge, a Path consisting of connected B-Rep edges or sketch curves.
- **Returns** (LoftCenterLineOrRail): Returns the new LoftCenterLineOrRail object or null in the case of a failure.

### addRail(entity: Base) -> LoftCenterLineOrRail
Add a rail to the loft definition. Multiple rails can be defined, so each call of this method adds a new rail.

If this LoftCenterLineOrRails object is associated with a created feature, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **entity** (Base): The entity that defines the rail. This can be a single sketch curve, a single BRepEdge, or a Path consisting of connected B-Rep edges or sketch curves.
- **Returns** (LoftCenterLineOrRail): Returns the new LoftCenterLineOrRail object or null in the case of a failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: integer) -> LoftCenterLineOrRail
Function that returns the specified LoftCenterLineOrRail using an index into the collection.
- **index** (integer): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (LoftCenterLineOrRail): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
The number of centerlines or rails in the collection.

### isCenterLine : boolean [read-only]
Indicates if a centerline or rails are currently defined.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
