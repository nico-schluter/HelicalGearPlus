# MachineItem
Namespace: adsk.cam
Inherits: Base
Since: September 2025

An item on a machine that can collide. That is, a MachinePart, or something attached to a MachinePart. Create them via InteractionsMachineElement::createMachineItem

**Accessed from:** InteractionsMachineElement.createMachineItem, MachineInteractionPair.item1, MachineInteractionPair.item2

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### itemType : MachineItemType [read-only]
The type of this MachineItem.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### part : MachinePart [read-only]
The machine part.
