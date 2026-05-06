# ScaleFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: January 2015

This class defines the methods and properties that pertain to the definition of a scale feature.

**Accessed from:** ScaleFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setToNonUniform(xScale: ValueInput, yScale: ValueInput, zScale: ValueInput) -> boolean
Sets the scale factor for the x, y, z directions to define a non-uniform scale. Calling this method will cause the isUniform property to be set to false. This will fail if the inputEntities collection contains sketches or components.
- **xScale** (ValueInput): A ValueInput object that defines the scale in the X direction.
- **yScale** (ValueInput): A ValueInput object that defines the scale in the Y direction.
- **zScale** (ValueInput): A ValueInput object that defines the scale in the Z direction.
- **Returns** (boolean): Returns true if successful.

## Properties

### inputEntities : ObjectCollection [read-write]
Gets and sets the input entities. This collection can contain sketches, BRep bodies and T-Spline bodies in parametric modeling. It can contain sketches, BRep bodies, T-Spline bodies, mesh bodies, root component and occurrences in non-parametric modeling. If the scaling is non-uniform (the isUniform property is false), this collection cannot contain sketches or components.

### isUniform : boolean [read-only]
Gets if the scale is uniform.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### point : Base [read-write]
Gets and sets the origin point of the scale. This can be a BRepVertex, a SketchPoint or a ConstructionPoint.

### scaleFactor : ValueInput [read-write]
Gets and sets the scale factor used for a uniform scale. Setting this value will cause the isUniform property to be set to true.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

### xScale : ValueInput [read-only]
Gets the scale in X direction.

### yScale : ValueInput [read-only]
Gets the scale in Y direction.

### zScale : ValueInput [read-only]
Gets the scale in Z direction.

## Samples
- **Scale Feature API Sample**: Demonstrates creating a new scale feature.
