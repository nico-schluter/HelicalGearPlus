# Selections
Namespace: adsk.core
Inherits: Base
Since: August 2014

Provides access to and control over the set of selected entities in the user interface.

**Accessed from:** UserInterface.activeSelections

## Methods

### add(entity: Base) -> boolean
Adds the entity to the set of currently selected entities. The user will see the entity become selected in the user interface.
- **entity** (Base): The entity to select and add to this selection set.
- **Returns** (boolean): Returns true if successful.

### asArray() -> Selection
Returns an array containing all of the current selections. This is useful in cases where you need to iterate over the set of selected entities but need to create or edit data as you process each one. Selections are fragile and creation and edit operations will clear the selections so you won't have access to the complete list after processing the first one.
- **Returns** (Selection): Returns an array of all of the current selections. Selection objects are returned so you'll need to call their entity properties to get the actual selected entity.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### clear() -> boolean
Clears the selection set so no entities are currently selected.
- **Returns** (boolean): Returns true if successful.

### item(index: uinteger) -> Selection
Returns the specified selection using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (Selection): Returns the specified item or null if an invalid index was specified.

### removeByEntity(entity: Base) -> boolean
Removes the selections that are associated with the specified entity from the set of selected entities.
- **entity** (Base): The entity to remove selections of.
- **Returns** (boolean): Returns true if the item was removed or not currently selected.

### removeByIndex(index: integer) -> boolean
Removes an item from the set of selected entities.
- **index** (integer): The index of the selection to remove.
- **Returns** (boolean): Returns true if the item was removed successfully.

### removeBySelection(selection: Selection) -> boolean
Removes the specified selection from the set of selected entities.
- **selection** (Selection): The selection to remove.
- **Returns** (boolean): Returns true if the item was removed or not currently selected.

## Properties

### all : ObjectCollection [read-write]
Gets or sets all entities currently selected.

### count : uinteger [read-only]
Gets the number of entities currently selected.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
