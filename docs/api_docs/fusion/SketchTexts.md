# SketchTexts
Namespace: adsk.fusion
Inherits: Base
Since: March 2015

The collection of text blocks in a sketch. This provides access to the existing text blocks and supports creating new text blocks.

**Accessed from:** Sketch.sketchTexts

## Methods

### add(input: SketchTextInput) -> SketchText
Creates a sketch text.
- **input** (SketchTextInput): A SketchTextInput object created using the SketchTexts.createInput method.
- **Returns** (SketchText): Returns the newly created SketchText object or null in the case of failure.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### createInput(formattedText: string, height: double, position: Point3D) -> SketchTextInput
This function is retired. See more information in the 'Remarks' section below.

Creates a SketchTextInput object that can be used to define additional settings when creating sketch text. The SketchTextInput object is equivalent to the Sketch Text dialog in that it collects all of the input required to create sketch text. Once the properties of the SketchTextInput object have been defined, use the add method to create the sketch text.
- **formattedText** (string): The text used for the sketch text. This is a simple string as no additional formatting is currently supported.
- **height** (double): The height of the text in centimeters.
- **position** (Point3D): The position of the text on the x-y plane of the sketch. The text must lie on the x-y plane so the Z component of the point is ignored and always treated as zero.
- **Returns** (SketchTextInput): Returns a SketchTextInput object that can be used to set additional formatting and is used as input to the add method.

### createInput2(formattedText: string, height: double) -> SketchTextInput
This function is retired. See more information in the 'Remarks' section below.

This method has been retired and replaced by createInput3. Use the new method to define text using an expression that can combine literal text with parameter values.
- **formattedText** (string): The text used for the sketch text. This is the equivalent of the text that would be entered into the "Text" command dialog. It can be a simple string or it can be an expression that combines text with parameter values. In the case of a simple string, no quotes are needed, but for an expression, text should be quoted using a single quote.
- **height** (double): The height of the text in centimeters.
- **Returns** (SketchTextInput): Returns a SketchTextInput object that can be used to set additional formatting and is used as input to the add method.

### createInput3(expression: string, height: ValueInput) -> SketchTextInput
Creates a SketchTextInput object that is used to define the additional input to create text. The SketchTextInput object is equivalent to the Sketch Text dialog in that it collects all of the input required to create sketch text. You must call setAsFitOnPath, setAsAlongPath, or setAsMultiLine methods to define one of the three types of text. Once the properties of the SketchTextInput object have been defined, pass the SketchTextInput to the add method to create the sketch text.
- **expression** (string): This defines the expression of the parameter that will be created when this SketchText is created. It can be a simple string or it can be an expression that combines text with parameter values. Simple text must be enclosed within single quotes, the same as it is required in the TEXT command dialog.

An example of a valid expression is: "'Length: ' + lengthParam" and will result in "Length: 3.0 mm". The expression result can be obtained by using the text property on the created SketchTextInput object.
- **height** (ValueInput): A ValueInput that defines the height of the text. This value is used to create a parameter that will control the height of the text. It can be a value where it defines the height of the text in centimeters, or it can be a string where it defines the equation of the parameter and must evaluate to a valid length.
- **Returns** (SketchTextInput): Returns a SketchTextInput object that can be used to set additional formatting and is used as input to the add method.

### item(index: uinteger) -> SketchText
Function that returns the specified sketch text using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (SketchText): Returns the specified item or null if an invalid index was specified.

## Properties

### count : uinteger [read-only]
Returns the number of texts in the sketch.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **SketchTextInput.setAsAlongPath**: Demonstrates the SketchTextInput.setAsAlongPath method.
- **SketchTextInput.setAsFitOnPath**: Demoonstrates the SketchTextInput.setAsFitOnPath method.
- **SketchTextInput.setAsMultiLine**: Demonstrates the SketchTextInput.setAsMultiLine method.
- **Sketch Text API Sample**: Demonstrates creating sketch text by creating both mult-line text and text along a curve.
