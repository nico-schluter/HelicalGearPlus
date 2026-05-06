# CAMArrangeParameterValue
Namespace: adsk.cam
Inherits: ParameterValue
Since: March 2024

A parameter value that is a CAMArrangeParameterValue. The user needs to set the parameter anew via the API after a model update or after the ArrangeSelections returned by getArrangeSelections() have been edited.

## Methods

### applyArrangeSelections(arrangeSelections: ArrangeSelections)
Set the values of the parameter as a collection of CadObjects.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### getArrangeSelections() -> ArrangeSelections
Get the values of the parameter as a collection of CadObjects, which currently consist of occurrences.
- **Returns** (ArrangeSelections): Returns current ArrangeSelections of the value.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parent : Base [read-only]
Get the parameter object that the value is associated with.
