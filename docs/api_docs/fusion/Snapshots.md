# Snapshots
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Provides access to the Snapshots within a design and provides methods to create new Snapshots.

**Accessed from:** Design.snapshots, FlatPatternProduct.snapshots, WorkingModel.snapshots

## Methods

### add() -> Snapshot
Creates a new snapshot. Creating a snapshot is only valid when the HasPendingTransforms property returns true.
- **Returns** (Snapshot): Returns the newly created snapshot.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> Snapshot
Function that returns the specified snapshot in the collection using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Snapshot): Returns the specified item or null if an invalid index was specified.

### revertPendingSnapshot() -> boolean
Reverts and changes that have been made that can be snapshot. This effectively reverts the design back to the last snapshot. This is only valid when the HasPendingSnapshot property returns true.
- **Returns** (boolean): Returns true if the revert was successful.

## Properties

### count : uinteger [read-only]
The number of items in the collection.

### hasPendingSnapshot : boolean [read-only]
Indicates if there are any changes that have been made than can be snapshot.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
