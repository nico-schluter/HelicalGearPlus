# CustomGraphicsGroups
Namespace: adsk.fusion
Inherits: Base
Since: September 2017

Provides access to a set of graphics groups that are either associated with a component or owned by another CustomGraphicsGroup object. This object also supports the creation of new custom graphics groups.

**Accessed from:** CAM.customGraphicsGroups, Component.customGraphicsGroups, FlatPatternComponent.customGraphicsGroups

## Methods

### add() -> CustomGraphicsGroup
Creates a new, empty CustomGraphicsGroup.
- **Returns** (CustomGraphicsGroup): Returns the new CustomGraphicsGroup object or null in the case of a failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> CustomGraphicsGroup
Function that returns the specified graphics group using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (CustomGraphicsGroup): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of graphics groups in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
