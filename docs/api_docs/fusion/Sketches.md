# Sketches
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Provides access to the sketches within a design and provides methods to create new sketches.

**Accessed from:** Component.sketches, FlatPatternComponent.sketches

## Methods

### add(planarEntity: Base, occurrenceForCreation: Occurrence) -> Sketch
Creates a new sketch on the specified planar entity.
- **planarEntity** (Base): A construction plane or planar face that defines the sketch plane
- **occurrenceForCreation** (Occurrence): A creation occurrence is needed if the planarEntity is in another component AND the sketch is not in the root component. The occurrenceForCreation is analogous to the active occurrence in the UI.

This is an optional argument whose default value is null.
- **Returns** (Sketch): Returns the newly created Sketch or null if the creation failed.

### addToBaseOrFormFeature(planarEntity: Base, targetBaseOrFormFeature: Base, includeFaceEdges: boolean) -> Sketch
Creates a parametric sketch that is associated with a base feature.

Because of a current limitation, if you want to create a sketch associated with a base feature, you must first call the edit method of the base feature, use this method to create the sketch, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.
- **planarEntity** (Base): A construction plane or planar face that defines the sketch plane.
- **targetBaseOrFormFeature** (Base): The existing base feature that you want to associate this sketch with.
- **includeFaceEdges** (boolean): When a BrepFace is used as the planarEntity argument, this defines if the edges of the face should be included in the sketch.
- **Returns** (Sketch): Returns the newly created Sketch or null if the creation failed.

### addWithoutEdges(planarEntity: Base, occurrenceForCreation: Occurrence) -> Sketch
Creates a new sketch on the specified planar entity. If a BRepFace is provided, the edges of the face are not projected into the sketch so the result of creating a new sketch with this method will always be a new empty sketch.
- **planarEntity** (Base): A construction plane or planar face that defines the sketch plane.
- **occurrenceForCreation** (Occurrence): A creation occurrence is needed if the planarEntity is in another component AND the sketch is not in the root component. The occurrenceForCreation is analogous to the active occurrence in the UI.

This is an optional argument whose default value is null.
- **Returns** (Sketch): Returns the newly created Sketch or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Sketch
Function that returns the specified sketch using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Sketch): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> Sketch
Returns the sketch with the specified name.
- **name** (string): The name of the sketch as seen in the browser and the timeline.
- **Returns** (Sketch): Returns the sketch or null if there isn't a sketch with that name.

## Properties

### count : uinteger [read-only]
Returns the number of sketches in a component

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **API Sample that demonstrates creating sketch lines in various ways.**: Demonstrates several ways to create sketch lines, including as the result of creating a rectangle.
- **Loft Feature API Sample**: Demonstrates creating a new loft feature.
- **Patch Feature API Sample**: Demonstrates creating a new patch feature.
