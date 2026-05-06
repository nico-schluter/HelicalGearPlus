# CoilFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: March 2016

This class defines the methods and properties that pertain to the definition of a coil feature.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setToHeightAndPitchCoil(height: ValueInput, pitch: ValueInput, angle: ValueInput) -> boolean
Sets the coil type to HeightAndPitchCoilType.
- **height** (ValueInput): A ValueInput object that defines the height.
- **pitch** (ValueInput): A ValueInput object that defines the pitch.
- **angle** (ValueInput): A ValueInput object that defines angle.
- **Returns** (boolean): Returns true if successful.

### setToRevolutionAndHeight(revolutions: ValueInput, height: ValueInput, angle: ValueInput) -> boolean
Sets the coil type to RevolutionsAndHeightCoilType.
- **revolutions** (ValueInput): A ValueInput object that defines the number of revolutions.
- **height** (ValueInput): A ValueInput object that defines the height.
- **angle** (ValueInput): A ValueInput object that defines angle.
- **Returns** (boolean): Returns true if successful.

### setToRevolutionsAndPitch(revolutions: ValueInput, pitch: ValueInput, angle: ValueInput) -> boolean
Sets the coil type to RevolutionsAndPitchCoilType.
- **revolutions** (ValueInput): A ValueInput object that defines the number of revolutions.
- **pitch** (ValueInput): A ValueInput object that defines the pitch.
- **angle** (ValueInput): A ValueInput object that defines angle.
- **Returns** (boolean): Returns true if successful.

### setToSpiral(revolutions: ValueInput, pitch: ValueInput) -> boolean
Sets the coil type to SpiralCoilType.
- **revolutions** (ValueInput): A ValueInput object that defines the number of revolutions.
- **pitch** (ValueInput): A ValueInput object that defines the pitch.
- **Returns** (boolean): Returns true if successful.

## Properties

### angle : ValueInput [read-only]
Gets the angle. Returns null in the case where the coilType property returns SpiralCoilType.

### basePlane : Base [read-write]
Gets and sets the base plane.

### coilSectionPosition : CoilFeatureSectionPositions [read-write]
Gets the section position of the coil. It defaults to InsideCoilSectionPosition.

### coilSectionType : CoilFeatureSectionTypes [read-write]
Gets the section type of the coil. It defaults to CircularCoilSectionType.

### coilType : CoilFeatureTypes [read-only]
Gets the type of the coil.

### diameter : ValueInput [read-write]
Gets and sets the diameter.

### height : ValueInput [read-only]
Gets the height. Returns null in the case where the coilType property returns RevolutionsAndPitchCoilType.

### isClockwiseRotation : boolean [read-write]
Gets and sets whether the rotation is clockwise or counter-clockwise. A value of true indicates clockwise rotation. It defaults to true.

### isSolid : boolean [read-write]
Specifies if the coil should be created as a solid or surface. This is initialized to true so a solid will be created if it's not changed. It only can be set to false in non-parametric modeling.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### operation : FeatureOperations [read-write]
Gets and sets the type of operation performed by the coil.

### pitch : ValueInput [read-only]
Gets the pitch. Returns null in the case where the coilType property returns RevolutionsAndHeightCoilType or SpiralCoilType.

### revolutions : ValueInput [read-only]
Gets the revolutions number. Returns null in the case where the coilType property returns HeightAndPitchCoilType.

### sectionSize : ValueInput [read-write]
Gets and sets the section size.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.
