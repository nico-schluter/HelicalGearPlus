# InterferenceInput
Namespace: adsk.fusion
Inherits: Base
Since: November 2015

Used to gather and define the various inputs and settings needed to calculate interference. This object is created using the Design.createInterferenceInput method.

**Accessed from:** Design.createInterferenceInput, FlatPatternProduct.createInterferenceInput, WorkingModel.createInterferenceInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### areCoincidentFacesIncluded : boolean [read-write]
Gets and sets whether any coincident faces in the input bodies are considered as interference or not. This property defaults to False for a newly created InterferenceInput object.

### entities : ObjectCollection [read-write]
Gets and set an ObjectCollection containing BRepBody and/or Occurrence entities that will be used when checking for interference. All entities must be in the context of the root component of the top-level design.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Analyze Interference API Sample**: Demonstrates analyzing the interference between components. This uses a direct modeling design because the ability to create bodies that represent the interference volume is only supported in a direct modeling design.
- **Interference API Sample**: Demonstrates Interference APIs.
