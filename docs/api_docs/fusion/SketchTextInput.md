# SketchTextInput
Namespace: adsk.fusion
Inherits: Base
Since: March 2015

The SketchTextInput object is equivalent to the Sketch Text dialog in that it collects all of the input required to create sketch text. Once the properties of the SketchTextInput object have been defined, use the add method to create the sketch text. A SketchTextInput object is created by using the createInput of the SketchTexts object.

**Accessed from:** SketchTexts.createInput, SketchTexts.createInput2, SketchTexts.createInput3

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### setAsAlongPath(path: Base, isAbovePath: boolean, horizontalAlignment: HorizontalAlignments, characterSpacing: double) -> boolean
Sets this SketchTextInput to define text that follows along a specified path.
- **path** (Base): The entity that defines the path for the text. This can be a SketchCurve or BRepEdge object.
- **isAbovePath** (boolean): Indicates if the text should be positioned above or below the path entity.
- **horizontalAlignment** (HorizontalAlignments): Specifies the horizontal alignment of the text with respect to the path curve.
- **characterSpacing** (double): The percentage change in default spacing between characters.
- **Returns** (boolean): Returns true if the setting the definition was successful.

### setAsFitOnPath(path: Base, isAbovePath: boolean) -> boolean
Sets this SketchTextInput to define text that fits along a specified path. Fitting on a path will space the characters so the text fits along the entire length of the path entity.
- **path** (Base): The entity that defines the path for the text. This can be a SketchCurve or BRepEdge object.
- **isAbovePath** (boolean): Indicates if the text should be positioned above or below the path entity.
- **Returns** (boolean): Returns true if the setting the definition was successful.

### setAsMultiLine(cornerPoint: Base, diagonalPoint: Base, horizontalAlignment: HorizontalAlignments, verticalAlignment: VerticalAlignments, characterSpacing: double) -> boolean
Defines the first corner point of the rectangle that will contain the text.
- **cornerPoint** (Base): Specifies the location of one of the corner points of the rectangle that will contain the text. This can be a Point3D object, with a Z component of zero, to define any arbitrary location on the X-Y plane of the sketch or it can be an existing SketchPoint that lies on the sketch X-Y plane.
- **diagonalPoint** (Base): Specifies the location of the diagonal point of the rectangle that will contain the text. This point cannot be aligned vertically or horizontally to the corner point but be a diagonal point to define a rectangle. This can be a Point3D object, with a Z component of zero, to define any arbitrary location on the X-Y plane of the sketch or it can be an existing SketchPoint that lies on the sketch X-Y plane and the sketch point will become the opposing corner point.
- **horizontalAlignment** (HorizontalAlignments): Specifies the horizontal alignment of the text with respect to the text rectangle.
- **verticalAlignment** (VerticalAlignments): Specifies the vertical alignment of the text with respect to the text rectangle.
- **characterSpacing** (double): The spacing between the characters. This is an additional spacing to apply that is defined as a percentage of the default spacing. A spacing of 0 indicates no additional spacing. A spacing of 50 indicates to use the default plus 50% of the default.
- **Returns** (boolean): Returns true if the setting the definition was successful.

## Properties

### angle : double [read-write]
This function is retired. See more information in the 'Remarks' section below.

Gets and sets the angle of the text relative to the x-axis of the x-y plane of the sketch.

### definition : SketchTextDefinition [read-only]
Returns the SketchTextDefinition object associated with this input. When the SketchTextInput is first created this property will return null. Once one of the "set" methods have been called, this will return the SketchTextDefinition of the appropriate type and can be used to make any additional changes to the text.

### expression : string [read-write]
Gets and sets the expression of the parameter that will be created when this SketchText is created. It can be a simple string or it can be an expression that combines text with parameter values. Simple text must be enclosed within single quotes, the same as it is required in the TEXT command dialog.

An example of a valid expression is: "'Length: ' + lengthParam" and will result in "Length: 3.0 mm". The expression result can be obtained by using the text property on the created SketchTextInput object.

### fontName : string [read-write]
Gets and sets the name of the font to use.

### height : double [read-write]
This function is retired. See more information in the 'Remarks' section below.

This property has been retired and replaced by the height2 property.

### height2 : ValueInput [read-write]
Gets and sets the ValueInput that defines the height of the text. This value is used to create a parameter that will control the height of the text. It can be a value where it defines the height of the text in centimeters, or it can be a string where it defines the equation of the parameter and must evaluate to a valid length.

### isHorizontalFlip : boolean [read-write]
Gets and sets if the text is flipped horizontally.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVerticalFlip : boolean [read-write]
Gets and sets if the text is flipped vertically.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### position : Point3D [read-write]
This function is retired. See more information in the 'Remarks' section below.

Gets and sets the position of the text on the x-y plane of the sketch. The text must lie on the x-y plane so the Z component of the point is ignored and always treated as zero.

### text : string [read-write]
Gets and sets the displayed text. This represents the text that results from evaluating the input formatted text. For example, if the formatted text is "'Length: ' + lengthParam", this property will return "Length: 3.0 in".

Setting this property will overwrite any equation defined by the expression and replace it with simple text. Use the expression property to be able to define a full expression.

### textStyle : TextStyles [read-write]
Gets and sets the text style to apply to the entire text. This is a bitwise enum so styles can be combined to apply multiple styles. For example you can apply bold and italic.

## Samples
- **Sketch Text API Sample**: Demonstrates creating sketch text by creating both mult-line text and text along a curve.
