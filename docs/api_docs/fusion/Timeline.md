# Timeline
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

A collection of TimelineObjects in a parametric design.

**Accessed from:** Design.timeline, FlatPatternProduct.timeline, WorkingModel.timeline

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteAllAfterMarker() -> boolean
Deletes all objects in the timeline that are after the current position of the marker.
- **Returns** (boolean): Returns true if successful.

### item(index: uinteger) -> TimelineObject
Function that returns the specified item in the timeline using an index into the collection. The items are returned in the order they appear in the timeline.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (TimelineObject): Returns the specified item or null if an invalid index was specified.

### moveToBeginning() -> boolean
Moves the marker to the beginning of the timeline.
- **Returns** (boolean): Returns true if the move is successful

### moveToEnd() -> boolean
Moves the marker to the end of the timeline.
- **Returns** (boolean): Returns true if the move is successful

### movetoNextStep() -> boolean
Moves the marker to the next step in the timeline.
- **Returns** (boolean): Returns true if the move is successful

### moveToPreviousStep() -> boolean
Moves the marker to the previous step in the timeline.
- **Returns** (boolean): Returns true if the move is successful

### play() -> boolean
Plays the timeline beginning at the current position of the marker.
- **Returns** (boolean): Returns true if playing the timeline was successful

## Properties

### count : uinteger [read-only]
Returns the number of items in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### markerPosition : integer [read-write]
Gets and sets the current position of the marker where 0 is at the beginning of the timeline and the value of Timeline.count is the end of the timeline.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### timelineGroups : TimelineGroups [read-only]
Returns the collection of groups within the timeline.

## Samples
- **Extrude Feature API Sample**: Demonstrates creating a new extrude feature.
- **Fillet Feature Edit API Sample**: Demonstrates editing a fillet feature.
To successfully run this sample you can use this
- **Ruled Surface Feature API Sample**: Demonstrates creating a new ruled surface feature.
