# ToolingCapabilitiesMachineElement
Namespace: adsk.cam
Inherits: MachineElement
Since: September 2025

Machine element representing the tooling capabilities of a machine.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### staticTypeId() -> string
Identifying name for all elements of this type. Pass this to the itemByType or itemById methods of MachineElements to filter to elements of this type.
- **Returns** (string): Returns identifier of this type.

## Properties

### elementId : string [read-only]
Identifier for this element. Unique within an element type.

### isToolChangerAutomatic : boolean [read-write]
If your machine has an automatic tool changer, set this to true. For machines with manual tool change capabilities, set this to false.

### isToolPreloadSupported : boolean [read-write]
If your machine has a staging function for the tool changer, set this to true. For machines without staging tool change capabilities, set this to false.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### maxToolCount : integer [read-write]
Property that represents the maximum number of tools available in the tool magazine, or the maximum number of tools that can be programmed in the control.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### typeId : string [read-only]
Identifier for this type of machine element.
