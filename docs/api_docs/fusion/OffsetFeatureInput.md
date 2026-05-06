# OffsetFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: June 2015

This class defines the methods and properties that pertain to the definition of an offset feature.

**Accessed from:** OffsetFeatures.createInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### distance : ValueInput [read-write]
Gets and sets the ValueInput object that defines the offset distance. A positive distance value results in an offset in the positive normal direction of the faces.

### entities : ObjectCollection [read-write]
An ObjectCollection containing the BRepFace objects being offset.

### isChainSelection : boolean [read-write]
Get and sets whether faces that are tangentially connected to the input faces will be included in the offset.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### operation : FeatureOperations [read-write]
Gets and sets the feature operation to perform. Can be 'NewBodyFeatureOperation' or 'NewComponentFeatureOperation'.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

## Samples
- **Offset Feature API Sample**: Demonstrates creating a new offset feature
