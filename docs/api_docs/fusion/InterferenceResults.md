# InterferenceResults
Namespace: adsk.fusion
Inherits: Base
Since: November 2015

Transient object used to return the result of an interference analysis.

**Accessed from:** Design.analyzeInterference, FlatPatternProduct.analyzeInterference, WorkingModel.analyzeInterference

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createBodies(allInterferenceBodies: boolean) -> ObjectCollection
Creates bodies in the model that represent the interference volumes. This is not supported in parametric modeling.
- **allInterferenceBodies** (boolean): Sets if all bodies or only individual bodies will be created as bodies in the model. If False, then only interferenceResult objects whose isCreateBody property is true will be created as a model body. If true, all interface volumes will be created as a body regardless of the value of the isCreateBody property on each InterferenceResult object.
- **Returns** (ObjectCollection): Returns an ObjectCollection containing the bodies that were created.

### item(index: uinteger) -> InterferenceResult
Function that returns the specified interference result using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (InterferenceResult): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of interference results in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Interference API Sample**: Demonstrates Interference APIs.
