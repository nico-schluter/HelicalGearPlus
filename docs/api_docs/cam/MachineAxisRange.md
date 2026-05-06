# MachineAxisRange
Namespace: adsk.cam
Inherits: Base
Since: April 2023

Class representing limits of motion for a machine axis.

**Accessed from:** LinearMachineAxis.physicalRange, LinearMachineAxisInput.physicalRange, MachineAxis.physicalRange, MachineAxisInput.physicalRange, MachineAxisRange.create, MachineAxisRange.createInfinite, RotaryMachineAxis.physicalRange, RotaryMachineAxisConfiguration.wrapAroundAtRange, RotaryMachineAxisInput.physicalRange

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### create(min: double, max: double) -> MachineAxisRange
Creates a new range object with limited extents. Requires min to be less than or equal to max. Types of the fields depend on where this range is being used. Centimeters are used for distances and radians for angles.
- **min** (double): New minimum value for range.
- **max** (double): New maximum value for range.
- **Returns** (MachineAxisRange): A new range object. Returns null if validation fails.

### createInfinite() -> MachineAxisRange
Creates a new unbounded range object.
- **Returns** (MachineAxisRange): A new range object.

## Properties

### isInfinite : boolean [read-only]
Is the range infinite.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### max : double [read-only]
Maximum value of range Type depends on where this range is being used. Centimeters are used for distances and radians for angles. Returns infinity if this range is infinite.

### min : double [read-only]
Minimum value of range. Type depends on where this range is being used. Centimeters are used for distances and radians for angles. Returns -infinity if this range is infinite.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
