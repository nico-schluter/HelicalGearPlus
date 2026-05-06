# RuleFilletFeatures
Namespace: adsk.fusion
Inherits: Base
Since: September 2015

This object is retired. See more information in the 'Remarks' section below.

This object is obsolete. You should use the FilletFeatures to access the rule fillet features. The FilletFeature.filletFeatureType can be used to determine if a FilletFeature is a rule fillet feature or not.

**Accessed from:** Features.ruleFilletFeatures

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> RuleFilletFeature
Function that returns the specified rule fillet feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (RuleFilletFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> RuleFilletFeature
Function that returns the specified rule fillet feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (RuleFilletFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of rule fillet features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
