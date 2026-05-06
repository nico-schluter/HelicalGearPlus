# MachineElement
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Base class for objects that compose a machine.

**Accessed from:** MachineElements.addElement, MachineElements.defaultItemByType, MachineElements.item, MachineElements.itemById, MachineElements.itemsByType

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### elementId : string [read-only]
Identifier for this element. Unique within an element type.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### typeId : string [read-only]
Identifier for this type of machine element.
