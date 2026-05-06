# DirectionCommandInput
Namespace: adsk.core
Inherits: CommandInput
Since: January 2016

Represents a command input that gets a direction from the user. This displays a button or a check-box in the command dialog where the user can flip the direction if desired and also displays a manipulator in the graphics window to allow flipping the direction by clicking and dragging on the manipulator.

**Accessed from:** CommandInputs.addDirectionCommandInput

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this Command input.
- **Returns** (boolean): Returns true if the delete was successful.

### setManipulator(origin: Point3D, direction: Vector3D) -> boolean
Defines a direction manipulator arrow in the graphics viewport whose direction can be flipped by the toggling the check box, clicking the button or by the user clicking and dragging on the manipulator arrow.
- **origin** (Point3D): The origin point of the direction manipulator (arrow) in the model space of the root component.
- **direction** (Vector3D): The direction of the manipulator (arrow) in the model space of the root component.
- **Returns** (boolean): Returns true if successful

## Properties

### commandInputs : CommandInputs [read-only]
Gets the CommandInputs class of the parent, which can be a Command, GroupCommandInput or TabCommandInput.

### id : string [read-only]
Gets the unique identifier for this input in the command's CommandInputs.

### isDirectionFlipped : boolean [read-write]
Gets and sets if the direction manipulator displayed is flipped (reversed 180 degrees as compared to the direction defined by the manipulatorDirection property). This is false for a newly created DirectionCommandInput.

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

### manipulatorDirection : Vector3D [read-only]
Gets the direction of the manipulator (arrow) in the model space of the root component. To set the direction use the setManipulator method.

### manipulatorOrigin : Point3D [read-only]
Gets the origin point of the direction manipulator (arrow) in the model space of the root component. To set the origin use the setManipulator method.

### name : string [read-only]
Gets the user visible name of this input.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### parentCommand : Command [read-only]
Gets the parent Command.

### parentCommandInput : CommandInput [read-only]
Gets the parent CommandInput if this commandInput is the child of a TabCommandInput or GroupCommandInput. Returns null if there is no parent.

### resourceFolder : string [read-write]
Gets and sets the folder that contains the icon to display on the button. The input is shown as a check box if the resource folder is set to an empty string. Icons can be defined using either PNG or SVG files. More information about icons can be found in the user manual topic User Interface Customization.

### toolClipFilename : string [read-write]
Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

### tooltip : string [read-write]
Gets or sets the base tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control.

### tooltipDescription : string [read-write]
Gets or sets additional text to display progressively along with the tooltip. The text for the description can contain some basic HTML formatting tags to format the tags. For example the br tag can be used to create multiple paragraphs. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip and description text.

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.
