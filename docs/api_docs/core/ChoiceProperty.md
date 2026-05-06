# ChoiceProperty
Namespace: adsk.core
Inherits: Property
Since: August 2014

A property that is a predefined list of choices.

This is most commonly used for properties associated with materials and appearances.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getChoices(names: string[], choices: string[]) -> boolean
Method that returns the list of available choices.
- **names** (string[]): An array of the names of the choices. These coincide with the array of choices returned by the choices argument.
- **choices** (string[]): An array of the choices. These coincide with the array of names returned by the names argument.
- **Returns** (boolean): Returns true if the call was successful.

## Properties

### id : string [read-only]
Returns the unique ID of this property.

### isReadOnly : boolean [read-only]
Indicates if this property is read-only. If True any attempted edits will fail.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
Returns the name of this property as seen in the user interface. This name is localized and can change based on the current language

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Returns the parent of this property.For properties associated with an appearance this will return the parent Appearance. For properties associated with a material, this will return the parent Material. For other types of properties, this will return the PropertyGroup it is in.

### value : string [read-write]
Gets and sets the which choice is selected from the set of choices. The value is a string that matches one of the predefined choices. The names of the available choices can be obtained using GetChoices method.
