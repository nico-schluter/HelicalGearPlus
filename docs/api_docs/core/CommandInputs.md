# CommandInputs
Namespace: adsk.core
Inherits: Base
Since: August 2014

Provides access to the set of inputs for a command. Command inputs are used to gather inputs from the user when a command is executed. The set of inputs used by a command are created and added to the command with the methods in this class.

**Accessed from:** AngleValueCommandInput.commandInputs, BoolValueCommandInput.commandInputs, BrowserCommandInput.commandInputs, ButtonRowCommandInput.commandInputs, Command.commandInputs, CommandInput.commandInputs, DirectionCommandInput.commandInputs, DistanceValueCommandInput.commandInputs, DropDownCommandInput.commandInputs, FloatSliderCommandInput.commandInputs, FloatSpinnerCommandInput.commandInputs, GroupCommandInput.children, GroupCommandInput.commandInputs, ImageCommandInput.commandInputs, InputChangedEventArgs.inputs, IntegerSliderCommandInput.commandInputs, IntegerSpinnerCommandInput.commandInputs, RadioButtonGroupCommandInput.commandInputs, SelectionCommandInput.commandInputs, SeparatorCommandInput.commandInputs, SliderCommandInput.commandInputs, StringValueCommandInput.commandInputs, TabCommandInput.children, TabCommandInput.commandInputs, TableCommandInput.commandInputs, TextBoxCommandInput.commandInputs, TriadCommandInput.commandInputs, ValidateInputsEventArgs.inputs, ValueCommandInput.commandInputs

## Methods

### addAngleValueCommandInput(id: string, name: string, initialValue: ValueInput) -> AngleValueCommandInput
Adds a new angle value input to the command. This displays a field in the command dialog where an angle value can be entered. It displays the angle in the dialog using degrees. There is also a graphical manipulator associated with the input to allow the user to graphically set the value. You use the setManipulator method of the returned AngleValueCommandInput object to define the position and orientation of the manipulator.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed label of this input as seen in the dialog. If a name is not specified (an empty string), the input will be centered horizontally within it's row in the dialog. If a name is specified it will appear as a left justified label aligned with the other command input labels, and the left side of the image will be aligned with the other command input controls.
- **initialValue** (ValueInput): The initial value of the input. If the value input is a number then it is interpreted as radians. If it is a string it uses the units specified in the string or if no units are specified it uses degrees.
- **Returns** (AngleValueCommandInput): Returns the created AngleValueCommandInput object or null if the creation failed.

### addBoolValueInput(id: string, name: string, isCheckBox: boolean, resourceFolder: string, initialValue: boolean) -> BoolValueCommandInput
Adds a new boolean input to the command. The input can be shown as a check box or a button. If it's a button you need to specify the resource folder to define the icon to use. Buttons don't have an up or down state but can just be clicked.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed name of this command as seen in the dialog.
- **isCheckBox** (boolean): Specifies if this input should be displayed as a check box or a button. If true a check box is displayed, if false a button is displayed that can be clicked to toggle it's state.
- **resourceFolder** (string): Specifies the folder that contains the icon for the input. This is optional if isCheckBox is true. If it's defined for a check box, the check box will display as a button using the icon and will have an up or down state. Icons can be defined using either PNG or SVG files. More information about icons can be found in the user manual topic User Interface Customization.

This is an optional argument whose default value is "".
- **initialValue** (boolean): Specifies the initial value of the check box or button where for a check box the value of True results in it being checked and for a button a value of true results in the button being pressed.

This is an optional argument whose default value is False.
- **Returns** (BoolValueCommandInput): Returns the created BoolValueCommandInput object or null if the creation failed.

### addBrowserCommandInput(id: string, name: string, htmlFileURL: string, minimumHeight: integer, maximumHeight: integer) -> BrowserCommandInput
Adds a new command input to the command that behaves as a browser.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed label of this input as seen in the dialog.

If a name is not specified (an empty string), the input will be centered horizontally within it's row in the dialog. If a name is specified, the name will appear as a left justified label aligned with the other command input labels, and the left side of the input will be aligned with the other command inputs.
- **htmlFileURL** (string): Specifies the URL to the HTML file that will be displayed in the tab. This can be a local file or on the web.
- **minimumHeight** (integer): Defines the minimum height of the browser within the command dialog. As the user resizes the dialog, the area taken up by the browser will shrink and grow to fit within the defined space. It will never shrink to be less than the minimum height or expand to be larger than the maximum height. If the dialog can't fit the browser at the minimum size a scroll bar will appear for the dialog to allow the user to scroll to access all the inputs in the dialog.
- **maximumHeight** (integer): An optional parameter that specifies the maximum height of the browser within the command dialog. As the user resizes the dialog, the area taken up by the browser will shrink and grow to fit within the defined space. It will never shrink to be less than the minimum height or expand to be larger than the maximum height. If the content displayed within the browser does not fit within the current area, a scroll bar will appear to allow the user to scroll to see the entire browser content. The default value of zero sets no maximum height, so the browser will expand to the maximum extent available.

This is an optional argument whose default value is 0.
- **Returns** (BrowserCommandInput): Returns the created BrowserCommandInput object or null if the creation failed.

### addButtonRowCommandInput(id: string, name: string, isMultiSelectEnabled: boolean) -> ButtonRowCommandInput
Adds a new row of buttons as a command input. Depending on the isMultiSelectEnabled argument it can act like an option list where only a single button on the row can be selected at a time or multiple buttons can be selected. The buttons are defined by using the returned ButtonRowCommandInput object.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed label of this command as seen in the dialog.
- **isMultiSelectEnabled** (boolean): Sets if this button row can have multiple items selected at once or not. If True, multiple buttons can be selected at once. If False only one button can be selected and selecting another button unselects the one currently selected.
- **Returns** (ButtonRowCommandInput): Returns the created ButtonRowCommandInput object or null if the creation failed.

### addDirectionCommandInput(id: string, name: string, resourceFolder: string) -> DirectionCommandInput
Adds a new direction command input to the command. The input can be shown as a check box or a button. If it's a button you need to specify the resource folder to define the icon to use for the Button.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed name of this command as seen in the dialog.
- **resourceFolder** (string): Specifies the folder that contains the icon to use for the input. This is an optional argument. The input is shown as a check box if the resource folder is not set. More information about icons can be found in the user manual topic User Interface Customization.

This is an optional argument whose default value is "".
- **Returns** (DirectionCommandInput): Returns the created DirectionCommandInput object or null if the creation failed.

### addDistanceValueCommandInput(id: string, name: string, initialValue: ValueInput) -> DistanceValueCommandInput
Adds a new distance value input to the command. This displays a field in the command dialog where a distance value can be entered. It displays the distance in the dialog using current document default unit. There is also a graphical manipulator associated with the input. You use the setManipulator method of the returned DistanceValueCommandInput object to define the position and orientation of the manipulator.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed label of this input as seen in the dialog. If a name is not specified (an empty string), the input will be centered horizontally within it's row in the dialog. If a name is specified it will appear as a left justified label aligned with the other command input labels, and the left side of the image will be aligned with the other command input controls.
- **initialValue** (ValueInput): The initial value of the input. If the value input is a number then it is interpreted as centimeters. If it is a string it uses the units specified in the string or if no units are specified it uses the active units of the design.
- **Returns** (DistanceValueCommandInput): Returns the created DistanceValueCommandInput object or null if the creation failed.

### addDropDownCommandInput(id: string, name: string, dropDownStyle: DropDownStyles) -> DropDownCommandInput
Adds a new empty drop-down input to the command. drop-downs of various types are supported. To add items to the drop down use the returned DropDownCommandInput object.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed label of this command as seen in the dialog.
- **dropDownStyle** (DropDownStyles): Specifies the style of the drop-down.
- **Returns** (DropDownCommandInput): Returns the created DropDownCommandInput object or null if the creation failed.

### addFloatSliderCommandInput(id: string, name: string, unitType: string, min: double, max: double, hasTwoSliders: boolean) -> FloatSliderCommandInput
Adds a new slider input to the command. The value type is double.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed name of this command as seen in the dialog.
- **unitType** (string): The unit type of the value. This will be used to validate the input and the returned value will be in the base units for this unit type. For example if you specify the unitType to be "in" the returned value will be in centimeters because inches are a length unit and the base unit for length is centimeters.
- **min** (double): Provides the minimum value in database units
- **max** (double): Provides the maximum value in database units
- **hasTwoSliders** (boolean): Optional input. Indicates if the slider input has two sliders.

This is an optional argument whose default value is False.
- **Returns** (FloatSliderCommandInput): Returns the created FloatSliderCommandInput object or null if the creation failed.

### addFloatSliderListCommandInput(id: string, name: string, unitType: string, valueList: double[], hasTwoSliders: boolean) -> FloatSliderCommandInput
Adds a new slider input to the command. The value type is float.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed name of this command as seen in the dialog.
- **unitType** (string): The unit type of the value. This will be used to validate the input and the returned Value object will be of this type.
- **valueList** (double[]): Provides the value list (in database units) of the slider command input. This defines all of the values that the slider can return. As the user moves the slider it will jump between these values. The low and high values of the list are used as the minimum and maximum values of the slider.
- **hasTwoSliders** (boolean): Optional input. Indicates if the slider input has two sliders.

This is an optional argument whose default value is False.
- **Returns** (FloatSliderCommandInput): Returns the created FloatSliderCommandInput object or null if the creation failed.

### addFloatSpinnerCommandInput(id: string, name: string, unitType: string, min: double, max: double, spinStep: double, initialValue: double) -> FloatSpinnerCommandInput
Adds a new spinner input to the command. The value type is float.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed name of this command as seen in the dialog.
- **unitType** (string): The unit type of the value. This will be used to validate the input and the returned Value object will be of this type.
- **min** (double): Provides the minimum value in database units.
- **max** (double): Provides the maximum value in database units.
- **spinStep** (double): Sets the spin step value in the unit type set by the unitType argument. The value should be more than zero. This is the amount the slider will advance when the user clicks the spin button beside the value.
- **initialValue** (double): The initial value of this input as shown in the dialog. This value is assumed to be in database units for the specified unit type
- **Returns** (FloatSpinnerCommandInput): Returns the created FloatSpinnerCommandInput object or null if the creation failed.

### addGroupCommandInput(id: string, name: string) -> GroupCommandInput
Adds a new Group input to the command. Group Command inputs organize a set of command inputs into a collapsible list within a command dialog.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed label of this group as seen in the dialog.
- **Returns** (GroupCommandInput): Returns the created GroupCommandInput object or null if the creation failed.

### addImageCommandInput(id: string, name: string, imageFile: string) -> ImageCommandInput
Adds a new Image input to the command.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed label of this Image as seen in the dialog. If a name is not specified (an empty string), the image will be left justified within the dialog. If a name is specified it will appear as a left justified label aligned with the other command input labels, and the left side of the image will be aligned with the other command input controls.
- **imageFile** (string): The full path and file name of the image file. Supported image format is .png Images are displayed in the command dialog using their actual size.
- **Returns** (ImageCommandInput): Returns the created ImageCommandInput object or null if the creation failed.

### addIntegerSliderCommandInput(id: string, name: string, min: integer, max: integer, hasTwoSliders: boolean) -> IntegerSliderCommandInput
Adds a new slider input to the command. The value type is integer.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed name of this command as seen in the dialog.
- **min** (integer): Provides the minimum value.
- **max** (integer): Provides the maximum value.
- **hasTwoSliders** (boolean): Optional input. Indicates if the slider input has two sliders.

This is an optional argument whose default value is False.
- **Returns** (IntegerSliderCommandInput): Returns the created IntegerSliderCommandInput object or null if the creation failed.

### addIntegerSliderListCommandInput(id: string, name: string, valueList: integer[], hasTwoSliders: boolean) -> IntegerSliderCommandInput
Adds a new slider input to the command. The value type is integer.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed name of this command as seen in the dialog.
- **valueList** (integer[]): Provides the value list of the slider command input. This defines all of the values that the slider can return. As the user moves the slider it will jump between these values. The low and high values of the list are used as the minimum and maximum values of the slider.
- **hasTwoSliders** (boolean): Optional input. Indicates if the slider has two sliders.

This is an optional argument whose default value is False.
- **Returns** (IntegerSliderCommandInput): Returns the created IntegerSliderCommandInput object or null if the creation failed.

### addIntegerSpinnerCommandInput(id: string, name: string, min: integer, max: integer, spinStep: uinteger, initialValue: integer) -> IntegerSpinnerCommandInput
Adds a new spinner input to the command. The value type is integer.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed name of this command as seen in the dialog.
- **min** (integer): Provides the minimum value.
- **max** (integer): Provides the maximum value.
- **spinStep** (uinteger): Provides the spin step. The value should be more than zero. This is the amount the slider will advance when the user clicks the spin button beside the value.
- **initialValue** (integer): The initial value of this input as shown in the dialog.
- **Returns** (IntegerSpinnerCommandInput): Returns the created IntegerSpinnerCommandInput object or null if the creation failed.

### addRadioButtonGroupCommandInput(id: string, name: string) -> RadioButtonGroupCommandInput
Adds a new Radio Button Group input to the command.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed label of this radio button group as seen in the dialog.

This is an optional argument whose default value is "".
- **Returns** (RadioButtonGroupCommandInput): Returns the created RadioButtonGroupCommandInput object or null if the creation failed.

### addSelectionInput(id: string, name: string, commandPrompt: string) -> SelectionCommandInput
Adds a new selection input to the command. This allows you to get entity selections from the user. The default behavior is that only one entity can be selected and it can be of any type. To change the selection behavior to select specific types and control the number of items selected use the methods and properties on the returned SelectionCommandInput object. You can also use the selectionEvent event that's associated with the command to have additional control over the selection process.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed name of this command as seen in the dialog.
- **commandPrompt** (string): The text in the tooltip shown next to the cursor.
- **Returns** (SelectionCommandInput): Returns the created SelectionCommandInput object or null if the creation failed.

### addSeparatorCommandInput(id: string) -> SeparatorCommandInput
Adds a new Separator input to the command. A separator input is for visual purposes only and creates a line in the dialog providing a visual separation between the command inputs above and below where the separator is inserted.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **Returns** (SeparatorCommandInput): Returns the created SeparatorCommandInput object or null if the creation failed.

### addStringValueInput(id: string, name: string, initialValue: string) -> StringValueCommandInput
Adds a new string input to the command.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed name of this command as seen in the dialog.
- **initialValue** (string): Specifies the initial value as shown in the dialog.

This is an optional argument whose default value is "".
- **Returns** (StringValueCommandInput): Returns the created StringValueCommandInput object or null if the creation failed.

### addTabCommandInput(id: string, name: string, resourceFolder: string) -> TabCommandInput
Adds a new Tab input to the command. Tab command inputs contain a set of command inputs and/or group command inputs
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed label of this tab as seen in the dialog.
- **resourceFolder** (string): An optional parameter that specifies the folder that contains the image for the tab. If no name is specified (no text on tab), a resourceFolder containing the image to appear on the tab needs to be provided. More information about icons can be found in the user manual topic User Interface Customization.

This is an optional argument whose default value is "".
- **Returns** (TabCommandInput): Returns the created TabCommandInput object or null if the creation failed.

### addTableCommandInput(id: string, name: string, numberOfColumns: integer, columnRatio: string) -> TableCommandInput
Adds a new table command input to the command.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed name of this command as seen in the dialog.
- **numberOfColumns** (integer): This argument is no longer used. The number of columns displayed is inferred by the number of columns that contain command inputs. As you add command inputs to the table the display of the table will adjust to show all of the columns that contain a command input.
- **columnRatio** (string): Sets the width ratio of the columns. This is defined using a string such as "1:1:1" where this defines that the first three columns are all the same width. A value of "2:1" defines that the first column is twice the width of the second.

If the table has more columns than are defined by this property, they will automatically default to a value of 1. If this property defines the width of more columns than are displayed, the extra definitions are ignored.

You can also specify 0 as a column width and this will have the effect of hiding that column. Setting a column width to 0 does not delete the column or the command inputs but only hides them so they can be turned back on at a later time by resetting the column ratio.
- **Returns** (TableCommandInput): Returns the created TableCommandInput object or null if the creation failed.

### addTextBoxCommandInput(id: string, name: string, formattedText: string, numRows: integer, isReadOnly: boolean) -> TextBoxCommandInput
Adds a text box input to the command.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed name of this command as seen in the dialog. If an empty string is provided then no name will be displayed and the text box will span the width of the command dialog.
- **formattedText** (string): Specifies the formatted text to display in the input. For example, you can use basic html formatting such as <b>Bold</b>, <i>Italic</i>, and <br /> for a line break. It also supports hyperlinks, which when clicked by the user, Fusion will open the specified URL in the default browser. Hyperlinks are defined using the <a> tag such as "You are using Autodesk's <a href=http://fusion.autodesk.com>Fusion</a>.".

If you are using HTML formatting in your text, it's best to set the text box to be read-only. However, if you want to use the text box as a way to get input from the user, it's best to use simple text so not HTML formatting is assumed. To do this, use an empty string for this argument and then set the text using the text property after the input is created. When the text property is used any HTML formatting is ignored and the text is treated as basics text. This can be useful if you're using the text box to have the user enter HTML code so it's treated as a simple string.
- **numRows** (integer): Specifies the height of the text box as defined by the number of rows of text that can be displayed. If the text is larger than will fit in the box a scroll bar will automatically be displayed.
- **isReadOnly** (boolean): Specifies if the text box is read-only or not.
- **Returns** (TextBoxCommandInput): Returns the created TextBoxCommandInput object or null if the creation failed.

### addTriadCommandInput(id: string, transform: Matrix3D) -> TriadCommandInput
Adds a new triad command input to the command. The input is initially invisible to allow you to define the desired behavior and then set the isVisible property to true when you're ready to display the triad.

The creation of a triad command input results in displaying many input fields in the command dialog. For example, there can be individual fields for the X, Y, and Z offset distances, the X, Y, and Z scales, the X, Y, and Z angles, etc. You control which fields are visible by setting properties on the returned TriadCommandInput. Even though each of these appears as an individual input in the command dialog, and they are all associated with the single TriadCommandInput object. It also results in graphics widgets being displayed to allow the user to define the values graphically.

When a new triad is created, it displays all inputs except those that control scaling. You can use the properties on the returned triad to define the inputs you want to display further.

To simplify your command dialog it can be useful put the TriadCommandInput within a GroupCommandInput so it's apparent to the user these items are related and they can be collapsed to reduce clutter in the dialog. This also allows you to label the set of displayed inputs by using the name of the GroupCommandInput.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **transform** (Matrix3D): Defines the initial position and orientation of the manipulator.
- **Returns** (TriadCommandInput): Returns the created TriadCommandInput object or null if the creation failed.

### addValueInput(id: string, name: string, unitType: string, initialValue: ValueInput) -> ValueCommandInput
Adds a new value input to the command.
- **id** (string): The unique ID of this command input. It must be unique with respect to the other inputs associated with this command.
- **name** (string): The displayed name of this command as seen in the dialog.
- **unitType** (string): The unit type of the value. This will be used to validate the input and the returned Value object will be of this type.
- **initialValue** (ValueInput): The initial value of this input as shown in the dialog. This can be a string or a real. If it's a string it must be able to be evaluated using the specified unit type. If it's a real it is assumed to be in database units for the specified unit type and is displayed as a string
- **Returns** (ValueCommandInput): Returns the created ValueCommandInput object or null if the creation failed.

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### item(index: uinteger) -> CommandInput
Returns the specified command input using an index into the collection.
- **index** (uinteger): The index of the item within the collection to return. The first item in the collection has an index of 0.
- **Returns** (CommandInput): Returns the specified item or null if an invalid index was specified.

### itemById(id: string) -> CommandInput
Returns the command input that has the specified ID.
- **id** (string): The unique ID of the command input you want to get.
- **Returns** (CommandInput): Returns the specified command input or null if the input ID doesn't match an existing command input.

## Properties

### command : Command [read-only]
Gets the parent Command object.

### count : uinteger [read-only]
Gets the number of inputs.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.
