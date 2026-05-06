# RectangularPatternFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

This class defines the methods and properties that pertain to the definition of a rectangular pattern feature.

**Accessed from:** RectangularPatternFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setDirectionTwo(directionTwoEntity: Base, quantityTwo: ValueInput, distanceTwo: ValueInput) -> boolean
Sets all of the input required to define the pattern in the second direction.
- **directionTwoEntity** (Base): Specifies the entity used to define the second direction entity. This can be a linear edge, construction axis, sketch line or rectangular pattern feature. If a rectangular pattern feature is set, the directionOneEntity and directionTwoEntity properties return the same rectangular pattern feature.

This argument can be null to indicate that the default second direction is to be used, which is 90 degrees to the first direction.
- **quantityTwo** (ValueInput): Specifies the number of instances in the second direction.
- **distanceTwo** (ValueInput): Specifies the distance in the second direction. How this value is used depends on the value of the PatternDistanceType property. If the value is ExtentPatternDistanceType then it defines the total distance of the pattern. If the value is SpacingPatternDistanceType then it defines the distance between each element.
- **Returns** (boolean): Returns true if it was successful.

## Properties

### directionOne : Vector3D [read-only]
Returns a Vector3D indicating the positive direction of direction one.

### directionOneEntity : Base [read-write]
Gets and sets the first direction entity. This can be a linear edge, construction axis, sketch line or rectangular pattern feature. If a rectangular pattern feature is set, the directionOneEntity and directionTwoEntity properties return the same rectangular pattern feature.

### directionTwo : Vector3D [read-only]
Returns a Vector3D indicating the positive direction of direction two.

### directionTwoEntity : Base [read-write]
Gets and sets the second direction entity. This can be a linear edge, construction axis, sketch line or rectangular pattern feature. If a rectangular pattern feature is set, the directionOneEntity and directionTwoEntity properties return the same rectangular pattern feature.

### distanceOne : ValueInput [read-write]
Gets and sets the distance in the first direction.

### distanceTwo : ValueInput [read-write]
Gets and sets the distance in the second direction.

### inputEntities : ObjectCollection [read-write]
Gets and sets the input entities. The collection can contain faces, features, bodies or occurrences. All of the entities must be of a single type. For example, it can't contain features and occurrences but only features or occurrences.

### isSymmetricInDirectionOne : boolean [read-write]
Gets and sets if the pattern in direction one is in one direction or symmetric.

### isSymmetricInDirectionTwo : boolean [read-write]
Gets and sets if the pattern in direction two is in one direction or symmetric.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### patternComputeOption : PatternComputeOptions [read-write]
Gets and sets the compute option when patterning features. The default value for this is AdjustPatternCompute. This property only applies when patterning features and is ignored in the direct modeling environment.

### patternDistanceType : PatternDistanceType [read-write]
Gets and sets how the distance between elements is computed.

### quantityOne : ValueInput [read-write]
Gets and sets the number of instances in the first direction.

### quantityTwo : ValueInput [read-write]
Gets and sets the number of instances in the second direction.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

## Samples
- **Manage Participant Bodies API Sample**: Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also.
- **RectangularPattern Feature**: Demonstrates creating a new rectangular pattern feature.
