# CommandDefinition
Namespace: adsk.core
Inherits: Base
Since: August 2014

The CommandDefinition is the base class of the various types of commands. Command types are based on the type of control used to execute them in the user-interface. For example, most commands will use a ButtonDefinition since they're executed using a button in the user-interface. A command definition contains the information that defines the user-interface. For example, the name and icon. The command definition and also gets the notification when the user interacts with the associated control.

**Accessed from:** ApplicationCommandEventArgs.commandDefinition, Command.parentCommandDefinition, CommandControl.commandDefinition, CommandDefinitions.addButtonDefinition, CommandDefinitions.addCheckBoxDefinition, CommandDefinitions.addListDefinition, CommandDefinitions.item, CommandDefinitions.itemById, SplitButtonControl.additionalDefinitions, SplitButtonControl.defaultCommandDefinition

## Methods

### [static] classType() -> string
Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType().
- **Returns** (string): Returns a string indicating the type of the object.

### deleteMe() -> boolean
Deletes this command definition. This is only valid for API created command definitions and will fail if the isNative property is true.
- **Returns** (boolean): Returns true or false indicating if the deletion was successful.

### execute(input: NamedValues) -> boolean
Executes this command definition. This is the same as the user clicking a button that is associated with this command definition.
- **input** (NamedValues): This argument is ignored and exists for possible future use.

This is an optional argument whose default value is null.
- **Returns** (boolean): Returns true or false indicating if the execution was successful.

## Properties

### controlDefinition : ControlDefinition [read-only]
Gets the ControlDefinition associated with this command. The control definition defines the type of control that can exist in the user interface to execute this command. You can use properties on the control definition to define the look and behavior of the control.

### id : string [read-only]
Gets the unique id for this command definition. This is guaranteed to be unique with respect to all other command definitions.

### isNative : boolean [read-only]
Gets if this is a native command definition. If True then there are limitations to edits that can be done on the command definition. For example a native command definition cannot be deleted.

### isValid : boolean [read-only]
Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference.

### name : string [read-write]
Gets or sets the visible name of the command when seen in the user interface.

### objectType : string [read-only]
This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.

It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType():

### resourceFolder : string [read-write]
This argument defines the resource folder that contains the images used for the command icon. Icons can be defined using either PNG or SVG files. More information about icons can be found in the user manual topic User Interface Customization.

### toolClipFilename : string [read-write]
Gets or sets the full filename of the image file (PNG) used for the tool clip. The tooltip is always shown but as the user hovers over the control it will progressively display the tool clip along with the tooltip text.

### tooltip : string [read-write]
Gets or sets the tooltip string. This is always shown for commands. If the tooltip description and/or tool clip are also specified then the tooltip will progressively display more information as the user hovers the mouse over the control.

The width of all tooltips is limited to 300 pixels. Word wrapping is enabled, so Fusion will automatically break the line and flow your text to the next line. However, if you include a long word that exceeds 300 pixels, it doesn't wrap and the right portion will be clipped. This is common when displaying paths or URL's. If a single word is longer than 300 pixels there are a couple of options to avoid the clipping.

The first option is to insert one or more zero width space characters within the word to define where the word should be broken. The UNICODE character '\u200b' defines a zero width space. This is not displayed is only used to designate a possible break point.

The second option is to shorten the word by removing a section. For example, if the word is a full path to a file and a portion of the path is common you can remove that portion and replace it with the ellipsis character to indicate there is some missing text. There is a single UNICODE character you can use the ellipsis. It is '\u2026'.

## Events

### commandCreated
This event is fired when the associated control is manipulated by the user. A new Command object is created and passed back through this event which you can then use to interact with the user to get any input the command requires.

## Samples
- **Command Inputs API Sample**: Creates a command dialog that demonstrates all of the available command inputs.


To use the sample, create a new Python or C++ script and copy and paste this code, replacing the default code. You also need to unpack this zip file which contains a resource folder into the same folder where the source code file (.py or .cpp) is.
- **Customizing the UI using the API Sample**: Demonstrates how to work with tabs, panels, and command in the user interface. The full source for C++ and Python samples can be downloaded. This is especially useful for getting the resource files.
