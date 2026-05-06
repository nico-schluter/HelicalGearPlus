# MoveFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: March 2015

This class defines the methods and properties that pertain to the definition of a move feature.

**Accessed from:** MoveFeatures.createInput, MoveFeatures.createInput2

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### defineAsFreeMove(transform: Matrix3D) -> boolean
This method will define a move feature whose translation and orientation is defined using a transformation matrix. A matrix can define any translation and orientation.
- **transform** (Matrix3D): The transformation matrix that defines the transform to apply. The matrix must be an orthogonal matrix; that is the axes are perpendicular to each other and there isn't any scaling or mirroring defined.
- **Returns** (boolean): Returns true if defining the type of move is successful.

### defineAsPointToPoint(originPoint: Base, targetPoint: Base) -> boolean
This method defines a move feature described by a translation from one point to another.
- **originPoint** (Base): The first point that defines the start position of the move.
- **targetPoint** (Base): The second point that defines the direction and distance of the move.
- **Returns** (boolean): Returns true if defining the type of move is successful.

### defineAsPointToPosition(point: Base, xDistance: ValueInput, yDistance: ValueInput, zDistance: ValueInput, isDesignSpace: boolean) -> boolean
This method defines a move feature described by a point and an offset. The distances define offsets in the X, Y, and Z directions in either design or component space. To not move the input entities at all the offset distances should be set to the current location of the point in either design or component space. Adding or subtracting to those values will then move the entities that distance. It's best to experiment with the command interactively to understand the behavior.
- **point** (Base): An entity that defines a point in space. This can be a sketch point, a construction point, or a BRepVertex.
- **xDistance** (ValueInput): A ValueInput object that defines the offset in the X direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units will be used.
- **yDistance** (ValueInput): A ValueInput object that defines the offset in the Y direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units will be used.
- **zDistance** (ValueInput): A ValueInput object that defines the offset in the Z direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units will be used.
- **isDesignSpace** (boolean): Defines if the translation is defined with respect to the design or component space. Design space is the same as the root component space.
- **Returns** (boolean): Returns true if defining the type of move is successful.

### defineAsRotate(axisEntity: Base, angle: ValueInput) -> boolean
This method defines a move feature that is described by an axis and rotation angle.
- **axisEntity** (Base): A linear entity that defines the axis of rotation. This can be a linear BRepEdge, ConstructionAxis, or a SketchLine. The natural direction of the entity defines a right-hand rule for the rotation direction.
- **angle** (ValueInput): A ValueInput object that defines the rotation angle. If the ValueInput is created using a real value, the angle is in radians. If it's defined using a string, the default document units will be used.
- **Returns** (boolean): Returns true if defining the type of move is successful.

### defineAsTranslateAlongEntity(linearEntity: Base, distance: ValueInput) -> boolean
This method will define a move feature that defines a translation along a specified entity.
- **linearEntity** (Base): A linear entity that defines the direction of the move. This can be a linear BRepEdge, ConstructionAxis, or a SketchLine. The entity defines the direction, not the distance. The natural direction of the entity defines the translation direction.
- **distance** (ValueInput): A ValueInput object that defines the offset distance. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units are used.
- **Returns** (boolean): Returns true if defining the type of move is successful.

### defineAsTranslateXYZ(xDistance: ValueInput, yDistance: ValueInput, zDistance: ValueInput, isDesignSpace: boolean) -> boolean
This method will define a move feature that defines a translation in X, Y, and Z.
- **xDistance** (ValueInput): A ValueInput object that defines the offset in the X direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units are used.
- **yDistance** (ValueInput): A ValueInput object that defines the offset in the Y direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units are used.
- **zDistance** (ValueInput): A ValueInput object that defines the offset in the Z direction. If the ValueInput is created using a real value, the distance is in centimeters. If it's defined using a string, the default document units are used.
- **isDesignSpace** (boolean): Defines if the translation is defined with respect to the design or component space. Design space is the same as the root component space.
- **Returns** (boolean): Returns true if defining the type of move is successful.

## Properties

### inputEntities : ObjectCollection [read-write]
An ObjectCollection containing the objects to move. The collection can contain BRepBody or BRepFace objects but not a mixture of the two types.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

### transform : Matrix3D [read-write]
This function is retired. See more information in the 'Remarks' section below.

Gets and sets the transform to apply to the input entities. This can describe a move (translation) or a rotation. The matrix must define an orthogonal transform. That is the axes remain perpendicular to each other and there isn't any scale or mirror defined.

## Samples
- **Move Feature API Sample**: Demonstrates creating a new move feature.
