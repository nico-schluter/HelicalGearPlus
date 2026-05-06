# MultiLineTextDefinition
Namespace: adsk.fusion
Inherits: SketchTextDefinition
Since: December 2020

Defines the information for multi-line text.

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### rotate(angle: double, keyPoint: TextBoxKeyPoints) -> boolean
Rotates the text box.
- **angle** (double): The angle to rotate the text, specified in radians.
- **keyPoint** (TextBoxKeyPoints): The key point the rotation is defined around. This is optional and defaults the center of the text box.

This is an optional argument whose default value is TextBoxKeyPoints.MiddleTextBoxKeyPoint.
- **Returns** (boolean): Returns true if successful.

## Properties

### characterSpacing : double [read-write]
Gets and sets the spacing between the characters. This is an additional spacing to apply that is defined as a percentage of the default spacing. A spacing of 0 indicates no additional spacing. A spacing of 50 indicates to use the default plus 50% of the default.

### horizontalAlignment : HorizontalAlignments [read-write]
Gets and sets the horizontal alignment of the text with respect to the text rectangle.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentSketchText : SketchText [read-only]
Returns the SketchText object this definition is associated with. This property will return null in the case the definition object was obtained from a SketchTextInput object because the SketchText object does not yet exist.

### rectangleLines : array [read-only]
Returns the four sketch lines that define the boundary of the sketch text. By adding constraints to these lines you can associatively control the size, position and angle of the sketch text. If the MultiLineTextDefinition object is obtained from a SketchTextInput object, this property will return null because the text and it's associated lines have not been created yet.

### verticalAlignment : VerticalAlignments [read-write]
Gets and sets the vertical alignment of the text with respect to the text rectangle.
