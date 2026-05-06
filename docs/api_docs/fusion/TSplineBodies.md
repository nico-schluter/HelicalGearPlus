# TSplineBodies
Namespace: adsk.fusion
Inherits: Base
Since: April 2019

A collection of TSpline bodies.

**Accessed from:** FormFeature.tSplineBodies

## Methods

### addByTSMDescription(tsmDescription: string) -> TSplineBody
Creates a new TSplineBody using the T-Spline description provided by the input string which contains TSM formatted text.
- **tsmDescription** (string): A string that contains a T-Spline description in TSM form.
- **Returns** (TSplineBody): Returns the newly created TSplineBody if successful or null in the case of failure.

### addByTSMFile(tsmFilename: string) -> TSplineBody
Creates a new TSplineBody by reading in a TSM file from disk.
- **tsmFilename** (string): The full filename of the TSM file on disk.
- **Returns** (TSplineBody): Returns the newly created TSplineBody if successful or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> TSplineBody
Function that returns the specified T-Spline body using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (TSplineBody): Returns the specified item or null if an invalid index was specified.

### itemByName(name: string) -> TSplineBody
Returns a TSplineBody by specifying the name of the body as seen in the browser.
- **name** (string): The name of the body, as seen in the browser. This is case sensitive.
- **Returns** (TSplineBody): Returns the specified item or null if a body with that name was not found.

## Properties

### count : uinteger [read-only]
The number of bodies in the collection.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():
