# SketchTextDefinition
Namespace: adsk.fusion
Inherits: Base
Since: December 2020

The base class for the classes that define how text can be defined.

**Accessed from:** SketchText.definition, SketchTextInput.definition

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentSketchText : SketchText [read-only]
Returns the SketchText object this definition is associated with. This property will return null in the case the definition object was obtained from a SketchTextInput object because the SketchText object does not yet exist.
