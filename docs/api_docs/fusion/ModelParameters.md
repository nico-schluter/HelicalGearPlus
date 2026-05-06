# ModelParameters
Namespace: adsk.fusion
Inherits: Base
Since: August 2014

Provides access to the Model Parameters within a component.

**Accessed from:** Component.modelParameters, CustomFeatureParameter.modelParameters, FlatPatternComponent.modelParameters, ModelParameter.modelParameters

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> ModelParameter
Function that returns the specified Model Parameter using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (ModelParameter): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> ModelParameter
Function that returns the specified Model Parameter using the name of the parameter as it is displayed in the parameters dialog.
- **name** (string): The name of the Model Parameter as it is displayed in the parameters dialog
- **Returns** (ModelParameter): Returns the specified item or null if an invalid name was specified.

## Properties

### component : Component [read-only]
Returns the component that owns the Model Parameters collection

### count : uinteger [read-only]
Returns the number of parameters in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
