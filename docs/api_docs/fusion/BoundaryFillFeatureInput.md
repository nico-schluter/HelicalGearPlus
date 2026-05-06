# BoundaryFillFeatureInput
Namespace: adsk.fusion
Inherits: Base
Since: June 2015

This class defines the methods and properties that pertain to the definition of a BoundaryFillFeatureInput.

**Accessed from:** BoundaryFillFeatures.createInput

## Methods

### cancel() -> boolean
To determine the possible boundaries and allow you to choose which cells to keep, the boundary fill feature does a partial compute when the input object is created. To do this it starts a boundary fill feature transaction and completes the transaction when you call the add method. If you don't call the add method to finish the transaction it leaves Fusion in a bad state and there will be undo problems and possibly a crash. If you have created a BoundFillFeatureInput object and don't want to finish the feature creation, you need to call the cancel method on the BoundaryFillFeatureInput object to safely abort the current boundary fill transaction.
- **Returns** (boolean): Returns true if successful.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### bRepCells : BRepCells [read-only]
Returns the collection of the valid cells that have been calculated based on the set of input tools. You use this collection to specify which cells you want included in the output.

### creationOccurrence : Occurrence [read-write]
In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the Boundary Fill is created based on geometry (e.g. a profile and/or face(s)) in another component AND (the Boundary Fill) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI

### isRemoveTools : boolean [read-write]
Gets and sets whether any BRepBodys that were used as tools should be removed as part of the feature creation.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### operation : FeatureOperations [read-write]
Gets and sets the type of operation performed by the boundary fill feature.

### targetBaseFeature : BaseFeature [read-write]
When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.

Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it.

### tools : ObjectCollection [read-write]
Gets and sets the collection of one or more construction planes and open or closed BRepBody objects that are used in calculating the possible closed boundaries.

## Samples
- **Boundary Fill Feature API Sample**: Demonstrates creating a new boundary fill feature.
