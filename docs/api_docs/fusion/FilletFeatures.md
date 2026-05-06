# FilletFeatures
Namespace: adsk.fusion
Inherits: Base
Since: November 2014

Collection that provides access to all of the existing fillet features in a component and supports the ability to create new fillet features.

**Accessed from:** Features.filletFeatures

## Methods

### add(input: FilletFeatureInput) -> FilletFeature
Creates a new fillet feature.
- **input** (FilletFeatureInput): A FilletFeatureInput object that defines the desired fillet. Use the createInput method to create a new FilletFeatureInput object and then use methods on it (the FilletFeatureInput object) to define the fillet.
- **Returns** (FilletFeature): Returns the newly created FilletFeature object or null if the creation failed.

### addFullRoundFillet(input: FullRoundFilletFeatureInput) -> FilletFeature
Creates a new full round fillet feature.
- **input** (FullRoundFilletFeatureInput): A FullRoundFilletFeatureInput object that defines the desired fillet. Use the createFullRoundFilletInput method to create a new FullRoundFilletFeatureInput object and then use methods on it (the FullRoundFilletFeatureInput object) to define the fillet.
- **Returns** (FilletFeature): Returns the newly created FilletFeature object or null if the creation failed.

### addRuleFillet(input: RuleFilletFeatureInput) -> FilletFeature
Creates a new rule fillet feature.
- **input** (RuleFilletFeatureInput): A RuleFilletFeatureInput object that defines the desired fillet. Use the createRuleFilletInput method to create a new RuleFilletFeatureInput object and then use methods on it(the RuleFilletFeatureInput object) to define the fillet.
- **Returns** (FilletFeature): Returns the newly created FilletFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createFullRoundFilletInput() -> FullRoundFilletFeatureInput
Creates a FullRoundFilletFeatureInput object. Use properties and methods on this object to define the fillet you want to create and then use the addFullRoundFillet method, passing in the FullRoundFilletFeatureInput object.
- **Returns** (FullRoundFilletFeatureInput): Returns the newly created FullRoundFilletFeatureInput object or null if the creation failed.

### createInput() -> FilletFeatureInput
Creates a FilletFeatureInput object. Use properties and methods on this object to define the fillet you want to create and then use the Add method, passing in the FilletFeatureInput object.
- **Returns** (FilletFeatureInput): Returns the newly created FilletFeatureInput object or null if the creation failed.

### createRuleFilletInput() -> RuleFilletFeatureInput
Creates a RuleFilletFeatureInput object. Use properties and methods on this object to define the fillet you want to create and then use the addRuleFillet method, passing in the RuleFilletFeatureInput object.
- **Returns** (RuleFilletFeatureInput): Returns the newly created RuleFilletFeatureInput object or null if the creation failed.

### item(index: uinteger) -> FilletFeature
Function that returns the specified fillet feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (FilletFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> FilletFeature
Function that returns the specified fillet feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (FilletFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of fillet features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Constant Radius Fillet API Sample**: Creates a constant radius fillet on the selected edge. If there are tangent contiguous edges that will also be included in the fillet.
- **Fillet Feature Edit API Sample**: Demonstrates editing a fillet feature.
To successfully run this sample you can use this
- **Fillet Feature API Sample**: Demonstrates creating fillets using the various types of fillets. Create a new design and add a box that is at least 2 cm on each side. The script creates a constant radius, variable radius and chord length fillets. After creating each one, it deletes it and then creates the next. To see any of the fillets that were deleted, undo to get the fillet back.
