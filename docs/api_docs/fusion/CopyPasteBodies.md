# CopyPasteBodies
Namespace: adsk.fusion
Inherits: Base
Since: June 2017

Collection that provides access to all of the existing copy-paste features in a design. These are created in the UI by copying and then pasting a B-Rep body.

**Accessed from:** Features.copyPasteBodies

## Methods

### add(sourceBody: Base) -> CopyPasteBody
Copies the specified body into the component that owns this CopyPasteBodies collection.
- **sourceBody** (Base): Either an ObjectCollection of BRepBodies or a single BRepBody object to copy.
- **Returns** (CopyPasteBody): Returns the newly created BRepBody object or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> CopyPasteBody
Function that returns the specified Copy/Paste Body feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (CopyPasteBody): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> CopyPasteBody
Function that returns the specified Copy/Paste Body feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (CopyPasteBody): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of Copy/Paste Body features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Copy Paste Bodies API Sample**: Demonstrates how to use Copy Paste Bodies related API.
