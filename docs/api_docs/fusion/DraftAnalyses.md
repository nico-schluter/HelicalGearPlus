# DraftAnalyses
Namespace: adsk.fusion
Inherits: Base
Since: January 2023

Provides access to any draft analyses results in the design.

**Accessed from:** Analyses.draftAnalyses

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> DraftAnalysis
A method that returns the specified DraftAnalysis object using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (DraftAnalysis): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> DraftAnalysis
A method that returns the specified DraftAnalysis object using the name of the analysis as displayed in the browser.
- **name** (string): The name of the DraftAnalysis object as displayed in the browser.
- **Returns** (DraftAnalysis): Returns the specified item or null if an invalid name was specified.

## Properties

### count : uinteger [read-only]
Returns the number of DraftAnalysis objects in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
