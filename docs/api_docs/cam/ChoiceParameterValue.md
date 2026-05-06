# ChoiceParameterValue
Namespace: adsk.cam
Inherits: ParameterValue
Since: September 2021

A parameter value that is a list of choices.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getChoices(names: string[], values: string[]) -> boolean
Method that returns the list of available choices.
- **names** (string[]): An array of the names of the choices. These coincide with the array of possible values returned by the values argument.
- **values** (string[]): An array of the possible values. These coincide with the array of names returned by the names argument.
- **Returns** (boolean): Returns true if the call was successful.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Get the parameter object that the value is associated with.

### value : string [read-write]
Get or set the value of the parameter. This value will correspond to one of the available values of the parameter.
