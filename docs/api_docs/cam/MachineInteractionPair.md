# MachineInteractionPair
Namespace: adsk.cam
Inherits: Base
Since: September 2025

MachineInteractionPair objects control how a pair of MachineItems interact with each other.

**Accessed from:** InteractionsMachineElement.createMachineInteractionPair, InteractionsMachineElement.item

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### reset()
Clear this MachineInteractionPair. This pair will then represent two MachineItems that do not interact.

## Properties

### isCheckedForCollisions : boolean [read-write]
Whether these MachineItems should be checked for collisions.

### isIgnored : boolean [read-only]
Whether this MachineInteractionPair will be ignored.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### item1 : MachineItem [read-only]
The first MachineItem involved in this MachineInteractionPair.

### item2 : MachineItem [read-only]
The second MachineItem involved in this MachineInteractionPair.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
