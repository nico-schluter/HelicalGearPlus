# DistanceValueCommandInput
Namespace: adsk.core
Inherits: CommandInput
Since: January 2016

Represents a command input that gets a distance from the user. This displays an entry in the command dialog where the user can enter a value and also displays a manipulator in the graphics window to allow them to graphically set the value. The input box is displayed in the dialog when the isVisible property of the command input is true. The manipulator is displayed in the graphics when both the isVisible and isEnabled properties are true.

**Accessed from:** CommandInputs.addDistanceValueCommandInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this Command input.
- **Returns** (boolean): Returns true if the delete was successful.

### setManipulator(origin: Point3D, direction: Vector3D) -> boolean
Defines the position and orientation of the manipulator. The manipulator is only visible when both the isVisible and isEnabled properties are true. If those properties are true and the setManipulator has not been called, the manipulator will be displayed in a default location (0,0,0) and direction (1,0,0). Because of that the input is typically set to be invisible and/or disabled and then enabled once enough input has been specified that you can display the manipulator in the desired location.
- **origin** (Point3D): Defines the position of the manipulator in root component space.
- **direction** (Vector3D): Defines the direction of the manipulator in root component space.
- **Returns** (boolean): Returns true if successful.

## Properties

### commandInputs : CommandInputs [read-only]
Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

### expression : string [read-write]
Gets or sets the expression displayed in the input field. This can contain equations and references to parameters but must result in a valid length expression. If units are not specified as part of the expression, the default units for the design are used.

### hasMaximumValue : boolean [read-write]
Gets and sets if there is a maximum value for this command input. When setting this property, it is only valid to set it to False to remove the maximum value. Setting the maximumValue property will result in this property being set to True.

### hasMinimumValue : boolean [read-write]
Gets and sets if there is a minimum value for this command input. When setting this property, it is only valid to set it to False to remove the minimum value. Setting the minimumValue property will result in this property being set to True.

### id : string [read-only]
Gets the unique identifier for this input in the command's CommandInputs.

### isEnabled : boolean [read-write]
Gets or sets if this input is currently enabled or disabled for user interaction.

Currently, the isEnabled property does not disable SelectionCommandInput objects but instead has the same effect as the SelectionCommandInput.hasFocus property.

### isFullWidth : boolean [read-write]
Gets or sets if this input fills the entire width of the dialog. If true, the name is ignored and the input control will fill the entire width of the command dialog. The default value for this property in a new command input if false, or not to fill the width. This property does not apply to GroupCommandInputs or TabCommandInputs.

### isMaximumValueInclusive : boolean [read-write]
Gets and sets if the value of the input includes the maximum value or is up to the maximum value. For example, if the maximum value is 100 and this property is True, the maximum value can be 100. If this is False, the minimum value must be less than 100. When the maximum value is first defined using the maximumValue property, this property is set to True. The value returned by this property is only meaningful when the hasMaximumValue property returns True.

### isMinimumValueInclusive : boolean [read-write]
Gets and sets if the value of the input includes the minimum value or is up to the minimum value. For example, if the minimum value is zero and this property is True, the minimum value can be zero. If this is False, the minimum value must be greater than zero. When the minimum value is first defined using the minimumValue property, this property is set to True. The value returned by this property is only meaningful when the hasMinimumValue property returns True.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### isValidExpression : boolean [read-only]
Returns true if the current expression is valid and can be evaluated. If this is false, the value returned should be ignored because there currently is not a valid value.

### isVisible : boolean [read-write]
Gets or sets if this input will be visible to the user.

Setting a SelectionCommandInput to be invisible will clear any selections it currently has.

### manipulatorDirection : Vector3D [read-only]
Gets the positive direction of the manipulator in the model space or the root component. To set the direction use the setManipulator method.

### manipulatorOrigin : Point3D [read-only]
Gets the origin point of the manipulator in the model space of the root component. To set the origin use the setManipulator method.

### maximumValue : double [read-write]
Gets and sets maximum value, if any, that the value can be. When getting this property you should first check the hasMaximumValue property to see if this property applies. Also, the isMaximumValueInclusive indicates if the maximum includes this value or will be up to this value.

### minimumValue : double [read-write]
Gets and sets minimum value, if any, that the value can be. When getting this property you should first check the hasMinimumValue property to see if this property applies. Also, the isMinimumValueInclusive indicates if the minimum includes this value or will be up to this value.

Setting this value will change the isMinimumValueInclusive to True and the hasMinimumValue property to True if hasMinimumValue is currently False, otherwise it will just update the value.

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

### value : double [read-write]
Gets and sets the current value of the command input. The value is in centimeters but will be displayed to the user in the current default document units. Setting this value can fail if the input value is not within the minimum and maximum value range.

The isValidExpression property should be checked before using this value within the command because if the expression can't be evaluated there isn't a valid value. Fusion won't allow the execution of a command that contains ValueCommandInput object with invalid expressions so you can dependably use the value in the execute event of the command.

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.
