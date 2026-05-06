# SharedPointCoincident
Namespace: adsk.fusion
Inherits: Base
Since: March 2025

An object that is only used when a glyph representing a special type of coincident constraint is selected in the user interface. An example of its use is when two lines are connected at their endpoints. If you hover the mouse over the shared endpoint, a coincident constraint glyph is displayed and highlights the two lines. Selecting the glyph and deleting it will cause the lines to be separate. In this case, there isn't a real coincident constraint, but the two lines share the same sketch point. The UI uses this "fake" coincident constraint to indicate that the lines share the same point. It also supports separating them when the glyph is deleted by creating a new point and moving one of the lines to it.

A selection returns this object when a glyph representing this special type of coincident constraint is selected. It is only used for selections and provides access to the highlighted entities when the glyph is selected.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

## Properties

### curveOne : SketchCurve [read-only]
Returns the first sketch curve that is highlighted when the glyph was selected.

### curveTwo : SketchCurve [read-only]
Returns the second sketch curve that is highlighted when the glyph was selected.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### point : SketchPoint [read-only]
Returns the sketch point that the sketch curves are connected to.
