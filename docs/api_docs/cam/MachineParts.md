# MachineParts
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Object that represents a collection of machine parts. These parts are the children of another part or the collection of base parts from MachineKinematics.

**Accessed from:** KinematicsMachineElement.parts, MachinePart.children

## Methods

### add(partInput: MachinePartInput) -> MachinePart
Add a new part to this collection. The part's parent will be set to the owner of this collection, or null if this is the root parts collection.

If the passed MachinePartInput has a MachineAxisInput a new MachineAxis will be created.
- **partInput** (MachinePartInput): Part input object used to create the new MachinePart.
- **Returns** (MachinePart): Returns the newly created MachinePart or null if creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createPartInput(partType: MachinePartTypes) -> MachinePartInput
Create a new MachinePartInput.
- **partType** (MachinePartTypes): The type of part to create. When this parameter is Axis, you must set a value for axisInput.
- **Returns** (MachinePartInput): Returns the new MachinePartInput or null if creation failed.

### item(index: integer) -> MachinePart
Get the part at index in this collection.
- **index** (integer): The index of the part.
- **Returns** (MachinePart): The MachinePart at index.

### itemById(id: string) -> MachinePart
Get the part with the given ID.
- **id** (string): The ID for the part to get.
- **Returns** (MachinePart): Returns the MachinePart with the given ID, or null if the given ID does not match any part in the collection.

## Properties

### count : uinteger [read-only]
Get the number of parts in this collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
