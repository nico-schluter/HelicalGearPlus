# AssemblyConstraints
Namespace: adsk.fusion
Inherits: Base
Since: July 2025

The collection of assembly constraints in this component. This provides access to all existing assembly constraints and supports the ability to create new assembly constraints.

**Accessed from:** Component.assemblyConstraints, FlatPatternComponent.assemblyConstraints

## Methods

### add(input: AssemblyConstraintInput) -> AssemblyConstraint
Creates a new assembly constraint.
- **input** (AssemblyConstraintInput): The AssemblyConstraintInput object that defines the geometry and various inputs that define an assembly constraint. An AssemblyConstraintInput object is created using the AssemblyConstraints.createInput method.
- **Returns** (AssemblyConstraint): Returns the newly created AssemblyConstraint or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput() -> AssemblyConstraintInput
Creates an assembly constraint input to define an assembly constraint. Use functionality on the returned AssemblyConstraintInput to define the input needed to create an assembly constraint.
- **Returns** (AssemblyConstraintInput): Returns an AssemblyConstraintInput.

### item(index: uinteger) -> AssemblyConstraint
Function that returns the specified assembly constraint using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (AssemblyConstraint): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> AssemblyConstraint
Function that returns the specified assembly constraint object using a name.
- **name** (string): The name of the item within the collection to return.
- **Returns** (AssemblyConstraint): Returns the specified item or null if an invalid name was specified.

## Properties

### count : uinteger [read-only]
Returns the number of assembly constraint objects in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
