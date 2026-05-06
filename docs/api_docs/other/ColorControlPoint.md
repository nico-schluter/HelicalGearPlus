# ColorControlPoint
Namespace: adsk.volume
Inherits: Base
Since: May 2025

A read-only structure that represents a control point used in ColorControlPointMapGraphNodeProperty.

**Accessed from:** ColorControlPointMapGraphNodeProperty.getPoint

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### interpolator : ControlPointInterpolators [read-only]
The interpolator function.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parameter : double [read-only]
The parameter inside the input domain of the control point map for this point.

### value : Color [read-only]
The output color value of the control point for this point.
