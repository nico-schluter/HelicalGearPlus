# ArrangeDefinition2DInput
Namespace: adsk.fusion
Inherits: ArrangeDefinitionInput
Since: January 2025

This object defines all of the settings associated with a 2D arrangement. This is used for both rectangular and true shape arrangements, but some properties are ignored in some cases.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### globalQuantity : ValueInput [read-write]
Gets and sets the global quantity, which is the default quantity value for components. This defaults to 1.

This value will become a parameter when the arrangement is created. When created with a real value it must be a whole number. You can also use a string where it is interpreted the same as when entered in the command dialog. The expression must result in a unitless whole number. It's also possible to use an equation like "Total / 4" where "Total" is an existing parameter and be evenly divided by four.

### globalRotation : ArrangeRotationTypes [read-write]
Gets and sets the global rotation type. This defaults to AllRotationsArrangeRotationType.

### grainDirection : ValueInput [read-write]
Defines the angle of the grain direction of the envelope. This is only used when the solver type is True Shape. An angle of 0 is in the X direction of the envelope, and the default value is zero.

This value will become a parameter when the arrangement is created. If the ValueInput is created using a real number it is in radians. If you use a string, it is evaluated the same as a value would be in the command dialog and uses degrees as the units. For example, if you specify "45" it will result in a 45 degree grain direction. Using a string you can also define an equation for the expression, "PartAngle / 2" where "PartAngle"

### isCreateCopies : boolean [read-write]
Gets and set if the original components will be moved or copied to create the arrangement. This defaults to true.

### isGlobalDirectionFaceUp : boolean [read-write]
Gets and sets the global direction for input faces. When true, the components specified by selecting a face will be oriented such that the selection face will be oriented upward in the arrangement. This defaults to true.

### isPartInPartAllowed : boolean [read-write]
Gets and sets if parts can be nested within void areas of other parts. This defaults to true.

This is only used when the solver type is 2D True Shape and is ignored for 2D Rectangular solutions.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### solverType : ArrangeSolverTypes [read-only]
Gets the type of arrange feature defined by this definition.
