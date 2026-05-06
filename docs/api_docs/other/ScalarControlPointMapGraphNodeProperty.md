# ScalarControlPointMapGraphNodeProperty
Namespace: adsk.volume
Inherits: GraphNodeProperty
Since: May 2025

A property value that defines a complex mapping curve from an input domain of double values to an output range of double values. The mapping is represented by a set of points ordered by their domain value parameters. For a given input value, the output value is interpolated from the values of the two points before and after it using the specified interpolation function for each point.

## Methods

### addPoint(parameter: double, value: double, interpolator: ControlPointInterpolators) -> boolean
Add a point to the map.
- **parameter** (double): Where in the input domain where the point lies.
- **value** (double): The double value of the parameter in the output domain.
- **interpolator** (ControlPointInterpolators): The function used to interpolate an output value for a input parameter between this point and the next.
- **Returns** (boolean): True if successfully added.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### clear() -> boolean
Remove all points from the map.
- **Returns** (boolean): True if successfully cleared.

### getPoint(index: uinteger) -> ScalarControlPoint
Get the point at index.
- **index** (uinteger): Index of the point to get.
- **Returns** (ScalarControlPoint): The control point at this index.

### removePoint(index: uinteger) -> boolean
Remove a point from the map.
- **index** (uinteger): Index of the point to remove.
- **Returns** (boolean): True if successfully removed.

## Properties

### description : string [read-only]
Returns the description of this property. This description is localized and can change based on the current language.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-only]
Gets the internal name of the property.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### pointCount : uinteger [read-only]
The number of points.
