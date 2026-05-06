# HemFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: September 2025

This class defines the methods and properties that pertain to the definition of a hem feature.

**Accessed from:** HemFeatures.createHemFeatureInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setDoubleHem(edge: BRepEdge, gap: ValueInput, length: ValueInput, setback: ValueInput, isFlipped: boolean, bendPositionType: BendPositionTypes) -> boolean
Sets the hem input with the values to be used in order to create a double hem feature.
- **edge** (BRepEdge): The BRepEdge that defines the location of the hem.
- **gap** (ValueInput): The gap distance of the hem.
- **length** (ValueInput): The length of the double hem.
- **setback** (ValueInput): The setback of the double hem.
- **isFlipped** (boolean): Indicates if the hem direction is flipped.
- **bendPositionType** (BendPositionTypes): The bend location type for the hem.
- **Returns** (boolean): Returns true if defining the hem is successful.

### setFlatHem(edge: BRepEdge, length: ValueInput, isFlipped: boolean, bendPositionType: BendPositionTypes) -> boolean
Sets the hem input with the values to be used in order to create a flat hem feature.
- **edge** (BRepEdge): The BRepEdge that defines the location of the hem.
- **length** (ValueInput): The length of the hem.
- **isFlipped** (boolean): Indicates if the hem direction is flipped.
- **bendPositionType** (BendPositionTypes): The bend location type for the hem.
- **Returns** (boolean): Returns true if defining the hem is successful.

### setOpenHem(edge: BRepEdge, length: ValueInput, gap: ValueInput, isFlipped: boolean, bendPositionType: BendPositionTypes) -> boolean
Sets the hem input with the values to be used in order to create an open hem feature.
- **edge** (BRepEdge): The BRepEdge that defines the location of the hem.
- **length** (ValueInput): The length of the hem.
- **gap** (ValueInput): The gap distance of the hem.
- **isFlipped** (boolean): Indicates if the hem direction is flipped.
- **bendPositionType** (BendPositionTypes): The bend location type for the hem.
- **Returns** (boolean): Returns true if defining the hem is successful.

### setRolledHem(edge: BRepEdge, radius: ValueInput, angle: ValueInput, isFlipped: boolean, bendPositionType: BendPositionTypes) -> boolean
Sets the hem input with the values to be used in order to create a rolled hem feature.
- **edge** (BRepEdge): The BRepEdge that defines the location of the hem.
- **radius** (ValueInput): The radius of the rolled hem.
- **angle** (ValueInput): The angle of the rolled hem.
- **isFlipped** (boolean): Indicates if the hem direction is flipped.
- **bendPositionType** (BendPositionTypes): The bend location type for the hem.
- **Returns** (boolean): Returns true if defining the hem is successful.

### setRopeHem(edge: BRepEdge, length: ValueInput, gap: ValueInput, radius: ValueInput, isFlipped: boolean, bendPositionType: BendPositionTypes) -> boolean
Sets the hem input with the values to be used in order to create a rope hem feature.
- **edge** (BRepEdge): The BRepEdge that defines the location of the hem.
- **length** (ValueInput): The length of the rope hem.
- **gap** (ValueInput): The gap distance of the hem.
- **radius** (ValueInput): The radius of the rope hem.
- **isFlipped** (boolean): Indicates if the hem direction is flipped.
- **bendPositionType** (BendPositionTypes): The bend location type for the hem.
- **Returns** (boolean): Returns true if defining the hem is successful.

### setTeardropHem(edge: BRepEdge, radius: ValueInput, length: ValueInput, gap: ValueInput, isFlipped: boolean, bendPositionType: BendPositionTypes) -> boolean
Sets the hem input with the values to be used in order to create a teardrop hem feature.
- **edge** (BRepEdge): The BRepEdge that defines the location of the hem.
- **radius** (ValueInput): The radius of the teardrop hem.
- **length** (ValueInput): The angle of the teardrop hem.
- **gap** (ValueInput): The gap distance of the hem.
- **isFlipped** (boolean): Indicates if the hem direction is flipped.
- **bendPositionType** (BendPositionTypes): The bend location type for the hem.
- **Returns** (boolean): Returns true if defining the hem is successful.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Hem Feature Sample**: Demonstrates creating a new sheet metal hem feature.
