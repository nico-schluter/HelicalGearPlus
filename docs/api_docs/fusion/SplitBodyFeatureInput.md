# SplitBodyFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: June 2015

This class defines the methods and properties that pertain to the definition of a split body feature.

**Accessed from:** SplitBodyFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isSplittingToolExtended : boolean [read-write]
Gets and sets whether or not the splitting tool is to be automatically extended (if possible) so as to completely intersect the bodyToSplit.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### splitBodies : Base [read-write]
Gets and sets the input solid or open bodies to be split. This can be a single BRepBody or an ObjectCollection if multiple bodies are to be split.

### splittingTool : Base [read-write]
Gets and sets the entity that defines the splitting tool. The splitting tool is a single entity that can be either a solid or open BRepBody, construction plane, profile, or a face.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

## Samples
- **Split Body Feature API Sample**: Demonstrates creating a new split body feature.
