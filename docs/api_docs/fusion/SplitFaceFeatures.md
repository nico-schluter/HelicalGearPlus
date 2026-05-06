# SplitFaceFeatures
Namespace: adsk.fusion
Inherits: Base
Since: June 2015

Collection that provides access to all of the existing split face features in a component and supports the ability to create new split face features.

**Accessed from:** Features.splitFaceFeatures

## Methods

### add(input: SplitFaceFeatureInput) -> SplitFaceFeature
Creates a new split face feature.
- **input** (SplitFaceFeatureInput): A SplitFaceFeatureInput object that defines the desired split face feature. Use the createInput method to create a new SplitFaceFeatureInput object and then use methods on it (the SplitFaceFeatureInput object) to define the split face.
- **Returns** (SplitFaceFeature): Returns the newly created SplitFaceFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(facesToSplit: ObjectCollection, splittingTool: Base, isSplittingToolExtended: boolean) -> SplitFaceFeatureInput
Creates a SplitFaceFeatureInput object. Use properties and methods on this object to define the split face you want to create and then use the Add method, passing in the SplitFaceFeatureInput object.

A newly created SplitFaceFeatureInput object defaults to creating a split face feature using the "Split with Surface" option. You can use functions on the SplitFaceFeatureInput object to define a different type of split type.
- **facesToSplit** (ObjectCollection): Input the faces to be split. The collection can contain one or more faces from solid and/or open bodies.
- **splittingTool** (Base): Input entity(s) that defines the splitting tool. The splitting tool can be a single entity or an ObjectCollection containing solid and/or open bodies, construction planes, faces, or sketch curves that partially or fully intersect the faces that are being split.
- **isSplittingToolExtended** (boolean): A boolean value for setting whether or not the splittingTool is to be automatically extended (if possible) so as to completely intersect the faces that are to be split. This is only used when the split type is "split with surface" which is the default type when a new createInput is created. Use functions on the returned SplitFaceFeatureInput to define a different type of split type.
- **Returns** (SplitFaceFeatureInput): Returns the newly created SplitFaceFeatureInput object or null if the creation failed.

### item(index: uinteger) -> SplitFaceFeature
Function that returns the specified split face feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SplitFaceFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> SplitFaceFeature
Function that returns the specified split face feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (SplitFaceFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of split face features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Split Face Feature API Sample**: Demonstrates creating a new split face feature.
