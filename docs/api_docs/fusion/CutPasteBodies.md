# CutPasteBodies
Namespace: adsk.fusion
Inherits: Base
Since: June 2017

Collection that provides access to all of the existing cut-paste features in a design. These are created in the UI by cutting and then pasting a B-Rep body.

**Accessed from:** Features.cutPasteBodies

## Methods

### add(sourceBody: Base) -> CutPasteBody
Cuts and copies the specified body into the component that owns this CutPasteBodies collection. This is effectively the equivalent of moving a body.
- **sourceBody** (Base): Either an ObjectCollection of BRepBodies or a single BRepBody object to cut.
- **Returns** (CutPasteBody): Returns the newly created BRepBody object or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> CutPasteBody
Function that returns the specified Cut/Paste Body feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (CutPasteBody): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> CutPasteBody
Function that returns the specified Cut/Paste Body feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (CutPasteBody): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of Cut/Paste Body features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Cut Paste Bodies API Sample**: Demonstrates how to use Cut Paste Bodies related API.
