# ValueCommandInput
Namespace: adsk.core
Inherits: CommandInput
Since: August 2014

Provides a command input to get a unit based value from the user.

**Accessed from:** CommandInputs.addValueInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this Command input.
- **Returns** (boolean): Returns true if the delete was successful.

## Properties

### commandInputs : CommandInputs [read-only]
Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

### expression : string [read-write]
Gets or sets the expression displayed in the input field. This can contain equations and references to parameters. It is evaluated using the specified unit type.

### id : string [read-only]
Gets the unique identifier for this input in the command's CommandInputs.

### isEnabled : boolean [read-write]
Gets or sets if this input is currently enabled or disabled for user interaction.

Currently, the isEnabled property does not disable SelectionCommandInput objects but instead has the same effect as the SelectionCommandInput.hasFocus property.

### isFullWidth : boolean [read-write]
Gets or sets if this input fills the entire width of the dialog. If true, the name is ignored and the input control will fill the entire width of the command dialog. The default value for this property in a new command input if false, or not to fill the width. This property does not apply to GroupCommandInputs or TabCommandInputs.

### isMaximumInclusive : boolean [read-write]
Gets and sets if the maximum value can be equal to the value defined by the maximumValue property or if it must be less than the maximum.

When a new ValueCommandInput is created, this defaults to true.

### isMaximumLimited : boolean [read-write]
Gets and sets whether the maximum value has a limit. The maximum limit is set using the maximumValue property, and the isMaximumInclusive property controls whether the maximum includes the maximum value or must be less than the maximum.

When a new ValueCommandInput is created this defaults to false so there is no limit.

### isMinimumInclusive : boolean [read-write]
Gets and sets if the minimum value can be equal to the value defined by the minimumValue property or if it must be greater than.

When a new ValueCommandInput is created, this defaults to true.

### isMinimumLimited : boolean [read-write]
Gets and sets whether the minimum value has a limit. The minimum limit is set using the minimumValue property, and the isMinimumInclusive property controls whether the minimum includes the minimum value or must be greater than the minimum.

When a new ValueCommandInput is created this defaults to false so there is no limit.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isValidExpression : boolean [read-only]
Returns true if the current expression is valid and can be evaluated. If this is false, the value returned should be ignored because there currently is not a valid value.

### isVisible : boolean [read-write]
Gets or sets if this input will be visible to the user.

Setting a SelectionCommandInput to be invisible will clear any selections it currently has.

### maximumValue : double [read-write]
Gets and sets the maximum value for the input. Setting this value will automatically set the isMaximumLimited property to true, enabling the use of the maximum value. Use the isMaximumInclusive property to control if the maximum can be equal to this value or must be less than the maximum.

### minimumValue : double [read-write]
Gets and sets the minimum value for the input. Setting this value will automatically set the isMinimumLimited property to true, enabling the use of the minimum value. Use the isMinimumInclusive property to control if the minimum can be equal to this value or must be greater than the minimum.

### name : string [read-only]
Gets the user visible name of this input.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentCommand : Command [read-only]
Gets the parent Command.

### parentCommandInput : CommandInput [read-only]
Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent.

### toolClipFilename : string [read-write]
Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

### tooltip : string [read-write]
Gets or sets the base tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control.

### tooltipDescription : string [read-write]
Gets or sets additional text to display progressively along with the tooltip. The text for the description can contain some basic HTML formatting tags to format the tags. For example the br tag can be used to create multiple paragraphs. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

### unitType : string [read-write]
Gets and sets the unit type that is used when evaluating the user's input.

### value : double [read-write]
Gets or sets the value associated with this input. The value is always in the database units of the unit type specified. For example, if the unit type is "inch" this value is in centimeters since centimeters are the database length unit. When setting the value it is converted into a string using the unit type and displayed in the input box. When getting the value, the current expression string is evaluated and the database value for the unit type is returned.

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.
