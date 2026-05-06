# FloatSliderCommandInput
Namespace: adsk.core
Inherits: SliderCommandInput
Since: June 2015

Provides a command input to get the value of a slider from the user, the value type is float.

**Accessed from:** CommandInputs.addFloatSliderCommandInput, CommandInputs.addFloatSliderListCommandInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this Command input.
- **Returns** (boolean): Returns true if the delete was successful.

### getText(isLeft: boolean) -> string
Gets the texts of the slider if text has been defined.
- **isLeft** (boolean): Indicates to get the left or right text.
- **Returns** (string): Returns the left or right text of the slider.

### setText(left: string, right: string) -> boolean
Sets the text of the slider. Both the left and the right text should be set.
- **left** (string): Indicates the text on the left side of the slider.
- **right** (string): Indicates the text on the right side of the slider.
- **Returns** (boolean): Returns true if successful.

## Properties

### commandInputs : CommandInputs [read-only]
Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

### expressionOne : string [read-write]
Uses an expression to set the value in the first input field. This can contain equations and is evaluated using the specified unit type.

### expressionTwo : string [read-write]
Uses an expression to set the value in the second input field. This can contain equations and is evaluated using the specified unit type.

This property is only available when the hasTwoSliders property returns true.

### hasTwoSliders : boolean [read-only]
Gets if the command input has two sliders.

### id : string [read-only]
Gets the unique identifier for this input in the command's CommandInputs.

### isEnabled : boolean [read-write]
Gets or sets if this input is currently enabled or disabled for user interaction.

Currently, the isEnabled property does not disable SelectionCommandInput objects but instead has the same effect as the SelectionCommandInput.hasFocus property.

### isFullWidth : boolean [read-write]
Gets or sets if this input fills the entire width of the dialog. If true, the name is ignored and the input control will fill the entire width of the command dialog. The default value for this property in a new command input if false, or not to fill the width. This property does not apply to GroupCommandInputs or TabCommandInputs.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isVisible : boolean [read-write]
Gets or sets if this input will be visible to the user.

Setting a SelectionCommandInput to be invisible will clear any selections it currently has.

### maximumValue : double [read-write]
Gets and sets maximum value of the slider in database units. Gets a failure when set if the value of this command input was added by value list.

### minimumValue : double [read-write]
Gets and sets minimum value of the slider in database units. Gets a failure when set if the value of this command input was added by value list.

### name : string [read-only]
Gets the user visible name of this input.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentCommand : Command [read-only]
Gets the parent Command.

### parentCommandInput : CommandInput [read-only]
Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent.

### spinStep : double [read-write]
Gets and sets the spin step value in the unit type set by the unitType argument. The value should be more than zero. This is the amount the slider will advance when the user clicks the spin button beside the value.

### toolClipFilename : string [read-write]
Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

### tooltip : string [read-write]
Gets or sets the base tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control.

### tooltipDescription : string [read-write]
Gets or sets additional text to display progressively along with the tooltip. The text for the description can contain some basic HTML formatting tags to format the tags. For example the br tag can be used to create multiple paragraphs. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

### unitType : string [read-write]
Gets and sets the unit type that is used when evaluating the user's input.

### valueList : array [read-only]
Gets the value list of the slider. This property is valid when this input represents a list type of slider command input. Otherwise an empty list will be returned.

### valueOne : double [read-write]
Gets or sets the first value associated with this input. The value is always in the database units of the unit type specified. For example, if the unit type is "inch" this value is in centimeters since centimeters are the database length unit. When setting the value it is converted into a string using the unit type and displayed in the input box.

### valueTwo : double [read-write]
Gets or sets the second value associated with this input. The value is always in the database units of the unit type specified. For example, if the unit type is "inch" this value is in centimeters since centimeters are the database length unit. When setting the value it is converted into a string using the unit type and displayed in the input box.

This property is only available when the hasTwoSliders property returns true.

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.
