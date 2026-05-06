# SilhouetteSplitFeatures
Namespace: adsk.fusion
Inherits: Base
Since: June 2015

Collection that provides access to all of the existing Silhouette Split features in a component and supports the ability to create new Silhouette Split features.

**Accessed from:** Features.silhouetteSplitFeatures

## Methods

### add(input: SilhouetteSplitFeatureInput) -> SilhouetteSplitFeature
Creates a new silhouette split feature.
- **input** (SilhouetteSplitFeatureInput): A SilhouetteSplitFeatureInput object that defines the desired silhouette split feature. Use the createInput method to create a new SilhouetteSplitFeatureInput object and then use methods on it (the SilhouetteSplitFeatureInput object) to define the silhouette split.
- **Returns** (SilhouetteSplitFeature): Returns the newly created SilhouetteSplitFeature object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(viewDirection: Base, targetBody: BRepBody, operation: SilhouetteSplitOperations) -> SilhouetteSplitFeatureInput
Creates a SilhouetteSplitFeatureInput object. Use properties and methods on this object to define the silhouette split you want to create and then use the Add method, passing in the SilhouetteSplitFeatureInput object.
- **viewDirection** (Base): A construction axis, linear BRepEdge, planar BRepFace or a construction plane that defines the view direction where the silhouette is calculated.
- **targetBody** (BRepBody): Input the single solid body to split
- **operation** (SilhouetteSplitOperations): The type of silhouette split operation to perform.
- **Returns** (SilhouetteSplitFeatureInput): Returns the newly created SilhouetteSplitFeatureInput object or null if the creation failed.

### item(index: uinteger) -> SilhouetteSplitFeature
Function that returns the specified silhouette split feature using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SilhouetteSplitFeature): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> SilhouetteSplitFeature
Function that returns the specified silhouette split feature using the name of the feature.
- **name** (string): The name of the feature within the collection to return. This is the name seen in the timeline.
- **Returns** (SilhouetteSplitFeature): Returns the specified item or null if the specified name was not found.

## Properties

### count : uinteger [read-only]
The number of Silhouette Split features in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Silhouette Split Feature API Sample**: Demonstrates creating a new silhouette split feature.
