# ChordLengthFilletEdgeSet
Namespace: adsk.fusion
Inherits: FilletEdgeSet
Since: November 2015

Provides access to the edges and the parameter associated with a chord length fillet.

**Accessed from:** FilletEdgeSets.addChordLengthEdgeSet

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes the fillet edge set from the fillet.

To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)
- **Returns** (boolean): Returns true if the operation was successful.

## Properties

### chordLength : ModelParameter [read-only]
Returns the model parameter that controls the chord length of the fillet. You can edit the chord length by using the properties on the returned ModelParameter object.

### continuity : SurfaceContinuityTypes [read-write]
Gets and sets the continuity of the fillet edge set. Valid values are TangentSurfaceContinuityType and CurvatureSurfaceContinuityType.

### edges : ObjectCollection [read-write]
Gets and sets an ObjectCollection containing the BRepEdge, BRepFace, and Feature that are filleted. If the isTangentChain argument is true additional edges or faces may also get filleted if they are tangentially connected to any of the input edges or faces.

To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True)

### isTangentChain : boolean [read-write]
Gets and sets the Tangent chain for fillet. This enables tangent chain option for fillet.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### tangencyWeight : ModelParameter [read-only]
Returns the model parameter that controls the G1 or G2 tangency weight of the fillet. It must be a real value between 0.1 and 2.0 inclusive. You can edit the tangency weight by using the properties on the returned ModelParameter object.

## Samples
- **Fillet Feature Edit API Sample**: Demonstrates editing a fillet feature.
To successfully run this sample you can use this
