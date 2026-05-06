# TimelineGroup
Namespace: adsk.fusion
Inherits: TimelineObject
Since: August 2014

Represents a group in the timeline.

**Accessed from:** TimelineGroup.parentGroup, TimelineGroups.add, TimelineGroups.item, TimelineObject.parentGroup

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

### deleteMe(deleteGroupAndContents: boolean) -> boolean
Deletes the group with the option of deleting or keeping the contents.
- **deleteGroupAndContents** (boolean): Indicates if the group and its contents should be deleted or if only the group should be deleted and the contents kept and expanded. A value of true will delete the group and its contents.
- **Returns** (boolean): Returns true if the delete was successful.

### item(index: uinteger) -> TimelineObject
Function that returns the specified timeline object within the group using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (TimelineObject): Returns the specified item or null if an invalid index was specified.

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

### count : uinteger [read-only]
The number of items in the group.

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

### isCollapsed : boolean [read-write]
Indicates if the group is collapsed or expanded.

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
