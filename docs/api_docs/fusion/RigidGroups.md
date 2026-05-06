# RigidGroups
Namespace: adsk.fusion
Inherits: Base
Since: September 2015

The collection of rigid groups in this component. This provides access to all existing rigid groups and supports the ability to create new rigid groups.

**Accessed from:** Component.rigidGroups, FlatPatternComponent.rigidGroups

## Methods

### add(occurrences: ObjectCollection, includeChildren: boolean) -> RigidGroup
Creates a new rigid group.
- **occurrences** (ObjectCollection): An ObjectCollection containing the occurrences to use in creating the rigid group.
- **includeChildren** (boolean): Boolean indicating if the children of the input occurrences should be included in the rigid group.
- **Returns** (RigidGroup): Returns the new RigidGroup object or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> RigidGroup
Function that returns the specified rigid group using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (RigidGroup): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> RigidGroup
Function that returns the specified rigid group using a name.
- **name** (string): The name of the item within the collection to return.
- **Returns** (RigidGroup): Returns the specified item or null if an invalid name was specified.

## Properties

### count : uinteger [read-only]
Returns number of joint origins in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Rigid Group API Sample**: Demonstrates creating a new Rigid Group.
