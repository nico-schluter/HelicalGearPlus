# InteractionsMachineElement
Namespace: adsk.cam
Inherits: MachineElement
Since: September 2025

Machine element representing the machine's interactions. This controls how MachineItems interact with each other.

## Methods

### apply(setting: MachineInteractionPair)
Add an MachineInteractionPair. This will overwrite any existing MachineInteractionPair with the same item1 and item2.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createMachineInteractionPair(item1: MachineItem, item2: MachineItem)
Create a MachineInteractionPair that will control how the two items interact.

### createMachineItem(type: MachineItemType, part: MachinePart)
Create a MachineItem.

### item(index: integer) -> MachineInteractionPair
Get the MachineInteractionPair at index in this collection.
- **index** (integer): The index of the MachineInteractionPair.
- **Returns** (MachineInteractionPair): The MachineInteractionPair at index.

### resetMachineInteractionPairs()
Restore all MachineInteractionPairs to their defaults.

### staticTypeId() -> string
Identifying name for all elements of this type. Pass this to the itemByType or itemById methods of MachineElements to filter to elements of this type.
- **Returns** (string): Returns identifier of this type.

## Properties

### count : uinteger [read-only]
Get the number of pairs in this collection.

### elementId : string [read-only]
Identifier for this element. Unique within an element type.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### typeId : string [read-only]
Identifier for this type of machine element.
