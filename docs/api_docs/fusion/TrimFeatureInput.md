# TrimFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: July 2015

This class defines the methods and properties that pertain to the definition of a TrimFeatureInput.

**Accessed from:** TrimFeatures.createInput

## Methods

### cancel()
To determine the possible boundaries and allow you to choose which cells to keep, the trim feature does a partial compute when the input object is created. To do this it starts a trim feature transaction and completes the transaction when you call the add method. If you don't call the add method it leaves Fusion in a bad state and there will be undo problems and it will possibly crash. If you have created a TrimFeatureInput object and don't want to finish the feature creation, you need to call the cancel method on the TrimFeatureInput object to safely abort the current trim feature transaction.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### bRepCells : BRepCells [read-only]
Returns the collection of the valid cells that have been calculated based on the trim tool. Use this collection to specify which cells to trim away.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

### trimTool : Base [read-write]
Gets and sets the entity (a patch body, B-Rep face, construction plane or sketch curve) that intersects the trim tool

## Samples
- **Trim Feature API Sample**: Demonstrates creating a new trim feature.
