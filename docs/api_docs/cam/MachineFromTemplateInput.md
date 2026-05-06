# MachineFromTemplateInput
Namespace: adsk.cam
Inherits: MachineInput
Since: April 2023

Object used as input to create a machine from a given template. Used by "Machine.create(MachineInput)" method. The object holds the data needed to create a machine based on the specified template.

**Accessed from:** MachineFromTemplateInput.create

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(machineTemplate: MachineTemplate) -> MachineFromTemplateInput
Create a "MachineFromTemplateInput" object to be used as input for "Machine.create(MachineInput)" method.
- **machineTemplate** (MachineTemplate): The template to act as a base for creating a machine from.
- **Returns** (MachineFromTemplateInput): The newly created "MachineFromTemplateInput" object in a valid state.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### machineTemplate : MachineTemplate [read-only]
Machine template identifier used to generate a certain type of machine.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
