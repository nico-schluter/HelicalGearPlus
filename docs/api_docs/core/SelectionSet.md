# SelectionSet
Namespace: adsk.core
Inherits: Base
Since: May 2022

The SelectionSet object represents a Selection Set as seen in the user interface. Using a SelectionSet, you can access all the associated data, activate, and delete a selection set.

In the user interface, selection sets are created by selecting geometry and then running the "Create Selection Set" command from the context menu. All existing selection sets are shown in a "Selection Sets" folder in the browser where they can be activated and deleted.

**Accessed from:** SelectionSets.add, SelectionSets.item, SelectionSets.itemByName

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this SelectionSet object.
- **Returns** (boolean): Returns true if the deletion was successful.

### select() -> boolean
Causes the entities in this SelectionSet object to be the active selection.
- **Returns** (boolean): Returns true if the selection was successful.

## Properties

### entities : array [read-write]
Gets and sets the entities in the selection set. Setting this property is the equivalent of using the "Update" option for a selection set in the user-interface.

Setting the entities can fail in the case where you provide an entity that is not valid for selection. All entities must be in the context of the root component. This means if the entity isn't directly owned by the root component, it must be a proxy.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets and sets the name of the SelectionSet object. If a name is assigned that is already used, Fusion will append a counter to the name to make it unique.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
