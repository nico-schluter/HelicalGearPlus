# TimelineObject
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Represents an object in the timeline.

**Accessed from:** ArrangeFeature.timelineObject, AsBuiltJoint.timelineObject, AssemblyConstraint.timelineObject, BaseFeature.timelineObject, BossFeature.timelineObject, BoundaryFillFeature.timelineObject, BoxFeature.timelineObject, Canvas.timelineObject, ChamferFeature.timelineObject, CircularPatternFeature.timelineObject, CoilFeature.timelineObject, CombineFeature.timelineObject, ConstructionAxis.timelineObject, ConstructionPlane.timelineObject, ConstructionPoint.timelineObject, CopyPasteBody.timelineObject, CornerClosureFeature.timelineObject, CustomFeature.timelineObject, CutPasteBody.timelineObject, CylinderFeature.timelineObject, Decal.timelineObject, DeleteFaceFeature.timelineObject, DeriveFeature.timelineObject, DraftFeature.timelineObject, EmbossFeature.timelineObject, ExtendFeature.timelineObject, ExtrudeFeature.timelineObject, Feature.timelineObject, FilletFeature.timelineObject, FlangeFeature.timelineObject, FlatPattern.timelineObject, FormFeature.timelineObject, HemFeature.timelineObject, HoleFeature.timelineObject, Joint.timelineObject, JointOrigin.timelineObject, LoftFeature.timelineObject, MeshCombineFaceGroupsFeature.timelineObject, MeshCombineFeature.timelineObject, MeshConvertFeature.timelineObject, MeshFeature.timelineObject, MeshGenerateFaceGroupsFeature.timelineObject, MeshReduceFeature.timelineObject, MeshRemeshFeature.timelineObject, MeshRemoveFeature.timelineObject, MeshRepairFeature.timelineObject, MeshReverseNormalFeature.timelineObject, MeshSeparateFeature.timelineObject, MeshShellFeature.timelineObject, MeshSmoothFeature.timelineObject, MirrorFeature.timelineObject, MotionLink.timelineObject, MoveFeature.timelineObject, Occurrence.timelineObject, OffsetFacesFeature.timelineObject, OffsetFeature.timelineObject, PatchFeature.timelineObject, PathPatternFeature.timelineObject, PipeFeature.timelineObject, RectangularPatternFeature.timelineObject, RefoldFeature.timelineObject, RemoveFeature.timelineObject, ReplaceFaceFeature.timelineObject, ReverseNormalFeature.timelineObject, RevolveFeature.timelineObject, RibFeature.timelineObject, RigidGroup.timelineObject, RipFeature.timelineObject, RuledSurfaceFeature.timelineObject, RuleFilletFeature.timelineObject, ScaleFeature.timelineObject, ShellFeature.timelineObject, SilhouetteSplitFeature.timelineObject, Sketch.timelineObject, Snapshot.timelineObject, SphereFeature.timelineObject, SplitBodyFeature.timelineObject, SplitFaceFeature.timelineObject, StitchFeature.timelineObject, SurfaceDeleteFaceFeature.timelineObject, SweepFeature.timelineObject, TangentRelationship.timelineObject, TessellateFeature.timelineObject, ThickenFeature.timelineObject, ThreadFeature.timelineObject, Timeline.item, TimelineGroup.item, TorusFeature.timelineObject, TrimFeature.timelineObject, UnfoldFeature.timelineObject, UnstitchFeature.timelineObject, UntrimFeature.timelineObject, VolumetricCustomFeature.timelineObject, VolumetricModelToMeshFeature.timelineObject, WebFeature.timelineObject

## Methods

### canReorder(beforeIndex: integer) -> boolean
Checks to see if this object can be reordered to the specified position. The default value of -1 indicates the end of the timeline.

This method will fail if this is a timelineGroup object and the group is expanded.
- **beforeIndex** (integer): The index number of the position in the timeline to check

This is an optional argument whose default value is -1.
- **Returns** (boolean): Returns true if the object can be reordered to the specified position

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### reorder(beforeIndex: integer) -> boolean
Reorders this object to the position specified. The default value of -1 indicates the end of the timeline.
- **beforeIndex** (integer): The index number of the position in the timeline to place this object before

This is an optional argument whose default value is -1.
- **Returns** (boolean): Returns true if the reorder operation was successful This method will fail and return false if this is a timelineGroup object and the group is expanded.

### rollTo(rollBefore: boolean) -> boolean
Rolls the timeline by repositioning the marker to either before or after this object. This method will fail if this is a timelineGroup object and the group is expanded.
- **rollBefore** (boolean): Set rollBefore to true to reposition the marker before this object or to false to reposition the marker after this object
- **Returns** (boolean): Returns true if the move was successful

## Properties

### entity : Base [read-only]
Returns the entity associated with this timeline object. Edit operations can be performed by getting the object representing the associated entity and using the methods and properties on that entity to make changes.

Returns null if this TimelineObject represents a TimelineGroup object, since it does not have an associated entity.

### errorOrWarningMessage : string [read-only]
Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string.

### healthState : FeatureHealthStates [read-only]
Returns the current health state of the object associated with this TimelineObject.

### index : integer [read-only]
Returns the position of this item within the timeline where the first item has an index of 0.

This property can return -1 in the two cases where this object is not currently represented in the timeline. The two cases are:

1. When this is a TimelineGroup object and the group is expanded.

2. When this object is part of a group and the group is collapsed.

### isGroup : boolean [read-only]
Indicates if this TimelineObject represents a group. If True you can operate on this object as a TimelineGroup object.

### isRolledBack : boolean [read-only]
Indicates if this item is currently not being computed because it has been rolled back.

If this is a timelineGroup object and the group is expanded the value of this property should be ignored.

### isSuppressed : boolean [read-write]
Gets and sets if this object is suppressed.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets and sets the name of this timeline object. This name is shared by the object the timeline object represents. For example, if the TimelineObject represents a Sketch and you change the name using the TimelineObject, the name of the sketch in the browser is also changed. The reverse is also true. Setting the name of an object; sketch, feature construction geometry, etc, will also change the name of the associated node in the timeline.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentGroup : TimelineGroup [read-only]
Returns the parent group, if this object is part of a group. Returns null if this object is not part of a group.

## Samples
- **Extrude Feature API Sample**: Demonstrates creating a new extrude feature.
- **Fillet Feature Edit API Sample**: Demonstrates editing a fillet feature.
To successfully run this sample you can use this
- **Ruled Surface Feature API Sample**: Demonstrates creating a new ruled surface feature.
