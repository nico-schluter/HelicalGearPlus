# MachinePart
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Object representing some part of a machine, such as the static base of the machine, an axis, or the attachment points for tools and fixtures.

**Accessed from:** MachineItem.part, MachinePart.parent, MachineParts.add, MachineParts.item, MachineParts.itemById

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe()
Delete this part and its children from the kinematics tree.

## Properties

### axis : MachineAxis [read-only]
Get the axis object for this part used to reference this part for other operations. Only valid when partType is Axis, otherwise returns null

### children : MachineParts [read-only]
Get the collection of child parts.

### id : string [read-only]
Get the internal ID of the part. This is unique with respect to other MachineParts in the Machine.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : MachinePart [read-write]
Get or set the parent of this part. Returns null if this part is a root part. Setting the parent will add this part to the end of the parent's children collection. Setting the parent will throw an error if the new parent is this part or a child of this part.

### partType : MachinePartTypes [read-only]
Get the type of this part.

### spindle : MachineSpindle [read-only]
Get the spindle object for this part used to reference this part for other operations. Will return null if the part has no spindle assigned.

### toolStation : MachineToolStation [read-only]
Get the tool station object for this part. Will return null if the part has no tool station assigned.
