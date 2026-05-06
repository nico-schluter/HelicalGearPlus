# TwoDistancesChamferEdgeSet
Namespace: adsk.fusion
Inherits: ChamferEdgeSet
Since: December 2020

Provides access to the edges and the parameters associated with a two distances chamfer.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes the chamfer edge set from the chamfer.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **Returns** (boolean): Returns true if the operation was successful.

## Properties

### distanceOne : ModelParameter [read-only]
Returns the model parameter that controls the first offset distance of the chamfer. You can edit the distance by using the properties on the returned ModelParameter object.

### distanceTwo : ModelParameter [read-only]
Returns the model parameter that controls the first offset distance of the chamfer. You can edit the distance by using the properties on the returned ModelParameter object.

### edges : ObjectCollection [read-write]
Gets and sets the edges that will be chamfered. This collection can contain BRepEdge, BRepFace, and Feature objects. If BRepFace or Feature are objects are provided, all of the edges associated with those objects will be chamfered.

To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### isFlipped : boolean [read-write]
Gets and sets if the chamfer is flipped. This swaps the directions for distance one and two.

To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### isTangentChain : boolean [read-write]
Gets and sets the Tangent chain for chamfer. This enables tangent chain option for chamfer.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
